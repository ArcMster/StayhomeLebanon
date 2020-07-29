from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Service, Email_list, Contact
from email.message import EmailMessage
import smtplib

# Create your views here.

def home(request):
    category = Category.objects.all()
    cat = Category.objects.last()
    
    #return render(request,'home.html', {'category': category})
    return render(request,'en.html', {'category': category})
    

def category(request,pk):
    category = 'abcd'
    cat = Category.objects.all()
    for i in cat:
        
        if str(i.pk) == str(pk):
            
            category = i.category
            break
    services = Service.objects.all()
    service_list = []
    for i in services:
        if str(i.category) == category:
            service_list.append(i)
    print('service list: ',service_list)
    
    #return render(request,'category.html',{'service_list': service_list,'category':category})
    #return render(request,'eproducts1.html')
    return render(request,'eproducts1.html',{'service_list': service_list,'category':category, 'category_list':cat})


def description(request,pk):
    category = Category.objects.all()
    services = Service.objects.all()
    nservices = Service.objects.filter(pk=pk)
    nitem = nservices[0]
    ncategory = nitem.category
    mservice = Service.objects.filter(category = ncategory)
    service_list = []
    for i in mservice:
        if i.pk!= nitem.pk and len(service_list)<5:
            service_list.append(i)
    category_list = Category.objects.filter(category = ncategory)
    item_category = category_list[0]

    #return render(request,'description.html', {'nitem': nitem,'service_list': service_list})
    return render(request,'eget10.html', {'nitem': nitem,'service_list': service_list, 'category':category, 'item_category':item_category})



"===============English version==================="



def eabout(request):
    category = Category.objects.all()
    return render(request,'eabout.html',{'category': category})

def eadd(request):
    category = Category.objects.all()
    return render(request,'eadd.html', {'category': category})

def econtact(request):
    category = Category.objects.all()
    return render(request,'econtact.html', {'category': category})

def eget(request):
    services = Service.objects.all()
    nservices = Service.objects.filter(pk=pk)
    nitem = nservices[0]
    ncategory = nitem.category
    mservice = Service.objects.filter(category = ncategory)
    service_list = []
    for i in mservice:
        if i.pk!= nitem.pk:
            service_list.append(i)
    return

def get(request):
    return

def en(request):
    return

def eproducts(request):
    category = 'abcd'
    cat = Category.objects.all()
    for i in cat:
        
        if str(i.pk) == str(pk):
            
            category = i.category
            break
    services = Service.objects.all()
    service_list = []
    for i in services:
        if str(i.category) == category:
            service_list.append(i)
    print('service list: ',service_list)
    return

def products(request):
    return


    


def add_service(request):
    new_service = Service()

    try:
        name = request.POST['appname']
        new_service.service_name_in_Arabic = name
    except:
        pass
    try:
        ename = request.POST['appnameen']
        new_service.service_name = ename
    except:
        pass
    try:
        category = request.POST['appcategory']
        category_list = Category.objects.filter(id = category)
        current_category = category_list[0]
        new_service.category = current_category
    except:
        pass
    try:
        details = request.POST['appdetails']
        new_service.service_details_Arabic = details
    except:
        pass
    try:
        edetails = request.POST['appdetailsen']
        new_service.service_details_English = edetails
    except:
        pass
    try:
        website = request.POST['website']
        new_service.website = website
    except:
        pass
    try:
        android = request.POST['android']
        new_service.android = android
    except:
        pass
    try:
        iphone = request.POST['iphone']
        new_service.iphone = iphone
    except:
        pass
    try:
        facebook = request.POST['facebook']
        new_service.facebook = facebook
    except:
        pass
    try:
        instagram = request.POST['instagram']
        new_service.instagram = instagram
    except:
        pass
    try:
        phone = request.POST['phone']
        new_service.phone = phone
    except:
        pass
    try:
        whatsapp = request.POST['whatsapp']
        new_service.whatsapp = whatsapp
    except:
        pass
    try:
        logo = request.POST['appimage']
        new_service.logo = logo
    except:
        pass
    
    new_service.save()
    subject = "A new service has been added (Automated Email)"
    body = "Service name: " + name + "(" + ename + ")" + "\n \n" + "Phone: " + phone + "\n \n \n" + "Thanks"

    email_list = Email_list.objects.all()
    for i in email_list:
        sendemail(subject,body,i.email)


    return redirect('en.html')
    #return HttpResponse(category)



def usercontact(request):
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    message = request.POST['message']

    new_contact = Contact()
    new_contact.name = name
    new_contact.mobile = mobile
    new_contact.email = email
    new_contact.message = message
    new_contact.save()

    subject = "A new message has been posted (Automated Email)"
    body = "Name: " + name +  "\n \n" + "Mobile: " + mobile + "\n \n" + "Email: " + email + "\n \n" + "Message: " + message + "\n \n \n" + "Thanks"

    email_list = Email_list.objects.all()
    for i in email_list:
        sendemail(subject,body,i.email)
    

    return redirect('en.html')


