import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import Restaurant, Rating, Sale

class Command(BaseCommand):
    help = "Generate random data for testing purposes."

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_user(
                username='admin',
                password='admin',
                is_staff=True,
                is_superuser=True
            )

        restaurants_data = [
            {'name': 'Pizzeria 1', 'date_opened': timezone.now() - timezone.timedelta(days=20), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 55.869829854, 'longitude': -4.28583219},
            # (other restaurant entries here) ...
        ]

        Restaurant.objects.all().delete()
        for res in restaurants_data:
            Restaurant.objects.create(**res)

        restaurants = Restaurant.objects.all()

        for _ in range(50):
            Rating.objects.create(
                restaurant=random.choice(restaurants),
                user=user,
                rating=random.randint(1, 10),
            )

        for _ in range(50):
            Sale.objects.create(
                restaurant=random.choice(restaurants),
                user=user,
                amount=random.randint(1, 100),
                date=timezone.now() - timezone.timedelta(days=random.randint(1, 30)),
            )
