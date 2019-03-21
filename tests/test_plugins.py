# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2019, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################


from __future__ import unicode_literals

import logging
import mock
from django.contrib.auth import get_user_model
from geonode.tests.base import GeoNodeBaseTestSupport
from mapstore2_adapter.plugins.serializers import GeoNodeSerializer
from collections import OrderedDict
import copy
from geonode.maps.models import Map

logger = logging.getLogger(__name__)

UserModel = get_user_model()

REQUEST_DATA = {
    u'attributes': [
        {
            u'label': u'Title',
            u'name': u'title',
            u'type': u'string',
            u'value': u'map_test'
        },
        {
            u'label': u'Abstract',
            u'name': u'abstract',
            u'type': u'string',
            u'value': u''
        }
    ],
    u'data': {
        u'catalogServices': {
            u'selectedService': u'GeoNode Catalogue',
            u'services': {
                u'Demo WMS Service': {
                    u'autoload': False,
                    u'title': u'Demo WMS Service',
                    u'type': u'wms',
                    u'url': u'https://demo.geo-solutions.it/geoserver/wms'
                },
                u'Demo WMTS Service': {
                    u'autoload': False,
                    u'title': u'Demo WMTS Service',
                    u'type': u'wmts',
                    u'url': u'https://demo.geo-solutions.it/geoserver/gwc/service/wmts'
                },
                u'GeoNode Catalogue': {
                    u'autoload': True,
                    u'title': u'GeoNode Catalogue',
                    u'type': u'csw',
                    u'url': u'http://localhost:8000/catalogue/csw'
                }
            }
        },
        u'map': {
            u'center': {
                u'crs': u'EPSG:4326',
                u'x': 63.5098725,
                u'y': 4.702489499999971
            },
            u'groups': [
                {
                    u'expanded': True,
                    u'id': u'Default'
                }
            ],
            u'layers': [
                {
                    u'dimensions': [],
                    u'group': u'background',
                    u'handleClickOnLayer': False,
                    u'hidden': False,
                    u'hideLoading': False,
                    u'id': u'mapnik__0',
                    u'name': u'mapnik',
                    u'opacity': 1,
                    u'singleTile': False,
                    u'source': u'osm',
                    u'title': u'Open Street Map',
                    u'type': u'osm',
                    u'useForElevation': False,
                    u'visibility': True
                },
                {
                    u'dimensions': [],
                    u'group': u'background',
                    u'handleClickOnLayer': False,
                    u'hidden': False,
                    u'hideLoading': False,
                    u'id': u'OpenTopoMap__1',
                    u'name': u'OpenTopoMap',
                    u'opacity': 1,
                    u'provider': u'OpenTopoMap',
                    u'singleTile': False,
                    u'source': u'OpenTopoMap',
                    u'title': u'OpenTopoMap',
                    u'type': u'tileprovider',
                    u'useForElevation': False,
                    u'visibility': False
                },
                {
                    u'dimensions': [],
                    u'format': u'image/png8',
                    u'group': u'background',
                    u'handleClickOnLayer': False,
                    u'hidden': False,
                    u'hideLoading': False,
                    u'id': u's2cloudless',
                    u'name': u's2cloudless:s2cloudless',
                    u'opacity': 1,
                    u'singleTile': False,
                    u'thumbURL': u'http://localhost:8000/static/mapstorestyle/img/s2cloudless-s2cloudless.png',
                    u'title': u'Sentinel-2 cloudless - https://s2maps.eu',
                    u'type': u'wms',
                    u'url': u'https://maps.geo-solutions.it/geoserver/wms',
                    u'useForElevation': False,
                    u'visibility': False
                },
                {
                    u'dimensions': [],
                    u'group': u'background',
                    u'handleClickOnLayer': False,
                    u'hidden': False,
                    u'hideLoading': False,
                    u'id': u'none',
                    u'name': u'empty',
                    u'opacity': 1,
                    u'singleTile': False,
                    u'source': u'ol',
                    u'title': u'Empty Background',
                    u'type': u'empty',
                    u'useForElevation': False,
                    u'visibility': False
                },
                {
                    u'availableStyles': [
                        {
                            u'TYPE_NAME': u'WMS_1_3_0.Style',
                            u'filename': u'indicator_data_improved_water_sustai_cities1.sld',
                            u'format': u'sld',
                            u'languageVersion': {
                                u'version': u'1.1.0'
                            },
                            u'legendURL': [
                                {
                                    u'TYPE_NAME': u'WMS_1_3_0.LegendURL',
                                    u'format': u'image/png',
                                    u'height': 120,
                                    u'onlineResource': {
                                        u'TYPE_NAME': u'WMS_1_3_0.OnlineResource',
                                        u'href': u'http://localhost:8080/geoserver/geonode/indicator_data_improved_water_sustai_cities1/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=indicator_data_improved_water_sustai_cities1&access_token=None',
                                        u'type': u'simple'
                                    },
                                    u'width': 104
                                }
                            ],
                            u'name': u'geonode:indicator_data_improved_water_sustai_cities1',
                            u'title': u'geonode:indicator_data_improved_water_sustai_cities1',
                            u'workspace': {
                                u'name': u'geonode'
                            }
                        },
                        {
                            u'TYPE_NAME': u'WMS_1_3_0.Style',
                            u'filename': u'indicator_data_improved_water_sustai_cities1.sld',
                            u'format': u'sld',
                            u'languageVersion': {
                                u'version': u'1.1.0'
                            },
                            u'legendURL': [
                                {
                                    u'TYPE_NAME': u'WMS_1_3_0.LegendURL',
                                    u'format': u'image/png',
                                    u'height': 120,
                                    u'onlineResource': {
                                        u'TYPE_NAME': u'WMS_1_3_0.OnlineResource',
                                        u'href': u'http://localhost:8080/geoserver/geonode/indicator_data_improved_water_sustai_cities1/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=indicator_data_improved_water_sustai_cities1&style=indicator_data_improved_water_sustai_cities1&access_token=None',
                                        u'type': u'simple'
                                    },
                                    u'width': 104
                                }
                            ],
                            u'name': u'geonode:indicator_data_improved_water_sustai_cities1',
                            u'title': u'geonode:indicator_data_improved_water_sustai_cities1',
                            u'workspace': {
                                u'name': u'geonode'
                            }
                        },
                        {
                            u'TYPE_NAME': u'WMS_1_3_0.Style',
                            u'filename': u'test.sld',
                            u'format': u'sld',
                            u'languageVersion': {
                                u'version': u'1.0.0'
                            },
                            u'legendURL': [
                                {
                                    u'TYPE_NAME': u'WMS_1_3_0.LegendURL',
                                    u'format': u'image/png',
                                    u'height': 20,
                                    u'onlineResource': {
                                        u'TYPE_NAME': u'WMS_1_3_0.OnlineResource',
                                        u'href': u'http://localhost:8080/geoserver/geonode/indicator_data_improved_water_sustai_cities1/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=indicator_data_improved_water_sustai_cities1&style=test&access_token=None',
                                        u'type': u'simple'
                                    },
                                    u'width': 20
                                }
                            ],
                            u'name': u'geonode:test',
                            u'title': u'orange square point style',
                            u'workspace': {
                                u'name': u'geonode'
                            }
                        },
                        {
                            u'TYPE_NAME': u'WMS_1_3_0.Style',
                            u'filename': u'Green Big Circle.sld',
                            u'format': u'sld',
                            u'languageVersion': {
                                u'version': u'1.0.0'
                            },
                            u'legendURL': [
                                {
                                    u'TYPE_NAME': u'WMS_1_3_0.LegendURL',
                                    u'format': u'image/png',
                                    u'height': 20,
                                    u'onlineResource': {
                                        u'TYPE_NAME': u'WMS_1_3_0.OnlineResource',
                                        u'href': u'http://localhost:8080/geoserver/geonode/indicator_data_improved_water_sustai_cities1/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=indicator_data_improved_water_sustai_cities1&style=Green%20Big%20Circle&access_token=None',
                                        u'type': u'simple'
                                    },
                                    u'width': 20
                                }
                            ],
                            u'name': u'geonode:Green Big Circle',
                            u'title': u'green big circle point style',
                            u'workspace': {
                                u'name': u'geonode'
                            }
                        }
                    ],
                    u'bbox': {
                        u'bounds': {
                            u'maxx': 15662650.1282,
                            u'maxy': 5361570.19282,
                            u'minx': -1522876.79413,
                            u'miny': -4018066.50808
                        },
                        u'crs': u'EPSG:3857'
                    },
                    u'description': u'No abstract provided',
                    u'dimensions': [
                        {
                            u'name': u'time',
                            u'source': {
                                u'type': u'multidim-extension',
                                u'url': u'http://localhost:8080/gs/gwc/service/wmts'
                            }
                        }
                    ],
                    u'featureInfo': {
                        u'format': u'TEMPLATE',
                        u'template': u'<div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">LATITUDE</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties.LATITUDE}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">LONGITUDE</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties.LONGITUDE}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">NAME</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties.NAME}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1990_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1990_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1991_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1991_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1992_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1992_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1993_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1993_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1994_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1994_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1995_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1995_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1996_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1996_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1997_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1997_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1998_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1998_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_1999_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._1999_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2000_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2000_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2001_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2001_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2002_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2002_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2003_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2003_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2004_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2004_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2005_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2005_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">_2006_1</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties._2006_1}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">LATESVALUE</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties.LATESVALUE}</div></div><div class="row"><div class="col-xs-4" style="font-weight: bold; word-wrap: break-word;">YEARLATVAL</div>                                         <div class="col-xs-8" style="word-wrap: break-word;">${properties.YEARLATVAL}</div></div></div>'
                    },
                    u'format': u'image/png',
                    u'group': u'',
                    u'handleClickOnLayer': False,
                    u'hidden': False,
                    u'hideLoading': False,
                    u'id': u'geonode:indicator_data_improved_water_sustai_cities1__4',
                    u'name': u'geonode:indicator_data_improved_water_sustai_cities1',
                    u'opacity': 1,
                    u'search': {
                        u'type': u'wfs',
                        u'url': u'http://localhost:8000/gs/ows'
                    },
                    u'singleTile': False,
                    u'style': u'geonode:test',
                    u'styles': [
                        {
                            u'legend': {
                                u'format': u'image/png',
                                u'height': u'40',
                                u'href': u'http://localhost:8080/geoserver/ows?service=wms&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=geonode%3Aindicator_data_improved_water_sustai_cities1',
                                u'width': u'22'
                            },
                            u'name': u'indicator_data_improved_water_sustai_cities1',
                            u'title': u'indicator_data_improved_water_sustai_cities1'
                        },
                        {
                            u'legend': {
                                u'format': u'image/png',
                                u'height': u'40',
                                u'href': u'http://localhost:8080/geoserver/ows?service=wms&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=geonode%3Aindicator_data_improved_water_sustai_cities1',
                                u'width': u'22'
                            },
                            u'name': u'test',
                            u'title': u'orange square point style'
                        },
                        {
                            u'legend': {
                                u'format': u'image/png',
                                u'height': u'40',
                                u'href': u'http://localhost:8080/geoserver/ows?service=wms&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=geonode%3Aindicator_data_improved_water_sustai_cities1',
                                u'width': u'22'
                            },
                            u'name': u'Green Big Circle',
                            u'title': u'green big circle point style'
                        }
                    ],
                    u'title': u'indicator_data_improved_water_sustai_cities1',
                    u'type': u'wms',
                    u'url': u'http://localhost:8080/geoserver/ows',
                    u'useForElevation': False,
                    u'visibility': True
                }
            ],
            u'mapOptions': {},
            u'maxExtent': [
                -20037508.34,
                -20037508.34,
                20037508.34,
                20037508.34
            ],
            u'projection': u'EPSG:3857',
            u'units': u'm',
            u'zoom': 4
        },
        u'version': 2,
        u'widgetsConfig': {}
    },
    u'name': u'map_test'
}


