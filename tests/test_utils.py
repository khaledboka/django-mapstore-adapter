from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Polygon
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.test import TestCase

from mapstore2_adapter import DjangoMapstore2AdapterBaseException
from mapstore2_adapter.utils import (GoogleZoom,
                                     get_valid_number)


logger = logging.getLogger(__name__)

UserModel = get_user_model()


class BaseTest(TestCase):

    def setUp(self):
        self.foo_user = UserModel.objects.create_user("foo_user", "test@example.com", "123456")
        self.bar_user = UserModel.objects.create_user("bar_user", "dev@example.com", "123456")

    def tearDown(self):
        self.foo_user.delete()
        self.bar_user.delete()


class TestAdapterUtils(BaseTest):

    def test_get_valid_numbers(self):
        self.assertEqual(get_valid_number(1.2), 1.2)
        self.assertEqual(get_valid_number('1.2'), 1.2)
        self.assertEqual(get_valid_number('1.2a'), 0)
        self.assertEqual(get_valid_number('1.2b', default=90, complementar=False), 90)
        self.assertEqual(get_valid_number('1.2c', default=90, complementar=True), -90)

    def test_google_zoom(self):
        google_zoom = GoogleZoom()
        self.assertIsNotNone(google_zoom)

        def get_zoom(ov_bbox, ov_crs):
            srid = int(ov_crs.split(':')[1])
            srid = 3857 if srid == 900913 else srid
            poly = Polygon((
                (ov_bbox[0], ov_bbox[1]),
                (ov_bbox[0], ov_bbox[3]),
                (ov_bbox[2], ov_bbox[3]),
                (ov_bbox[2], ov_bbox[1]),
                (ov_bbox[0], ov_bbox[1])), srid=srid)
            gcoord = SpatialReference(4326)
            ycoord = SpatialReference(srid)
            trans = CoordTransform(ycoord, gcoord)
            poly.transform(trans)
            zoom = GoogleZoom().get_zoom(poly)
            return zoom

        # 1. Test Over Max Earth Extent
        ov_bbox = [get_valid_number(-180),
                   get_valid_number(-90),
                   get_valid_number(180),
                   get_valid_number(90), ]
        ov_crs = 'EPSG:4326'

        with self.assertRaises(DjangoMapstore2AdapterBaseException) as cm:
            get_zoom(ov_bbox, ov_crs)

        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'Geometry width and height should not exceed that of the Earth.')

        # 2. Test Valid BBOX WGS-84
        ov_bbox = [get_valid_number(-89.871902282000000),
                   get_valid_number(14.130479802000000),
                   get_valid_number(-88.711514902000000),
                   get_valid_number(15.098465755000000), ]
        ov_crs = 'EPSG:4326'
        self.assertEqual(get_zoom(ov_bbox, ov_crs), 8)

        # 3. Test Valid BBOX UTM
        ov_bbox = [get_valid_number(419999.997500000000000),
                   get_valid_number(4248999.996700000000000),
                   get_valid_number(500000.000000000000000),
                   get_valid_number(4416000.000000000000000), ]
        ov_crs = 'EPSG:26918'
        self.assertEqual(get_zoom(ov_bbox, ov_crs), 7)

        # 4. Test Valid BBOX Google Mercator
        ov_bbox = [get_valid_number(-1.000449439865508E7),
                   get_valid_number(1589190.418957951),
                   get_valid_number(-9875320.66639054),
                   get_valid_number(1700550.5842322353), ]
        ov_crs = 'EPSG:900913'
        self.assertEqual(get_zoom(ov_bbox, ov_crs), 8)
