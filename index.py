from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {
        'name': 'fish',
        'category': 1,
        'price': 20.5,
        'instock': 200
    },
    {
        'name': 'hotdog',
        'category': 2,
        'price': 30.5,
        'instock': 150
    }
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET an item by name
@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    for item in items:
        if item['name'] == name:
            return jsonify(item)
    return jsonify({'message': 'Item not found'})

# CREATE an item
@app.route('/items', methods=['POST'])
def create_item():
    item = {
        'name': request.json['name'],
        'category': request.json['category'],
        'price': request.json['price'],
        'instock': request.json['instock']
    }
    items.append(item)
    return jsonify({'message': 'Item created', 'item': item})

# UPDATE an item
@app.route('/items/<string:name>', methods=['PUT'])
def update_item(name):
    for item in items:
        if item['name'] == name:
            item['category'] = request.json['category']
            item['price'] = request.json['price']
            item['instock'] = request.json['instock']
            return jsonify({'message': 'Item updated', 'item': item})
    return jsonify({'message': 'Item not found'})

# DELETE an item
@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    for item in items:
        if item['name'] == name:
            items.remove(item)
            return jsonify({'message': 'Item deleted'})
    return jsonify({'message': 'Item not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)