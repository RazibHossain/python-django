from django.shortcuts import render,redirect
from .models import Employee
import sqlite3

def index(request):
    mem=Employee.objects.all()

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute("SELECT * FROM employee_employee")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    conn.close()

    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['phone']
    mem=Employee(firstName=x,lastName=y,phone=z)
    mem.save()
    return redirect("/")
def delete(request,id):
    mem=Employee.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Employee.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Employee.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.phone=z
    mem.save()
    return redirect("/")    