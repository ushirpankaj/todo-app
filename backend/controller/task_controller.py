from app import app,db
from flask import jsonify
from models.Task import Task

@app.route("/")
def home():
    return "Home Page"

@app.route("/tasks",methods=['GET'])
def getAllTasks():
    return Task.query.all()

@app.route("/task/<int:id>", methods=['GET'])
def getTask(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    })

@app.route("/task/create", methods=["POST"])
def createTask():
    pass


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"})