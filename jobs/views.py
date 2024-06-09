from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from jobs.models import freelancer, business
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.

def index(req):
    return HttpResponse("<h1>CampusConnect</h1>")

class freelancerlistview(ListView):
    model = freelancer

class freelancerdetailview(DetailView):
    model = freelancer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        freelancer_obj = self.get_object()
        # Ensure Skills is processed as a list
        if isinstance(freelancer_obj.Skills, str):
            context['skills_list'] = [skill.strip() for skill in freelancer_obj.Skills.split(',')]
        else:
            context['skills_list'] = []
        
        # Ensure Reviews is processed as a list of dictionaries
        try:
            context['reviews_list'] = json.loads(freelancer_obj.Reviews)
        except json.JSONDecodeError:
            context['reviews_list'] = []
        
        return context

class freelancercreateview(LoginRequiredMixin, CreateView):
    model = freelancer
    fields = ['name', 'profile_pic', 'tagline', 'bio', 'website', 'Skills', 'Reviews', 'Phone_number', 'Email']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class businesscreateview(LoginRequiredMixin, CreateView):
    model = business
    fields = ['name', 'profile_pic', 'bio', 'Reviews', 'Phone_number', 'Email']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)   

@login_required
def handle_login(req):
    if req.user.get_freelancer() or req.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))
    return render(req, 'jobs/choose_account.html',{})