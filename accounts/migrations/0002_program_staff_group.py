from django.db import migrations


GROUP_NAME = 'Program staff'


def create_program_staff_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    group, _ = Group.objects.get_or_create(name=GROUP_NAME)
    permission_codes = ('add_course', 'add_batch')
    permissions = Permission.objects.filter(codename__in=permission_codes)
    group.permissions.add(*permissions)


def remove_program_staff_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name=GROUP_NAME).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0001_initial'),
        ('batches', '0002_enrollment'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(
            create_program_staff_group,
            remove_program_staff_group,
        ),
    ]
