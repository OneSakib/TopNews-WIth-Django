from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib import messages as mb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import Group


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': post})


def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            mb.success(request, "Congratulation U can get Success Signup You have the Author")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/login')
        mb.warning(request, "Enter right detail in this fields")
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                print(uname, upass)
                user = authenticate(username=uname, password=upass)
                print(user)
                if user is not None:
                    login(request, user)
                    mb.success(request, "Login Successfully")
                    return HttpResponseRedirect('/daskboard')
            mb.warning(request, "Please Enter right details ")
        form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/daskboard')


def logout_form(request):
    if request.user.is_authenticated:
        logout(request)
        mb.success(request, 'Successfully Logout')
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')


def daskboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        full_name = request.user.get_full_name()
        gps = Group.objects.all()
        return render(request, 'blog/daskboard.html',
                      {'user': request.user, 'posts': post, 'full_name': full_name, 'groups': gps})
    else:
        mb.warning(request, "Please First login")
        return HttpResponseRedirect('/login')


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                mb.success(request, 'Successfully add data')
                form = PostForm()
                return HttpResponseRedirect('/daskboard')
            mb.warning(request, 'some errors')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def updatePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                mb.success(request, "Data is Successfully Save")
                return HttpResponseRedirect('/daskboard')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def deletepost(request, id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/daskboard')
    else:
        return HttpResponseRedirect('/login')
