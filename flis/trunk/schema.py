import flatland as fl

CommonString = fl.String.using(optional=True) \
                        .with_properties(widget='input')

SourcesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('short_name').with_properties(label=u"Short name")
        .using(optional=False),
    CommonString.named('long_name').with_properties(label=u"Long name")
        .using(optional=False),
    CommonString.named('year_of_publication')
        .with_properties(label=u"Year of publication")
        .using(optional=False),
    CommonString.named('author').with_properties(label=u"Author")
        .using(optional=False),
    CommonString.named('url')
        .with_properties(label=u"URL (to online availability)")
        .using(optional=False),
    CommonString.named('summary')
        .with_properties(widget='textarea', label=u"Summary"),
)
