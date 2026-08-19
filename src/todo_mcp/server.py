from mcp.server.fastmcp import FastMCP
import json
import os

# Initialize the MCP Server
mcp = FastMCP("TodoManager")
TODO_FILE = "todos.json"

# Helper functions to read and write to our local JSON file
def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

# --- MCP TOOLS ---
# These are the actions the AI can take

@mcp.tool()
def add_task(task: str) -> str:
    """Add a new task to the todo list."""
    todos = load_todos()
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    return f"Task '{task}' added successfully."

@mcp.tool()
def list_tasks() -> str:
    """List all tasks in the todo list."""
    todos = load_todos()
    if not todos:
        return "Your todo list is empty."
    result = []
    for i, t in enumerate(todos):
        status = "[x]" if t["completed"] else "[ ]"
        result.append(f"{i}: {status} {t['task']}")
    return "\n".join(result)

@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed using its ID (index)."""
    todos = load_todos()
    if 0 <= task_id < len(todos):
        todos[task_id]["completed"] = True
        save_todos(todos)
        return f"Task {task_id} marked as completed."
    return f"Task ID {task_id} not found."

@mcp.tool()
def delete_task(task_id: int) -> str:
    """Delete a task from the list using its ID."""
    todos = load_todos()
    if 0 <= task_id < len(todos):
        removed = todos.pop(task_id)
        save_todos(todos)
        return f"Task '{removed['task']}' deleted."
    return f"Task ID {task_id} not found."

# --- MCP RESOURCES ---
# This is read-only data the AI can look at anytime

@mcp.resource("todo://summary")
def get_summary() -> str:
    """Get a quick summary of pending vs completed tasks."""
    todos = load_todos()
    completed = sum(1 for t in todos if t["completed"])
    pending = len(todos) - completed
    return f"Total Tasks: {len(todos)}\nCompleted: {completed}\nPending: {pending}"


