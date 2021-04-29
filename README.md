# TikTok- Tredning Prediction based on Description

* Created  a app using React Native, Sklearn library to predict weather the video will be tredning on TikTok or not based on its Description.

* Scraped over 10000 tiktok data with details such as username, userid, videoid, video desc, video time,video length, video link, likes, shares, comments and plays using python API.

* Data Preprocessing is done using Python and if the tiktok has likes >= 40000, shares >= 10000 and comments >= 500 will be trending tiktok.

* Applying different algorithms with Natural language processing to find out best accurancy among them.

* Saved the data model using joblib and used that model with REST API and flask.

* Developed a React Native app, which will take into as a tiktok description and based on the model will predict if it will be tredning or not.

# Code and Resources Used 
 
**Packages for Data model** : Pandas, TikTokApi, stopwords, CountVectorizer, sklearn, nltk, joblib, flask

**Packages for Frontend App** : React Native, axios, react-navigation-stack, react-navigator

**TikTok Api** : https://towardsdatascience.com/how-to-collect-data-from-tiktok-tutorial-ab848b40d191

# Data Scraping 
 Using TikTop API in python collected 10000 tiktok data. With each tiktok video we got the following
* Username
* User_id
* Video_id
* Video_desc
* Video_time
* Video_length
* Likes
* Shares
* Comments
* Plays
 
 
# Data Preprocessing 
After collecting the data, based on no of likes, shares and comments decided which tiktok will be trending.
* Added one more column called trending.
* If the TikTok has likes >= 40000 and shares >= 10000 and comments >= 500 then it is trending and the trending column has value **1**
* Else the trending column has value **0** (not trending tiktok)
* Final csv file has the following data:
 
<img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/Data_CSV.png" width="1000" />


# Model Building
I split the data into train and tests sets with a test size of 30%.Training set has 6252 samples.
Testing set has 2680 samples.

Natural Language processing is used before spliting the data into training and testing.
* Removed the stop words from the description.
* Created worldcloud for trending and non-trending description from data set.
* Converted the words into vectorized form so we can use the data with following models.

I tried four different models and evaluated tehm using accurancy.

Models which I have tried are :
* Multi Naive-Base
* Support Vector Machine
* K-nearest neighbors
* Rondom Forest


# Model Performance

Accuracy  in %

* Rondom Forest : 87.537
* Support Vector Machine : 85.037
* K-nearest Neighbors :84.440
* Multi Naive-Base : 83.582

<img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/BarGrpahA.png" width="500" />



<img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/RF.png" width="200" /> <img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/SVM.png" width="200" />


<img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/KNN.png" width="210" /> <img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/MultiNB.png" width="200" />


# Productionization 

In this step, first I saved Random Forest model using Joblib. After the model is saved, I build a API endpoint using Flask, that will take ine input as description apply the saved model on the description and predict wheather it will be trending  or not. 
Developed an frontend app using React native that will take description and using axios app sends the description to Flask Api and it returns wheather the description will be trending or not. 

# React Native App

<img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/FE-pt1.png" width="204" /> <img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/FE-pt2.png" width="202" /> <img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/FE-pt3.png" width="200" /> <img src="https://github.com/PranjalVarade/TikTok-Prediction/blob/main/Images/FE-pt4.png" width="195" />


# Demo

Click [here](https://drive.google.com/file/d/1R3Fu7BYxmJb_Otirmd7ZDA6UaiMG8Je4/view?usp=sharing) for demo.
