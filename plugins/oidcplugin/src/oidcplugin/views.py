from mozilla_django_oidc.views import OIDCAuthenticationCallbackView
from django.contrib.auth.models import Group
import logging

logger = logging.getLogger(__name__)


class CustomOIDCCallbackView(OIDCAuthenticationCallbackView):

    def update_user(self, user, claims):
        """
        Sync Keycloak groups to Django groups
        """
        kc_groups = claims.get("groups", [])

        if not isinstance(kc_groups, list):
            kc_groups = []

        django_groups = []

        for group_name in kc_groups:
            group, _ = Group.objects.get_or_create(name=group_name)
            django_groups.append(group)

        user.groups.set(django_groups)
        user.save()

        logger.info(
            "User %s synced with groups %s",
            user.username,
            kc_groups,
        )

        return user
