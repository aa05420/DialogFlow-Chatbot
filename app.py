# # save this as app.py
# from flask import Flask
# from flask import request
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"


# @app.route('/webhook',methods=['POST'])
# def webhook():
#     req = request.get_json(force=True)
#     print(req)

#     #process 
#     return {
#         'fulfillmentText':'Hello'
#     }

from flask import Flask, request, jsonify
import requests
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json(force=True)
    print(req) 
    order_id = req.get('queryResult').get('parameters')['orderId']
    print(order_id)

    try:
        # Call the external API to fetch shipment date
        api_url = f'https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus'
        # response = requests.post(api_url).json()
        response = requests.post(url=api_url, data={"orderId": str(order_id)}).json()

        print(response)
        shipment_date = response.get('shipmentDate')
        parsed_shipment_date = datetime.strptime(shipment_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        shipment_date = parsed_shipment_date.strftime("%m-%d-%Y %H:%M:%S")

        print(shipment_date)
        if shipment_date:
            
            fulfillment_text = f"The shipment for order {order_id} is scheduled for {shipment_date} UTC."
        else:
            fulfillment_text = "Shipment date not available."
    except Exception as e:
        print("Error:", e)
        fulfillment_text = "Sorry, an error occurred while processing your request."

    print(fulfillment_text)
    return {
        'fulfillment_text':fulfillment_text
        
    }

