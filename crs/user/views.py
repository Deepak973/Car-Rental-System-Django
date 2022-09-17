from django.shortcuts import render ,redirect
from django.http.response import HttpResponseRedirect
from user.models import user ,booking
from adm.models import location , vehicles
from django.contrib import messages
import random
from django.contrib.sessions.models import Session
from datetime import datetime, date,timedelta
# Create your views here.

def register(request):
    if request.method =="POST":
        f_name = request.POST['fname']
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword =request.POST["c_password"]
        contact_no= request.POST["contact_no"]
        lic_no = request.POST["lic_no"]
        dob = request.POST["dob"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]
        
        if password==cpassword:
            if user.objects.filter(email_id=email).exists():
                messages.success(request,"Email already exists")
                return render(request,'register.html')
            else:
                
                saverecord=user()
                saverecord.fullname=f_name
                saverecord.email_id=email
                saverecord.password=password
                saverecord.contact_no =contact_no
                saverecord.lic_no =lic_no
                saverecord.dob = dob
                saverecord.address =address
                saverecord.city=city
                saverecord.country =country
                saverecord.save()
                messages.success(request,"Registered sucessfully")
                return render(request,'Login.html')
        else:
            messages.success(request,"Password and confirm Password doesnot match")
            return render(request,'register.html')    
    else:
     
      return render(request,'register.html',) 


def login(request):    
    
    if request.method =="POST":
       email = request.POST["email"]
       password = request.POST["pwd"]
         
       if user.objects.filter(email_id=email,password=password).exists():
          request.session['user']= email
          name = user.objects.get(email_id=email)
          return render(request,'home.html',{'name':name})

       else:
        messages.error(request,"Wrong Credentials")
        return render(request,'login.html')    
    
    else: 
       
       return render(request,'login.html',) 


def home(request):
    if request.session.has_key('user'):
      email = request.session.get('user')
      name = user.objects.get(email_id=email)  
      return render(request,'home.html',{'name':name})
    else:
      return render(request,'login.html')     

def logout(request):    

    if request.session.has_key('user'):
       request.session.flush()
       return render(request,'login.html',) 
    
    else:
        return render(request,'login.html') 


'''book a ride starts'''

def bookaridel(request):
     loc= location.objects.all() 
     presentday = datetime.now()
     tomorrow = presentday + timedelta(1)
     print(tomorrow)
     b=tomorrow.strftime("%Y-%m-%dT%H:%M")
     print(b)
    
     return render(request,'bar.html',{'loc':loc ,'now':b})     

def bookaridev(request):
    if request.method =="POST":
       lname = request.POST["location"]
       sdate = request.POST["sdate"]
       edate = request.POST["edate"]
       a = datetime.strptime(str(sdate), '%Y-%m-%dT%H:%M')
       b = datetime.strptime(str(edate), '%Y-%m-%dT%H:%M')
       fdate=a.date()
       tdate=b.date()
       status="booked"
       delta = b - a
       days= delta.days
       seconds=delta.seconds
       hrs =seconds//3600
       hrd =days*24
       ''''''
       total_hrs = hrs+hrd
       check = booking.objects.raw("select * from user_booking where ((from_date >= %s and from_date <= %s) or (to_date >= %s and to_date <= %s)) and status =%s group by veh_id",(a,b,a,b,status))
       print(check)
      
       ''''''
       veh = vehicles.objects.filter(l_name=lname)  
       if veh.exists():
          return render(request,'selectvehicle.html',{'veh':veh,'sdate':sdate,'edate':edate,'hrs':total_hrs,"res":check}) 
       else:
          messages.error(request,"Soory no vehicles available at this location. will reach this location soon")
          return render(request,'selectvehicle.html')   
            
        
