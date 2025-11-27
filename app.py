from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
        message="Hello from Flask on Kubernetes!",
        status="ok"
    )

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    # For local testing only; in Docker/K8s we use gunicorn or `flask run`
    app.run(host="0.0.0.0", port=5000, debug=True)
