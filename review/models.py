# model
from django.db import models
from user.models import User
from goods.models import Goods
from django.core.validators import MaxValueValidator, MinValueValidator



class Review(models.Model):
    class Meta:
        db_table = 'Review'
        ordering = ['-created_at']

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete = models.CASCADE)
    content = models.CharField(max_length=500, blank=False)
    manner_score = models.SmallIntegerField(
            default=50,
            validators=[
            MaxValueValidator(5),
            MinValueValidator(-20)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

# 