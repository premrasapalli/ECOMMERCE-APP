from flask import Flask, jsonify

# WHY:
# Create the Flask application object.
# This object receives HTTP requests and sends responses.
app = Flask(__name__)


# WHY:
# We have not created a database yet.
# For now, we are storing product data in a Python list.
# Later, we will move this data into a SQLite database.
products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 70000,
        "category": "Mobile",
        "stock": 10
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 65000,
        "category": "Mobile",
        "stock": 8
    },
    {
        "id": 3,
        "name": "Dell Laptop",
        "price": 55000,
        "category": "Laptop",
        "stock": 5
    }
]


# WHY:
# This health endpoint is used to check whether
# the application is running successfully.
# DevOps monitoring tools can use this endpoint.
@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "ECOMMERCE-APP"
    })


# WHY:
# This is the home endpoint.
# It helps us verify that the application is reachable.
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ECOMMERCE-APP"
    })


# WHY:
# This API returns all available products.
# GET is used because we are retrieving data.
@app.route("/api/products")
def get_products():
    return jsonify(products)


# WHY:
# This API returns details for one specific product.
# The product ID is received from the URL.
#
# Examples:
# /api/products/1
# /api/products/2
@app.route("/api/products/<int:product_id>")
def get_product(product_id):

    # WHY:
    # Search through the products list
    # to find the product with the requested ID.
    for product in products:

        # WHY:
        # Compare the ID from the URL
        # with the ID of each product.
        if product["id"] == product_id:

            # WHY:
            # If the product is found,
            # return its details as JSON.
            return jsonify(product)

    # WHY:
    # If no product matches the requested ID,
    # return a 404 "Not Found" response.
    return jsonify({
        "error": "Product not found"
    }), 404


# WHY:
# Start the Flask development server when
# this file is executed directly using:
#
# python app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
