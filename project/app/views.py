from django.shortcuts import render
from .models import Customers
from .models import Query

# Create your views here.

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password==cpassword:
            user=Customers.objects.filter(cust_email=email)
            if user:
                use_name=Customers.objects.filter(cust_name=name)
                if use_name:
                    msg="Email ID and Name already exist"
                    return render(request, 'registration.html',{'msg':msg})
                else:
                    msg="Email id already exist please choose other 'email ID'"
                    return render(request, 'registration.html',{'msg':msg})
            else:
                Customers.objects.create(cust_name=name,cust_email=email,cust_contact=contact,cust_password=password)
                msg="YOUR DATA SUCCESSFULLY RECORDED"
                return render(request,'home.html',{'msg':msg})
        else:
            msg="Password not match"
            return render (request,"registration.html",{'msg':msg})

        print(name1,email1,contact1,password1)
    else:
        return render(request,'registration.html')
    

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)

        user_data=Customers.objects.filter(cust_email=email)
        if user_data:
            data=Customers.objects.get(cust_email=email)
            name1=data.cust_name
            email1=data.cust_email
            contact1=data.cust_contact
            password1=data.cust_password

            if password==password1:
                my_data={
                    'nm':name1,
                    'em':email1,
                    'con':contact1,
                    'pas':password1
                }
                return render (request,'dashboard.html',{'data':my_data})
            else:
                msg="Incorrect Password"
                return render(request,'home.html',{'msg':msg})
        else:
            msg="You Are Not Register , Please Register First"
            return render(request,'home.html',{'msg':msg})

    else:
        return render(request,'home.html')
    
    
def query(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        query=request.POST['query']

        print(name,email,query)

        Query.objects.create(cust_name=name,cust_email=email,cust_query=query)
        user_data=Customers.objects.get(cust_email=email)
        my_data={
            'nm':user_data.cust_name,
            'em':user_data.cust_email,
            'con':user_data.cust_contact,
            'pas':user_data.cust_password
        }
        print(my_data)
        all_query=Query.objects.filter(cust_email=email)
        return render(request, 'dashboard.html',{'key1':all_query,'data':my_data})
        print(all_query)
   
    else:
        return render(request,'dashboard.html')
    
def querydata(request,x):
    queryData=Query.objects.filter(cust_email=x)
    print(queryData)

    user_data=Customers.objects.get(cust_email=x)
    my_data={
            'nm':user_data.cust_name,
            'em':user_data.cust_email,
            'con':user_data.cust_contact,
            'pas':user_data.cust_password
        }
    print(my_data)
    all_query=Query.objects.filter(cust_email=x)
    return render(request, 'querys.html',{'key1':all_query,'data':my_data})

def delete(request,x,y):
    querydata=Query.objects.filter(id=x)
    if querydata:
        querydata=Query.objects.get(id=x)
        email=querydata.cust_email

        querydata.delete()

        user_data=Customers.objects.get(cust_email=email)
        my_data={
            'nm':user_data.cust_name,
            'em':user_data.cust_email,
            'con':user_data.cust_contact,
            'pas':user_data.cust_password
        }
        print(my_data)
        all_query=Query.objects.filter(cust_email=email)
        return render(request, 'querys.html',{'key1':all_query,'data':my_data})
    else:
        user_data=Customers.objects.get(cust_email=y)
        my_data={
            'nm':user_data.cust_name,
            'em':user_data.cust_email,
            'con':user_data.cust_contact,
            'pas':user_data.cust_password
        }
        print(my_data)
        all_query=Query.objects.filter(cust_email=y)
        return render(request, 'querys.html',{'key1':all_query,'data':my_data})
    
def edit(request,x):
    print(x)
    querydata=Query.objects.get(id=x)
    # print(querydata)
    email1=querydata.cust_email
    name1=querydata.cust_name
    query1=querydata.cust_query

    # print(query1)

    user_data=Customers.objects.get(cust_email=email1)
    my_data={
            'nm':user_data.cust_name,
            'em':user_data.cust_email,
            'con':user_data.cust_contact,
            'pas':user_data.cust_password
        }
    # print(my_data)

    all_query=Query.objects.filter(cust_email=email1)
    edit_data={
        'id':x,
        'em':email1,
        'nm':name1,
        'qu':query1
    }
    return render(request, 'querys.html',{'key1':all_query,'data':my_data,'key2':edit_data})

def update(request,x):
        if request.method=="POST":
            name1=request.POST['name']
            email1=request.POST['email']
            query1=request.POST['query']

            print(query1)

            querydata=Query.objects.get(id=x)
            querydata.cust_name=name1
            querydata.cust_email=email1
            querydata.cust_query=query1

            querydata.save()

            user_data=Customers.objects.get(cust_email=email1)
            my_data={
                'nm':user_data.cust_name,
                'em':user_data.cust_email,
                'con':user_data.cust_contact,
                'pas':user_data.cust_password
                }
            print(my_data)
            all_query=Query.objects.filter(cust_email=email1)
            return render(request, 'querys.html',{'key1':all_query,'data':my_data})

def logout(request):
    return render (request, 'home.html')


