from django.db import connection
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from adm.models import login, location, vehicles 
from user.models import user , booking
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from datetime import datetime, timedelta


    


'''admin login'''
def alogin(request):    
    
    if request.method =="POST":
       email = request.POST["email"]
       password = request.POST["pwd"]
         
       if login.objects.filter(username=email,password=password).exists():
        return render(request,'ahome.html')

       else:
        messages.success(request,"Wrong Credentials")
        return render(request,'aminlogin.html')    
    
    else: 
       
       return render(request,'aminlogin.html') 

def ahome(request):
    return render(request,'ahome.html')       


'''adding location start'''
def addlocation(request):
       
    if request.method =="POST":
       pcode = request.POST["pincode"]
       lname = request.POST["lname"]   
       if location.objects.filter(pincode=pcode).exists():
                messages.success(request,"Pincode already exists")
                return render(request,'add_location.html')
       elif location.objects.filter(l_name=lname).exists():
                messages.success(request,"location already exists")
                return render(request,'add_location.html')
       else: 
            saverecord=location()
            saverecord.pincode=pcode
            saverecord.l_name=lname        
            saverecord.save()
            messages.success(request,"Added sucessfully")
            return render(request,'add_location.html')    

    else:
        return render(request,'add_location.html')     
  
    

def viewl(request):
    loc= location.objects.all() 
    return render(request,"viewl.html",{'loc':loc})

def deletel(request , id):
    loc = location.objects.get(id=id)
    loc.delete()
    messages.success(request,"location deleted sucessfully")
    return render(request,'add_location.html')    

def editl(request, id):
    
    loc = location.objects.get(id=id)
    return render(request,'update.html',{'loc':loc})    

def updatel(request, id):
    loc = location.objects.get(id=id)
    if request.method =="POST":
       pcode = request.POST["pincode"]
       lname = request.POST["lname"] 
       if location.objects.filter(pincode=pcode).exists():
                messages.success(request,"Pincode already exists")
                return render(request,'update.html',{'loc':loc})   
       elif location.objects.filter(l_name=lname).exists():
                messages.success(request,"location already exists")
                return render(request,'update.html',{'loc':loc})    
       else:         
            location.objects.filter(id=id).update(pincode=pcode ,l_name =lname)
            messages.success(request,"Updated sucessfully")
            return render(request,'update.html') 
    else:
        return HttpResponseRedirect("not found")

'''adding location end'''

'''adding vehicle start'''

def addvehicle(request):
        
    if request.method =="POST":
        
        for v in vehicles.objects.all():
            vehnos = v.vehicle_no

        vbrand = request.POST["vbrand"]
        lname = request.POST["location"]
        v_name = request.POST["v_name"]
        '''for image'''
        img =request.FILES["img"]
        fs =FileSystemStorage()
        filename = fs.save(img.name, img)
        url =fs.url(filename)
        ''''''
        ppd = request.POST["ppd"]
        ft = request.POST["ft"]
        sc = request.POST["sc"]   
        ac = request.POST["ac"]
        ab = request.POST["ab"]  
        vehno = request.POST["vehno"]   
        vehnoup = vehno.upper()
        if vehnoup==vehnos:
           loc = location.objects.all()
           messages.success(request,"Vehicle with this vehicle no. already exists.")
           return render(request,'add_vehicle.html',{"locs":loc}) 
          
        else:
            saverecord= vehicles()
            saverecord.vehicle_brand= vbrand
            saverecord.l_name = lname
            saverecord.vehicle_name  = v_name  
            saverecord.vehicle_image = url
            saverecord.price_per_day = ppd
            saverecord.fuel_type =ft
            saverecord.seating_capacity =sc
            saverecord.aircondition =ac
            saverecord.airbag =ab
            saverecord.vehicle_no =vehnoup

            saverecord.save()
            messages.success(request,"Added sucessfully")
            return render(request,'add_vehicle.html')    

    else:
        loc = location.objects.all()
        return render(request,'add_vehicle.html',{"locs":loc})     

def viewv(request):
  
    veh= vehicles.objects.all() 
    return render(request,"viewv.html",{'veh':veh})

def editv(request, id):
    for v in vehicles.objects.raw('SELECT id, l_name  FROM adm_vehicles where id =%s',[id]):
          ln = v.l_name

    loc = location.objects.exclude(l_name=ln)
    vec = vehicles.objects.get(id=id)
    return render(request,'updatev.html',{'vec':vec ,'locs':loc})   