def bookvehicle(request,id,sdate,edate):
        a = datetime.strptime(str(sdate), '%Y-%m-%dT%H:%M')
        b = datetime.strptime(str(edate), '%Y-%m-%dT%H:%M')
        fdate=a.date()
        tdate=b.date()
        status="booked"
        res=None
        for check in booking.objects.raw("select * from user_booking where veh_id = %s and ((from_date >= %s and from_date <= %s) or (to_date >= %s and to_date <= %s)) and status =%s",(id,a,b,a,b,status)):
           res =check.veh_id
        if res is not None:
          messages.error(request,"Soory this vehicle is not available on your selected date and time")
          return render(request,'selectvehicle.html') 
        else:    
            for v in vehicles.objects.filter(id=id):
                price =v.price_per_day
            random_num =  random.randint(2345678909800, 9923456789000)
            uniqe_confirm = booking.objects.filter(booking_number=random_num)
            while uniqe_confirm:
                random_num =  random.randint(1, 100000)
                if not vehicles.objects.filter(booking_number=random_num):
                    break
                        
            b_no = random_num
            email = request.session.get('user')
            email_id = email  
            
            a = datetime.strptime(str(sdate), '%Y-%m-%dT%H:%M')
            b = datetime.strptime(str(edate), '%Y-%m-%dT%H:%M')
            delta = b - a
            days= delta.days  
            seconds=delta.seconds
            hrs =seconds//3600
            hrd =days*24
            total_hrs = hrs+hrd
            total_price = int(price) * int(total_hrs)
            saverecord=booking()
            saverecord.booking_number= b_no
            saverecord.email_id= email_id
            saverecord.veh_id= id
            saverecord.from_date =sdate
            saverecord.to_date = edate
            saverecord.from_destination = "location"
            saverecord.status = "payment pending"
            saverecord.total_price= total_price
            saverecord.save()
            record = booking.objects.filter(booking_number=b_no)  
            print(record)
            return render(request,'payment.html',{'th':total_hrs,'record':record,'price':price})

def payment(request):

     if request.method =="POST":
         id =request.POST["bno"]
         status= "booked"
         booking.objects.filter(booking_number=id).update(status= status) 
         messages.success(request,"Booked sucessfully")
         return render(request,'home.html')



def cancelbooking(request ,bookingid):
    cbooking = vehicles.objects.raw('SELECT *  FROM user_booking  inner join adm_vehicles on adm_vehicles.id = user_booking.veh_id  where user_booking.booking_number = %s',(bookingid,))
    for c in cbooking:
        dates = c.from_date    
        amount = c.total_price
        fdate = dates.date()
        cdate = date.today()
        print(fdate)
        print(cdate)
        delta = fdate - cdate
        days= delta.days
        print(days)
        if days==0:
            percent = 0.6
        elif days==1:
           percent = 0.5
        elif days==2:
           percent = 0.3
        elif days==3:
            percent = 0.2
        else:
           percent = 0
        amt_diff = amount*percent  
        print(amt_diff)
        refund_amt = amount - amt_diff
        print(refund_amt)

    return render(request,'canclebooking.html',{'cb':cbooking,'ra':refund_amt}) 
    
def cancelbookingconfirm(request,bookingid,refund_amt):
     
     b = booking.objects.filter(booking_number=bookingid)
     for a in b:
         price=a.total_price
     print(refund_amt)    
     tprice = price - float(refund_amt)
     status = "cancelled"
     booking.objects.filter(booking_number=bookingid).update(status= status,diff_amount =tprice,refund_price=refund_amt)
     messages.success(request,"Booking Cancelled sucessfully,Your money will be refunded in 2-3 working days")
     return render(request,'booked.html')
    
   
def booked(request):
    email = request.session.get('user')
    email_id = email
    status ="booked"
    book = vehicles.objects.raw('SELECT *  FROM user_booking inner join adm_vehicles on adm_vehicles.id = user_booking.veh_id where user_booking.email_id = %s and user_booking.status= %s',(email_id,status))
    return render(request,'booked.html',{'book':book})     

def completed(request):
    email = request.session.get('user')
    email_id = email
    status ="complete"
    book = vehicles.objects.raw('SELECT *  FROM user_booking inner join adm_vehicles on adm_vehicles.id = user_booking.veh_id where user_booking.email_id = %s and user_booking.status= %s',(email_id,status))
    return render(request,'completed.html',{'book':book})      

def cancelled(request):
    email = request.session.get('user')
    email_id = email
    status ="cancelled"
    book = vehicles.objects.raw('SELECT *  FROM user_booking inner join adm_vehicles on adm_vehicles.id = user_booking.veh_id where user_booking.email_id = %s and user_booking.status= %s',(email_id,status))
    return render(request,'cancelled.html',{'book':book})       

def additionalcharges(request,booking_id):
    
    if request.method=="POST":
       charge = request.POST["add"]
       id =request.POST["id"]
       booking.objects.filter(booking_number=id).update(additional_charge= charge)
       messages.success(request,"added sucessfully")
       return render(request,'ahome.html')  
    else:
        booking_id = booking_id
        return render(request,'additionalcharges.html',{'booking_id':booking_id})  


def contactus(request):
       return render(request,'contactus.html')   

