import boto3

def saveUserRequest(message,reply):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('mealBuddy_customer')
    table.put_item(Item={
       'id':str(datetime.datetime.now()),
       'request':str(message),
       'reply':str(reply)
     })
    return 'success'