from django.shortcuts import render,redirect
from .models import Patient ,ClinicalData
from .forms import ClincalDataForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

class PatientListView(ListView):
    model= Patient     

class PatientCreateView(CreateView):
    model=Patient 
    success_url = reverse_lazy('index')
    fields=['firstName','lastName','age']  
    
class PatientUpdateView(UpdateView):
    model=Patient   
    success_url = reverse_lazy('index')
    fields=['lastName','firstName','age'] 
    
class PatientDeleteView(DeleteView):
    model=Patient   
    success_url = reverse_lazy('index')     
    
    
def addData(request,**kwargs):
    form=ClincalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form=ClincalDataForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            
            form.save()
            return redirect('/')
    
    return render(request,'clinicalsApp/clinicalData_form.html' ,{'form':form,'patient':patient})
    
 
def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData=[]
    
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightandweight=eachEntry.componentValue.split('/')
            if len(heightandweight)>1:
                feetToMeters=float(heightandweight[0]) * 0.4536
                BMI=(float(heightandweight[1]))/(feetToMeters*feetToMeters)
                bmiEntry=ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)   
    
    return render(request,'clinicalsApp/generateReport.html',{'data':responseData})
        
    
