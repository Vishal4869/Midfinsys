from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    name = models.CharField(max_length=128, null=True)
    file = models.FileField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name

