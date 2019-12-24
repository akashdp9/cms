from django.db import models
import jsonfield

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True,help_text='The name of category of specific product')
    parent_category = models.ForeignKey('category',null=True, blank=True ,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True,)


    def __str__(self):
        return self.name


    
    def get_breadcrumbs(self):
        breadcrumbs = []
        category=self
        while category.parent_category is not None:
            breadcrumbs.append(category.name)
            category = category.parent_category
        breadcrumbs.append(category.name)
        breadcrumbs.reverse()
        return breadcrumbs



class Brand(models.Model):
    name = models.CharField(max_length=250,unique=True,help_text='Brand Name')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    specification = jsonfield.JSONField()


    def __str__(self):
        return self.name



# class Specification(models.Model):
#     key = models.CharField(max_length=250)
#     value = models.CharField(max_length=250)
#     unit = models.CharField(max_length=250)
#     product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.key+ ': ' + self.value+ ' '+(self.unit if self.unit else '')