def updatev(request, id):
    for v in vehicles.objects.exclude(id=id):
            vehnos = v.vehicle_no
            print(vehnos)
    vec = vehicles.objects.get(id=id)
    if request.method =="POST":
        vbrand = request.POST["vbrand"]
        lname = request.POST["location"]
        v_name = request.POST["v_name"]
        '''for image'''
        img =request.FILES["img"]
        fs =FileSystemStorage()
        filename = fs.save(img.name, img)
        url =fs.url(filename)
        ''''''
        ppd = request.POST["ppd"]
        ft = request.POST["ft"]
        sc = request.POST["sc"]   
        ac = request.POST["ac"]
        ab = request.POST["ab"]  
        vehno = request.POST["vehno"]  
        if vehno==vehnos:
    
           for v in vehicles.objects.raw('SELECT id, l_name  FROM adm_vehicles where id =%s',[id]):
               ln = v.l_name
           messages.success(request,"Vehicle with this vehicle no. already exists.")
           loc = location.objects.exclude(l_name=ln)
           vec = vehicles.objects.get(id=id)
           return render(request,'updatev.html',{'vec':vec ,'locs':loc})   
        else:   
            vehicles.objects.filter(id=id).update(vehicle_brand= vbrand,l_name = lname,vehicle_name  = v_name ,vehicle_image = url,price_per_day = ppd,fuel_type =ft,seating_capacity =sc,aircondition =ac,airbag =ab,vehicle_no =vehno)
            messages.success(request,"Vehicle Updated sucessfully")
            return render(request,'add_vehicle.html') 
    else:
        return HttpResponseRedirect("not found")    

def deletev(request , id):
    veh = vehicles.objects.get(id=id)
    veh.delete()
    messages.success(request,"Vehicle removed sucessfully")
    return render(request,'add_vehicle.html')   

'''adding vehicles end'''      

def viewuser(request):
       
   viewuser= user.objects.all() 
   return render(request,"userdetails.html",{'vu':viewuser})  

def viewuserdetails(request,email_id):
    status="complete"
    status1="booked"
    status2="cancelled"
    book = vehicles.objects.raw('SELECT *  FROM user_booking inner join adm_vehicles on adm_vehicles.id = user_booking.veh_id where user_booking.email_id = %s and (user_booking.status= %s or user_booking.status= %s or user_booking.status= %s)',(email_id,status,status1,status2))
    
    return render(request,"aviewbooking.html",{'book':book})       

def completebooking(request,booking_id):
    status="complete"
    booking.objects.filter(booking_number=booking_id).update(status= status)
    return render(request,"ahome.html")     

def accountingselect(request):
     presentday = datetime.now()
     tomorrow = presentday + timedelta(1)
     print(tomorrow)
     b=tomorrow.strftime("%Y-%m-%dT%H:%M")
     print(b)
    
     return render(request,"accountingselect.html",{'a':b})  
    


def accounting(request):

    sdate = request.POST["sdate"]
    edate = request.POST["edate"]
    a = datetime.strptime(str(sdate), '%Y-%m-%dT%H:%M')
    b = datetime.strptime(str(edate), '%Y-%m-%dT%H:%M')
    status = request.POST["status"]
  
    details = booking.objects.raw('SELECT * from user_booking where status=%s  and (from_date >= %s and from_date <= %s)',[status,a,b]) 
    total_amount = booking.objects.raw('SELECT id, SUM(total_price) as total from user_booking where status="complete" and (from_date >= %s and from_date <= %s)',[a,b])
    booked_amount = booking.objects.raw('SELECT id, SUM(total_price) as btotal from user_booking where status="booked" and (from_date >= %s and from_date <= %s)',[a,b]) 
    diff_amount = booking.objects.raw('SELECT id, SUM(diff_amount) as dtotal from user_booking where status="cancelled" and (from_date >= %s and from_date <= %s)',[a,b])
    add= booking.objects.raw('SELECT id, SUM(additional_charge) as adtotal from user_booking where status="complete" and (from_date >= %s and from_date <= %s)',[a,b])
    return render(request,"accounting.html",{'details':details,'fdate':a,'tdate':b,'ta':total_amount,'da':diff_amount,'ba':booked_amount,'status':status ,'ad':add})   


