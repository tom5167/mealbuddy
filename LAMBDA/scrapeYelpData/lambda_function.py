import boto3
import datetime
import json
from time import sleep
from decimal import *
from botocore.vendored import requests
from urlparse import urljoin
import warnings


def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


API_KEY = "T-K64h1YLhBnreA69A0zy_ZPk518bg0_TFzlaSL2DGt2vhb3XCpsUxDiKFDR2qQTa2yIEayQqECso-wxMotP5bUAJz_GmE0e4lp0iDIisBAQlmfX8TtaKhfbFmXWXnYx"

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('yelp_restaurant')


API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Toronto'
restaurants = {}


def search(cuisine, offset):
    url_params = {
        'location': DEFAULT_LOCATION,
        'offset': offset,
        'limit': 1000,
        'term': cuisine + " restaurants",
        'sort_by': 'rating'
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


def request(host, path, url_params=None):
    url_params = url_params or {}
    url = urljoin(host, path)
    headers = {
        'Authorization': 'Bearer ' + API_KEY,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)
    rjson = response.json()
    # business_list = rjson['businesses']
    return rjson


def addItems(data, cuisine):
    global restaurants
    with table.batch_writer() as batch:
        for rec in data:
            try:
                if rec["alias"] in restaurants:
                    continue;
                rec["rating"] = Decimal(str(rec["rating"]))
                restaurants[rec["alias"]] = 0
                rec['cuisine'] = cuisine
                rec['insertedAtTimestamp'] = str(datetime.datetime.now())
                rec["coordinates"]["latitude"] = Decimal(str(rec["coordinates"]["latitude"]))
                rec["coordinates"]["longitude"] = Decimal(str(rec["coordinates"]["longitude"]))
                rec['address'] = rec['location']['display_address']
                rec.pop("distance", None)
                rec.pop("location", None)
                rec.pop("transactions", None)
                rec.pop("display_phone", None)
                rec.pop("categories", None)
                if rec["phone"] == "":
                    rec.pop("phone", None)
                if rec["image_url"] == "":
                    rec.pop("image_url", None)

                # print(rec)
                batch.put_item(Item=rec)
                sleep(0.001)
            except Exception as e:
                print(e)
                print(rec)


def scrape():
    cuisines = ['italian', 'chinese', 'indian', 'american', 'mexican', 'spanish', 'greek', 'latin', 'Persian']
    for cuisine in cuisines:
        offset = 0
        while offset < 1000:
            js = search(cuisine, offset)
            addItems(js["businesses"], cuisine)
            #print(cuisine)
            #print(js["businesses"][0])
            #print("----------------")
            offset += 50
            
def lambda_handler(event, context):
    
    scrape()
    return {
        'statusCode': 200,
        'body': json.dumps('Scrape yelp data is success')
    }