from fastapi import FastAPI, Request
from model import Task
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
tasks = {}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    name: str = ""
    return templates.TemplateResponse("root.html", {"request": request, "tasks": name})


@app.get("/tasks", response_class=HTMLResponse)
async def show_all_tasks():
    global tasks
    return templates.TemplateResponse("root.html", {"request": tasks, "tasks": tasks})


# Makes a table with all tasks.
@app.get("/tasks/{id}", response_class=HTMLResponse)
async def show_one_task(id: int, request: Request):
    global tasks
    try:
        response = {id: tasks[id]}
        return templates.TemplateResponse("root.html", {"request": request, "tasks": response})
    except LookupError:
        return "<h1> NO TASK FOUND </h1>"


# Adds new task.
@app.post("/tasks", response_class=HTMLResponse)
async def add_task(Name: str, Description: str, Status: bool, request:Request):
    global tasks
    task = Task(Name=Name, Description=Description, Status=Status)
    tasks[len(tasks) + 1] = task
    return templates.TemplateResponse("root.html", {"request": request, "tasks": {(len(tasks) + 1): task}})


# Update a task.
@app.put("/tasks/{id}", response_class=HTMLResponse)
async def update_task(id: int, Name: str, Description: str, Status: bool, request:Request):
    global tasks
    try:
        temp = tasks[id]
        temp.Name = Name
        temp.Description = Description
        temp.Status = Status
        tasks[id] = temp
        return templates.TemplateResponse("root.html", {"request": request, "tasks": temp})
    except LookupError:
        return "<h1> NO TASK FOUND </h1>"


# Delete a task.
@app.delete("tasks/{id}", response_class=HTMLResponse)
async def delete_task(id: int, request:Request):
    global tasks
    try:
        tasks[id]
        tasks.pop(id)
        return templates.TemplateResponse("root.html", {"request": request, "tasks": temp})
    except LookupError:
        return "<h1> NO TASK FOUND </h1>"

