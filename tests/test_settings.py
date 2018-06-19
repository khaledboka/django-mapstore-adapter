from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
from mapstore2_adapter.settings import (MAP_BASELAYERS,
                                        CATALOGUE_SERVICES)

logger = logging.getLogger(__name__)

UserModel = get_user_model()


class BaseTest(TestCase):

    def setUp(self):
        self.foo_user = UserModel.objects.create_user("foo_user", "test@example.com", "123456")
        self.bar_user = UserModel.objects.create_user("bar_user", "dev@example.com", "123456")

    def tearDown(self):
        self.foo_user.delete()
        self.bar_user.delete()


class TestApplicationSettings(BaseTest):

    def test_adapter_settings(self):
        self.assertIsNotNone(MAP_BASELAYERS)
        self.assertEqual(len(MAP_BASELAYERS), 11)

        local_geoserver = MAP_BASELAYERS[0]
        self.assertEqual(local_geoserver['title'], 'Local GeoServer')
        self.assertEqual(local_geoserver['url'], settings.OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms")

        self.assertIsNotNone(CATALOGUE_SERVICES)
        self.assertEqual(len(CATALOGUE_SERVICES), 3)

        local_geonode = CATALOGUE_SERVICES['GeoNode Catalogue']['GeoNode Catalogue']
        self.assertEqual(local_geonode['title'], 'GeoNode Catalogue')
        self.assertEqual(local_geonode['url'], settings.CATALOGUE['default']['URL'])
