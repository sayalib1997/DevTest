import flatland as fl
from flatkit.schema import ValuesFromTable, DictFromTable

from flatland.validation import Validator, Converted, IsEmail
from flatland.signals import validator_validated
from flatland.schema.base import NotEmpty


class ListEmails(Validator):

    fail = None

    def validate(self, element, state):
        if element.properties.get("not_empty_error"):
            self.fail = fl.validation.base.N_(element.properties["not_empty_error"])
        else:
            self.fail = fl.validation.base.N_(u'One or more email addresses are not valid.')

        is_email_validator = IsEmail()
        if not element.optional and not element:
            return self.note_error(element, state, 'fail')
        for e in element:
            if e.value and not is_email_validator.validate(e, None):
                return self.note_error(element, state, 'fail')

        return True

class ListValue(Validator):

    fail = None

    def validate(self, element, state):
        if element.properties.get("not_empty_error"):
            self.fail = fl.validation.base.N_(element.properties["not_empty_error"])
        else:
            self.fail = fl.validation.base.N_(u'%(u)s is not a valid value for %(label)s.')

        for e in element.value:
            if e not in element.properties['valid_values']:
                return self.note_error(element, state, 'fail')

        return True

class EnumValue(Validator):

    fail = None

    def validate(self, element, state):
        if element.properties.get("not_empty_error"):
            self.fail = fl.validation.base.N_(element.properties["not_empty_error"])
        else:
            self.fail = fl.validation.base.N_(u'%(u)s is not a valid value for %(label)s.')
        if element.valid_values:
            if element.value not in element.valid_values:
                return self.note_error(element, state, 'fail')
        return True

CommonString = fl.String.using(optional=True) \
                        .with_properties(widget='input')

CommonEnum = fl.Enum.using(optional=True) \
                    .including_validators(EnumValue()) \
                    .with_properties(widget="select")
CommonEnum.value_labels = None

# CommonBoolean has optional=False because booleans are
# required to be True or False (None is not allowed)
CommonBoolean = fl.Boolean.using(optional=True).with_properties(widget="checkbox")
CommonDict = fl.Dict.with_properties(widget="group")
CommonList = fl.List.using(optional=True)
CommonInteger = fl.Integer.using(optional=True)
_valid_date = Converted(incorrect=u"%(label)s is not a valid date")
CommonDate = fl.Date.using(optional=True).including_validators(_valid_date) \
                    .with_properties(widget='date', attr={"class": "picker"}
                    )
CommonDateTime = fl.DateTime.using(optional=True).including_validators(_valid_date) \
                            .with_properties(widget='date', attr={"class": "picker"})


class SourceField(CommonEnum, object):
    valid_values = ValuesFromTable('sources', field=None)
    value_labels = DictFromTable('sources', value_field='short_name', key_field=None)

class ThematicCategoryField(CommonEnum, object):
    valid_values = ValuesFromTable('thematic_categories', field=None)
    value_labels = DictFromTable('thematic_categories',
            value_field='description', key_field=None)

class GeoScaleField(CommonEnum, object):
    valid_values = ValuesFromTable('geo_scales', field=None)
    value_labels = DictFromTable('geo_scales',
            value_field='code', key_field=None)

class GeoCoverageField(CommonEnum, object):
    valid_values = ValuesFromTable('geo_coverages', field=None)
    value_labels = DictFromTable('geo_coverages',
            value_field='code', key_field=None)

class TimelineField(CommonEnum, object):
    valid_values = ValuesFromTable('timelines', field=None)
    value_labels = DictFromTable('timelines',
            value_field='title', key_field=None)

class SteepCategoryField(CommonEnum, object):
    valid_values = ValuesFromTable('steep_categories', field=None)
    value_labels = DictFromTable('steep_categories', value_field='description',
                                 key_field=None)

class TrendField(CommonEnum, object):
    valid_values = ValuesFromTable('trends', field=None)
    value_labels = DictFromTable('trends', value_field='description',
                                 key_field=None)

class IndicatorField(CommonEnum, object):
    valid_values = ValuesFromTable('indicators', field=None)
    value_labels = DictFromTable('indicators', value_field='code',
                                 key_field=None)

class GMTField(CommonEnum, object):
    valid_values = ValuesFromTable('gmts', field=None)
    value_labels = DictFromTable('gmts', value_field='code',
                                 key_field=None)

@validator_validated.connect
def validated(sender, element, result, **kwargs):
    if sender is NotEmpty:
        if not result:
            label = getattr(element, 'label', element.name)
            msg = element.properties.get("not_empty_error",
                                         u"%s is required" % label)
            element.add_error(msg)

