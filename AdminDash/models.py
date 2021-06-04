from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(AbstractUser):
    user_type_choices = ((1,'Admin'), (2,'Staff'),(3,'Merchant'), (4,'Customer'))
    user_type = models.CharField(max_length=255,choices=user_type_choices, default=1)

class AdminUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

class StaffUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

class MarchantUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    Categorie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class SubCategories(models.Model):
    SubCategorie_id = models.AutoField(primary_key=True)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255)
    SubCategories_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    product_added_by_marchant = models.ForeignKey(MarchantUser, on_delete=models.CASCADE)
    in_total_stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsMedia(models.Model):
    product_media_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    media_type_choice = ((1,'Image'),(2,'Video'))
    media_type = models.CharField(max_length=255)
    media_content = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsTransaction(models.Model):
    product_transaction_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    transaction_type_choices = ((1,'BUY'),(2,"SELL"))
    product_transaction_count = models.IntegerField(default=1)
    transaction_type = models.CharField(choices=transaction_type_choices, max_length=2555)
    transaction_description = models.TextField( )
    created_at = models.DateTimeField(auto_now_add=True)



class ProductsDetails(models.CharField):
    product_details_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsAbout(models.CharField):
    product_about_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductsTags(models.Model):
    product_tag_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsQuestions(models.Model):
    product_question_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    questions = models.TextField()
    answera = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsReviews(models.Model):
    product_review_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    review_image = models.FileField()
    ratting = models.CharField(default='5', max_length=255)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

class ProductsReviewVoting(models.Model):
    product_voting_id = models.AutoField(primary_key=True)
    products_views_id = models.ForeignKey(ProductsReviews, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 

class ProductsVarient(models.Model):
    product_varient_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
class ProductsVarientItems(models.Model):
    product_varient_item_id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(ProductsVarient, on_delete=models.CASCADE)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerOrders(models.Model):
    customer_order_id = models.AutoField(primary_key=True)
    products_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    cupon_code = models.CharField(max_length=255)
    discount_amount = models.CharField(max_length=255)
    products_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderDeliveryStatus(models.Model):
    order_delivery_id = models.AutoField(primary_key=True)
    orders_id = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    status_msg = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type == 2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type == 3:
            MarchantUser.objects.create(auth_user_id=instance)
        if instance.user_type == 4:
            CustomerUser.objects.create(auth_user_id=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.staffuser.save()
    if instance.user_type == 3:
        instance.marchantuser.save()
    if instance.user_type == 4:
        instance.customeruser.save()