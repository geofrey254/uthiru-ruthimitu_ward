from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from .forms import Birth_CertificateForm

# models imports
from .models import Projects, Post, Gallery, Events, Downloads

# Create your views here.


def home(request):
    posts = Post.objects.order_by('-created_on')[0:3]

    context = {
        'posts':posts
    }
    return render(request, 'home/landing.html', context)


def projects(request):
    project_list = Projects.objects.filter(status=1).order_by('created_on')
    context = {
        'project_list': project_list
    }
    return render(request, 'home/projects.html', context)


def events(request):
    events = Events.objects.order_by('created_on')
    context = {
        'events':events
    }
    return render(request, 'home/events.html', context)


def facilities(request):
    return render(request, 'home/facilities.html')


def uthimitu(request):
    return render(request, 'home/uthimitu.html')


def history(request):
    return render(request, 'home/history.html')


def committee(request):
    return render(request, 'home/committee.html')


def emergency(request):
    return render(request, 'home/emergencies.html')


def contacts(request):
    return render(request, 'home/contact_us.html')


def garbage(request):
    return render(request, 'home/garbage.html')


def programmes(request):
    return render(request, 'home/program.html')


def blogs(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }

    return render(request, 'home/blogger.html', context)

# Article views
def article_detail(request, slug, *args, **kwargs):
    post        =   Post.objects.get(slug=slug)
    
    context     =   {
        "post": post,
    }

    return render(request, "home/article.html", context)


def maps(request):
    return render(request, 'home/mappy.html')


def downloads(request):
    downloads = Downloads.objects.order_by('created_on')
    context = {
        'downloads':Downloads
    }
    return render(request, 'home/downloads.html', context)


def tenders(request):
    return render(request, 'home/tenders.html')


def gallery(request):
    gallery = Gallery.objects.order_by('created_on')
    context={
        'gallery':gallery
    }
    return render(request, 'home/gallery.html', context)

# Forms Views


def birth(request):
    form = Birth_CertificateForm(request.POST or None, request.FILES)
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name
    }
    return render(request, 'home/birth.html', context)