"==================Arabic Version ==================="


def index(request):
    category = Category.objects.all()
    cat = Category.objects.last()
    
    #return render(request,'home.html', {'category': category})
    return render(request,'index.html', {'category': category})

def categoryar(request,pk):
    category = 'abcd'
    cat = Category.objects.all()
    for i in cat:
        
        if str(i.pk) == str(pk):
            
            category = i.category
            break
    services = Service.objects.all()
    service_list = []
    for i in services:
        if str(i.category) == category:
            service_list.append(i)
    print('service list: ',service_list)
    
    #return render(request,'category.html',{'service_list': service_list,'category':category})
    #return render(request,'eproducts1.html')
    return render(request,'products1.html',{'service_list': service_list,'category':category, 'category_list':cat})

def descriptionar(request,pk):
    
    services = Service.objects.all()
    category = Category.objects.all()
    nservices = Service.objects.filter(pk=pk)
    nitem = nservices[0]
    ncategory = nitem.category
    mservice = Service.objects.filter(category = ncategory)
    service_list = []
    for i in mservice:
        if i.pk!= nitem.pk and len(service_list)<5:
            service_list.append(i)
    category_list = Category.objects.filter(category = ncategory)
    item_category = category_list[0]

    #return render(request,'description.html', {'nitem': nitem,'service_list': service_list})
    return render(request,'get10.html', {'nitem': nitem,'service_list': service_list, 'category':category, 'item_category':item_category})


def about(request):
    category = Category.objects.all()
    return render(request,'about.html',{'category': category})

def add(request):
    category = Category.objects.all()
    return render(request,'add.html', {'category': category})
    

def contact(request):
    category = Category.objects.all()
    return render(request,'contact.html', {'category': category})



def add_servicear(request):
    new_service = Service()

    try:
        name = request.POST['appname']
        new_service.service_name_in_Arabic = name
    except:
        pass
    try:
        ename = request.POST['appnameen']
        new_service.service_name = ename
    except:
        pass
    try:
        category = request.POST['appcategory']
        category_list = Category.objects.filter(id = category)
        current_category = category_list[0]
        new_service.category = current_category
    except:
        pass
    try:
        details = request.POST['appdetails']
        new_service.service_details_Arabic = details
    except:
        pass
    try:
        edetails = request.POST['appdetailsen']
        new_service.service_details_English = edetails
    except:
        pass
    try:
        website = request.POST['website']
        new_service.website = website
    except:
        pass
    try:
        android = request.POST['android']
        new_service.android = android
    except:
        pass
    try:
        iphone = request.POST['iphone']
        new_service.iphone = iphone
    except:
        pass
    try:
        facebook = request.POST['facebook']
        new_service.facebook = facebook
    except:
        pass
    try:
        instagram = request.POST['instagram']
        new_service.instagram = instagram
    except:
        pass
    try:
        phone = request.POST['phone']
        new_service.phone = phone
    except:
        pass
    try:
        whatsapp = request.POST['whatsapp']
        new_service.whatsapp = whatsapp
    except:
        pass
    try:
        logo = request.POST['appimage']
        new_service.logo = logo
    except:
        pass
    
    new_service.save()
    subject = "A new service has been added (Automated Email)"
    body = "Service name: " + name + "(" + ename + ")" + "\n \n" + "Phone: " + phone + "\n \n \n" + "Thanks"

    email_list = Email_list.objects.all()
    for i in email_list:
        sendemail(subject,body,i.email)


    return redirect('index.html')


def usercontactar(request):
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    message = request.POST['message']

    new_contact = Contact()
    new_contact.name = name
    new_contact.mobile = mobile
    new_contact.email = email
    new_contact.message = message
    new_contact.save()

    subject = "A new message has been posted (Automated Email)"
    body = "Name: " + name +  "\n \n" + "Mobile: " + mobile + "\n \n" + "Email: " + email + "\n \n" + "Message: " + message + "\n \n \n" + "Thanks"

    email_list = Email_list.objects.all()
    for i in email_list:
        sendemail(subject,body,i.email)
    

    return redirect('index.html')


def sendemail(subject,body,email):
    msg = EmailMessage()
    msg['From'] = '"Stay Home Lebanon" <stayhomelebanon@gmail.com>'
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(body)
    smtplibObj = smtplib.SMTP('smtp.gmail.com',587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login("stayhomelebanon@gmail.com", "sthome@1234")
        
    smtplibObj.send_message(msg)
    smtplibObj.quit()

