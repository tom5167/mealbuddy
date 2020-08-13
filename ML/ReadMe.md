# Amazon SageMaker

Amazon SageMaker is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. SageMaker removes the heavy lifting from each step of the machine learning process to make it easier to develop high quality models.

We studied how to make restaurant recommendation systems based on semi-supervised learning.
For that , we  fetched the details of restaurants  [id, cuisine, rating and review] from yelp fusion API.
Then we are storing the data into a csv file for further use. From there by using machine learning techniques we created different models to train and test them. The different machine learning models will be evaluated to find  the best model which will give  the best  restaurant with its rating and reviews
Now we are going through different ML algorithms (Decision tree, Random forest , xgboost algorithm) to understand which is better to choose. 

Notebook - resturantRecommendationML
 - Notebook instance - typeml.t2.medium
 - Volume Size - 5GB EBS

1.Gathering Data
- Gathered data using yelp api and dump to yelp_restaurant.csv

2.Data Preparation
- read yelp_restaurant.csv and store in data frame
- add column 'recommended' 
  - 1 based on rating > avg(rating) and review_counting > avg(reviews_counting)
  - 0 based on rating < avg(rating) and review_counting < avg(reviews_counting)
- create df_recommend and sort by rating and reviews_counting
- create df_non_recommend  and sort by rating and reviews_counting
- create semisupervised_train will 80% df_recommend + 80% df_non_recommend and save as 'semisupervised_train.csv'
- create unsupervised_train will 20% df_recommend + 20% df_non_recommend and save as 'unsupervised_train.csv'
- Convert categorical variable into dummy/indicator variables for cuisine
 
 ex. 	
 
 review_count	rating	recommend	cuisine_american	cuisine_chinese	cuisine_greek	cuisine_indian	cuisine_italian	cuisine_latin	cuisine_mexican	cuisine_persian	cuisine_spanish
 
 0	98	4.5	1	0	0	0	1	0	0	0	0	0

- train, validation = train_test_split(semisupervised_train_for_model, test_size=0.1, random_state=42)
- train.to_csv('train.csv', index=False, header=False)
- validation.to_csv('validation.csv', index=False, header=False)

3.Choosing a Model and Parameter Tuning
- trainDF, validationDF = train_test_split(trainingDF, test_size=0.1, random_state=42)
- decison tree > random forest > xgboost algorithm
- xgb = sagemaker.estimator.Estimator(container,role,train_instance_count=1,train_instance_type='ml.m4.xlarge',
output_path='s3://{}/output'.format(bucket),sagemaker_session=sess)
- xgb.set_hyperparameters(max_depth=3,eta=0.2,gamma=4,min_child_weight=4,subsample=0.8,silent=0,
objective='binary:logistic',num_round=20)
- xgb.fit({'train': s3_input_train,'validation': s3_input_validation})

5.Deploy
- xgb_predictor = xgb.deploy(initial_instance_count=1,instance_type='ml.m4.xlarge')

6.Prediction
- xgb_predictor.predict(array).decode('utf-8')



