from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model
from django.test import TestCase

from mapstore2_adapter.utils import to_json
from mapstore2_adapter.converters import BaseMapStore2ConfigConverter
from mapstore2_adapter.plugins.geonode import GeoNodeMapStore2ConfigConverter


logger = logging.getLogger(__name__)

UserModel = get_user_model()
BaseConfigConverter = BaseMapStore2ConfigConverter()
GeoNodeConfigConverter = GeoNodeMapStore2ConfigConverter()


class BaseTest(TestCase):

    def setUp(self):
        self.foo_user = UserModel.objects.create_user("foo_user", "test@example.com", "123456")
        self.bar_user = UserModel.objects.create_user("bar_user", "dev@example.com", "123456")

    def tearDown(self):
        self.foo_user.delete()
        self.bar_user.delete()


class TestBaseConfigConverter(BaseTest):

    def test_base_interface(self):
        with self.assertRaises(NotImplementedError):
            BaseConfigConverter.convert(None, None)

        with self.assertRaises(NotImplementedError):
            BaseConfigConverter.get_overlays(None)

        with self.assertRaises(NotImplementedError):
            BaseConfigConverter.get_center_and_zoom(None, None)

        with self.assertRaises(NotImplementedError):
            BaseConfigConverter.viewer_json(None, None)


GEONODE_SAMPLE_GXP_CONFIG = """{
    "map": {
        "layers": [{
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "args": ["No background"],
            "visibility": false,
            "source": "0",
            "group": "background",
            "fixed": true,
            "type": "OpenLayers.Layer",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "title": "UNESCO",
            "args": ["UNESCO", "http://en.unesco.org/tiles/${z}/${x}/${y}.png"],
            "visibility": false,
            "group": "background",
            "source": "0",
            "attribution": "&copy; UNESCO",
            "fixed": true,
            "type": "OpenLayers.Layer.XYZ",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "title": "UNESCO GEODATA",
            "args": ["UNESCO GEODATA", "http://en.unesco.org/tiles/geodata/${z}/${x}/${y}.png"],
            "visibility": false,
            "group": "background",
            "source": "0",
            "attribution": "&copy; UNESCO",
            "fixed": true,
            "type": "OpenLayers.Layer.XYZ",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "title": "Humanitarian OpenStreetMap",
            "args": ["Humanitarian OpenStreetMap", "http://a.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png"],
            "visibility": false,
            "group": "background",
            "source": "0",
            "attribution": "&copy; <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a>",
            "fixed": true,
            "type": "OpenLayers.Layer.XYZ",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "title": "MapBox Satellite Streets",
            "args": ["MapBox Satellite Streets",
                     "http://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/${z}/${x}/${y}"],
            "visibility": false,
            "group": "background",
            "source": "0",
            "attribution": "&copy; <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> &copy",
            "fixed": true,
            "type": "OpenLayers.Layer.XYZ",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "background",
            "title": "MapBox Streets",
            "args": ["MapBox Streets",
                     "http://api.mapbox.com/styles/v1/mapbox/streets-v9/tiles/${z}/${x}/${y}"],
            "visibility": false,
            "group": "background",
            "source": "0",
            "attribution": "&copy; <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> &copy",
            "fixed": true,
            "type": "OpenLayers.Layer.XYZ",
            "id": 1
        }, {
            "opacity": 1,
            "wrapDateLine": true,
            "displayOutsideMaxExtent": true,
            "name": "mapnik",
            "title": "OpenStreetMap",
            "visibility": true,
            "group": "background",
            "source": "1",
            "attribution": "&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors",
            "fixed": true,
            "type": "OpenLayers.Layer.OSM",
            "id": 1
        }, {
            "opacity": 1.0,
            "crs": {
                "type": "name",
                "properties": "EPSG:4326"
            },
            "wrapDateLine": true,
            "selected": true,
            "attribution": "<span class='gx-attribution-title'>Alberto Hernandez-salinas</span>",
            "name": "geonode:a__4202_Precipitacion",
            "format": "image/png",
            "title": "a__4202_Precipitacion",
            "visibility": true,
            "capability": {
                "styles": [{
                    "title": "a__4202_Precipitacion",
                    "legend": {
                        "height": "40",
                        "width": "22",
                        "href": "http://ihp-wins.unesco.org/geoserver/ows?service=wms&request=GetLegendGraphic&...",
                        "format": "image/png"
                    },
                    "name": "a__4202_Precipitacion"
                }],
                "attribution": {
                    "title": "Alberto Hernandez-salinas"
                },
                "name": "geonode:a__4202_Precipitacion",
                "infoFormats": ["text/plain",
                                "application/vnd.ogc.gml",
                                "text/xml",
                                "application/vnd.ogc.gml/3.1.1",
                                "text/xml; subtype=gml/3.1.1",
                                "text/html",
                                "application/json"],
                "abstract": "Pas de r\u00e9sum\u00e9",
                "title": "a__4202_Precipitacion",
                "srs": {
                    "EPSG:3857": true
                },
                "prefix": "geonode",
                "bbox": {
                    "EPSG:900913": {
                        "srs": "EPSG:900913",
                        "bbox": [-10004494.3987, 1589190.41896, -9875320.66639, 1700550.58423]
                    },
                    "EPSG:4326": {
                        "srs": "EPSG:4326",
                        "bbox": [-89.871902282, 14.130479802, -88.711514902, 15.098465755]
                    },
                    "EPSG:3857": {
                        "srs": "EPSG:3857",
                        "bbox": [-10004494.3987, 1589190.41896, -9875320.66639, 1700550.58423]
                    }
                },
                "formats": ["image/png",
                            "application/atom xml",
                            "application/atom+xml",
                            "application/json;type=utfgrid",
                            "application/openlayers",
                            "application/pdf",
                            "application/rss xml",
                            "application/rss+xml",
                            "application/vnd.google-earth.kml",
                            "application/vnd.google-earth.kml xml",
                            "application/vnd.google-earth.kml+xml",
                            "application/vnd.google-earth.kml+xml;mode=networklink",
                            "application/vnd.google-earth.kmz",
                            "application/vnd.google-earth.kmz xml",
                            "application/vnd.google-earth.kmz+xml",
                            "application/vnd.google-earth.kmz;mode=networklink",
                            "atom",
                            "image/geotiff",
                            "image/geotiff8",
                            "image/gif",
                            "image/gif;subtype=animated",
                            "image/jpeg",
                            "image/png8",
                            "image/png; mode=8bit",
                            "image/svg",
                            "image/svg xml",
                            "image/svg+xml",
                            "image/tiff",
                            "image/tiff8",
                            "image/vnd.jpeg-png",
                            "kml",
                            "kmz",
                            "openlayers",
                            "rss",
                            "text/html; subtype=openlayers",
                            "utfgrid"],
                "keywords": [],
                "queryable": true,
                "llbbox": [-89.871902282, 14.130479802, -88.711514902, 15.098465755]
            },
            "srs": "EPSG:3857",
            "bbox": [-10004494.3987, 1589190.41896, -9875320.66639, 1700550.58423],
            "getFeatureInfo": {
                "fields": ["GRAY_INDEX"],
                "propertyNames": {
                    "GRAY_INDEX": null
                }
            },
            "fixed": false,
            "source": "2"
        }],
        "center": [0.0, -7.081154550627918e-10],
        "units": "m",
        "maxResolution": 156543.03390625,
        "maxExtent": [-20037508.34, -20037508.34, 20037508.34, 20037508.34],
        "zoom": 0,
        "projection": "EPSG:3857"
    },
    "about": {
        "abstract": "",
        "title": ""
    },
    "sources": {
        "1": {
            "ptype": "gxp_osmsource"
        },
        "0": {
            "ptype": "gxp_olsource"
        },
        "3": {
            "url": "http://ihp-wins.unesco.org/geoserver/wms",
            "restUrl": "/gs/rest",
            "ptype": "gxp_wmscsource",
            "title": "Local Geoserver"
        },
        "2": {
            "url": "http://ihp-wins.unesco.org/geoserver/ows",
            "restUrl": "/gs/rest",
            "ptype": "gxp_wmscsource"
        }
    },
    "aboutUrl": "../about",
    "defaultSourceType": "gxp_wmscsource",
    "id": 0
}"""


