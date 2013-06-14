
from django import forms
from django_tools.middlewares import ThreadLocal
from flis import models


class CleanCountry(object):

    def clean_country(self):
        data = self.cleaned_data['country']
        request = ThreadLocal.get_current_request()
        if not request.country == data:
            raise forms.ValidationError('Country not valid')
        return data


class InterlinkForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Interlink

    def __init__(self, *args, **kwargs):
        super(InterlinkForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_gmt = self.fields['gmt'].queryset
        self.fields['gmt'].queryset = qs_gmt.filter(country=country)

        qs_t = self.fields['trend'].queryset
        self.fields['trend'] = qs_t.filter(country=country)

        qs_1 = self.fields['indicator_1'].queryset
        self.fields['indicator_1'].queryset = qs_1.filter(country=country)

        qs_2 = self.fields['indicator_2'].queryset
        self.fields['indicator_2'].queryset = qs_2.filter(country=country)

        qs_3 = self.fields['indicator_3'].queryset
        self.fields['indicator_3'].queryset = qs_3.filter(country=country)

        qs_4 = self.fields['indicator_4'].queryset
        self.fields['indicator_4'].queryset = qs_4.filter(country=country)


class SourceForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Source


class GMTForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.GMT

    def __init__(self, *args, **kwargs):
        super(GMTForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class FlisModelForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.FlisModel

    def __init__(self, *args, **kwargs):
        super(FlisModelForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class HorizonScanningForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.HorizonScanning

    def __init__(self, *args, **kwargs):
        super(HorizonScanningForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class MethodToolForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.MethodTool

    def __init__(self, *args, **kwargs):
        super(MethodToolForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class UncertaintyForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Uncertainty

    def __init__(self, *args, **kwargs):
        super(UncertaintyForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class WildCardForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.WildCard

    def __init__(self, *args, **kwargs):
        super(WildCardForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class EarlyWarningForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.EarlyWarning

    def __init__(self, *args, **kwargs):
        super(EarlyWarningForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_sc = self.fields['steep_category'].queryset
        self.fields['steep_category'].queryset = qs_sc.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class IndicatorForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Indicator

    def __init__(self, *args, **kwargs):
        super(IndicatorForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_tc = self.fields['thematic_category'].queryset
        self.fields['thematic_category'].queryset = qs_tc.filter(country=country)

        qs_gs = self.fields['geographical_scale'].queryset
        self.fields['geographical_scale'].queryset = qs_gs.filter(country=country)

        qs_gc = self.fields['geographical_coverage'].queryset
        self.fields['geographical_coverage'].queryset = qs_gc.filter(country=country)

        qs_t = self.fields['timeline'].queryset
        self.fields['timeline'].queryset = qs_t.filter(country=country)

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class TrendForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Trend

    def __init__(self, *args, **kwargs):
        super(TrendForm, self).__init__(*args, **kwargs)
        country = ThreadLocal.get_current_request().country

        qs_s = self.fields['source'].queryset
        self.fields['source'].queryset = qs_s.filter(country=country)


class BlossomForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Blossom

    def __init__(self, *args, **kwargs):
         super(BlossomForm, self).__init__(*args, **kwargs)
         self.fields['date_of_conclusion_planned'].input_formats = ['%d/%m/%Y']
         self.fields['date_of_conclusion_final'].input_formats = ['%d/%m/%Y']


class ThematicCategoryForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.ThematicCategory


class GeographicalScaleForm(CleanCountry, forms.ModelForm):

   class Meta:
        model = models.GeographicalScale


class ScenarioForm(CleanCountry, forms.ModelForm):

   class Meta:
        model = models.Scenario


class GeographicalCoverageForm(CleanCountry, forms.ModelForm):

   class Meta:
        model = models.GeographicalCoverage


class SteepCategoryForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.SteepCategory


class TimelineCreateForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Timeline
