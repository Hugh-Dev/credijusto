from django.db import models

# Create your models here.

class TokenModel(models.Model):
    """docstring for MedicalModel."""
    token = models.CharField(primary_key=True, max_length=200, blank=False, null=False)
    status = models.CharField(max_length=20, blank=False, null=False)
    life = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'TokenModel'
        verbose_name_plural = 'TokenModels'
        ordering = ['token']

    def __str__(self):
        return self.token