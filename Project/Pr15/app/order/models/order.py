from django.db import models
from django.contrib.auth.models import User
from furniture.models import Furniture

class PaymentStatus(models.TextChoices):
    PENDING = "на рассмотрении"
    PROCESSED = "в обработке"
    SHIPPED = "Отправлен"
    DELIVERED = "Доставлен"

class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=PaymentStatus)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} for {self.customer_user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantity} of {self.furniture} for {self.order}"