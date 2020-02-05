from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView, DeleteView)
from basic_app import models


class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
