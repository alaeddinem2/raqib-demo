from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login,logout
from django.http import  HttpResponse, HttpResponseRedirect



from demo.EmailBackEnd import EmailBackEnd
from demo.models import Driver, InOut, Vehicle
from datetime import datetime
import datetime
# Create your views here.

def login_demo(request):
    return render(request,'demo/login.html')

def home_demo(request):
    today = datetime.datetime.now()
    
    print(today)
    drivers = Driver.objects.all().count()
    
    vehicles = Vehicle.objects.all().count()
    logs = InOut.objects.values('in_out')

    
    print(logs)
    log ={ 'in' : 0 , 'out': 0}
    for e in logs:
        if e['in_out'] == True :
             log['in'] +=1
        else :
             log['out'] +=1    
            
    
    data = { 'drivers' : drivers, 'vehicles': vehicles , 'log' : log}    
    return render(request,'demo/home_content.html',data)
    
def user_login(request):
    if request.method != "POST":
        return HttpResponse("<H2> ")
    else:
        user = EmailBackEnd.authenticate(request,username = request.POST.get("email"),password = request.POST.get('password'))
        if user != None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect("/demo/home")
            #return HttpResponse ("email : "+request.POST.get("email")+"password :"+request.POST.get('password'))
            elif user.user_type =="2":
                return   HttpResponse(" Agent LOGIN !")
            
            
        else:
            messages.error(request,"INVALID LOGIN DETAILS !")
            return HttpResponseRedirect("/")
            #return HttpResponse("<H2> INVALID LOGIN !")

def add_vehicle(request):
    drivers = Driver.objects.all()
    data = {
        "drivers" : drivers
    }
    return render(request,'demo/add_vehicle_template.html',data)
    
def add_vehicle_save(request):
    if request.method != "POST" :
        return HttpResponse("METHOD NOT ALLOWED !")
    else : 
        plate_number = request.POST.get('plate_number')
        name = request.POST.get('name')
        year = request.POST.get('year')
        driver_id = request.POST.get('driver')
        
        try:  
            vehicle = Vehicle(plateNumber=plate_number,name=name,year=year)
            driver_obj = Driver.objects.get(id=driver_id)
            vehicle.driver = driver_obj
            vehicle.save()
            messages.success(request," the Vehicle Added !")
            return HttpResponseRedirect('/demo/add_vehicle')
        except :
            messages.error(request,'Failed to add Vehicle !')
            return HttpResponseRedirect('/demo/add_vehicle')

def manage_vehicle(request):
    vehicles = Vehicle.objects.all()
    data = { 'vehicles': vehicles}
    return render(request,'demo/manage_vehicle_template.html',data)
def vehicle_logs(request,id):
    logs = InOut.objects.filter(vehicle=id).values()
    vehicle = Vehicle.objects.get(id = id)
    print(logs)
    data = { 'logs' : logs,'vehicle' : vehicle }

    return render(request,'demo/vehicle_logs_template.html',data)
    
    

def add_driver(request):
    return render(request,'demo/add_driver_template.html')

def add_driver_save(request):
    if request.method != "POST" :
        return HttpResponse("METHOD NOT ALLOWED !")
    else : 
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        departement = request.POST.get('departement')
        
        try:  
            driver = Driver(name=name,phone=phone,departement=departement)
            driver.save()
            messages.success(request," the Driver Added !")
            return HttpResponseRedirect('/demo/add_driver')
        except :
            messages.error(request,'Failed to add Driver !')
            return HttpResponseRedirect('/demo/add_driver')
    
def manage_drivers(request):
    drivers = Driver.objects.all()
    data = {'drivers' : drivers}
    return render(request,'demo/manage_drivers_template.html',data)

def edit_drivers(request,id):
    driver = Driver.objects.get(id = id)
    data = {'driver': driver}
    return render(request,'demo/edit_drivers_template.html',data)

def edit_driver_save(request):
    if request.method != "POST" :
        return HttpResponse("METHOD NOT ALLOWED !")
    else :
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        departement = request.POST.get('departement')
        driver_id = request.POST.get('driver_id')
        
        try:
            driver = Driver.objects.get(id = driver_id)
            driver.name = name
            driver.phone = phone
            driver.departement = departement
            driver.save()
            messages.success(request," the Driver Edited !")
            return HttpResponseRedirect('/demo/manage_drivers')
        except :
            messages.error(request,'Failed to add Driver !')
            return HttpResponseRedirect('/demo/edit_drivers'+ driver_id)
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/demo")