from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Manage(models.Model):
    __tablename__ = 'manage'
    title = models.CharField(max_length=300)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='create', blank=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='type_menu', blank=True)
    slug = models.SlugField(default='', null=False)
    # content = models.CharField(max_length=300, default=None, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Manage, self).save(args, kwargs)

    def __str__(self):
        return self.title

    # self.price, self.photo

    class Meta:
        ordering = ['title']
