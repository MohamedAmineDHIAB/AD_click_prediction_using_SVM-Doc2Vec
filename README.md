# Click_prediction_using_SVM-Doc2Vec

This REPO contains a Data Science Challenge which consists of predicting whether an AD is going to be clicked or not depending on some given features. After some preprocessing and data analysis we have to choose which features are the most important as well as to determine the embeddings of the text contained in the Topic Line of the Advertisement. 

We use some text embedding technics like Doc2Vec and then we apply a classification SVM model to predict the class (0,1) of each feature vector.

In the end we used Hold-Out Validation to assess some trained SVM models and got the following results :

![image](https://user-images.githubusercontent.com/85687148/126534497-c1956a73-16e8-402f-8985-da796a405200.png)

where Model 1 : 
  - Input features :
    * Day of the Month
    * Hour of the Day
    * Daily Time Spent on Site
    * Age
    * Area Income
    * Daily Internet Usage
    * gender
    * Embeddings of Ad Topic Line (using Doc2Vec)
and Model 2 :
  - Input features :
    * Day of the Month
    * Hour of the Day
    * Daily Time Spent on Site
    * Age
    * Area Income
    * Daily Internet Usage
    * Embeddings of Ad Topic Line (using Doc2Vec)
    
