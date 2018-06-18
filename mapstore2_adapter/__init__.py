import pkg_resources


__version__ = pkg_resources.require("django-mapstore-adapter")[0].version

default_app_config = "mapstore2_adapter.apps.DOTConfig"
