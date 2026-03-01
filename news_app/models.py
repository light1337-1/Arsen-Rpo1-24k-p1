from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Категорияның аты", max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Жаңалықтың тақырыбы", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField("Сипаттамасы")
    image_url = models.CharField("Суреттің URL cілтемесі", max_length=500)
    created_at = models.DateTimeField("Жариялау уақыты мен күні", auto_now_add=True)

    def __str__(self):
        return self.title

class Adv(models.Model):
    name = models.CharField("Компания аты", max_length=255, default="Company name")
    image_url = models.CharField("URL сілтемесі", max_length=500)

def __str__(self):
        return self.name