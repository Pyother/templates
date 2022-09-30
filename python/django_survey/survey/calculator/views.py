import csv
from django.shortcuts import render
from django.http import HttpResponse
from calculator.forms import CandidateForm
from django.views.generic import TemplateView
from multiprocessing import context
from .forms import *
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    
    form = CandidateForm()
    if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_editor(request):
    return render(request, 'editor.html')
    
class EditorView(TemplateView):
    template_name = 'editor.html'

def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = System.objects.create(Empcode=dbframe.Empcode,firstName=dbframe.firstName, middleName=dbframe.middleName,
                                                lastName=dbframe.lastName, email=dbframe.email, phoneNo=dbframe.phoneNo, address=dbframe.address, 
                                                exprience=dbframe.exprience, gender=dbframe.gender, DOB=fromdate_time_obj,
                                                qualification=dbframe.qualification)
                print(type(obj))
                obj.save()
 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})

def export_users_csv(request):
    
     
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="EmployeeData.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Employee Detail'])       
                 
         
        writer.writerow(['Employee Code','Employee Name','Relation Name','Last Name','gender','DOB','e-mail','Contact No' ,'Address' ,'exprience','Qualification'])
 
        users = System.objects.all().values_list('Empcode','firstName' , 'middleName' , 'lastName','gender','DOB','email','phoneNo' ,'address','exprience','qualification')
         
        for user in users:
            writer.writerow(user)
        return response
 
    return render(request, 'importexcel.html')