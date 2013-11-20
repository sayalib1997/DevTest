from django.views.generic import View
from django.shortcuts import render
from live_catalogue import forms


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class NeedEdit(View):

    def get(self, request):
        return render(request, 'need_edit.html')

    def post(self, request):
        pass
