from django.shortcuts import render
from .models import Footer
from .models import Contact
from .models import Blog
from .models import Login
from .models  import Signin
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def foo(request):
    if request.method=='GET':
       return render(request,"index.html")
    elif request.method=='POST':
         if "btn_submit" in request.POST:
            f=Footer()
            f.name=request.POST.get('name',"N/A")
            f.email=request.POST.get('email',"N/A")
            f.hello=request.POST.get('hello',"N/A")
            f.save()
            return render(request,"index.html")  
         elif "reset-button" in request.POST:
            f=Footer()
            f.name=request.POST.get('name',"N/A")
            f.email=request.POST.get('email',"N/A")
            f.hello=request.POST.get('hello',"N/A")
            f.save()
            return HttpResponse("<h1>Removed successfully</h1>")  
    return render(request,"index.html")             
def about(request):
    return render(request,"About.html")
def login(request):
    return render(request,"Login.html")
def log(request):
    if request.method=='GET': 
     return render(request,"Login.html")
    elif request.method=='POST':
       if "reset-button" in request.POST:
          l=Login()
          l.f_nm=request.POST.get('fname',"N/A")
          l.l_nm=request.POST.get('lname',"N/A")
          l.e_mai=request.POST.get('e_mai',"N/A")
          l.p_word=request.POST.get('p_word',"N/A")
          l.save()
    return HttpResponse("<h1>logged in successfully!</h1>")

def signin(request):
   return render(request,"signin.html")
def sign(request):
    if request.method=='GET':
      return render(request,"login.html")
    elif request.method=='POST':
       if "btn1" in request.POST:
        i=Signin()
        i.f_nam=request.POST.get('f_nam',"N/A")
        i.l_nam=request.POST.get('l_nam',"N/A")
        i.e_ma=request.POST.get('e_ma',"N/A")
        i.pa_word=request.POST.get('pa_word',"N/A")
        i.p=request.POST.get('p',"N/A")
        if i.pa_word==i.p:
         i.save()
        else:
           return HttpResponse("<p>password not matched</p>")
    return HttpResponse("<h1>signed in successfully</h1>")



def contactreg(request):
   if request.method=="GET":
      return render(request,"contact.html")
   elif request.method=="POST":
      con=Contact()
      con.fname=request.POST.get("fname","N/A")
      con.lname=request.POST.get("lname","N/A")
      con.mail=request.POST.get("email","N/A")
      con.con_no=request.POST.get("number","N/A")
      con.mes_sage=request.POST.get("message","N/A")
      con.save()
      return HttpResponse("<h1>form submitted successfully</h1>")


def blog(request):
   return render(request,"blog.html")
def blogblog(request):
    if request.method=='GET':
     d=render(request,"blog.html")
     return d
    elif request.method=='POST':
       if "btn_submit" in request.POST:
          b=Blog()
          b.title=request.POST.get('title',"N/A")
          b.category=request.POST.get('Category',"N/A")
          b.Pic=request.POST.get('pic',"N/A")
          b.des=request.POST.get('des',"N/A")
          b.save()
    return HttpResponse("<h1>Blog created successfully</h1>")

def contact(request):
   res=render(request,"contact.html")
   return res
   


    
