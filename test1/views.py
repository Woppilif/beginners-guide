from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, redirect
from test1.forms import MessagesForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MessagesForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("Ok")
            return redirect("test1:index")
    form = MessagesForm()
    return render(request,"index.html",{"form":form})

def index_base(request):
    return HttpResponse("Ok ",status=200)