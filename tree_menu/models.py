from django.db import models
from django.utils.text import slugify


class MenuItem(models.Model):
    """Tree menu item model"""
    name = models.CharField(max_length=100, verbose_name='Name')
    url = models.CharField(max_length=100, verbose_name='URL', unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Parent')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Menu')

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'


class Menu(models.Model):
    """Tree menu model"""
    name = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'Menu'
