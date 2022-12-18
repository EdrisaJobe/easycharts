from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'app/index.html')

def bar_chart(request):

    return render(request, 'app/forms/bar_chart.html')