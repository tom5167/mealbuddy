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
- semi supervised

2.Data Preparation
- read yelp_restaurant.csv and store in dataDF
- create trainingDF add column 'recommended' 
  - 1 based on rating>4.9 and review_counting>avg(reviews_counting) - 30% of dataDF
  - 0 based on rating<1 and review_counting<avg(reviews_counting) - 30% of dataDF
- so trainingDF will be 30+30=60% of dataDF
- do correlation matrix

3.Choosing a Model
- trainDF, validationDF = train_test_split(trainingDF, test_size=0.1, random_state=42)
- decison tree > random forest > xgboost algorithm

4.Evaluation

5.Parameter Tuning

6.Prediction
