from django import forms
from live_catalogue.models import Catalogue, Keyword, CataloguePermission


class CatalogueForm(forms.ModelForm):

    NRC_FLIS, EIONET = 'nrc_flis', 'eionet'
    PERMS_CHOICES = ((NRC_FLIS, 'NRC Flis'), (EIONET, 'All members of EIONET'),)

    REQUIRED_FIELDS = ('status', 'title', 'keywords', 'start_date',
                       'contact_person', 'email', 'institution', 'country',)

    keywords = forms.CharField(max_length=128, required=False)
    perms = forms.ChoiceField(choices=PERMS_CHOICES, widget=forms.RadioSelect(),
                              initial=NRC_FLIS)

    class Meta:

        model = Catalogue
        exclude = ('kind', 'created_by', 'created_on', 'last_updated', 'draft',
                  'resources', 'perms')

        widgets = {
            'address': forms.Textarea(),
        }
        labels = {
            'status': 'Type of need',
            'need_urgent': 'Is this need urgent?',
        }

    def __init__(self, *args, **kwargs):
        self.is_draft = kwargs.pop('is_draft', False)
        super(CatalogueForm, self).__init__(*args, **kwargs)

        self.fields['status'].empty_label = None
        self.fields['status'].choices = self.fields['status'].choices[1:]

        if self.is_draft is False:
            for f in self.REQUIRED_FIELDS:
                self.fields[f].required = True

    def save(self):
        catalogue = super(CatalogueForm, self).save(commit=False)
        catalogue.kind = self.KIND
        catalogue.is_draft = self.is_draft

        catalogue.category = self.cleaned_data['category']
        catalogue.flis_topic = self.cleaned_data['flis_topic']
        catalogue.theme = self.cleaned_data['theme']

        catalogue.title = self.cleaned_data['title']
        catalogue.description = self.cleaned_data['description']

        keywords = self.cleaned_data['keywords'].split(',')
        for k in keywords: # TODO use manual transactions here
            if not k: # skip empty strings
                continue
            keyword = Keyword.objects.get_or_create(pk=k, defaults={'name': k})
            # catalogue.keywords.add(keyword)

        catalogue.status = self.cleaned_data['status']
        catalogue.geographic_scope = self.cleaned_data['geographic_scope']
        catalogue.start_date = self.cleaned_data['start_date']
        catalogue.end_date = self.cleaned_data['end_date']
        catalogue.contact_person = self.cleaned_data['contact_person']
        catalogue.email = self.cleaned_data['email']
        catalogue.phone_number = self.cleaned_data['phone_number']
        catalogue.institution = self.cleaned_data['institution']
        catalogue.address = self.cleaned_data['address']
        catalogue.country = self.cleaned_data['country']
        catalogue.url = self.cleaned_data['url']
        catalogue.info = self.cleaned_data['info']
        catalogue.document = self.cleaned_data['document']
        catalogue.save()
        perms = self.cleaned_data['perms']
        CataloguePermission.objects.create(catalogue=catalogue,
                                           permission=perms)
        return catalogue


class NeedForm(CatalogueForm):

    KIND = 'need'

    class Meta(CatalogueForm.Meta):

        labels = {
            'status': 'Type of need',
            'need_urgent': 'Is this need urgent?',
        }

    def save(self):
        catalogue = super(NeedForm, self).save()
        catalogue.need_urgent = self.cleaned_data['need_urgent']
        catalogue.save()
        return catalogue
