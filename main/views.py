from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume.objects.create(user=user, food_consumed=consume)

    return render(request, 'main/index.html', {"foods": foods, "consumed_food": consumed_food})

def delete(request, pk):
    delete_consume = Consume.objects.get(id=pk)
    if request.method == "POST":
        delete_consume.delete()
        return redirect('/')
    return render(request, 'main/delete.html')
