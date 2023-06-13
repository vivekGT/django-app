from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import Person,Sample
import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import get_user_model
from .models import User,salesEx
def sales_ex(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        # Read the file in binary mode
        raw_data = csv_file.read()

        # Decode the file, ignoring any errors or null bytes
        decoded_file = raw_data.decode('utf-8', errors='ignore').replace('\x00', '')

        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        print(csv_data)
        next (csv_data)


        for row in csv_data:
            print(row)
            # Assuming the CSV file has columns: name, email, age
            
            mspin = int(row[0])
            dse_name = row[1]
            team_leader_name= row[3]
            ageing = row[2]
            enquiry_total =int (row[5])
            test_drive =int(row[6])
            home_visit= int(row[7])
            unit_name = row[4]
            print(mspin)
            print(ageing)
            # Save the data in the database (adjust this part according to your model and database setup)
            # Example using a model called Person:
            sales = salesEx(mspin=mspin, dse_name=dse_name,team_leader_name=team_leader_name,ageing=ageing, enquiry_total=enquiry_total,test_drive=test_drive,home_visit=home_visit,unit_name=unit_name)
            sales.save()
        
        return render(request, 'success.html')
    
    return render(request, 'upload1.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('success')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'um.html')


User = get_user_model()

def some_view(request,user_n):
    user = User.objects.get(username=user_n)  # Replace 'example' with the actual username or appropriate lookup
    user_role = user.role  # Access the 'role' field of the user
    return user_role
    # Rest of the view logic



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            check_user = authenticate(request, username=username, password=password)
            if check_user is not None:
               login(request, check_user)
            #    return redirect('admin')
               usr_role=some_view(request,user_n=username)
               if usr_role == 'client_admin':
                   return redirect ('client_admin_dashboard')
               elif usr_role == 'tl':
                   return redirect ('sales_dashboard')
               elif usr_role == 'admin':
                   return redirect("Analytics")
               elif usr_role == 'user':
                   return redirect('sales_homepage')
            
            
           
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def admin_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'admin_dashboard.html')

def client_admin_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'client_admin_dashboard.html')

def sales_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'sales_homepage.html')

def user_dashboard(request):
    team_all=TeamLeaderData.objects.all()
    return render (request,"user_dashboard.html",{"team_all":team_all})
