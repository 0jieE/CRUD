from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *

def fruits_table (request):
    fruits = Fruits.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'fruits/list.html', context)

def add_fruit(request):
    if request.method == 'POST':
        form = AddFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fruits')
    else:
        form = AddFruitForm()
    context = {
        'form':form
    }
    return render(request, 'fruits/add.html', context)

def edit_fruit(request, pk):
    fruit = get_object_or_404(Fruits, pk=pk)
    if request.method == 'POST':
        form = AddFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('fruits')
    else:
        form = AddFruitForm(instance=fruit)
    context = {
        'form':form
    }
    return render(request, 'fruits/edit.html', context)

def delete_fruit(request, pk):
    fruit = get_object_or_404(Fruits, pk=pk)
    if request.method == 'POST':
        fruit.delete()
        return redirect('fruits')
    else:
        context = {
            'fruit':fruit
        }
    return render(request, 'fruits/delete.html', context)