from flask import Flask, jsonify

# Create the Flask application
# Why:
# Flask(__name__) creates our web application object.
# This object will receive HTTP requests and return responses.
app = Flask(__name__)


# Health-check API
# Why:
# DevOps teams need a simple endpoint to check whether
# the application is running correctly.
@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "ECOMMERCE-APP"
    })


# Root/home API
# Why:
# This gives us a simple endpoint to verify that
# the application itself is reachable.
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ECOMMERCE-APP"
    })


# Start the application
# Why:
# This allows us to run the Flask application directly
# using: python app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
