from django.shortcuts import render

# Create your views here.
def happy(request):
    return render(request,'index.html')
def happy2(request):
    return render(request,'index2.html')