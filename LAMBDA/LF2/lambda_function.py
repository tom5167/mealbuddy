import json
import boto3
import logging
import searchYelpRestaurant
import saveUserRequest
import sendSNS
import deleteSQSmessage
import callAIModel
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    
    phone = '+14372177746'
    sendMessage = "Sorry cannot process sqs"
    message = {}
    
    # Receive a message from SQS queue
    try:
        
        response = sqs.receive_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/702727121783/LF1SQSLF2.fifo",
            AttributeNames=['All'],
            MaxNumberOfMessages=10
        )
        
        try:
            message = response.get("Messages")[0]
        except Exception as Ex:
            sendMessage = "Error:- No messages on the queue! - "+str(Ex)
            logger.debug(sendMessage)
            saveUserRequest.saveUserRequest(message,sendMessage)
            return {
                'statusCode': 200,
                'body': json.dumps('No messages on the queue! - '+str(Ex))
            }
        
        #"[{\"Body\": \"{\\\"EventName\\\": \\\"Restaurant suggestion\\\", \\\"Location\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"toronto\\\"}, \\\"DiningDate\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"2020-07-23\\\"}, \\\"DiningTime\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"11:28\\\"}, \\\"NumPeople\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"5\\\"}, \\\"Cuisine\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"indian\\\"}, \\\"PhoneNum\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"+437217746\\\"}, \\\"EmailId\\\": {\\\"DataType\\\": \\\"String\\\", \\\"StringValue\\\": \\\"t@gmail.com\\\"}}\", \"Attributes\": {\"ApproximateFirstReceiveTimestamp\": \"1595518246783\", \"SequenceNumber\": \"74195428964391360000\", \"SenderId\": \"AROA2HHOM5N3SI64WWQT6:LF1\", \"MessageDeduplicationId\": \"2915b71211d7bf3826bf3b04dbfcf20a9e45d93f136c302feb6c893e65f27daa\", \"SentTimestamp\": \"1595518240442\", \"ApproximateReceiveCount\": \"17\", \"MessageGroupId\": \"messageGroup1\"}, \"ReceiptHandle\": \"AQEBjQPy5kJm+zBiZoif4Q1HAMpVB9BWHnQlnAM9GSGghmIXdD2W1cGOPngfyDxFlgZasQmC23fxSHMxoU6hO+/1n8rArxpKgNe9+dJepnMyu5JlDd4y8UEf42MLJ4Pg5lZ/C9TPZqPCi8F1co+x4xf9GQfM6aols3ZoGfripYRfMkMcA6Ir60h8C2BXekhwK9nmF7XnUfEKTB2l+M5oW2og7TR+4Zr7WwQKuHlrRHMVkVSJuB/PRvpZcg7yvOfv4m8dcTcKp9rMuXe5MGy6fdnNAg==\", \"MD5OfBody\": \"5740a92cd3d59d50cce0d4a9a43bee68\", \"MessageId\": \"0e81ed39-3cf7-4391-acdf-3ef52534004b\"}]",
        
        msgBody = message['Body']
        msgBody = json.loads(msgBody)
        location = msgBody['Location']['StringValue']
        cuisine = msgBody['Cuisine']['StringValue']
        dining_date =  msgBody['DiningDate']['StringValue']
        dining_time = msgBody['DiningTime']['StringValue']
        num_people = msgBody['NumPeople']['StringValue']
        phone =  msgBody['PhoneNum']['StringValue']
        
        # Get URL for SQS queue
        response = sqs.get_queue_url(QueueName='LF1SQSLF2.fifo')
        queue_url = response['QueueUrl']
        
        #delete message from queue
        deleteSQSmessage.deleteMessageSQS(queue_url,message['ReceiptHandle'] )
        
        #call dynamodb search
        searchResponse = ""
        searchResponse = searchYelpRestaurant.search(location,cuisine,dining_date,dining_time,num_people,phone)
        if(len(searchResponse) != 0):
            sendMessage = ""
        #sendMessage = searchResponse
        
        #make prediction
        predictionList = callAIModel.makePrediction(searchResponse)
        #sendMessage = "".join(predictionList)

        #format reply message for user
        restaurantList = []
        count = 1
        for item in predictionList:
            restaurantList.append(str(count)+"."+item.split(',')[1]+" ("+item.split(',')[2]+")")
            count = count + 1
        sendMessage = "Enjoy "+", ".join(restaurantList)
        if(len(sendMessage)>150):
            print("More than 160 characters, Count-"+str(len(sendMessage)))
            sendMessage = "More than 160 characters, Count-"+str(len(sendMessage))
        elif (sendMessage == "Enjoy "):
            print("Sorry no restuarants found with good ranking")   
            sendMessage = "Sorry no restuarants found with good ranking"
        
        #send reply message
        sendMessage = sendSNS.sendMessageNotification(phone,sendMessage)
        
    except Exception as ex:
        errormessage = "Error occurred - "+str(ex)
        sendMessage = errormessage
        #sendSNS.sendMessageNotification(phone,sendMessage)

    #save user request to dynamodb
    saveUserRequest.saveUserRequest(message,sendMessage)
        
    return {
        'statusCode': 200,
        'body': json.dumps(sendMessage)
    }