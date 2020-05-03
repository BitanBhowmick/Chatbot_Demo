from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import json
import apiai

CLIENT_ACCESS_TOKEN = '2c6d9f0a0e174ad4aa510b7ccb1a4ef1'

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('test.html')

@app.route('/',methods=['POST'])
def process():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    req = ai.text_request()
    user_input=request.form['user_input']
    req.query = user_input
    response = json.loads(req.getresponse().read())

    #print (response["result"]["parameters"])
    result = response['result']
    fulfillment = result['fulfillment']
    
    print('bot: ' + fulfillment['speech'])
    #print("Friend: "+bot_response)
    return render_template('test.html',user_input=user_input,
            bot_response=fulfillment['speech']
            )
        


if __name__=='__main__':
	app.run(debug=True)
