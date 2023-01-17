from flask import Flask, render_template, url_for, request, jsonify 
import requests
from datetime import *
from dateutil.relativedelta import *
import calendar

application = Flask (__name__)



@application.route("/data/<string:symbol>", methods = ['GET'])
def data(symbol):
    token_id = 'dba09041d3f74d6661a2e620087813c35682f331'
    tingo_url = 'https://api.tiingo.com/tiingo/daily/'+symbol+'?token='+token_id
    
    req = requests.get(tingo_url)
    json_data = req.json();
    json_new = jsonify (json_data)
    return json_new


@application.route("/stock/<string:symbol>", methods = ['GET'])
def stock(symbol):
    token_id = 'dba09041d3f74d6661a2e620087813c35682f331'
    tingo_url = 'https://api.tiingo.com/iex/'+symbol+'?token='+token_id
    
    req = requests.get(tingo_url)
    json_data = req.    json();
    json_new = jsonify (json_data)
    return json_new


@application.route("/news/<string:symbol>", methods = ['GET'])
def news(symbol):
    token_id = '6e16e72a27944e5a9ba21dd5a03fe420'
    news_url = 'https://newsapi.org/v2/everything?apiKey='+token_id+'&q='+symbol
    #print ('In news, I received: '+ symbol);
    req = requests.get(news_url)
    json_data = req.json();
    json_new = jsonify (json_data)
    return json_new



@application.route("/charts/<string:symbol>", methods = ['GET'])
def charts(symbol):
    token_id = 'dba09041d3f74d6661a2e620087813c35682f331'
    TODAY = date.today()
    startDate = TODAY + relativedelta(months=-6)
    tingo_url = 'https://api.tiingo.com/iex/'+symbol+'/prices?startDate='+str(startDate)+'&resampleFreq=12hour&columns=open,high,low,close,volume&token='+token_id
    
    req = requests.get(tingo_url)
    json_data = req.json();
    json_new = jsonify (json_data)
    return json_new



@application.route("/")
@application.route ("/home")
def hello():
    data = {'username':'vishwanath'}
    return application.send_static_file('index.html')


if __name__ == "__main__":
    
    application.debug = True
    application.run()

