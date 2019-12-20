from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.shortcuts import render, redirect


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # self.object に save() されたユーザーオブジェクトが格納される
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
