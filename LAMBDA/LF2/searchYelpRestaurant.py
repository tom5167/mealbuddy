import boto3
from boto3.dynamodb.conditions import Key, And
import json 

def search(location,cuisine,dining_date,dining_time,num_people,phone):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('yelp_restaurant')
    filters = dict()
    filters['cuisine'] = cuisine
    filters['price'] = '$$'
    response = table.scan(FilterExpression=And(*[(Key(key).eq(value)) for key, value in filters.items()]))
    
    print(len(response['Items']))
    
    responseList = []
    for i in range(0,10):
        name = response['Items'][i]['name']
        address = response['Items'][i]['address']
        address = ", ".join(address)
        num_reviews = str(response['Items'][i]['review_count'])
        rating = str(response['Items'][i]['rating'])
        cuisine = cuisine
        phone = str(response['Items'][i]['phone'])
        responseList.append([name,phone,address,num_reviews,rating,cuisine])
        
    return responseList