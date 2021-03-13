from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Orders, OrderUpdate
from math import ceil
from twilio.rest import Client 
import json
# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'resale/index.html', params)
    
def about(request):
    return render(request, 'resale/about.html')
def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'resale/contact.html', {'thank': thank})
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'resale/tracker.html')
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'resale/search.html', params)
def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'resale/prodView.html', {'product':product[0]})
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        msg(amount,phone)
        return render(request, 'resale/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'resale/checkout.html')
def msg(val,phone):
    account_sid = 'AC88d4562da72fc05eb55b52edebe70bbc' 
    auth_token = 'bb8f6b4c5a619dad2594de11eae9803a' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Pay ' + val,      
                                  to='whatsapp:' + phone
                              ) 
 
    print(message.sid)

def form(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        price = request.POST.get('price', '')
        phone = request.POST.get('phone', '')
        desc  = request.POST.get('desc','')
        category = request.POST.get('category','')
        date = request.POST.get('date','')
        image = request.POST.get('img','')
        product_name = request.POST.get('prodName','')
        size = request.POST.get('size','')
        prod = Product(user_name=name, product_name=product_name, phone=phone, price=price, desc=desc, category=category, pub_date=date, image=image, size=size)
        prod.save()
    
    return render(request, 'resale/form.html')