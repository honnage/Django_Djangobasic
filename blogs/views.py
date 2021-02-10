from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
# Create your views here.
def hello(request):
    #Query Data from Model
    data = Post.objects.all()
    return render(request, 'index.html',{'posts':data})

def page1(request):
    return render(request, 'page1.html')

def createForm(request):
    return render(request, 'form.html')

def addBlog(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    
    user=User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=firstname,
        last_name=lastname
        )

    user.save()

    return render(request,'result.html')