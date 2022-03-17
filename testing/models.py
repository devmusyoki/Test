from django.db import models


class Name(models.Model):
    Title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Name"

    def __str__(self):
        return f"{self.Title}"


class Type(models.Model):
    rows = models.BooleanField(default=False)
    dropdown = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Type"

    def __str__(self):
        return f"{self.rows}{self.dropdown}"


class Category(models.Model):
    Entries = models.ManyToManyField(Name, blank=False)
    Title = models.CharField(max_length=20)
    Type = models.OneToOneField(Type, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.Title}"
