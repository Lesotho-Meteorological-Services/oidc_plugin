from climweb.base.registries import Plugin
from django.urls import path, include


class PluginNamePlugin(Plugin):
    type = "oidcplugin"

    def get_urls(self):
        return [
            path(
                "oidc/",
                include("mozilla_django_oidc.urls"),
            ),
        ]
