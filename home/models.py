from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length = 20)
    useremail = models.EmailField()
    pfimage = models.ImageField(upload_to = 'profileimages')

    def __str__(self):
        return self.username
