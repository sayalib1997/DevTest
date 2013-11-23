from mock import patch
from .base import BaseWebTest
from .base import user_admin_mock, user_anonymous_mock
from .base import user_dk_group_mock
from .factories import ROCountryFactory, IndicatorFactory
from .factories import ThematicCategoryFactory, GeographicalScaleFactory
from .factories import SourceFactory, TimelineFactory


__all__ = ('IndicatorPermTests', )


class IndicatorPermTests(BaseWebTest):

    def setUp(self):
        self.country = ROCountryFactory()
        ThematicCategoryFactory.reset_sequence()
        GeographicalScaleFactory.reset_sequence()
        TimelineFactory.reset_sequence()
        SourceFactory.reset_sequence()
        IndicatorFactory.reset_sequence()
        super(IndicatorPermTests, self).setUp()

    @patch('flis.frame.requests')
    def test_indicator_new_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        data = IndicatorFactory.attributes(create=True)
        url = self.reverse('indicator_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['indicator-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Indicator', pk=1,
                                    code='indicator_1',
                                    description='indicator_description',
                                    thematic_category=data['thematic_category'],
                                    geographical_scale=data['geographical_scale'],
                                    timeline=data['timeline'],
                                    source=data['source'],
                                    base_year='2000',
                                    end_year='2004',
                                    ownership='ownership')

    @patch('flis.frame.requests')
    def test_indicator_new_dk_group_perm(self, mock_requests):
        mock_requests.get.return_value = user_dk_group_mock
        data = IndicatorFactory.attributes(create=True)
        url = self.reverse('indicator_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['indicator-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Indicator', pk=1,
                                    code='indicator_1',
                                    description='indicator_description',
                                    thematic_category=data['thematic_category'],
                                    geographical_scale=data['geographical_scale'],
                                    timeline=data['timeline'],
                                    source=data['source'],
                                    base_year='2000',
                                    end_year='2004',
                                    ownership='ownership')

    @patch('flis.frame.requests')
    def test_indicator_new_anonymous_perm_fails(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        data = IndicatorFactory.attributes(create=True)
        url = self.reverse('indicator_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.pyquery.find('#restricted-title')))

    @patch('flis.frame.requests')
    def test_indicator_edit_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        indicator = IndicatorFactory()
        thematic_category = ThematicCategoryFactory()
        geographical_scale = GeographicalScaleFactory()
        data = {
            'code': indicator.code,
            'description': indicator.description,
            'thematic_category': thematic_category,
            'geographical_scale': geographical_scale,
            'timeline': indicator.timeline,
            'source': indicator.source,
            'base_year': indicator.base_year,
            'end_year': indicator.end_year,
            'ownership': indicator.ownership,
        }
        url = self.reverse('indicator_edit', pk=indicator.pk, country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['indicator-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Indicator', pk=1,
                                    code='indicator_1',
                                    description='indicator_description',
                                    thematic_category=data['thematic_category'],
                                    geographical_scale=data['geographical_scale'],
                                    timeline=data['timeline'],
                                    source=data['source'],
                                    base_year='2000',
                                    end_year='2004',
                                    ownership='ownership')

    @patch('flis.frame.requests')
    def test_indicator_edit_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        indicator = IndicatorFactory()
        url = self.reverse('indicator_edit', pk=indicator.pk, country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.pyquery.find('#restricted-title')))

    @patch('flis.frame.requests')
    def test_indicator_delete_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        indicator = IndicatorFactory()
        url = self.reverse('indicator_delete', pk=indicator.pk, country='ro')
        resp = self.app.delete(url)
        with self.assertRaises(AssertionError):
            self.assertObjectInDatabase('Indicator', pk=1)

    @patch('flis.frame.requests')
    def test_indicator_delete_anonymous_perm(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        indicator = IndicatorFactory()
        url = self.reverse('indicator_delete', pk=indicator.pk, country='ro')
        resp = self.app.delete(url)
        self.assertObjectInDatabase('Indicator', pk=1)
