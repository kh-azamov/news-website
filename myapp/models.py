from django.db import models
from django.conf import settings
# from .validators import validate_decimal, validate_integer, validate_string

'''For the ImageField workability we need ti install pip install pillow'''
# news_line


class Article(models.Model):
    class ArticleCategory(models.TextChoices):
        POLITICS = 'P',
        SPORTS = 'S',
        ECONOMICS = 'E',
        TECHNOLOGIES = 'T',
        MEDICINE = 'M',
        BUSINESS = 'B',
        OTHER = 'o',
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='article', blank=True, null=True)
    url = models.URLField()
    category = models.CharField(max_length=1, choices=ArticleCategory.choices)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    full_name = models.CharField(max_length=200)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
