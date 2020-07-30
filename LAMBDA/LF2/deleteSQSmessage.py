import boto3

def deleteMessageSQS(QueueUrl,receipt_handle):
    sqs = boto3.client('sqs')
    response = sqs.get_queue_url(QueueName='LF1SQSLF2.fifo')
    queue_url = response['QueueUrl']
    sqs.delete_message(
        QueueUrl=QueueUrl,
        ReceiptHandle=receipt_handle
    )
  