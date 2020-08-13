"""
    LF1
"""
import os
import time
import helper_function
import thank_you_intent
import suggest_intent
import greet_intent

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


'''
    Fulfill intents
'''
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))
    intent_name = intent_request['currentIntent']['name']
    
    # Dispatch to your bot's intent handlers
    if intent_name == 'Greet':
        return greet_intent.greet(intent_request)
    elif intent_name == 'SuggestDining':
        return suggest_intent.suggest_dining_sqs(intent_request)
    elif intent_name == 'ThankYou':
        return thank_you_intent.thank(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

# Entry point
def lambda_handler(event, context):
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'Canada/Toronto'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return dispatch(event)

