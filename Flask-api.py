from flask import Flask, request, jsonify

app = Flask(__name__)

items = {}

@app.route('/data', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'id' in data and 'name' in data:
        item_id = data['id']
        item_name = data['name']
        items[item_id] = item_name
        return jsonify({"Info": "Item added successfully."}), 201
    else:
        return jsonify({"Info": "Invalid request data."}), 400

@app.route('/del/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({"Info": f"Item {item_id} deleted successfully."})
    else:
        return jsonify({"Info": f"Item {item_id} not found."}), 404

if __name__ == '__main__':
    app.run()
