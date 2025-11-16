from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Creates default user groups and assigns permissions.'

    def handle(self, *args, **kwargs):
        # Retrieve permissions
        can_view = Permission.objects.get(codename='can_view')
        can_create = Permission.objects.get(codename='can_create')
        can_edit = Permission.objects.get(codename='can_edit')
        can_delete = Permission.objects.get(codename='can_delete')

        # Create groups
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        editors_group.permissions.set([can_view, can_edit, can_create])
        viewers_group.permissions.set([can_view])
        admins_group.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))
