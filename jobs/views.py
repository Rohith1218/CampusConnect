from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView
from jobs.models import freelancer, business
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(req):
    return HttpResponse("<h1>CampusConnect</h1>")


class freelancerlistview(ListView):
    model = freelancer


class freelancerdetailview(DetailView):
    model = freelancer

class freelancercreateview(LoginRequiredMixin, CreateView):
    model=freelancer
    fields=['name','profile_pic', 'tagline', 'bio', 'website']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(freelancercreateview, self).form_valid(form)
    
class businesscreateview(LoginRequiredMixin, CreateView):
    model=business
    fields=['name', 'profile_pic', 'bio']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(businesscreateview, self).form_valid(form)   

@login_required
def handle_login(req):
    if req.user.get_freelancer() or req.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))
    return render(req, 'jobs/choose_account.html',{})




