from django.shortcuts import render,redirect
from ..models.employee import Employee

def index(request):
    mem=Employee.objects.all()
    return render(request,'index.html',{'mem':mem})


def indexJson(request):
    mem=Employee.objects.all()

    employee_data = []
    for employee in mem:
        employee_data.append({
            'id': employee.id,
            'firstName': employee.firstName,
            'lastName': employee.lastName,
            'phone': employee.phone
        })
    return JsonResponse({'employees': employee_data})
    


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
    print('zzzzzzzzzzzzzzzzzzzzzzzzzz',mem.__dict__)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['phone']
    mem=Employee.objects.get(id=id)
    mem.firstName=x
    mem.lastName=y
    mem.phone=z
    mem.save()
    return redirect("/")    