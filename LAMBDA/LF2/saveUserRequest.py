import boto3
import datetime

def saveUserRequest(message,reply):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('mealbuddy_customer_responses')
    table.put_item(Item={
       'id':str(datetime.datetime.now()),
       'request':str(message),
       'reply':str(reply)
     })
    return 'success'