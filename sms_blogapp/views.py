from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import blogforms
from .forms import Blogpostform
from . models import blog
from django.contrib import messages
# Create your views here.

def func(request):
    obj1 = blog.objects.all()
    return render(request,'index.html',{'result':obj1})

def register(request):
    if request.method=="POST":
        Uname = request.POST['UserName']
        mail = request.POST['email']
        pswd1 = request.POST['Password1']
        pswd2 = request.POST['Password2']

        if pswd1==pswd2:
            if User.objects.filter(username=Uname).exists():
                messages.info(request,"UserName already Taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email already Taken")
                return redirect('register')
            user = User.objects.create_user(username=Uname,email=mail,password=pswd1)
            # Red color "username" is the field of auth user, White color is fetching value from form
            user.save();
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        UnamE = request.POST['UserName']
        PswD = request.POST['Password']
        UseR=auth.authenticate(username=UnamE,password=PswD)
        # obj1 = blog.objects.filter(name=request.user)
        if UseR is not None:
            auth.login(request,UseR)
            obj1 = blog.objects.filter(name=request.user)
            # request.user will give the username of user login data (from auth user)
            return render(request,"reg_user.html",{'result':obj1})
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def update(request,id):
    blog1 = blog.objects.get(id=id)
    form = blogforms(request.POST or None, instance=blog1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'blog1': blog1, 'form': form})


def delete(request,id):
    blog1=blog.objects.get(id=id)
    if request.method == 'POST':
        blog1.delete()
        return redirect('/')
    return render(request,'delete.html',{'blog':blog1})

def add_blogs(request):
    if request.method == "POST":
        form = Blogpostform(request.POST,request.FILES)
        if form.is_valid():
            blog1=form.save(commit=False)
            blog1.name = request.user
            # request.user will give the username of user login data (from auth user)
            blog1.save()
            return redirect('/')
    else:
        form = Blogpostform()
    return render(request, 'add_blog.html', {'form': form})


# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render,redirect
# from .forms import blogforms
# from .forms import Blogpostform
# from . models import blog
# from django.contrib import messages
#
# # Create your views here.
#
# def func(request):
#     obj1 = blog.objects.all()
#     return render(request,'index.html',{'result':obj1})
#
# def register(request):
#     if request.method=="POST":
#         Uname = request.POST['UserName']
#         mail = request.POST['email']
#         pswd1 = request.POST['Password1']
#         pswd2 = request.POST['Password2']
#
#         if pswd1==pswd2:
#             if User.objects.filter(username=Uname).exists():
#                 messages.info(request,"UserName already Taken")
#                 return redirect('register')
#             elif User.objects.filter(email=mail).exists():
#                 messages.info(request,"Email already Taken")
#                 return redirect('register')
#             user = User.objects.create_user(username=Uname,email=mail,password=pswd1)
#             # Red color "username" is the field of auth user, White color is fetching value from form
#             user.save()
#         else:
#             messages.info(request, "Password not matched")
#             return redirect('register')
#         return redirect('/')
#     else:
#         return render(request,"register.html")
#
# def login(request):
#     if request.method=="POST":
#         UnamE = request.POST['UserName']
#         PswD = request.POST['Password']
#         UseR=auth.authenticate(username=UnamE,password=PswD)
#         obj1 = blog.objects.filter(name=request.user)
#         if UseR is not None:
#             auth.login(request,UseR)
#
#             return render(request,"reg_user.html",{'result':obj1})
#         else:
#             messages.info(request,'invalid username or password')
#             return redirect('login')
#     else:
#         return render(request,"login.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#
# def update(request,id):
#     blog1 = blog.objects.get(id=id)
#     form = blogforms(request.POST or None, instance=blog1)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'edit.html', {'blog1': blog1, 'form': form})
#
#
# def delete(request,id):
#     blog1=blog.objects.get(id=id)
#     if request.method == 'POST':
#         blog1.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'blog':blog1})
#
# def add_blogs(request):
#     if request.method == "POST":
#         form = Blogpostform(request.POST,request.FILES)
#         if form.is_valid():
#             blog1=form.save(commit=False)
#             blog1.name = request.user
#             blog1.save()
#             return redirect('/')
#     else:
#         form = Blogpostform()
#     return render(request, 'add_blog.html', {'form': form})

    # request.user will give the username of user login data (from auth user)

    # if request.method == "POST":
    #     form = Blogpostform(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         blog1 = form.save(commit=False)
    #         # blog1 = form.save()
    #         # blog1.name = request.user
    #         blog1.save()
    #         # form.save()
    #         obj = form.instance
    #         alert = True
    #         return render(request, "add_blog.html", {'obj': obj, 'alert': alert})
    #         # return render(request, "add_blog.html", {'obj': obj})
    # else:
    #     form = Blogpostform()
    #     return render(request, "add_blog.html", {'form': form})

    # else:
    #     form=Blogpostform()
    # return render(request, "add_blog.html", {'form':form})

    # form = Blogpostform(request.POST)
    # if form.is_valid():
    #     form.save()
    #
    # else:
    #     form = Blogpostform()
    #
    # return render(request, 'add_blog.html', {'form': form})

# form = Blogpostform(request.POST or None,)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # return render(request, 'add_blog.html', {'form': form})


    # if request.method=="POST":
    #     form = Blogpostform(data=request.POST or none, files=request.FILES)
    #     if form.is_valid():
    #         blog1 = form.save(commit=False)
    #         # blog = form.save()
    #         # blog1.name = request.user
    #         blog1.save()
    #         # form.save()
    #         obj = form.instance
    #         alert = True
    #         return render(request, "add_blog.html",{'obj':obj, 'alert':alert})
    #         # return render(request, "add_blog.html", {'obj': obj})
    # else:
    #     form=Blogpostform()
    # return render(request, "add_blog.html", {'form':form})