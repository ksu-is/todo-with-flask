# todo-with-flask
simple todo manager project in flase
# 🛣 Project Roadmap: Simple To-Do List Manager (Flask)

This roadmap outlines the development plan for a web-based To-Do List Manager using Python and Flask. The project is divided into 3 sprints, each focusing on different aspects of development.

---

##  Sprint 1: Core Functionality (Week 1)

###  Goal:
Build the basic functionality of the to-do list, ensuring task persistence and essential CRUD operations.

### Tasks:
- [x] Set up project structure and GitHub repo
- [x] Create Flask app (`app.py`) with basic routing
- [x] Implement file-based storage using JSON
- [x] Add task: form submission and POST route
- [x] Display tasks on the homepage using Jinja2 templates
- [x] Delete task feature (GET route)
- [x] Mark task as complete
- [ ] Test core functionality

---

##  Sprint 2: UI and Experience (Week 2)

###  Goal:
Improve the visual design and user experience of the app.

### Tasks:
- [x] Create reusable base HTML template (`base.html`)
- [x] Design `index.html` with input field, buttons, and task list
- [x] Add CSS for styling via `static/style.css`
- [ ] Improve visual feedback for completed tasks (e.g., strikethrough or icons)
- [ ] Add flash messages (task added, deleted, completed)
- [ ] Add input validation (empty task prevention)
- [ ] Refactor code for readability (helper functions)

---

## 🚀 Sprint 3: Optional Features & Final Touches (Week 3)

###  Goal:
Add advanced features, polish the app, and prepare for final submission/demo.

### Tasks:
- [ ] Add task priority (e.g., dropdown: High, Medium, Low)
- [ ] Add optional due date for tasks
- [ ] Sort tasks by due date or priority
- [ ] Add filtering (e.g., show only incomplete or completed tasks)
- [ ] Add button to clear completed tasks
- [ ] Add error handling for file read/write
- [ ] Final code cleanup and comments
- [ ] Update `README.md` with setup and usage instructions
- [ ] Final testing and presentation readiness

---

##  Notes
- Each sprint builds on the previous.
- JSON is used for data storage instead of a database for simplicity.
- Flask templates (Jinja2) provide dynamic rendering of tasks.
- CSS will be kept simple and minimalistic.
