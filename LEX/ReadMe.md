# Amazon Lex

Conversational AI for Chatbots

Amazon Lex is a service for building conversational interfaces into any application using voice and text. 
Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. 

With Amazon Lex, the same deep learning technologies that power Amazon Alexa are now available to any developer, enabling you to quickly and easily build sophisticated, natural language, conversational bots (“chatbots”).

With Amazon Lex, you can build bots to increase contact center productivity, automate simple tasks, and drive operational efficiencies across the enterprise. As a fully managed service, Amazon Lex scales automatically, so you don’t need to worry about managing infrastructure.

URL: https://aws.amazon.com/lex/

1)create a new bot
https://tutorials.botsfloor.com/say-hello-to-your-own-amazon-lex-chat-bot-9f22e7a0f9b0
Select custom bot→ give the details and create the bot→ create an alias name

2)create intent
A chatbot is a collection of responses for certain messages which is stored in intents
Click create intent→ name the intent→ Add sample utterances

3)Sample Utterances
Utterances are the phrases that you want this intent to reply to.

4)Slots In Lex, variables are stored in Slots that contain the following:
● property name 
● slot type 
● prompt. 
There are a few different ways to create new slots and I’ll discuss a few methods below.

In the Slots section, add the following information to create a new slot. 
● Name: “Name” 
● Slot type: “AMAZON.GB_FIRST_NAME” 
● Prompt: “Hi there, what’s your name?” The smart bit about Amazon Lex is that it uses Natural Language Understanding (NLU) to work out what the user is trying to say.

5)Response No we need to reply to this message. Click the “Add Message” button in the response box. This creates a new message box for us to fill in.
In here you can type in whatever you want the bot to respond. You can enter multiple answers so the user can get varied and more natural responses.
Lex input json format
https://medium.com/velotio-perspectives/amazon-lex-aws-lambda-beyond-hello-world-1403c1825e72
Changed the invocation source to fulfillment codehook for invoking lambda LF1 to push message to sqs

6)LEX integration with Lambda LF1
Choose the corresponding lambda
Thing to remember :The variable name should be same in both lex and lambda.Else null value will return in sqs.
Now click the save intent and then we can build and test intent.

7)Building and Testing the Bot To get your new chatbot working we first need to build it. This allows Lex to take your sample utterances and put them all together. Click the “Build” button on the top right of the page (and click on “Build” once again if a pop-up is displayed). It can take a few minutes to finish building the bot so be patient. When it’s finished you get a new area on the right called Test Bot (latest). This is where you can try chatting to your newly created bot and test it out. Try asking your new bot it’s name.
