from climweb.base.registries import Plugin


class PluginNamePlugin(Plugin):
    type = "oidcplugin"

    def get_urls(self):
        return []
