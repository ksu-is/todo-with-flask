from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()
    task_text = request.form["task"]
    tasks.append({"text": task_text, "done": False})
    save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete(task_id):
    tasks = load_tasks()
    tasks[task_id]["done"] = True
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks.pop(task_id)
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
