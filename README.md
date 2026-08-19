# Personal To-Do List MCP Server 📝

[![Model Context Protocol](https://img.shields.io/badge/MCP-Server-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://python.org)

A minimalistic and functional Model Context Protocol (MCP) server that provides AI assistants with a robust local To-Do list manager. 

This project follows a professional Python package structure (`src/todo_mcp`).

## ⚡ Features & Capabilities

### 🛠️ Tools
1. **`add_task(task: str)`** - Adds a new task.
2. **`list_tasks()`** - Returns a formatted list of all tasks.
3. **`complete_task(task_id: int)`** - Marks a task as completed.
4. **`delete_task(task_id: int)`** - Permanently removes a task.

### 📊 Resources
- **`todo://summary`** - Read-only dashboard summary of tasks.

## 💾 Storage
Data is stored securely in a local `todos.json` file. It is explicitly ignored in `.gitignore` to protect personal data.

## 📁 Project Structure
```text
├── docs/                      # Learning outcomes and documentation
├── src/
│   └── todo_mcp/              # Core MCP server package
│       ├── __init__.py
│       ├── __main__.py        # Execution entrypoint
│       └── server.py          # Tools and resources logic
├── .gitignore
├── pyproject.toml             # Modern Python package configuration
└── README.md
```

## 🚀 Quickstart

### Installation
Because this project uses the modern `pyproject.toml` standard, you can install it locally using `pip`:
```bash
pip install .
```

### Running Locally (Inspector)
To test the tools in the interactive MCP Inspector UI:
```bash
npx @modelcontextprotocol/inspector python -m src.todo_mcp
```

### Connecting to an AI Client
Add the following to your client's `config.json`:
```json
{
  "mcpServers": {
    "todo-manager": {
      "command": "python",
      "args": ["-m", "src.todo_mcp"]
    }
  }
}
```
*(Ensure you run this from the root of the project).*
