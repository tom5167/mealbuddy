import boto3

def sendMessageNotification(phone, me):
    sns = boto3.client('sns')
    sns.publish(
        PhoneNumber = phone,
        Message = sendMessage
    )
    return {
        'statusCode': 200,
        'body': json.dumps('sendMessageNotification is success')
    }
