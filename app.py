from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple API key (hardcoded for demo)
API_KEY = "my-secret-key"

# Public API (no authentication)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "App is healthy"
    }), 200


# Protected API (requires API key)
@app.route("/secure", methods=["GET"])
def secure():
    api_key = request.headers.get("x-api-key")

    if api_key != API_KEY:
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "status": "success",
        "message": "You are authenticated"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
