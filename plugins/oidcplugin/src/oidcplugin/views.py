from mozilla_django_oidc.views import OIDCAuthenticationCallbackView
from django.contrib.auth.models import Group
import logging

logger = logging.getLogger(__name__)


class CustomOIDCCallbackView(OIDCAuthenticationCallbackView):

    def create_user(self, claims):
        user = super().create_user(claims)

        username = claims.get("preferred_username")
        email = claims.get("email")

        if username:
            user.username = username

        if email:
            user.email = email

        user.save()
        return user

    def update_user(self, user, claims):
        # --- username ---
        username = claims.get("preferred_username")
        if username and user.username != username:
            user.username = username

        # --- email ---
        email = claims.get("email")
        if email:
            user.email = email

        # --- groups ---
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
