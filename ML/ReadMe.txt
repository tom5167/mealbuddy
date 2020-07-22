1.Gathering Data
- Done

2.Data Preparation
- read csv and store in dataDF
- create trainingDF add column 'recommended' 
  - 1 based on rating>4.9 and review_counting>avg(reviews_counting) - 30% of dataDF
  - 0 based on rating<1 and review_counting<avg(reviews_counting) - 30% of dataDF
- so trainingDF will be 30+30=60% of dataDF
- do correlation matrix

3.Choosing a Model
- trainDF, validationDF = train_test_split(trainingDF, test_size=0.1, random_state=42)

4.Evaluation

5.Parameter Tuning

6.Prediction
