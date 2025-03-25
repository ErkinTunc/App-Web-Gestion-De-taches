# Collaborative Task Management Web App

> **Project type**: L2 Web Server Coursework  
> **Technology stack**: *(To be completed: Django / Spring / Symfony / etc.)*  
> **Group**: [Name 1] - [Group #], [Name 2] - [Group #]

---

## 📄 Description

This is a collaborative task management web application designed for multi-user environments. It allows authenticated users to manage personal and team tasks with access control and assignment features.

---

## ✅ Main Features

### 🔐 Authentication
- User registration and login using email/password
- Session-based or token-based authentication (depending on implementation)

### 👤 Users
- Name, email, optional description
- One optional associated team
- View other users’ profiles and public tasks

### 👥 Teams
- Create, join, and leave teams
- Each team has a name and a list of members
- Tasks can be assigned to teams

### 📋 Tasks
- Title, description (optional), status (to-do or done)
- Sub-tasks supported
- Assignable to users and/or teams
- Privacy: public (visible to all) or private (creator + assignees only)
- Task operations: create, update, delete, assign, unassign

---

## 📦 Data Models (Entities)

### User
```json
{
  "id": int,
  "name": string,
  "email": string,
  "password": string,
  "description": string?,
  "team_id": int?
}
```

### Team
```json
{
  "id": int,
  "name": string,
  "members": [User]
}
```

### Task
```json
{
  "id": int,
  "title": string,
  "description": string?,
  "status": "todo" | "done",
  "private": boolean,
  "creator_id": int,
  "assigned_users": [User],
  "assigned_teams": [Team],
  "sub_tasks": [Task]
}
```

---

## 🔀 API Routes (Example)

### Auth
- `POST /register` – Create user
- `POST /login` – Authenticate
- `POST /logout` – End session

### User
- `GET /users/:id` – View user profile
- `GET /users/:id/tasks/public` – View public assigned tasks

### Team
- `GET /teams` – List teams
- `POST /teams` – Create team
- `GET /teams/:id` – View team profile
- `POST /teams/:id/join` – Join
- `POST /teams/:id/leave` – Leave

### Task
- `GET /tasks` – List tasks (filtered by visibility)
- `POST /tasks` – Create new task
- `PUT /tasks/:id` – Update task
- `DELETE /tasks/:id` – Delete task
- `POST /tasks/:id/assign/user/:userId` – Assign user
- `POST /tasks/:id/unassign/user/:userId` – Unassign user
- `POST /tasks/:id/assign/team/:teamId` – Assign team
- `POST /tasks/:id/unassign/team/:teamId` – Unassign team

---

## ⚙️ Installation

1. **Clone the project**
```bash
git clone <repo-url>
cd project-folder
```

2. **Install dependencies**
```bash
# For Django (example)
pip install -r requirements.txt
```

3. **Run the server**
```bash
# Django
python manage.py runserver
```

---

## 📁 Project Structure (example)
```
/project-root
  /app
    /models
    /views
    /controllers
  /templates
  /static
  README.md
  requirements.txt
```

---

## 📌 Notes

- Built using an MVC architecture
- Only creators and assignees can access private tasks
- Git is used for version control and collaboration
- Compatible with future extensions (notifications, calendar view, etc.)