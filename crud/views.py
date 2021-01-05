from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Crud

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Crud
    
class CrudDetailsView(DetailView):
    template_name = 'crud_details.html'
    model = Crud
    
class CrudCreateView(CreateView):
    template_name = 'crud_create.html'
    model = Crud
    fields = ['name', 'rank', 'eater']

class CrudUpdateView(UpdateView):
    template_name = 'crud_update.html'
    model = Crud
    fields = ['name', 'rank', 'eater']

class CrudDeleteView(DeleteView):
    template_name = 'crud_delete.html'
    model = Crud
    fields = ['name', 'rank', 'eater']
    success_url = reverse_lazy('home')