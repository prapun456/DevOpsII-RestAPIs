from flask import Flask, request, jsonify, json

app = Flask(__name__)

items = [
    {"name": "cakes", "category": 1, "price": 100, "instock": 200},
    {"name": "hot chips", "category": 2, "price": 50, "instock": 250},
    {"name": "burgers", "category": 3, "price": 99, "instock": 100},
    {"name": "pizzas", "category": 4, "price": 199, "instock": 300},
    {"name": "chocolate", "category": 5, "price": 65, "instock": 400},
]
def _find_next_name(name):
    data = [x for x in items if x['name'] == name]
    return data


@app.route('/items/<name>', methods=["DELETE"])
def delete_item(name: str):

    data = _find_next_name(name)
    if not data:
        return {"error": "items not found"}, 404
    else:
        items.remove(data[0])
        return "items deleted successfully", 200

#REST API
@app.route('/items', methods=["GET"])
def get_item():
    return jsonify(items)

# GET -by name
@app.route('/items/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    return jsonify(data)

@app.route('/items', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request"}, name
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/update_items/<c_name>', methods=["PUT"])
def update_item(c_name):
    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')


    for items in items:
        if c_name == items["name"]:
            items["category"] = int(category)
            items["price"] = int(price)
            items["instock"] = int(instock)
            return jsonify(items)

    else:
        return "Error", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)