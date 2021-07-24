from django.db import models


class Design(models.Model):
    title = models.CharField(
        max_length=10,
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
    )


class Like(models.Model):
    design = models.ForeignKey(
        Design,
        on_delete=models.CASCADE,
    )