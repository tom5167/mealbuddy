# SLACK

Slack is a proprietary business communication platform developed by American software company Slack Technologies. 
Slack offers many IRC-style features, including persistent chat rooms organized by topic, private groups, and direct messaging
URL: https://slack.com/intl/en-ca/

Step 1: Create an Amazon Lex Bot

Step 2: Sign Up for Slack and Create a Slack Team - Sign up for a Slack account and create a Slack team.

Step 3: Create a Slack Application

  a. Create a Slack application on the Slack API Console
  
  b. Configure the application to add interactive messaging to your bot: you will get application credentials (Client Id, Client Secret, and Verification Token).
  
Step 4: Integrate the Slack Application with the Amazon Lex Bot

  a. Sign in to the AWS Management Console, and open the Amazon Lex console at https://console.aws.amazon.com/lex/.
  
  b. Choose the Amazon Lex bot that you created in Step 1.
  
  c. Choose the Channels tab.
  
  d. In the left menu, choose Slack.
  
  e. On the Slack page, provide the following:
  
  f. Type a name. For example, BotSlackIntegration.
  
  g. Choose "aws/lex" from the KMS key drop-down.
  
  h. For Alias, choose the bot alias.
  
  i. Type the Client Id, Client secret, and Verification Token, which you recorded in the preceding step. These are the credentials of the Slack application.
  
  j. Choose Activate. The console creates the bot channel association and returns two URLs (Postback URL and OAuth URL). Record them. In the next step, you update your Slack application configuration to use these endpoints.
  
  k. The Postback URL is the Amazon Lex bot's endpoint that listens to Slack events. You use this URL:
  
    * As the request URL in the Event Subscriptions feature of the Slack application.
    
    * To replace the placeholder value for the request URL in the Interactive Messages feature of the Slack application.
    
  l. The OAuth URL is your Amazon Lex bot's endpoint for an OAuth handshake with Slack.
  
Step 5: Complete Slack Integration

  a. Update the OAuth & Permissions feature as follows:
  
    * In the left menu, choose OAuth & Permissions.
    
    * In the Redirect URLs section, add the OAuth URL that Amazon Lex provided in the preceding step. Choose Add a new Redirect URL, and then choose Save URLs.
    
    * In the Bot Token Scopes section, add two permissions with the Add an OAuth Scope button. Filter the list with the following text:
    
      * chat:write
      
      * team:read
      
  b. Update the Interactivity & Shortcuts feature by updating the Request URL value to the Postback URL that Amazon Lex provided in the preceding step. Enter the postback URL that you saved in step 4, and then choose Save Changes.
  
  c. Subscribe to the Event Subscriptions feature as follows:
  
    * Enable events by choosing the On option.
    
    * Set the Request URL value to the Postback URL that Amazon Lex provided in the preceding step.
    
    * In the Subscribe to Bot Events section, subscribe to the message.im bot event to enable direct messaging between the end user and the Slack bot.
    
    * Save the changes.
    
Step 6: Test the Integration

  a. Choose Manage Distribution under Settings. Choose Add to Slack to install the application. Authorize the bot to respond to messages.
  
  b. You are redirected to your Slack team. In the left menu, in the Direct Messages section, choose your bot. If you don't see your bot, choose the plus icon (+) next to Direct Messages to search for it.
  
  c. Engage in a chat with your Slack application, which is linked to the Amazon Lex bot. Your bot now responds to messages.

