def setup(settings):
    """
    This function is called after climweb has setup its own Django settings file but
    before Django starts. Read and modify provided settings object as appropriate
    just like you would in a normal Django settings file. E.g.:

    settings.INSTALLED_APPS += ["some_custom_plugin_dep"]
    """

    settings.INSTALLED_APPS += ["mozilla_django_oidc"]
    settings.AUTHENTICATION_BACKENDS += ['mozilla_django_oidc.auth.OIDCAuthenticationBackend']

    settings.OIDC_RP_CLIENT_ID = "share"
    settings.OIDC_RP_CLIENT_SECRET = "ypz9oJ2MJnCjjl1m3NPCYh5OmbbKOyAN"

    settings.OIDC_RP_CALLBACK_URL = "https://share.csis.gov.ls/oidc/callback/"
    settings.OIDC_RP_SIGN_ALGO = "RS256"

    settings.OIDC_OP_AUTHORIZATION_ENDPOINT = "https://auth.csis.gov.ls/realms/master/protocol/openid-connect/auth"
    settings.OIDC_OP_TOKEN_ENDPOINT = "https://auth.csis.gov.ls/realms/master/protocol/openid-connect/token"
    settings.OIDC_OP_USER_ENDPOINT = "https://auth.csis.gov.ls/realms/master/protocol/openid-connect/userinfo"
    settings.OIDC_OP_JWKS_ENDPOINT = "https://auth.csis.gov.ls/realms/master/protocol/openid-connect/certs"

    # User creation & mapping
    settings.OIDC_CREATE_USER = True
    settings.OIDC_UPDATE_USER = True

    # Username and email
    settings.OIDC_USERNAME_CLAIM = "preferred_username"
    settings.OIDC_EMAIL_CLAIM = "email"

    # Scopes (standard only)
    settings.OIDC_RP_SCOPES = "openid profile email"

    # Custom callback
    settings.OIDC_CALLBACK_CLASS = "oidcplugin.views.CustomOIDCCallbackView"

    settings.LOGIN_URL = '/oidc/authenticate/'
    settings.LOGOUT_REDIRECT_URL = '/'
    settings.LOGIN_REDIRECT_URL = '/'