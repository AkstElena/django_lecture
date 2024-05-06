from django.db import models


class User(models.Model):  # ID не указывается, его Django добавит автоматически
    name = models.CharField(max_length=100)  # проверка на заполнение набором букв с максимальной длиной 100
    email = models.EmailField()  # проверка на почту
    password = models.CharField(max_length=100)
    age = models.IntegerField()  # поле с целым числом

    def __str__(self):  # для вывода
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # чисел после запятой 2
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # изображения, ссылки на папку, где будут храниться


class Order(models.Model):
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)  # внешняя ссылка на пользователя, при удалении пользователя удаляются все его заказы
    products = models.ManyToManyField(
        Product)  # один продукт может находится в нескольких разных заказах, разные заказы могут содержать один и тот же продукт
    date_ordered = models.DateTimeField(auto_now_add=True)  # при создании заказа дата и время создается автоматически
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'
