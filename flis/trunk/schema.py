import flatland as fl
from flatland.signals import validator_validated
from flatland.schema.base import NotEmpty

CommonString = fl.String.using(optional=True) \
                        .with_properties(widget='input')

_SourcesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('short_name')
        .with_properties(label=u"Short name *",
                         not_empty_error=u"Please provide the short name")
        .using(optional=False),
    CommonString.named('long_name')
        .with_properties(label=u"Long name *",
                         not_empty_error=u"Please provide the long name")
        .using(optional=False),
    CommonString.named('year_of_publication')
        .with_properties(label=u"Year of publication *",
                         not_empty_error=u"Please provide the year of publication")
        .using(optional=False),
    CommonString.named('author')
        .with_properties(label=u"Author *",
                         not_empty_error=u"Please provide the author")
        .using(optional=False),
    CommonString.named('url')
        .with_properties(label=u"URL (to online availability) *",
                         not_empty_error=u"Please provide the URL")
        .using(optional=False),
    CommonString.named('summary')
        .with_properties(widget='textarea', label=u"Summary"),
)

class SourcesSchema(_SourcesSchema):

    @property
    def value(self):
        return Source(super(SourcesSchema, self).value)

class Source(dict):

    id = None

    @staticmethod
    def from_flat(sources_row):
        source = SourcesSchema.from_flat(sources_row)

        source = source.value
        source.id = sources_row.id

        return source

@validator_validated.connect
def validated(sender, element, result, **kwargs):
    if sender is NotEmpty:
        if not result:
            label = getattr(element, 'label', element.name)
            msg = element.properties.get("not_empty_error",
                                         u"%s is required" % label)
            element.add_error(msg)