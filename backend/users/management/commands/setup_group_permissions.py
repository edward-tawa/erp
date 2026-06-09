from loguru import logger
from users.permissions.role_permission_mapping import ROLE_PERMISSION_MAPPING
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


def create_permission_groups():
    for role, permission_codenames in ROLE_PERMISSION_MAPPING.items():
        group, created = Group.objects.get_or_create(name=role)

        if created:
            logger.info(f"Created group '{role}'")
        else:
            logger.info(f"Group '{role}' already exists. Updating permissions.")

        permissions = []
        for perm in permission_codenames:
            try:
                # Split into app_label and codename
                app_label, codename = perm.split(".")

                # Look up the permission
                permission = Permission.objects.get(
                    codename=codename,
                    content_type__app_label=app_label,
                )
                permissions.append(permission)
                logger.info(f"Found permission: {perm}")

            except Permission.DoesNotExist:
                logger.error(f"Permission '{perm}' not found in database")
            except ValueError:
                logger.error(
                    f"Invalid permission format: '{perm}' - expected 'app_label.codename'"
                )
            except Exception as e:
                logger.error(f"Error adding permission '{perm}' to group '{role}': {e}")

        # Assign all permissions to the group
        group.permissions.set(permissions)
        logger.info(f"Assigned {len(permissions)} permissions to group '{role}'")


class Command(BaseCommand):
    help = "Set up user group permissions based on the ROLE_PERMISSION_MAPPING."

    def handle(self, *args, **options):
        create_permission_groups()
        self.stdout.write(self.style.SUCCESS("Successfully set up group permissions."))
        logger.info("Group permissions setup completed.")
