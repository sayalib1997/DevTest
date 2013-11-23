from mock import patch
from .base import BaseWebTest
from .base import user_admin_mock, user_anonymous_mock
from .base import user_ro_group_mock, user_dk_group_mock, user_blank_admin_mock
from .factories import ROCountryFactory, InterlinkFactory, TrendFactory


__all__ = ('InterlinksPermTests', )


class InterlinksPermTests(BaseWebTest):

    def setUp(self):
        self.country = ROCountryFactory()
        super(InterlinksPermTests, self).setUp()

    @patch('flis.frame.requests')
    def test_interlinks_new_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        data = InterlinkFactory.attributes(create=True)
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['interlink-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Interlink', pk=1,
                                    gmt=data['gmt'],
                                    trend=data['trend'],
                                    indicator_1=data['indicator_1'],
                                    uncertainty=data['uncertainty'],
                                    country=self.country,
                                    user_id='admin')

    @patch('flis.frame.requests')
    def test_interlinks_new_with_blank_admin_user_perm(self, mock_requests):
        mock_requests.get.return_value = user_blank_admin_mock
        data = InterlinkFactory.attributes(create=True)
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['interlink-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Interlink', pk=1,
                                    gmt=data['gmt'],
                                    trend=data['trend'],
                                    indicator_1=data['indicator_1'],
                                    uncertainty=data['uncertainty'],
                                    country=self.country,
                                    user_id='')

    @patch('flis.frame.requests')
    def test_interlinks_new_ro_group_perm(self, mock_requests):
        mock_requests.get.return_value = user_ro_group_mock
        data = InterlinkFactory.attributes(create=True)
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        form = resp.forms['interlink-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Interlink', pk=1,
                                    gmt=data['gmt'],
                                    trend=data['trend'],
                                    indicator_1=data['indicator_1'],
                                    uncertainty=data['uncertainty'],
                                    country=self.country,
                                    user_id='john')

    @patch('flis.frame.requests')
    def test_interlinks_new_anonymous_perm_fails(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        data = InterlinkFactory.attributes(create=True)
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.pyquery.find('#restricted-title')))

    @patch('flis.frame.requests')
    def test_interlinks_new_dk_group_perm_fails(self, mock_requests):
        mock_requests.get.return_value = user_dk_group_mock
        data = InterlinkFactory.attributes(create=True)
        url = self.reverse('interlink_new', country='ro')
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.pyquery.find('#restricted-title')))

    @patch('flis.frame.requests')
    def test_interlinks_edit_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        interlink = InterlinkFactory(country=self.country)
        trend = TrendFactory()
        data = {
            'trend': trend,
            'gmt': interlink.gmt,
            'uncertainty': interlink.uncertainty,
            'indicator_1': interlink.indicator_1,
        }
        url = self.reverse('interlink_edit', country='ro', pk=interlink.pk)
        resp = self.app.get(url)
        form = resp.forms['interlink-edit']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase('Interlink', pk=1,
                                    trend=trend,
                                    gmt=data['gmt'],
                                    indicator_1=data['indicator_1'],
                                    uncertainty=data['uncertainty'],
                                    user_id='admin',
                                    country=self.country)

    @patch('flis.frame.requests')
    def test_interlinks_edit_anonymous_perm_fails(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        interlink = InterlinkFactory(country=self.country)
        trend = TrendFactory()
        data = {
            'trend': trend,
            'gmt': interlink.gmt,
            'indicator_1': interlink.indicator_1,
        }
        url = self.reverse('interlink_edit', country='ro', pk=interlink.pk)
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.pyquery.find('#restricted-title')))

    @patch('flis.frame.requests')
    def test_interlinks_delete_admin_perm(self, mock_requests):
        mock_requests.get.return_value = user_admin_mock
        interlink = InterlinkFactory(country=self.country)
        url = self.reverse('interlink_delete', pk=interlink.pk, country='ro')
        self.app.delete(url)
        with self.assertRaises(AssertionError):
            self.assertObjectInDatabase('Interlink', pk=1)

    @patch('flis.frame.requests')
    def test_interlinks_delete_anonymous_perm_fails(self, mock_requests):
        mock_requests.get.return_value = user_anonymous_mock
        interlink = InterlinkFactory(country=self.country)
        url = self.reverse('interlink_delete', pk=interlink.pk, country='ro')
        self.app.delete(url)
        self.assertObjectInDatabase('Interlink', pk=1)