class TestGeoNodeConfigConverter(BaseTest):

    def test_ms2_config_convert(self):
        ms2_config = to_json(GeoNodeConfigConverter.convert(GEONODE_SAMPLE_GXP_CONFIG, None))

        self.assertIsNotNone(ms2_config)
        self.assertIsNotNone(ms2_config['version'])

        self.assertEqual(ms2_config['version'], 2)

        self.assertIsNotNone(ms2_config['catalogServices'])
        self.assertIsNotNone(ms2_config['catalogServices']['selectedService'])
        self.assertIsNotNone(ms2_config['catalogServices']['services'])

        self.assertEqual(ms2_config['catalogServices']['selectedService'], 'GeoNode Catalogue')
        self.assertEqual(len(ms2_config['catalogServices']['services']), 3)

        self.assertIsNotNone(ms2_config['map'])

        self.assertIsNotNone(ms2_config['map']['center'])
        self.assertIsNotNone(ms2_config['map']['layers'])
        self.assertIsNotNone(ms2_config['map']['maxExtent'])
        self.assertIsNotNone(ms2_config['map']['maxResolution'])
        self.assertIsNotNone(ms2_config['map']['projection'])
        self.assertIsNotNone(ms2_config['map']['units'])
        self.assertIsNotNone(ms2_config['map']['zoom'])

        self.assertEqual(ms2_config['map']['maxExtent'], [-20037508.34, -20037508.34, 20037508.34, 20037508.34])
        self.assertEqual(ms2_config['map']['maxResolution'], 156543.03390625)
        self.assertEqual(ms2_config['map']['projection'], 'EPSG:3857')
        self.assertEqual(ms2_config['map']['units'], 'm')
        self.assertEqual(ms2_config['map']['zoom'], 9)

        self.assertEqual(ms2_config['map']['center']['crs'], 'EPSG:3857')
        self.assertEqual(ms2_config['map']['center']['x'], -9939907.532545)
        self.assertEqual(ms2_config['map']['center']['y'], 1644870.5015949998)

        self.assertEqual(len(ms2_config['map']['layers']), 12)

    def test_gxp_config_convert(self):
        ms2_config = GeoNodeConfigConverter.convert(GEONODE_SAMPLE_GXP_CONFIG, None)
        gxp_config = GeoNodeConfigConverter.viewer_json(ms2_config, None)

        self.assertIsNotNone(gxp_config)
        # TODO
