from mozilla_django_oidc.views import OIDCAuthenticationCallbackView
from django.contrib.auth.models import Group
import logging

logger = logging.getLogger(__name__)


class CustomOIDCCallbackView(OIDCAuthenticationCallbackView):

    def create_user(self, claims):
        user = super().create_user(claims)

        # --- username ---
        username = claims.get("preferred_username")
        if username:
            user.username = username

        # --- email ---
        email = claims.get("email")
        if email:
            user.email = email

        # --- first / last name ---
        first_name = claims.get("given_name")
        last_name = claims.get("family_name")

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

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

        # --- first / last name ---
        first_name = claims.get("given_name")
        last_name = claims.get("family_name")

        if first_name and user.first_name != first_name:
            user.first_name = first_name

        if last_name and user.last_name != last_name:
            user.last_name = last_name

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
            "User %s (%s %s) synced with groups %s",
            user.username,
            user.first_name,
            user.last_name,
            kc_groups,
        )

        return user
