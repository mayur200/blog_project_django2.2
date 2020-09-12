from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



# Create your models here.
# username:mayur200
# emailid:mayur.pardeshi96@gmail.com
# pass:aai123

# Create your models here.

# class User(AbstractUser):
#     pass

class Post(models.Model):

    # REQUIRED_FIELDS = ('post')


    post = models.CharField(max_length=500)
    thumb = models.ImageField(default='default.png',blank=True)
    # USERNAME_FIELD = 'post'

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,)
    # author = models.OneToOneField(User, default='', null=True, on_delete=models.CASCADE)


    # def post_save_receiver(sender, instance, created, **kwargs):
    #     pass
    #
    # post_save.connect(Post, sender=settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        return reverse('sign_up:post-detail', kwargs={'pk': self.pk})

    # def get_absolute_url(self):
    #     return reverse('sign_up:update-detail', kwargs={'pk': self.pk})



