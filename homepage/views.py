from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
from .models import Service

def home(request):
    services = Service.objects.all()
    set_length = services.count()
    print(set_length)
    #
    # for s in services:
    #    print(s);
    #
    # agu = 'forloop.counter%2 and not forloop.last'
    # items = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8]
    # ]

    return render(request, 'homepage/home.html',{'services' :services })


def service(request):
    return render(request, 'price/home.html')

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    comment = request.POST.get('comment')

    send_mail("%s 's feedback to Setup systems" % (name),
              comment,
              email,
              ['ermiyeasti22@gmail.com'],
              fail_silently=False)


    services = Service.objects.all()
    sent=True
    return render(request, 'homepage/home.html',{'services' :services,'sent':sent,'name':name })

