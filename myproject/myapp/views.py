from email import message
from django.shortcuts import render,redirect,HttpResponse
from .models import *
# from .models import User

from django.contrib.auth import authenticate,login,logout
def home(request):
 
    return render(request,"home.html")

def index(request):
 
    return render(request,"index.html")

def teacherhome(request):
 
    return render(request,"teacherhome.html")

def studhome(request):
 
    return render(request,"studhome.html")


def adminhome(request):
 
    return render(request,"adminhome.html")

def adminhome1(request):
 
    return render(request,"adminhome1.html")
def adddep(request):
    if request.method=="GET":
        return render(request,"department.html")
    elif request.method=="POST":
        department=request.POST['adddep']
       
        
        b=Department.objects.create(department=department)
        return redirect('adddep')

def StuRegi(request):
    if request.method=="GET":
        dview=Department.objects.all()

        return render(request,"stureg.html",{'dview':dview})
    elif request.method=="POST":
        
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        dep_id=request.POST.get('dep_id')
        User.objects.create_user(name=name,address=address, age=age,phoneno=phoneno,email=email,username=username,password=password,djoin='2022-06-12',dep_id_id=dep_id,is_staff=0,is_active=0)
        return redirect('h')

def TeachRegi(request):
    if request.method=="GET":
        dview=Department.objects.all()

        return render(request,"teacherreg.html",{'dview':dview})
    elif request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        qualification=request.POST.get('qualification')
        djoin=request.POST.get('djoin')
        username=request.POST.get('username')
        password=request.POST.get('password')
        dep_id=request.POST.get('dep_id')
        

        User.objects.create_user(name=name,address=address,phoneno=phoneno,email=email, qualification=qualification,djoin=djoin,age='00',username=username,password=password,dep_id_id=dep_id,is_staff=1)
        return redirect('adminhome1')

def logins(request):
    if request.method=='POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request,username=usern,password=passw)
        

        if user is not None and user.is_superuser == 1:
            login(request,user)
            return render(request,'adminhome.html')
        
        elif user is not None and user.is_staff ==1 and user.is_superuser==0:
            login(request,user)
            request.session['t_id']=user.id

            return render(request,'teacherhome.html')

        elif user is not None and user.is_staff ==0 and  user.is_superuser==0:
            request.session['s_id']=user.id
            login(request,user)
            return render(request,'studhome.html')
        else:
            return HttpResponse('Sorry Invalid details')
    else:
        return render(request, 'logi.html')


def viewstud(request):
    st=User.objects.filter(is_staff=0, is_active=0)
    return render(request,"viewstudent.html",{'st':st})


def viewapprovest(request):
    st=User.objects.filter(is_staff=0, is_active=1)
    return render(request,"viewapprovest.html",{'st':st})







def teacherview(request):
    tview=User.objects.filter(is_staff=1)
    return render(request,"teacherview.html",{'tview':tview})


def editteacher(request):
    if request.method=="GET":
        id=request.session['t_id']

        em=User.objects.get(id=id)
        context={}
     
        context['data']=em
        return render(request,"editteacher.html",context)
    elif request.method=="POST":
        id=request.session['t_id']

        name=request.POST['name']
        address=request.POST['address']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        qualification=request.POST['qualification']
        # djoin=request.POST['djoin']

        a=User.objects.filter(id=id).update(name=name,address=address,phoneno=phoneno,email=email,qualification=qualification)
        return redirect('editteacher')



def editstudent(request):
    if request.method=="GET":
        id=request.session['s_id']
        em=User.objects.get(id=id)
        context={}
     
        context['data1']=em
        return render(request,"editstudent.html",context)
    elif request.method=="POST":
        id=request.session['s_id']

        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        phoneno=request.POST['phoneno']
        email=request.POST['email']


        a=User.objects.filter(id=id).update(name=name,address=address,age=age,phoneno=phoneno,email=email)
        return redirect('editstudent')


        
def studapprove(request,id):
   
    # # user=User.objects.get(id=id).update(is_active=1)
    user=User.objects.filter(id=id).update(is_active=1)
    # user.save()

    return redirect("viewstud")


def reject(request,id):
    
    # # user=User.objects.get(id=id).update(is_active=1)
    user=User.objects.get(id=id)
    user.delete()

    return redirect("viewstud")

def lgout(request):
    logout(request)
    return redirect('logins')

def regi(request):
    return render(request,"regi.html")


def table(request):
    return render(request,"table.html")
def viewdpbyst(request):
    id=request.session['t_id']
    teacher=User.objects.get(id=id)
    dep_id=teacher.dep_id
    students=User.objects.filter(dep_id=dep_id,is_staff=0)

    return render(request,"viewdpbyst.html",{'st':students})

def viewdpbyte(request):
    students=User.objects.get(id=request.user.id)
    dep_id=students.dep_id
    teacher=User.objects.filter(dep_id=dep_id)
    return render(request,"viewdpbyte.html",{'tview':teacher})

