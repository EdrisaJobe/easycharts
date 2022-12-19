from django.shortcuts import render, redirect
from django.core.management import call_command
from .models import UserInput
from .forms import InputForm

# Create your views here.
def index(request):

    return render(request, 'app/index.html')

### BAR CHART ###
def bar_chart(request):
    
    amounts = UserInput.objects.all()
    
    if request.method == "POST":
        
        form = InputForm(request.POST)
        
        # save our data to database
        if form.is_valid():
            form.save()
            return redirect('barchart')
        else:
            # reset the database
            UserInput.objects.all().delete()
            return redirect('barchart')
    else:
        form = InputForm()
    
    return render(request, 'app/forms/bar_chart.html', {'amounts': amounts, 'form':form})

### LINE CHART ###
def line_chart(request):
    amounts = UserInput.objects.all()
    
    if request.method == "POST":
        
        form = InputForm(request.POST)
        
        # save our data to database
        if form.is_valid():
            form.save()
            return redirect('linechart')
        else:
            # reset the database
            UserInput.objects.all().delete()
            return redirect('linechart')
    else:
        form = InputForm()
    
    return render(request, 'app/forms/line_chart.html', {'amounts': amounts, 'form':form})

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