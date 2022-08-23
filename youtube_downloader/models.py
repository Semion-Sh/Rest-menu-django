from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Video(models.Model):
    __tablename__ = 'manage'
    title = models.CharField(max_length=300)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='create')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='number')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='type_menu')

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['title']


# Create your models here.
