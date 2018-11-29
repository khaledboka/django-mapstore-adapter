import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(PROJECT_ROOT, "uploaded"))
MEDIA_URL = ""

STATIC_ROOT = os.getenv('STATIC_ROOT',
                        os.path.join(PROJECT_ROOT, "static_root")
                        )
STATIC_URL = "/static/"

# Make this unique, and don"t share it with anybody.
SECRET_KEY = "1234567890geo-solutions-it0987654321"

SITE_ID = 1
SITEURL = "http://localhost:8000/"

# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith('/'):
    SITEURL = '{}/'.format(SITEURL)

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "example.sqlite",
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = "UTC"

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.admin",

    "mapstore2_adapter",
    "tests",
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "tests": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "mapstore2_adapter": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    }
}

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)

GEOSERVER_PUBLIC_LOCATION = os.getenv(
    #  'GEOSERVER_PUBLIC_LOCATION', '{}geoserver/'.format(SITEURL)
    'GEOSERVER_PUBLIC_LOCATION', GEOSERVER_LOCATION
)

OGC_SERVER_DEFAULT_USER = os.getenv(
    'GEOSERVER_ADMIN_USER', 'admin'
)

OGC_SERVER_DEFAULT_PASSWORD = os.getenv(
    'GEOSERVER_ADMIN_PASSWORD', 'geoserver'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': OGC_SERVER_DEFAULT_USER,
        'PASSWORD': OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOFENCE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': False,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'PG_GEOGIG': False,
        'TIMEOUT': 10  # number of seconds to allow for HTTP requests
    }
}

# If you want to enable Mosaics use the following configuration
UPLOADER = {
    # 'BACKEND': 'geonode.rest',
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': True,
        'MOSAIC_ENABLED': False,
        'GEOGIG_ENABLED': False,
    },
    'SUPPORTED_CRS': [
        'EPSG:4326',
        'EPSG:3785',
        'EPSG:3857',
        'EPSG:32647',
        'EPSG:32736'
    ],
    'SUPPORTED_EXT': [
        '.shp',
        '.csv',
        '.kml',
        '.kmz',
        '.json',
        '.geojson',
        '.tif',
        '.tiff',
        '.geotiff',
        '.gml',
        '.xml'
    ]
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
        'ALTERNATES_ONLY': True,
    }
}

PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform' \
            ' that facilitates the creation, sharing, and collaborative use' \
            ' of geospatial data',
            'identification_keywords': 'sdi, catalogue, discovery, metadata,' \
            ' GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on ' \
            'weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# GeoNode javascript client configuration

# default map projection
# Note: If set to EPSG:4326, then only EPSG:4326 basemaps will work.
DEFAULT_MAP_CRS = "EPSG:3857"

DEFAULT_LAYER_FORMAT = "image/png"

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 0

# To enable the MapStore2 based Client enable those
GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'mapstore'  # DEPRECATED use HOOKSET instead
GEONODE_CLIENT_HOOKSET = "geonode_mapstore_client.hooksets.MapStoreHookSet"


def get_geonode_catalogue_service():
    if PYCSW:
        pycsw_config = PYCSW["CONFIGURATION"]
        if pycsw_config:
            pycsw_catalogue = {
                ("%s" % pycsw_config['metadata:main']['identification_title']): {
                    "url": CATALOGUE['default']['URL'],
                    "type": "csw",
                    "title": pycsw_config['metadata:main']['identification_title'],
                    "autoload": True
                }
            }
            return pycsw_catalogue
    return None


GEONODE_CATALOGUE_SERVICE = get_geonode_catalogue_service()

MAPSTORE_CATALOGUE_SERVICES = {
    "Demo WMS Service": {
        "url": "https://demo.geo-solutions.it/geoserver/wms",
        "type": "wms",
        "title": "Demo WMS Service",
        "autoload": False
    },
    "Demo WMTS Service": {
        "url": "https://demo.geo-solutions.it/geoserver/gwc/service/wmts",
        "type": "wmts",
        "title": "Demo WMTS Service",
        "autoload": False
    }
}

MAPSTORE_CATALOGUE_SELECTED_SERVICE = "Demo WMS Service"

if GEONODE_CATALOGUE_SERVICE:
    MAPSTORE_CATALOGUE_SERVICES[list(GEONODE_CATALOGUE_SERVICE.keys())[0]] = GEONODE_CATALOGUE_SERVICE
    MAPSTORE_CATALOGUE_SELECTED_SERVICE = list(GEONODE_CATALOGUE_SERVICE.keys())[0]

DEFAULT_MS2_BACKGROUNDS = [{
    "type": "osm",
    "title": "Open Street Map",
    "name": "mapnik",
    "source": "osm",
    "group": "background",
    "visibility": True
}, {
    "type": "google",
    "title": "Google HYBRID",
    "name": "HYBRID",
    "source": "google",
    "group": "background",
    "visibility": False
}, {
    "type": "mapquest",
    "title": "MapQuest OSM",
    "name": "osm",
    "source": "mapquest",
    "group": "background",
    "visibility": False
}, {
    "type": "tileprovider",
    "title": "NASAGIBS Night 2012",
    "provider": "NASAGIBS.ViirsEarthAtNight2012",
    "name": "Night2012",
    "source": "nasagibs",
    "group": "background",
    "visibility": False
}, {
    "type": "wms",
    "url": "http://www.realvista.it/reflector/open/service",
    "visibility": False,
    "title": "e-Geos Ortofoto RealVista 1.0",
    "name": "rv1",
    "group": "background",
    "format": "image/jpeg"
}, {
    "type": "tileprovider",
    "title": "OpenTopoMap",
    "provider": "OpenTopoMap",
    "name": "OpenTopoMap",
    "source": "OpenTopoMap",
    "group": "background",
    "visibility": False
}]

MAPSTORE_BASELAYERS = DEFAULT_MS2_BACKGROUNDS

LOCAL_GEOSERVER = {
    "type": "wms",
    "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
    "visibility": True,
    "title": "Local GeoServer",
    "group": "background",
    "format": "image/png8",
    "restUrl": "/gs/rest"
}
baselayers = MAPSTORE_BASELAYERS
MAPSTORE_BASELAYERS = [LOCAL_GEOSERVER]
MAPSTORE_BASELAYERS.extend(baselayers)
