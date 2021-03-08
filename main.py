from secret import *

import requests
from flask import Flask, render_template
app = Flask(__name__)


# 1. get raw json merchant data from API
merchant_list_raw = requests.get(api_list_all_merchants, 
                            headers = {'FApiToken': api_token, 'accept': 'application/json'},
                            params = {'FCanteenId': technoedge_aircon_id}
                            ).json()

# 2. define class for Merchant objects, to store only the required info
class Merchant:
    # contains info about merchant name, logo, id.
    def __init__(self, name, logo_url, iden):  
        self.name = name  
        self.logo_url = logo_url
        self.iden = iden

# 3. define array to store Merchant objects
merchant_list = []

# 4. create Merchant objects and store in list
for x in range (0,len(merchant_list_raw['listData'])):
    name = merchant_list_raw['listData'][x]['FMerchantName']
    logo_url = merchant_list_raw['listData'][x]['Imgs'][0]['FUrl']
    iden = merchant_list_raw['listData'][x]['FMerchantId']
    merchant_list.append(Merchant(name, logo_url, iden))

# 5. define class for FoodList objects, to store only the required info
class FoodList:
    # TODO: extract out relevant attributes (foodcat, food.foodname, food.price)
    def __init__(self, data):  
        self.data = data

# 6. define array to store FoodList objects
food_list = []

# 7. create FoodList objects and store in list
for x in range (0,len(merchant_list)):
    food_list_raw = requests.get(api_list_food_by_category, 
                                headers = {'FApiToken': api_token, 'accept': 'application/json'},
                                params = {'FMerchantId': merchant_list[x].iden}
                                ).json()
    food_list.append(FoodList(food_list_raw['listData']))


# TODO: find out if its possible to not repeat the @app.route so many times

# Stall 0: Western
@app.route('/stall_zero', methods=['GET'])
def display_menu_zero():
    return render_template('menu.html', r = food_list[0].data)

# Stall 1: Nasi Padang
@app.route('/stall_one', methods=['GET'])
def display_menu_one():
    return render_template('menu.html', r = food_list[1].data)

# Stall 2: Vegetarian
@app.route('/stall_two', methods=['GET'])
def display_menu_two():
    return render_template('menu.html', r = food_list[2].data)

# Stall 3: Ma La Xiang Guo
@app.route('/stall_three', methods=['GET'])
def display_menu_three():
    return render_template('menu.html', r = food_list[3].data)

# Stall 4: Indian Cuisine
@app.route('/stall_four', methods=['GET'])
def display_menu_four():
    return render_template('menu.html', r = food_list[4].data)

# Stall 5: Chinese Mixed Rice
@app.route('/stall_five', methods=['GET'])
def display_menu_five():
    return render_template('menu.html', r = food_list[5].data)

# Stall 6: Drinks & Snacks
@app.route('/stall_six', methods=['GET'])
def display_menu_six():
    return render_template('menu.html', r = food_list[6].data)

# Stall 7: Fruits & Juices
@app.route('/stall_seven', methods=['GET'])
def display_menu_seven():
    return render_template('menu.html', r = food_list[7].data)

# Stall 8: Taiwan Ichiban
@app.route('/stall_eight', methods=['GET'])
def display_menu_eight():
    return render_template('menu.html', r = food_list[8].data)

# Stall 9: Ramen & Fish Soup
@app.route('/stall_nine', methods=['GET'])
def display_menu_nine():
    return render_template('menu.html', r = food_list[9].data)
