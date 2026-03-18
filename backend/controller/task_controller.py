from app import app,db
from flask import jsonify, request
from models.Task import Task

@app.route("/")
def home():
    return "Home Page"

@app.route("/tasks",methods=['GET'])
def getAllTasks():
    tasks =  Task.query.all()
    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "is_completed": t.is_completed,
            "created_at": t.created_at
        })
    return result

@app.route("/task/<int:id>", methods=['GET'])
def getTask(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description":task.description,
        "is_completed": task.is_completed
    })

@app.route("/task/create", methods=["POST"])
def createTask():
    data = request.get_json()

    task = Task(**data)   # maps title, description, is_completed

    db.session.add(task)
    db.session.commit()

    return {"msg": "Task Created", "id": task.id}, 201

@app.route("/task/update/<int:id>",methods=["PUT"])
def updateTask(id):
    data = request.get_json()
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.title = data.get('title',task.title)
    task.description = data.get('description', task.description)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()

    return {"msg": "Task updated"}

@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"})