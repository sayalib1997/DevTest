from django import forms
from live_catalogue.models import Catalogue


class NeedForm(forms.ModelForm):

    NRC_FLIS = 'nrc_flis'
    EIONET = 'eionet'
    PERMISSIONS_CHOICES = (
        (NRC_FLIS, 'NRC Flis'),
        (EIONET, 'All members of EIONET'),
    )

    permissions = forms.ChoiceField(choices=PERMISSIONS_CHOICES,
                                    widget=forms.RadioSelect())

    class Meta():
        model = Catalogue
        exclude = ('kind', 'created_by', 'created_on', 'last_updated', 'draft',
                  'resources', 'permissions')

        widgets = {
            'keywords': forms.TextInput(),
            'address': forms.Textarea(),
        }

        labels = {
            'status': 'Type of need',
            'need_urgent': 'Is this need urgent?',
        }

    def __init__(self, *args, **kwargs):
        self.draft = kwargs.pop('draft', False)
        super(NeedForm, self).__init__(*args, **kwargs)

        self.fields['status'].required = True
        self.fields['status'].empty_label = None
        self.fields['status'].choices = self.fields['status'].choices[1:]

        self.fields['title'].required = True
        self.fields['keywords'].required = True
        self.fields['start_date'].required = True
        self.fields['contact_person'].required = True
        self.fields['email'].required = True
        self.fields['institution'].required = True
        self.fields['country'].required = True

    def save(self):
        need = super(NeedForm, self).save(commit=False)
        nee.kind = Catalogue.NEED
        return need

