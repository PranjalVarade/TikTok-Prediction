# TikTok- Tredning Prediction based on Description

* Created  a app using React Native, Sklearn library to predict weather the video will be tredning on TikTok or not based on its Description.

* Scraped over 10000 tiktok data with details such as username, userid, videoid, video desc, video time,video length, video link, likes, shares, comments and plays.

* Data Preprocessing is done using Python and if the tiktok has likes >= 40000, shares >= 10000 and comments >= 500 will be trending tiktok.

* Applying different algorithms with Natural language processing to find out best accurancy among them.

* Saved the data model using joblib and used that model with REST API and flask.

* Developed a React Native app, which will take into as a tiktok description and based on the model will predict if it will be tredning or not.
