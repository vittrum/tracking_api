from django.db import models

# Create your models here.


class Qualification(models.Model):
    licence = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)


class Contact(models.Model):
    email = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)


class Client(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=256)
    status = models.IntegerField() # add choices
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    status = models.IntegerField()  # add choices
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'workers'

    def __str__(self):
        return self.name

