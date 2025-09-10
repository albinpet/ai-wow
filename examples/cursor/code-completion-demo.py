"""
AI-Powered Todo List Manager
A simple example demonstrating AI-assisted code completion in Cursor

This example shows how to use Cursor's AI features to:
1. Generate boilerplate code
2. Add intelligent completions
3. Suggest improvements and optimizations

Try using Cursor's AI chat (Cmd/Ctrl + K) with prompts like:
- "Add error handling to this code"
- "Optimize this function for better performance"
- "Add type hints to this Python code"
- "Create unit tests for this class"
"""

from datetime import datetime
from typing import List, Optional
import json


class TodoItem:
    """Represents a single todo item with AI-suggested improvements."""
    
    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        self.id = hash(title + str(datetime.now()))
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def mark_complete(self) -> None:
        """Mark this todo item as completed."""
        self.completed = True
        self.completed_at = datetime.now()
    
    def to_dict(self) -> dict:
        """Convert todo item to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }


class TodoManager:
    """Manages a collection of todo items with AI-enhanced functionality."""
    
    def __init__(self):
        self.todos: List[TodoItem] = []
    
    def add_todo(self, title: str, description: str = "", priority: str = "medium") -> TodoItem:
        """Add a new todo item to the list."""
        todo = TodoItem(title, description, priority)
        self.todos.append(todo)
        return todo
    
    def get_todos(self, completed: Optional[bool] = None) -> List[TodoItem]:
        """Get todos, optionally filtered by completion status."""
        if completed is None:
            return self.todos
        return [todo for todo in self.todos if todo.completed == completed]
    
    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """Find a todo item by its ID."""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def complete_todo(self, todo_id: int) -> bool:
        """Mark a todo as completed by ID."""
        todo = self.get_todo_by_id(todo_id)
        if todo and not todo.completed:
            todo.mark_complete()
            return True
        return False
    
    def get_todos_by_priority(self, priority: str) -> List[TodoItem]:
        """Get todos filtered by priority level."""
        return [todo for todo in self.todos if todo.priority == priority]
    
    def export_to_json(self, filename: str) -> None:
        """Export todos to a JSON file."""
        data = {
            "todos": [todo.to_dict() for todo in self.todos],
            "exported_at": datetime.now().isoformat()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_stats(self) -> dict:
        """Get statistics about the todo list."""
        total = len(self.todos)
        completed = len([t for t in self.todos if t.completed])
        pending = total - completed
        
        priority_counts = {}
        for priority in ["low", "medium", "high"]:
            priority_counts[priority] = len(self.get_todos_by_priority(priority))
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "priority_distribution": priority_counts
        }


# Example usage and AI-suggested demonstrations
if __name__ == "__main__":
    # Create a todo manager
    manager = TodoManager()
    
    # Add some example todos
    manager.add_todo("Learn Cursor AI features", "Explore AI chat, code completion, and refactoring", "high")
    manager.add_todo("Write documentation", "Create comprehensive README and examples", "medium")
    manager.add_todo("Set up CI/CD pipeline", "Implement automated testing and deployment", "medium")
    manager.add_todo("Optimize performance", "Profile and improve application speed", "low")
    
    # Mark one as completed
    todos = manager.get_todos()
    if todos:
        manager.complete_todo(todos[0].id)
    
    # Display statistics
    stats = manager.get_stats()
    print("Todo List Statistics:")
    print(f"Total todos: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"Pending: {stats['pending']}")
    print(f"Completion rate: {stats['completion_rate']:.1f}%")
    
    # Export to JSON
    manager.export_to_json("todos_export.json")
    print("\nTodos exported to todos_export.json")

"""
AI Prompt Suggestions for Cursor:

1. "Add input validation to the TodoManager methods"
2. "Create a CLI interface for this todo manager"
3. "Add search functionality to find todos by keyword"
4. "Implement todo categories and tags"
5. "Add due date functionality with reminders"
6. "Create a web API using FastAPI for this todo manager"
7. "Add database persistence using SQLAlchemy"
8. "Implement user authentication and multi-user support"
9. "Add comprehensive error handling and logging"
10. "Create unit tests for all methods"

Try pasting this code into Cursor and experiment with these prompts!
"""