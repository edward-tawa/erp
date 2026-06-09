from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from loguru import logger

User = get_user_model()


# Store original role before save
@receiver(pre_save, sender=User)
def store_original_role(sender, instance, **kwargs):
    if instance.pk:  # Existing user
        try:
            original = sender.objects.get(pk=instance.pk)
            instance._original_role = original.role
        except sender.DoesNotExist:
            instance._original_role = None
    else:
        instance._original_role = None


# Handle group assignment after save
@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    """Handle group assignment on creation or role change"""

    # Check if this is a new user OR role has changed
    role_changed = (
        not created
        and hasattr(instance, "_original_role")
        and instance._original_role != instance.role
    )

    if created or role_changed:
        if not instance.role:
            return

        try:
            group = Group.objects.get(name=instance.role)

            # If role changed, remove from old group
            if role_changed and instance._original_role:
                try:
                    old_group = Group.objects.get(name=instance._original_role)
                    instance.groups.remove(old_group)
                    logger.info(
                        f"Removed user '{instance.email}' from group '{instance._original_role}'"
                    )
                except Group.DoesNotExist:
                    pass

            # Add to new group (if not already in it)
            if not instance.groups.filter(name=instance.role).exists():
                instance.groups.add(group)
                logger.info(
                    f"Assigned user '{instance.email}' to group '{instance.role}'"
                )

        except Group.DoesNotExist:
            logger.error(
                f"Group '{instance.role}' does not exist. Run 'python manage.py setup_group_permissions' first."
            )
