import boto3

def sendMessageNotification(phone, sendMessage):
    if '+1' not in str(phone):
        phone = '+1'+str(phone)
    sns = boto3.client('sns')
    sns.publish(
        PhoneNumber = phone,
        Message = sendMessage
    )
    return 'sendMessageNotification is success for '+str(phone)+', '+sendMessage
