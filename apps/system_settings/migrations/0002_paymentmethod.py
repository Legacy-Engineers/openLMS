# Generated by Django 4.2.23 on 2025-07-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system_settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentMethod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Unique code for the payment method (e.g., cash, card, mobile_money)",
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Display name for the payment method", max_length=100
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Optional description of the payment method",
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        help_text="Optional icon class (e.g., fa-money-bill, fa-credit-card)",
                        max_length=50,
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this payment method is available for selection",
                    ),
                ),
                (
                    "requires_verification",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this payment method requires additional verification",
                    ),
                ),
                (
                    "sort_order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Display order in lists (lower numbers appear first)",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Payment Method",
                "verbose_name_plural": "Payment Methods",
                "ordering": ["sort_order", "name"],
            },
        ),
    ]
