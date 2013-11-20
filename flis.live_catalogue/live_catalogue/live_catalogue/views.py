from django.views.generic import View
from django.shortcuts import render

from braces.views import AjaxResponseMixin, JSONResponseMixin
from live_catalogue import forms, models


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


class ApiKeywords(JSONResponseMixin, AjaxResponseMixin, View):

    def get_ajax(self, request):
        q = request.GET.get('q', '').strip()
        keywords = models.Keyword.objects.all()
        if q:
            keywords = keywords.filter(name__contains=q)
        return self.render_json_response({
            'status': 'success',
            'results': [{'id': k.pk, 'text': k.name} for k in keywords]
        })

