from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Otros campos personalizados si los tienes

    class Meta:
        # Especifica un nombre de tabla personalizado si lo necesitas
        db_table = 'custom_user'

    # Agrega un related_name único para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )
