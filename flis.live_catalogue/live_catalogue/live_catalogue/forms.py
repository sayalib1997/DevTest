from django import forms
from live_catalogue.models import Catalogue


class NeedForm(forms.ModelForm):

    class Meta():
        model = Catalogue
        exclude = ('kind', 'created_by', 'created_on', 'last_updated', 'draft',
                  'resources',)


    def save(self):
        need = super(NeedForm, self).save(commit=False)
        return need

