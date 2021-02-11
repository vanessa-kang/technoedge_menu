from secret import api_token

import requests
from flask import Flask, render_template
app = Flask(__name__)

url = 'https://food.nus-apps.com/smart-dining/interface/user/listFoodByCategory'
merchant_id = '402880e5762b562c01762b563fb60019'

# renders index.html
@app.route('/', methods=['GET'])
def hello_world():
    r = requests.get(url, 
                     headers = {'FApiToken': api_token, 'accept': 'application/json'},
                     params = {'FMerchantId': merchant_id}
                     ).json()
    return render_template('index.html', r = r)

# # renders menu.html
# @app.route('/menu', methods=['GET'])
# def display_menu():
#     r = requests.get(url, 
#                      headers = {'FApiToken': 'M8vU9n293Lu197T', 'accept': 'application/json'},
#                      params = {'FMerchantId': '402880e5762b562c01762b563fb60019'}
#                      ).json()
#     # return r['listData'][1]['foods'][0]['FFoodName'] + str(r['listData'][1]['foods'][0]['FPrice'])
#     return render_template('menu.html', r = r)