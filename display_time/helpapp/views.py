from django.http import HttpResponse
from django.shortcuts import render , HttpResponse
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d" , gmtime()),"date" : strftime("%H:%M %p" , gmtime())}
    return render(request,'index.html', context)
