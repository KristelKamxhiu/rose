from django.db import models

# Create your models here
class Category(models.Model):
    category_title = models.CharField(max_length=150, null=True, blank=True)
    category_image = models.ImageField(upload_to="category/", null=True, blank=True)
    def __str__(self):
        return f"{self.category_title}"


class Product(models.Model):
    product_title = models.CharField(max_length=150, null=True, blank=True)   #per vendosjen e nje teksti te shkurter;
    product_description = models.TextField(max_length=500, null=True, blank=True)   #per vendosjen e nje teksti me te gjate(paragraf);
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)    #per vendosjen e imazheve;
    product_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  #per vendosjen e cmimit;
    # product_quantity_int = models.IntigerField(null=True, blank=True)       #per vendosjen e sasise;
    # product_quantity_float = models.FloatField(null= True, blank=True)      #per vendosjen e numrave me presje;
    product_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_title}"




class Contact(models.Model):
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_lastname = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_comment = models.TextField(max_length=300, null=True, blank=True)
    def __str__(self):
        return f"{self.contact_name} {self.contact_lastname} {self.contact_email} {self.contact_comment}"







    








