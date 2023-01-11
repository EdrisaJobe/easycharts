from django.shortcuts import render, redirect
from .models import UserInput, FileInputModel
from .forms import InputForm, FileForm
import pandas as pd

# Create your views here.
def index(request):

    return render(request, 'app/index.html')

### BAR CHART ###
def bar_chart(request):

    data = {}
    labels = []
    file_form = FileForm()

    # grab all model data instance
    values = UserInput.objects.all()
    
    if request.method == "POST":
        
        form = InputForm(request.POST)
        file_form = FileForm(request.POST, request.FILES)
        
        # when the file has been submitted
        if file_form.is_valid():
            file_form.save()

            # we grab the info saved within our media
            files = file_form.cleaned_data.get('files')

            # read the file, turn the data to a map 'list' format, we grab the key which is the first row
            try:
                data = pd.read_excel(files)
                data = data.to_dict(orient='list')
                labels = list(data.keys())
            except:
                return redirect('barchart')

        # save our data to database
        elif form.is_valid():

            try:
                form.save()
                return redirect('barchart')
            except:
                UserInput.objects.all().delete()
                return redirect('barchart')
        else:
            # reset the database
            UserInput.objects.all().delete()
            return redirect('barchart')
    else:
        form = InputForm()
        file_form = FileForm()
    
    return render(request, 'app/forms/bar_chart.html', {'values': values, 'form':form, 'file_form':file_form, 'data':data, 'labels':labels})

### LINE CHART ###
def line_chart(request):

    data = {}
    labels = []
    file_form = FileForm()

    # grab all model data instance
    values = UserInput.objects.all()
    
    if request.method == "POST":
        
        form = InputForm(request.POST)
        file_form = FileForm(request.POST, request.FILES)

        if file_form.is_valid():
            file_form.save()
            files = file_form.cleaned_data.get('files')

            try:
                data = pd.read_excel(files)
                data = data.to_dict(orient='list')
                labels = list(data.keys())
            except Exception as e:
                
                return redirect('linechart')

        # save our data to database
        elif form.is_valid():

            try:
                form.save()
                return redirect('linechart')
            except:
                UserInput.objects.all().delete()
                return redirect('linechart')
        else:
            # reset the database
            UserInput.objects.all().delete()
            return redirect('linechart')
    else:
        form = InputForm()
        file_form = FileForm()
    
    return render(request, 'app/forms/line_chart.html', {'values': values, 'form':form, 'file_form':file_form, 'data':data, 'labels':labels})

### PIE CHART ###
def pie_chart(request):
    
    amounts = UserInput.objects.all()
    
    if request.method == 'POST':
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
