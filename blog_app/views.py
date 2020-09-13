# from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from blog_app.models import Post


# Home Page
class HomeView(ListView):
    model = Post
    template_name = 'index.html'


# About Page
class AboutView(TemplateView):
    template_name = 'about.html'

# def index(request):
#     return render(request, 'index.html', {})
