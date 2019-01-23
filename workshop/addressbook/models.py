from django.db import models

# Create your models here.


class Person(models.Model):
    first_name=models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{} {} ({})".format(self.first_name,self.last_name,self.id)


class Address(models.Model):
    city=models.CharField(max_length=128)
    street=models.CharField(max_length=128)
    building_number=models.IntegerField()
    apartment_number=models.IntegerField()
    person=models.ForeignKey(Person,on_delete=models.CASCADE)


class Phone(models.Model):
    PHONE_TYPE=(
        (-1, 'not defined'),
        (0, 'home'),
        (1, 'work'),
        (2, 'mobile'),
        (3, 'fax'),
        (4, 'other'),
    )
    phone_number=models.IntegerField()
    phone_type=models.IntegerField(choices=PHONE_TYPE, default=-1)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)


class Email(models.Model):
    EMAIL_TYPE=(
        (-1, 'not defined'),
        (0, 'home'),
        (1, 'work'),
        (2, 'other'),
    )
    email=models.CharField(max_length=256)
    email_type=models.IntegerField(choices=EMAIL_TYPE, default=-1)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)


class Group(models.Model):
    group_name=models.CharField(max_length=256)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return "{}".format(self.group_name)



