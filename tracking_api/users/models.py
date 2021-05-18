from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'contacts'


class NotificationSettings(models.Model):
    receive_sms = models.BooleanField(default=False)
    receive_call = models.BooleanField(default=False)
    receive_email = models.BooleanField(default=True)
    receive_app_notification = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification_settings'


class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    status = models.IntegerField()  # add choices
    # TODO: uncomment in prod
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    notification_settings = models.ForeignKey(NotificationSettings, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Qualification(models.Model):
    licence = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    class Meta:
        db_table = 'qualifications'


class Client(User):
    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.name


class Worker(User):
    # TODO: uncomment in production
    # qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'workers'

    def __str__(self):
        return self.name
