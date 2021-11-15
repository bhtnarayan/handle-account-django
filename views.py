from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User 
from django.http import HttpResponse
from . models import Profile
from django.contrib import messages 
from main.models import Post, Rating
from django.db.models import Avg, Sum 
from django.contrib.auth.decorators import login_required
from . forms import CustomUserCreationForm, EditProfileForm, UserForm, ProfileForm
from django.contrib.auth import login

# Create your views here.

def my_profile(request):
    p = request.user.profile 
    you = p.user 
    user_posts = Post.objects.filter(user = you) 
    user_posts_count = Post.objects.filter(user = you).count() 

    context = {
        'u': you,
        'user_posts': user_posts,
        'user_posts_count': user_posts_count,
    }
    return render(request, "registration/profile.html", context) 
    

def user_profile_view(request, slug):
    p = Profile.objects.filter(slug = slug).first() 
    u = p.user 
    user_posts = Post.objects.filter(user = u)
    user_posts_count = Post.objects.filter(user = u).count()  

    rate_post = Rating.objects.filter(username = u) 
    # rate_post = Post.objects.filter(post = user_post)
    photographer_rate =  rate_post.aggregate(Avg('rate'))['rate__avg']

    context = {
        'u':u, 
        'user_posts':user_posts,
        'user_posts_count': user_posts_count,
        'photographer_rate': photographer_rate,
    }
    return render(request, "registration/profile.html", context) 



@login_required(login_url = "login")
def edit_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance = request.user) 
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() 
            profile_form.save() 
            messages.success(request, ('Your profile was successfully updated')) 
            return redirect('/accounts/profile')
        else:
            messages.error(request, ('Please correct the error below')) 

    else:
        user_form = UserForm(instance = request.user) 
        profile_form = ProfileForm(instance= request.user.profile) 

    return render(request, 'registration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    }) 


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            messages.success(request, f'Your account has been created! Successfully.')
            return redirect("/") 
    else:
        form = CustomUserCreationForm() 
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context) 
    

@login_required(login_url = "login")
def Settings(request):
    return render(request, "registration/settings.html")

def search_users(request):
    query = request.GET.get('query') 
    object_list = User.objects.filter(username__icontains = query) 
    context = {
        'users': object_list,
    }
    return render(request, "registration/search_users.html", context) 
    