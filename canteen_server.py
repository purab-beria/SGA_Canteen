from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Veg Sandwich", "price": 50},
    {"id": 2, "name": "Masala Maggi", "price": 40},
    {"id": 3, "name": "Veg Burger", "price": 70},
    {"id": 4, "name": "Cold Coffee", "price": 60}
]

orders = []


@app.route("/")
def home():
    return "Canteen Server is Running!"


@app.route("/menu")
def get_menu():
    return jsonify(menu)


@app.route("/order", methods=["POST"])
def place_order():

    data = request.get_json()

    orders.append(data)

    return jsonify({
        "message": "Order placed successfully!",
        "order": data
    })


if __name__ == "__main__":
    app.run(debug=True)