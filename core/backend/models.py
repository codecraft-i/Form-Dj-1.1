from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    AGES = (
        ('17-20', '17-20'),
        ('21-24', '21-24'),
        ('25-30', '25-30'),
        ('30 Dan Yuqori', '30 Dan Yuqori'),
    )
    age = models.CharField(max_length=45, choices=AGES)
    EXPERIENCES = (
        ('1-3 Oy', '1-3 Oy'),
        ('3-6 Oy', '3-6 Oy'),
        ('1-3 Yil', '1-3 Yil'),
        ('3-5 Yil', '3-5 Yil'),
        ('5 Yildan Yuqori', '5 Yildan Yuqori'),
    )
    experience = models.CharField(max_length=45, choices=EXPERIENCES)
    JOBS = (
        ('Ofitsant', 'Ofitsant'),
        ('Milliy Taomlar Oshpazi', 'Milliy Taomlar Oshpazi'),
        ('Uygçur Taomlar Oshpazi', 'Uygçur Taomlar Oshpazi'),
        ('Shashlikpaz', 'Shashlikpaz'),
        ('Idish yuvuchi', 'Idish yuvuchi'),
    )
    job = models.CharField(max_length=45, choices=JOBS)
    phone = models.CharField(max_length=15)
    text = models.TextField()