class TestGeoNodeSerializer(GeoNodeBaseTestSupport):

    geonode_serializer = GeoNodeSerializer()

    def setUp(self):
        super(TestGeoNodeSerializer, self).setUp()
        self.foo_user = UserModel.objects.create_user(
            "foo_user", "test@example.com", "123456"
        )

    @mock.patch("mapstore2_adapter.api.serializers.MapStoreResourceSerializer",
                autospec=True)
    @mock.patch("mapstore2_adapter.api.views.MapStoreResourceViewSet")
    def test_set_geonode_map(self, caller, serializer):

        # To prevent pop
        request_data = copy.deepcopy(REQUEST_DATA)

        # Login
        login_ok = self.client.login(username='foo_user', password='123456')
        self.assertTrue(login_ok)
        # Mock caller and serializer
        serializer.validated_data = OrderedDict([(u'name', u'map_test')])
        caller.request.user = self.foo_user
        # Call the function
        self.geonode_serializer.set_geonode_map(
            caller=caller,
            serializer=serializer,
            map_obj=None,
            data=request_data["data"],
            attributes=request_data["attributes"]
        )
        # Map
        map_obj = Map.objects.filter(
            title=REQUEST_DATA['name']
        ).first()
        self.assertIsNotNone(map_obj)
        # Layers
        for map_layer in REQUEST_DATA['data']['map']['layers']:
            layer = [lyr for lyr in map_obj.layers if lyr.name == map_layer['name']][0]
            self.assertTrue(layer)
            # Styles
            if 'styles' in map_layer:
                for style in map_layer['styles']:
                    self.assertTrue(style['name'] in layer.styles)
            # Dimensions
            if 'dimensions' in map_layer:
                for dim in map_layer['dimensions']:
                    self.assertIn(dim['name'], layer.layer_params)
                    self.assertIn(dim['source']['type'], layer.layer_params)
                    self.assertIn(dim['source']['url'], layer.layer_params)
            # Opacity
            self.assertEquals(map_layer['opacity'], layer.opacity)
            # Visibility
            self.assertEquals(map_layer['visibility'], layer.visibility)



