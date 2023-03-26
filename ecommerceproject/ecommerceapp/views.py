from django.shortcuts import render
from .models import Contact,Product
from django.contrib import messages
from math import ceil



def index(request):

    allProds = []
    catprods = Product.objects.values('category','id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    

    return render(request,"index.html",params)

def contact(request):
    if request.method=='POST':
        email = request.POST['email']
        Name = request.POST['Name']
        desc = request.POST['desc']
        mycontact = Contact(email=email,Name=Name,desc=desc)
        mycontact.save()
        messages.info(request,'we will get you soon..:)')
    return render(request,'contact.html')



def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request,'profile.html')

