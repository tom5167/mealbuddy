# Lambda Function 2 (LF2)

The lambda function main contains majority of processes. 
It is scheduled by cloudwatch for 1 minute interval.

1. Read message from SQS - if empty send error message
2. Delete the processed message using reciept handle
3. Search DynamoDB for restaurant details based on user input (Max 10)
4. Using Sagemaker Enpoint call make prediction and Top 3 results
5. Format the reply for user
6. Send the message using SNS
7. If any error send error message
8. Store the request and reply message in DynamoDB
