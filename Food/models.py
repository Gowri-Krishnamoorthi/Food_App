from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Item(models.Model):
    
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=10447, default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Ensure this exists

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})  # Correct spelling