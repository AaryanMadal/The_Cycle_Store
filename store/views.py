from django.shortcuts import render,HttpResponse

from .models import *
# Create your views here.
def index(request):
    allCycles=[]
    catCycles=Cycles.objects.values('Category','Cycle_id')
    cats={item['Category'] for item in catCycles}
    print(cats)
    for cat in cats:
        cyc=Cycles.objects.filter(Category=cat)
        allCycles.append(cyc)
    
    ser=False
    return render(request,'index.html',{'allCycles':allCycles,'ser':ser})

def eachManufact(request,manu):
 
    prod=Cycles.objects.filter(manufacturer=manu)

    return render(request,'eachManufact.html',{'prod':prod})

def cycleview(request,myid):
    cycle=Cycles.objects.filter(Cycle_id=myid)
    return render(request,'cycleview.html',{'cycle':cycle[0]})

def mancyc(request,myid):
    cycle=Cycles.objects.filter(Cycle_id=myid)
    return render(request,'cycleview.html',{'cycle':cycle[0]})

def contact(request):
    thank=False
    if(request.method=="POST"):
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
    return render(request,'contact.html',{'thank':thank})

def about(request):
    return render(request,'about.html')

def checkout(request):
    thank=False
    if(request.method=="POST"):
        thank=True
        itemsJson=request.POST.get('itemsJson','')
        amount=request.POST.get('amount','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Order(items_json=itemsJson,amount=amount,name=name,email=email,address=address,city=city,state=state,
                    zip_code=zip_code,phone=phone)
        order.save()
        id=order.order_id
        return render(request,'checkout.html',{'thank':thank,'id':id})
        
    return render(request,'checkout.html')
def search(request):
    print("reached")
    txt=request.GET.get('search','')
    allCycles=[]
    inc=Cycles.objects.values('Cycle_name')
    print(inc)
    help=[]
    it={item['Cycle_name'] for item in inc}
    for x in it:
        if(x.lower().find(txt.lower())!=-1):
            alt=Cycles.objects.filter(Cycle_name=x)
            for c in alt:
                help.append(c)
                if len(help)>8:
                    allCycles.append(help)
                    help=[]

    allCycles.append(help)
    ser=True
    return render(request,'index.html',{'allCycles':allCycles,'ser':ser})
    
