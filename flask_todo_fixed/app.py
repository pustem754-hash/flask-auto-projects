#!/usr/bin/env python3
from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)
todos = []

HTML = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TODO List</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
        }
        h1 { color: #667eea; text-align: center; margin-bottom: 30px; }
        .input-group { display: flex; gap: 10px; margin-bottom: 30px; }
        input { flex: 1; padding: 15px; border: 2px solid #667eea; border-radius: 10px; font-size: 16px; }
        button { padding: 15px 30px; background: linear-gradient(135deg, #667eea, #764ba2); 
                 color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; }
        button:hover { transform: scale(1.05); }
        .todo-list { list-style: none; }
        .todo-item { background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 10px;
                     display: flex; justify-content: space-between; align-items: center; }
        .todo-item.completed { text-decoration: line-through; opacity: 0.5; }
        .todo-text { flex: 1; cursor: pointer; }
        .delete-btn { background: #ef4444; padding: 8px 15px; }
        .empty { text-align: center; color: #999; padding: 40px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 TODO List</h1>
        <div class="input-group">
            <input type="text" id="todoInput" placeholder="Add task..." onkeypress="if(event.key==='Enter')addTodo()">
            <button onclick="addTodo()">Add</button>
        </div>
        <ul class="todo-list" id="todoList"><li class="empty">No tasks yet!</li></ul>
    </div>
    <script>
        let todos = [];
        function loadTodos() {
            fetch('/api/todos').then(r => r.json()).then(data => {
                todos = data;
                const list = document.getElementById('todoList');
                if (todos.length === 0) {
                    list.innerHTML = '<li class="empty">No tasks yet!</li>';
                    return;
                }
                list.innerHTML = todos.map((t, i) => 
                    '<li class="todo-item ' + (t.completed ? 'completed' : '') + '">' +
                    '<span class="todo-text" onclick="toggleTodo(' + i + ')">' + t.text + '</span>' +
                    '<button class="delete-btn" onclick="deleteTodo(' + i + ')">Delete</button></li>'
                ).join('');
            });
        }
        function addTodo() {
            const input = document.getElementById('todoInput');
            if (input.value.trim()) {
                fetch('/api/todos', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: input.value})
                }).then(() => { input.value = ''; loadTodos(); });
            }
        }
        function toggleTodo(i) {
            fetch('/api/todos/' + i + '/toggle', {method: 'POST'}).then(() => loadTodos());
        }
        function deleteTodo(i) {
            fetch('/api/todos/' + i, {method: 'DELETE'}).then(() => loadTodos());
        }
        loadTodos();
    </script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todos.append({'text': data['text'], 'completed': False})
    return jsonify({'success': True})

@app.route('/api/todos/<int:index>/toggle', methods=['POST'])
def toggle_todo(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = not todos[index]['completed']
    return jsonify({'success': True})

@app.route('/api/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return jsonify({'success': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5010))
    app.run(host='0.0.0.0', port=port, debug=False)
