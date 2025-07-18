import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#importing the inputScript file used to analyze the URL
import inputScript


#load model
app = Flask(__name__)
model = pickle.load(open(r'C:\Users\itzan\OneDrive\Desktop\SDP Project 10 og (2)\SDP Project 10 og\SDP Project 10\Website\Phishing_Website.pkl', 'rb'))
# model_path = 'D:/SDP Project 10/Website/Flask/Phishing_Website.pkl'
# try:
#     model = pickle.load(open(model_path, 'rb'))
# except FileNotFoundError:
#     print(f"Model file not found at {model_path}. Ensure the path is correct.")


#Redirects to the page to give the user iput URL.
@app.route('/predict')
def predict():
    return render_template('final.html')

#Fetches the URL given by the URL and passes to inputScript
@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    url = request.form['URL']
    print(url)
    checkprediction = inputScript.main(url)
    print(checkprediction)
    prediction = model.predict(checkprediction)
    print(prediction)
    
    output=prediction[0]
    if(output==1):
        pred="Your are safe!! This is a Legitimate Website."
        
    else:
        pred="You are on the wrong site. Be cautious!"
    return render_template('final.html', prediction_text='{}'.format(pred),url=url)

#Takes the input parameters fetched from the URL by inputScript and returns the predictions
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
