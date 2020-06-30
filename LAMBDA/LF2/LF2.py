import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    
    # Get URL for SQS queue
    response = sqs.get_queue_url(QueueName='LF1SQSLF2.fifo')
    queue_url = response['QueueUrl']
    
    sendMessage = {}
    message = {}
    # Receive a message from SQS queue
    try:
        response = sqs.receive_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/702727121783/LF1SQSLF2.fifo",
            AttributeNames=['All'],
            MaxNumberOfMessages=10
        )
        logger.debug("sqs response >>>>>:")
        #logger.debug(response)
        
        message = response['Messages'][0]
        
        body = message['Body']
        logger.debug(body)
        
        message = json.loads(body)
        location = message['Location']['StringValue']
        cuisine = message['Cuisine']['StringValue']
        dining_date =  message['DiningDate']['StringValue']
        dining_time = message['DiningTime']['StringValue']
        num_people = message['NumPeople']['StringValue']
        phone =  message['PhoneNum']['StringValue']
        logger.debug('variabless>>>'+location+' '+cuisine+' '+dining_date+' '+dining_time+' '+num_people+' '+phone)
        #sendMessage = location+' '+cuisine+' '+dining_date+' '+dining_time+' '+num_people+' '+phone
        #call elastic search
        
        #after elastic search
        name = "Filgy Resturant"
        address = "Country 1399"
        num_reviews = "1000"
        rating = 5
        
        #name = response['Items'][0]['Name']
        #address = response['Items'][0]['Address']
        #num_reviews = response['Items'][0]['Num_of_Reviews']
        #rating = response['Items'][0]['Rating']
        
        sendMessage = "Hello! For {}, we recommend the {} {} restaurant on {}. The place has {} of reviews and an average score of {} on Yelp. Enjoy!".format(location, name, cuisine, address, num_reviews, rating)
        logger.debug(sendMessage)
        
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        errormessage = template.format(type(ex).__name__, ex.args)
        if errormessage.find("An exception of type KeyError occurred. Arguments:") == -1:
            logger.debug("Error:- Empty sqs queue")
        else:
            logger.debug("Error:- "+errormessage)
    
    return {
        'statusCode': 200,
        'body': json.dumps(sendMessage)
    }
