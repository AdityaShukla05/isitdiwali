from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'isdiwal.html',{
        'day': datetime.now().day,
        'month': datetime.now().month
    })