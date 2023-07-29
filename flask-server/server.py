import base64
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@app.route('/products', methods=["GET"])
def get_products():
    products = [
        {
            "id": 1,
            "productName": "Frock",
            "price": 999.0,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/1.jpg"),
        },
        {
            "id": 2,
            "productName": "Jeans",
            "price": 1999.0,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/2.jpg"),
        },
        {
            "id": 3,
            "productName": "Shirt",
            "price": 699.0,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/3.webp"),
        },
        {
            "id": 4,
            "productName": "Kurta",
            "price": 499.0,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/4.jpg"),
        },
        {
            "id": 5,
            "productName": "Saree",
            "price": 1999.99,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/5.jfif"),
        },
        {
            "id": 6,
            "productName": "Jump Suit",
            "price": 2999.0,
            "productImage": encode_image("D:/E-commerce/client/src/assets/products/6.jpg"),
        },
    ]
    return jsonify(products)

@app.route('/offers', methods=["GET"])
def get_offers():
    offers=[
        {
            "id": 11,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer1.jpg"),
        },
        {
            "id": 12,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer2.gif"),
        },
        {
            "id": 13,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer3.jpg"),
        },
        {
            "id": 14,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer4.gif"),
        },
        {
            "id": 15,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer5.jpg"),
        },
        {
            "id": 16,
            "offerImage": encode_image("D:/E-commerce/client/src/assets/products/offer6.jpg"),
        },
    ]
    return jsonify(offers)

if __name__ == "__main__":
    app.run(debug=True)
