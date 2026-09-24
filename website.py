import requests

url = "http://127.0.0.1:5000/menu"

response = requests.get(url)

if response.status_code == 200:

    menu = response.json()

    print("CANTEEN MENU")
    print("--------------------")

    for item in menu:
        print(item["id"], "-", item["name"], "- ₹", item["price"])

    print("\nPlacing an order...")

    order = {
        "customer": "Purab",
        "item": "Veg Sandwich",
        "quantity": 2
    }

    order_url = "http://127.0.0.1:5000/order"

    order_response = requests.post(order_url, json=order)

    print(order_response.json())

else:
    print("Failed to get menu")