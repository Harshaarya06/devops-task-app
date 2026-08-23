from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "completed": True
    },
    {
        "id": 2,
        "title": "Learn Kubernetes",
        "completed": False
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Task Manager",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )