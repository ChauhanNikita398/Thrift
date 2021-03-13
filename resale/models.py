from django.db import models

# Create your models here.
class Product(models.Model):
      product_id = models.AutoField
      product_name = models.CharField(max_length=50)
      category = models.CharField(max_length=50, default="")
      price = models.CharField(max_length=50, default="")
      desc = models.CharField(max_length=300, default="")
      pub_date = models.DateField()
      phone = models.CharField(max_length=111, default="")
      image = models.ImageField(upload_to="shop/images", default="")
      user_name = models.CharField(max_length=300, default="")
      size = models.CharField(max_length=20, default="")
      brand = models.CharField(max_length=50, default="")
      bought = models.CharField(max_length = 20, default="")
      used = models.CharField(max_length=10, default="")
      def __str__(self):
          return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."



      