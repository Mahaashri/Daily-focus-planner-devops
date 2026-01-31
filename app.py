from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/')
def home():
    return render_template('index.html')

# Add Task
@app.route('/add_task', methods=['POST'])
def add_task():
    global task_id
    data = request.json
    task = {
        "id": task_id,
        "task": data["task"],
        "energy": data["energy"],
        "status": "Pending"
    }
    tasks.append(task)
    task_id += 1
    return jsonify(tasks)

# Update Task
@app.route('/update_task', methods=['PUT'])
def update_task():
    data = request.json
    for t in tasks:
        if t["id"] == data["id"]:
            t["task"] = data.get("task", t["task"])
            t["energy"] = data.get("energy", t["energy"])
            t["status"] = data.get("status", t["status"])
    return jsonify(tasks)

# Delete Task
@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return jsonify(tasks)

# Get Tasks
@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)

# UNIQUE Focus Generator
@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    active_tasks = [t for t in tasks if t["status"] != "Completed"]

    timeline = []
    productive = 0

    for t in active_tasks:
        if t["energy"] == "High":
            focus = 45
        elif t["energy"] == "Medium":
            focus = 30
        else:
            focus = 20

        timeline.append({
            "task": t["task"],
            "type": "Focus",
            "duration": focus
        })
        timeline.append({
            "task": "Break",
            "type": "Break",
            "duration": 10
        })

        productive += focus

    total_time = productive + (len(active_tasks) * 10)
    score = round((productive / total_time) * 100, 2) if total_time else 0

    return jsonify({
        "timeline": timeline,
        "score": score
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

