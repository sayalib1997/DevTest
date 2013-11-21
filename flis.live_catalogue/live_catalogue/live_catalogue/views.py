from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from braces.views import AjaxResponseMixin, JSONResponseMixin
from live_catalogue import forms, models


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class NeedEdit(View):

    def get(self, request, pk=None):
        catalogue = get_object_or_404(models.Catalogue, pk=pk) if pk else None
        form = forms.NeedForm(instance=catalogue)
        return render(request, 'need_edit.html', {
            'catalogue': catalogue,
            'form': form,
        })

    def post(self, request, pk=None):
        is_draft = True if request.POST['save'] == 'draft' else False
        catalogue = get_object_or_404(models.Catalogue, pk=pk) if pk else None
        form = forms.NeedForm(request.POST, instance=catalogue, is_draft=is_draft)
        if form.is_valid():
            form.save()
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

