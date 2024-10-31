# dashboard/migrations/000X_auto_<timestamp>.py

from django.db import migrations
from django.contrib.auth import get_user_model

User = get_user_model()  # Use the custom user model

def create_default_users(apps, schema_editor):
    # Get the User model from the historical version
    User = apps.get_model('dashboard', 'CustomUser')  # Update if 'dashboard' isn't your app's name

    # Create an admin user
    if not User.objects.filter(username='admin').exists():  # Prevent duplication
        User.objects.create_superuser(
            username='admin',
            password='testpass@12345',  # Hardcoded for simplicity; consider using environment variables
            email='admin@example.com',
            first_name='Admin',
            last_name='User'
        )

    # Create a sales clerk user
    if not User.objects.filter(username='Frank').exists():  # Prevent duplication
        User.objects.create_user(
            username='Frank',
            password='testpass@1234',  # Hardcoded for simplicity
            first_name='Frank',
            last_name='Clerk',
            email='frank@example.com'
        )

    # Create a manager user
    if not User.objects.filter(username='Boss').exists():  # Prevent duplication
        manager = User.objects.create_user(
            username='Boss',
            password='testpass@1234',  # Hardcoded for simplicity
            first_name='Boss',
            last_name='Manager',
            email='boss@example.com'
        )
        manager.is_staff = True
        manager.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '000X_previous_migration'),  # Update to reflect your latest migration
    ]

    operations = [
        migrations.RunPython(create_default_users),
    ]
