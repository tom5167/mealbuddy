
import json
import boto3
import helper_function
import validate_dining

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def suggest_dining_sqs(intent_request):
    logger.debug("inside suggest_dining_sqs")
    slots = intent_request['currentIntent']['slots']
    location = helper_function.try_ex(lambda: slots['location'])
    cuisine = helper_function.try_ex(lambda: slots['cuisine'])
    dining_date = helper_function.try_ex(lambda: slots['diningDate'])
    dining_time = helper_function.try_ex(lambda: slots['diningTime'])
    num_people = helper_function.try_ex(lambda: slots['numPeople']) # not supported by Yelp API
    phone_num = helper_function.try_ex(lambda: slots['phoneNum'])
    mail_id = helper_function.try_ex(lambda: slots['mailid'])
    
    session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}

    # Load confirmation history and track the current reservation.
    reservation = json.dumps({
        'location': location,
        'cuisine': cuisine,
        'diningDate': dining_date,
        'diningTime': dining_time,
        'numPeople': num_people,
        'phoneNum': phone_num,
        'mailid': mail_id
    })

    session_attributes['currentReservation'] = reservation
    
    logger.debug("inside suggest_dining_sqs() : before validation")
    
    if intent_request['invocationSource'] == 'DialogCodeHook':
        # Validate any slots which have been specified.  If any are invalid, re-elicit for their value
        validation_result = validate_dining.validate_dining(intent_request['currentIntent']['slots'])
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return helper_function.elicit_slot(
                session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message']
            )
        session_attributes['currentReservation'] = reservation
        return helper_function.delegate(session_attributes, intent_request['currentIntent']['slots'])
    
    
    logger.debug("inside suggest_dining_sqs() : after validation")
    
    logger.debug("inside suggest_dining_sqs() : before sqs")
    
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/702727121783/LF1SQSLF2.fifo'
    msgBody = json.dumps( 
            {'EventName':'Restaurant suggestion',
            'Location': {
                'DataType': 'String',
                'StringValue': location
            },
            'DiningDate': {
                'DataType': 'String',
                'StringValue': dining_date
            },
            'DiningTime': {
                'DataType': 'String',
                'StringValue': dining_time
            },
            'NumPeople': {
                'DataType': 'String',
                'StringValue': num_people
            },
            'Cuisine': {
                'DataType': 'String',
                'StringValue': cuisine
            },
            'PhoneNum': {
                'DataType': 'String',
                'StringValue': phone_num
            },
            'EmailId': {
                'DataType': 'String',
                'StringValue': mail_id
            }
        }
    )
    
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=msgBody,
        MessageGroupId='messageGroup1'
    )
    
    logger.debug("inside suggest_dining_sqs() : after sqs")
    
    reply = 'You’re all set. Expect my suggestions as message on phone '+phone_num +' for '+ cuisine+ ' cuisine in '+location+ ' on ' + dining_date + ' at '+ dining_time+ ' for ' +num_people +' people shortly! Have a good day.'
        
    return helper_function.close(
        session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': reply
        }
    )

