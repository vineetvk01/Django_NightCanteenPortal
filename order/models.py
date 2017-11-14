from django.db import models

MAYBECHOICE = (
    (0, 'Yes'),
    (1, 'No'),
)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 15)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 80)

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr = models.CharField(max_length = 400)
    verified = models.CharField(max_length=1, choices=MAYBECHOICE)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 20)
    transactionid = models.CharField(max_length = 20)
    mop = models.CharField(max_length = 20)

    def __str__(self):
        return self.transactionid

class Food_items(models.Model):
    name  = models.CharField(max_length = 100)
    price = models.IntegerField()
    image = models.CharField(max_length = 300)

    def __str__(self):
        return self.name

class Order_info(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    food_i = models.ForeignKey(Food_items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
