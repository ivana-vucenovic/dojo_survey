from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def process(request):
    if request.method == 'GET':
        return render (request, 'result.html')
    if request.method == 'POST':
        request.session['first_name']=request.POST['first_name']
        request.session['city']=request.POST['city']
        request.session['comment']=request.POST['comment']
        request.session['leng']=request.POST.getlist('leng')
        
    return redirect ('/process')

def index(request):
   
    return render (request, 'django.html')


