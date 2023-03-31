from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Post(models.Model):

    TRAVEL = 'T'
    HEALTH = 'H'
    STUDING = 'S'
    EVENTS = 'E'
    
    TOPICS_CHOISES = [
        (TRAVEL, 'Путешествия'),
        (HEALTH, 'Здоровье'),
        (STUDING, 'Учеба'),
        (EVENTS, 'События')
    ]

    title = models.CharField(max_length=110, default='', validators=[
        MinLengthValidator(1)
    ])

    date = models.DateField(auto_now=False, auto_now_add=True, null=True)

    description = models.CharField(max_length=110, default='', validators=[
        MinLengthValidator(1)
    ])

    topic = models.CharField(
        max_length=1,
        choices=TOPICS_CHOISES,
        default=EVENTS,
    )

    content = models.TextField()

    picture = models.FileField(upload_to='users_pics_folder')

    slug = models.SlugField(default='', null=False)


    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

