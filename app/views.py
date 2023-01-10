from django.shortcuts import render, redirect
from .models import UserInput
from .forms import InputForm, FileForm
import pandas as pd

# Create your views here.
def index(request):

    return render(request, 'app/index.html')

### BAR CHART ###
def bar_chart(request):
    
    amounts = UserInput.objects.all()
    
    if request.method == "POST":
        
        form = InputForm(request.POST)
        file_form = FileForm(request.FILES.get('csv_file'))

        # save our data to database
        if form.is_valid():
            form.save()
            return redirect('barchart')

        elif file_form.is_valid():
            pass
        else:
            # reset the database
            UserInput.objects.all().delete()
            return redirect('barchart')
    else:
        form = InputForm()
        file_form = FileForm()
    
    return render(request, 'app/forms/bar_chart.html', {'amounts': amounts, 'form':form, 'file_form':file_form})

### LINE CHART ###
def line_chart(request):
    
    data = []
    if request.method == "POST":
        
        file_form = FileForm(request.POST, request.FILES)
        
        if file_form.is_valid():
            
            file = request.FILES['file']
            
            if file.endswith('.csv'):
                data = pd.read_csv(file)
                labels = data.columns.values.tolist()
                data = data.values.tolist()
        
    else:
        file_form = FileForm()
        
    return render(request, 'app/forms/line_chart.html', {'file_form':file_form, 'data':data, 'labels':labels})

### PIE CHART ###
def pie_chart(request):
    
    amounts = UserInput.objects.all()
    
    if request.method == "POST":
        form = InputForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('piechart')
        else:
            
            UserInput.objects.all().delete()
            return redirect('piechart')
    else:
        form = InputForm()
    
    return render(request, 'app/forms/pie_chart.html', {'amounts':amounts, 'form':form})
