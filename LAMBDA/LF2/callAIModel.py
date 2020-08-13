import json
import boto3

def recommendSorter(e):
  return e[0]

def makePrediction(payload):
    
    responseList = []
    topResponseList = []
    endpoint_name = 'xgboost-2020-08-05-21-17-49-856'
    runtime = boto3.Session().client(service_name='sagemaker-runtime',region_name='us-east-1')
    
    #review_count	rating	cuisine_american	cuisine_chinese	cuisine_greek	
    #cuisine_indian	cuisine_italian	cuisine_latin	cuisine_mexican	cuisine_persian	cuisine_spanish
    
    #125.0,3.5,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    for item in payload:
        inputData = ",".join(item[3:5])
        if(item[5] == 'american'):
            inputData = inputData + ",1,0,0,0,0,0,0,0,0"
        elif(item[5] == 'chinese'):
            inputData = inputData + ",0,1,0,0,0,0,0,0,0"
        elif(item[5] == 'greek'):
            inputData = inputData + ",0,0,1,0,0,0,0,0,0"
        elif(item[5] == 'indian'):
            inputData = inputData + ",0,0,0,1,0,0,0,0,0"
        elif(item[5] == 'italian'):
            inputData = inputData + ",0,0,0,0,1,0,0,0,0"
        elif(item[5] == 'latin'):
            inputData = inputData + ",0,0,0,0,0,1,0,0,0"
        elif(item[5] == 'mexican'):
            inputData = inputData + ",0,0,0,0,0,0,1,0,0"
        elif(item[5] == 'persian'):
            inputData = inputData + ",0,0,0,0,0,0,0,1,0"
        elif(item[5] == 'spanish'):
            inputData = inputData + ",0,0,0,0,0,0,0,0,1"
        try:
            response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='text/csv', Body=inputData)
            recommend = float(response['Body'].read())
            responseList.append(str(recommend)+","+','.join(item))
            #topResponseList = inputData
            responseList.sort(key=recommendSorter)
        except Exception as ex:
            raise ex
    
    itr = 1
    for item in responseList:
        topResponseList.append(item)
        itr = itr+1
        if(itr>3):
            break
    
    return topResponseList
