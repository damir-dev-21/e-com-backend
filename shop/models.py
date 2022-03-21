from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
import json


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(max_length=30, unique=False)
    name = models.CharField(unique=True, max_length=100, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, max_length=500, verbose_name="Email пользователя")
    password = models.CharField(max_length=100, verbose_name="Пароль пользователя")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name',"password"]

    def __str__(self):
        return self.name


class Item(TimeBasedModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    id = models.AutoField(primary_key = True)
    name = models.CharField(verbose_name="Наименование Товара", max_length=500)
    photo = models.CharField(verbose_name="Изображение", max_length=5000)
    description = models.TextField(verbose_name="Описание Товара", max_length=5000, null=True)
    price = models.CharField(verbose_name="Цена", max_length=200)
    category_name = models.CharField(verbose_name="Название категории", max_length=500)
    subcategory_name = models.CharField(verbose_name="Название подкатегории", max_length=500)
    created_at = models.DateTimeField(verbose_name="Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата редактирования",auto_now=True)

    def __str__(self):
        return f"№{self.id} - {self.name}"

class ItemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class Order(TimeBasedModel):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.SET(0))
    total = models.IntegerField(verbose_name="Общая сумма")
    purchase_time = models.DateTimeField(verbose_name="Время покупки", auto_now_add=True)
    success = models.BooleanField(verbose_name="Оплачено", default=False)

    def __str__(self):
        return f"№{self.id}"


class OrderItem(TimeBasedModel):
    class Meta:
        verbose_name = "Товары в корзине"
        verbose_name_plural = "Список товаров"

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.CharField(verbose_name="Стоимость",max_length=200)
    quantity = models.IntegerField(verbose_name="Количество")