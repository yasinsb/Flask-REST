from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')    

# post

stores = [
    {
        'name':'My Store',
        'items': [
            {
                'name':'Item 1',
                'price': 15.99
            }
        ]

    }
]

@app.route("/store", methods = ['POST'])
def create_store():
    request_data = request.get_json()
    store_names = [store['name'] for store in stores]
    if request_data['name'] not in store_names:
        new_store = {
            'name':request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store)
    return jsonify({'Response':'Store exists'})


# get
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store':store})
    return jsonify({'data':'Error! not such store '+name})

@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'data':'Error! not such store '+name})


@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'data':'Item Error! not such store '+name})




app.run(port=5000)