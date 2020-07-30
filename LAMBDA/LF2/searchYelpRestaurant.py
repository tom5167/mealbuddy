import boto3
from boto3.dynamodb.conditions import Key, And

def searchYelpRestaurant(location,cuisine,dining_date,dining_time,num_people,phone):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('yelp_restaurant')
    filters = dict()
    filters['cuisine'] = cuisine
    filters['price'] = '$$'
    response = table.scan(FilterExpression=And(*[(Key(key).eq(value)) for key, value in filters.items()]))
    name = response['Items'][0]['name']
    address = response['Items'][0]['address']
    num_reviews = str(response['Items'][0]['review_count'])
    rating = str(response['Items'][0]['rating'])
    response = {
        'name':name,
        'address':address,
        'num_reviews':num_reviews,
        'rating':rating
    }
    return json.dumps(response)