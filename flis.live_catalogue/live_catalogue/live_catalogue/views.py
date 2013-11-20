from django.views.generic import View
from django.shortcuts import render
from live_catalogue import forms


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class NeedEdit(View):

    def get(self, request):
        form = forms.NeedForm()
        return render(request, 'need_edit.html', {
            'form': form,
        })

    def post(self, request):
        form = forms.NeedForm(request.POST)
        if form.is_valid():
            return redirect('home')
        return render(request, 'need_edit.html', {
            'form': form,
        })
