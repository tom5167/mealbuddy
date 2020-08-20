# Amazon Simple Notification Service

Fully managed pub/sub messaging for microservices, distributed systems, and serverless applications

Amazon Simple Notification Service (SNS) is a fully managed messaging service for both system-to-system and app-to-person (A2P) communication. It enables you to communicate between systems through publish/subscribe (pub/sub) patterns that enable messaging between decoupled microservice applications or to communicate directly to users via SMS, mobile push and email.
The system-to-system pub/sub functionality provides topics for high-throughput, push-based, many-to-many messaging. Using Amazon SNS topics, your publisher systems can fanout messages to a large number of subscriber systems or customer endpoints including Amazon SQS queues, AWS Lambda functions and HTTP/S, for parallel processing. 

In this project we are using SNS service to send text message to the phone number we got from SQS.LF2 is triggered everytime e need to send text messages to the user.
You can get started with Amazon SNS in minutes by using the AWS Management Console, AWS Command Line Interface (CLI), or AWS Software Development Kit (SDK).

https://aws.amazon.com/sns/
