from django.shortcuts import render
from .forms import ContactForm


def showpage(request):
    F=ContactForm()
    return render(request,'Contact.html',{'form':F})

def handledForm(request):
    if request.method=='POST':
        F=ContactForm(request.POST)
    if F.is_valid():
        data=F.cleaned_data
        return render(request,'showdata.html',data)
    else:
        return render(request,'Contact.html',{'Form':F})
