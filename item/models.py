from django.db import models

class Category (models.Model):
    name=models.CharField(max_length=255)
#  configuration for the model
    class Meta:
        ordering = ('name',)
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

    
