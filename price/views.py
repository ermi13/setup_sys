from django.shortcuts import render
from .models import Discount
from homepage.models import Plan
# Create your views here.


def price(request, name):
    plan = Plan.objects.filter(service__name= name)
    size = plan.count()

    print(size)

    print(name)
    return render(request, 'price/price.html',{'name' :name, 'plans':plan , 'count':size })

