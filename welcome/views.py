from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    return render(request,'welcome/home.html')


def level(request):
    #value = request.GET.get('level1')
    a=['rahul','himanshu','avishek','aditya','atal','prince','navin']
    p = random.choice(a)
    l = len(p)
    rule =  'Rule of this game : ' 
    first ='1. We generate a random name' 
    sec = '2. Your task to guess that name' 
    thir = '3. You  have n lives (where n is the length of name )'
    four = '4. If you choose a correct a letter your lives not decrease'
    five =  '5.If you choose incorrect letter your lives decrease '
          
    d={'head':'what is your name ->> ','rule':rule,'first':first,'second':sec,'third':thir,'four':four,'five':five}
    
    return render(request, 'welcome/easy.html',d)