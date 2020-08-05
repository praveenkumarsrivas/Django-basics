from django.shortcuts import render
from django.contrib import messages
from feedapp.models import Feedback
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def feedback(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        rate=request.POST.get('rate')
        suggestion=request.POST.get('suggestion')
        best=request.POST.get('best')
        worst = request.POST.get('worst')
        if len(name) < 2 or len(number) < 10 or len(email) < 5 or (rate < 1 and rate > 5):
            message.warning(request, 'Invalid Entries')
        else:
            connect = Feedback(name=name, email=email, rate=rate, suggestion=suggestion, best=best, worst=worst, date=datetime.now())
            connect.save()
            message.success(request,'Thanks for your feedback!')
    return render(request,'feedback.html')