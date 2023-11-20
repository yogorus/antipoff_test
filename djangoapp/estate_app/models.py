from django.db import models


# Create your models here.
class CadastralRequest(models.Model):
    cadastral_number = models.CharField(max_length=20)
    longitude = models.DecimalField(
        decimal_places=6,
        max_digits=9,
    )
    latitude = models.DecimalField(
        decimal_places=6,
        max_digits=9,
    )
    status = models.BooleanField(blank=True)
    date = models.DateTimeField(auto_now=True)
