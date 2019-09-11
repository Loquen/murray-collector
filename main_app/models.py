from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Bill(models.Model):
  name = models.CharField(max_length=100)
  movie = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'bill_id': self.id})

class Quote(models.Model):
  text = models.CharField(max_length=250, default="urrrgggghh (Zombie Sounds)")

  bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

  def __str__(self):
    return f"Bill says {self.text}"

class Skill(models.Model):
  name = models.CharField(max_length=100)
  level = models.IntegerField(
    default=10,
      validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
      ]
  )