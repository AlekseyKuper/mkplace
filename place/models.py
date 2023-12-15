from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.

class Things(models.Model):
    name = models.CharField(max_length=120, default='<none>', verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость', default=0)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменеия')
    date_expired = models.DateField(null=True, verbose_name='Дата истечения срока')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Фото')
    exist = models.BooleanField(default=True, verbose_name='В наличии?')

    suplier = models.ForeignKey('Suplier', on_delete=models.CASCADE, null=True, verbose_name='Поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хрень'
        verbose_name_plural = 'Хреновины'
        ordering = ['-name']


class Suplier(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название потсавщика')
    agent_name = models.CharField(max_length=100, verbose_name='Иммя агента')
    agent_firstname = models.CharField(max_length=100, verbose_name='Фамилия поставщика')
    agent_patronymic = models.CharField(max_length=100, verbose_name='Отчество агента')
    exist = models.BooleanField(default=True, verbose_name='Сотрудничаем?')

    def get_absolute_url(self):
        return reverse("one_show_suplier", kwargs={"suplier_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['title']


class Order(models.Model):
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_finish = models.DateTimeField(null=True, verbose_name='Дата завершения')
    price = models.FloatField(verbose_name='Стоимость заказа')
    address_delivery = models.CharField(max_length=150, verbose_name='Адресс доставки')
    status = models.CharField(max_length=150, verbose_name='Статус',
                              choices=[("1", 'Создан'), ("2", 'Отменен'), ("3", 'В пути'), ("4", 'Завершен')])

    thing = models.ManyToManyField(Things, through='Pos_order')

    def __str__(self):
        return f"{self.date_create} {self.status} {self.price}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['date_create']


class Pos_order(models.Model):
    thing = models.ForeignKey(Things, on_delete=models.PROTECT, null=True, verbose_name='Наименование')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Сумма')

    def __str__(self):
        return self.thing.name + " " + self.order.address_delivery + self.order.status

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'
        ordering = ['thing', 'order', 'price']


class Chegue(models.Model):
    date_print = models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи')
    address_print = models.CharField(max_length=150, verbose_name='Адресс выдачи')
    terminal = models.CharField(max_length=100, verbose_name='Номер терминала')
    order = models.OneToOneField(Order, on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return str(self.date_print) + " " + self.terminal

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
        ordering = ['terminal', 'date_print']
