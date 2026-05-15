from django.db import models

# Create your models here.

class Post(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )

  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  content = models.TextField()
  status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title