from django.db import models


class Design(models.Model):
    TYPE_CHOICE_INTERIOR = 'interior'
    TYPE_CHOICE_PRODUCT = 'product'
    TYPE_CHOICE_3D = '3d'
    TYPE_CHOICE_OTHER = 'other'

    TYPE_CHOICES = (
        (TYPE_CHOICE_INTERIOR, 'Interior design'),
        (TYPE_CHOICE_PRODUCT, 'Product design'),
        (TYPE_CHOICE_3D, '3D visualizations'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='Other',
    )
    title = models.CharField(
        max_length=25,
    )
    city = models.CharField(
        max_length=15,
    )
    country = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='designs',
        null=True,
        blank=True,
    )


class Like(models.Model):
    design = models.ForeignKey(
        Design,
        on_delete=models.CASCADE,
    )