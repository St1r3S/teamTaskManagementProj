import base64
import io

# import matplotlib.pyplot as plt
# import openpyxl
from django.shortcuts import render, redirect

from teamTaskManager.dtos import TaskDTO, WorkerDTO
from teamTaskManager.forms import TaskForm, WorkerForm
from teamTaskManager.models import Task, Worker


# Return all tasks data
def task_list(request):
    tasks = list()
    for task in Task.objects():
        tasks.append(TaskDTO(task.id.__str__(), task.name, task.additional_info, task.priority, task.is_completed).__dict__)
    return render(request, "task-list.html", {'tasks': tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.data
            task = Task()
            task.name = form_data.get("name")
            task.additional_info = form_data.get("additional_info")
            task.priority = form_data.get("priority")
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task-create.html', {'form': form})


def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(initial={'name': task.name, 'additional_info': task.additional_info, 'priority': task.priority})
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.data
            task.name = form_data.get("name")
            task.additional_info = form_data.get("additional_info")
            task.priority = form_data.get("priority")
            task.save()
            return redirect('task-list')
    return render(request, 'task-update.html', {'form': form})


def task_delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('task-list')


def task_toggle(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task-list')


# ////////////////////////////////////////////////////////////////////////////////////////

def worker_list(request):
    workers = list()
    for worker in Worker.objects():
        workers.append(WorkerDTO(worker.id.__str__(), worker.first_name, worker.last_name, worker.role, worker.is_busy).__dict__)
    return render(request, "worker-list.html", {'workers': workers})


def worker_create(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form_data = form.data
            worker = Worker()
            worker.first_name = form_data.get("first_name")
            worker.last_name = form_data.get("last_name")
            worker.role = form_data.get("role")
            worker.save()
            return redirect('worker-list')
    else:
        form = WorkerForm()
    return render(request, 'worker-create.html', {'form': form})


def worker_update(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    form = WorkerForm(initial={'first_name': worker.first_name, 'last_name': worker.last_name, 'role': worker.role})
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form_data = form.data
            worker.first_name = form_data.get("first_name")
            worker.last_name = form_data.get("last_name")
            worker.role = form_data.get("role")
            worker.save()
            return redirect('worker-list')
    return render(request, 'worker-update.html', {'form': form})


def worker_delete(request, worker_id):
    Worker.objects.get(id=worker_id).delete()
    return redirect('worker-list')


def worker_toggle(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    worker.is_busy = not worker.is_busy
    worker.save()
    return redirect('worker-list')