import csv
from django.shortcuts import render
from .models import TeamLeaderData
from datetime import datetime
def team(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        # Read the file in binary mode
        raw_data = csv_file.read()

        # Decode the file, ignoring any errors or null bytes
        decoded_file = raw_data.decode('utf-8', errors='ignore').replace('\x00', '')

        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        print(csv_data)
        next (csv_data)


        for row in csv_data:
            print(row)
            # Assuming the CSV file has columns: name, email, age
            
            team_leader_name= row[0]
            team_leader_territory = row[1]
            per_day_asking = float(row[2])
            enquiry_total = int(row[3])
            test_drive_percentage =int(row[4])
            home_visit_percentage = int(row[5])
            
            # Save the data in the database (adjust this part according to your model and database setup)
            # Example using a model called Person:
            team_leader_data = TeamLeaderData(team_leader_name=team_leader_name, team_leader_territory= team_leader_territory, per_day_asking= per_day_asking,enquiry_total= enquiry_total,test_drive_percentage= test_drive_percentage,home_visit_percentage=home_visit_percentage)
            team_leader_data.save()
        
        return render(request, 'success.html')
    
    return render(request, 'upload1.html')
def Please_upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        # Read the file in binary mode
        raw_data = csv_file.read()

        # Decode the file, ignoring any errors or null bytes
        decoded_file = raw_data.decode('utf-8', errors='ignore').replace('\x00', '')

        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        print(csv_data)
        next (csv_data)


        for row in csv_data:
            print(row)
            # Assuming the CSV file has columns: name, email, age
            
            Model = row[0]
            DMS_Stock = int(row[1])
            WS_TGT = int(row[2])
            WS_ACH =int(row[3])
            BAL_WS = int(row[4])
            Total_Probable_Stock = int(row[5])
            print(Model)
            print(DMS_Stock)
            print(WS_TGT)
            print(WS_ACH)
            print(BAL_WS)
            print(Total_Probable_Stock)
            # Save the data in the database (adjust this part according to your model and database setup)
            # Example using a model called Person:
            sample = Sample(Model=Model, DMS_Stock=DMS_Stock, WS_TGT= WS_TGT, WS_ACH= WS_ACH,BAL_WS= BAL_WS,Total_Probable_Stock= Total_Probable_Stock)
            sample.save()
        
        return render(request, 'success_csv.html')
    
    return render(request, 'upload1.html')


from django.shortcuts import render
from django.db.models import Sum
from .models import Sample
def analytics_dash(request):
    analytics_sample=Sample.objects.all()
    team_data=TeamLeaderData.objects.all()
    sales_all=salesEx.objects.all()

    
    return render(request, 'Analytics.html',{'analytics_sample':analytics_sample, 'team_data':team_data,'sales_data':sales_all})

from django.shortcuts import render

def data_analytics_view(request):
    return render(request, 'data-analytics2.html')

def sales_table(request):
    sales_data1={}
    sales_data=salesEx.objects.all()
    if request.method=="GET":
            user_n = request.GET.get('event')
            print(user_n)
            for event in sales_data:
                if event.dse_name == user_n:
                    sales_data1.update({"id":event.id,"team_leader_name":event.team_leader_name,'dse_name':event.dse_name,"home_visit":event.home_visit,"test_drive":event.test_drive,
                                "ageing":event.ageing,"enquiry_total":event.enquiry_total,'mspin':event.mspin,'unit_name':event.unit_name}) 
            
    return JsonResponse(sales_data1,safe=False) 


def restricted_view(request):
    # Logic for the restricted view
    return render(request, 'restricted.html')


def logout_view(request):
    logout(request)
    return redirect("login")

def usermanagement (request):
    all_details=User.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('um')
    else: 
        form = RegistrationForm()
   
    return render(request, 'um.html', {'all_details': all_details,'form': form})
def billing_summary(request):
    return render(request,"billing.html")
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
def header(request):
    try:
        if request.method=="POST":
            user_n = request.POST.get('username')
            data = {
                "username": user_n
            }
           

            return render(request, 'header.html', data)
    except:
        data = {
                "username": "User"
            }
        return render(request, 'header.html', data) 
def team_scorecard(request):
    team_all=TeamLeaderData.objects.all()
    return render (request,"user_dashboard.html",{"team_all":team_all})

def teamleaderdetails(request):
     team_data1 = {}
     team_data=TeamLeaderData.objects.all()
     if request.method=="GET":
            user_n = request.GET.get('event')
            print(user_n)
            for event in team_data:
                if event.team_leader_name == user_n:
                    team_data1.update({"id":event.id,"team_leader_name":event.team_leader_name,'team_leader_territory':event.team_leader_territory,"home_visit_percentage":event.home_visit_percentage,"test_drive_percentage":event.test_drive_percentage,
                                "per_day_asking":event.per_day_asking,"enquiry_total":event.enquiry_total})
            
            
     return JsonResponse(team_data1,safe=False)   


    
def sales_analytics_view(request):
    sales_all=salesEx.objects.all()
   
    return render(request,'sales_dashboard.html',{'sales_all':sales_all})

from django.shortcuts import render
from .forms import CSVUploadForm
from .models import TeamLeaderData, Sample, salesEx





def vechicledetails(request):
     vechicle_data1 = {}
     vechicle_data=Sample.objects.all()

     if request.method=="GET":
            user_n = request.GET.get('event')
            print(user_n)
            for event in vechicle_data:
                if event.Model == user_n:
                    vechicle_data1.update({"id":event.id,"Model":event.Model,'WS_TGT':event.WS_TGT,"WS_ACH":event.WS_ACH,"Total_Probable_Stock":event.Total_Probable_Stock,
                                "BAL_WS":event.BAL_WS,'DMS_Stock':event.DMS_Stock})
        
     return JsonResponse(vechicle_data1,safe=False)        
     


def unique_tl(request): 
    return render (request,'uniquetl.html')

def unique_sales(request):
    return render (request,'uniquesales_ex.html')







