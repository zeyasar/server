from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=12)
    gender_choices = [("Female","Female"), ("Male","Male"), ("Other","Other")]
    gender = models.CharField(choices=gender_choices, max_length=10)

    def __str__(self):
        return f'{self.username}'
