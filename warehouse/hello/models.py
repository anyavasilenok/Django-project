from django.db import models


class Storage(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=7)

    objects = models.Manager()


class Employee(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=20)

    objects = models.Manager()

    def __srt__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20)

    objects = models.Manager()


class PackingList(models.Model):
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    amount = models.IntegerField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
    date = models.DateField()

    objects = models.Manager()


class SalesInvoice(models.Model):
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    amount = models.IntegerField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
    date = models.DateField()

    objects = models.Manager()
