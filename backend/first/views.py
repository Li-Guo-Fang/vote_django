from random import sample
from django.shortcuts import render
from django.http import HttpResponse


def show_index(request):
    fruits = [
        '苹果','橘子','香梨','香蕉',
        '火龙果','榴莲','葡萄','西瓜'
    ]
    select_fruits = sample(fruits,3)
    return render(request,'index.html',{'fruits':select_fruits})
