from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Skill(models.Model):
  name = models.CharField(max_length=100)
  level = models.IntegerField(
    default=10,
      validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
      ]
  )

  def __str__(self):
    return f"{self.name}: {self.level}"

  def get_absolute_url(self):
    return reverse('skills_detail', kwargs={'pk': self.id})

class Bill(models.Model):
  name = models.CharField(max_length=100)
  movie = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release = models.IntegerField()
  skills = models.ManyToManyField(Skill)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'bill_id': self.id})

class Quote(models.Model):
  text = models.CharField(max_length=250, default="urrrgggghh (Zombie Sounds)")

  bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

  def __str__(self):
    return f"Bill says {self.text}"

class Photo(models.Model):
  url = models.CharField(max_length=200)
  bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for bill_id: {self.bill_id} @{self.url}"

