from django.db import models

# Create your models here.

class ResumeParsing(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField()
    mobile = models.CharField(max_length = 12)
    dob = models.DateField()
    address = models.CharField(max_length = 100)

    def __str__(self):
        return ' '.join([self.name, self.email, self.mobile, self.address])
