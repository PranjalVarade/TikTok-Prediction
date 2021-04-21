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
* Final csv file has the following  data:

--Username

... UserId

...VideoDesc

...VideoTime

...VideoLength

...VideoLink

...Likes

...Shares

...Comments

...Plays

...Trending
