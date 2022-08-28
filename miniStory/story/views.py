from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm,LoginForm, PostForm
from story import views
from django.contrib.auth import authenticate, login, logout
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'story/home.html', {'posts':posts})

def about(request):
    return render(request, 'story/about.html')

def contact(request):
    return render(request, 'story/contact.html')

def user_signup(request):

    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulaions!! You have become autor.')
            form.save()
    else:    
        form = SignUpForm()
    return render(request, 'story/signup.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password'] 
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'story/login.html', {'form':form})
    

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'story/dashboard.html', {'posts':posts})
    else:
        return HttpResponseRedirect('/login/')    


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()        
        return render(request, 'story/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)        
        return render(request, 'story/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
