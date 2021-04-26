from flask import Flask, render_template, request
import joblib

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'WorkingRF.pkl'
classifier = joblib.load('WorkingRF.pkl')

app = Flask(__name__)

@app.route('/')


@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        input_json = request.get_json(force=True)
        dictToReturn = {input_json['desctext']}


        print(dictToReturn)
        my_prediction = classifier.predict(dictToReturn)
        print(my_prediction)
        if(my_prediction==1):
            return "Yes This will be Tredning"
        else:
            return "Sorry This will be not Trending"




if __name__ == '__main__':
	app.run(debug=True)