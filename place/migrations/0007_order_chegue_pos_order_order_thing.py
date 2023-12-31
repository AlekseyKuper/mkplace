# Generated by Django 4.2.7 on 2023-12-09 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_remove_order_thing_remove_pos_order_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_finish', models.DateTimeField(null=True, verbose_name='Дата завершения')),
                ('price', models.FloatField(verbose_name='Стоимость заказа')),
                ('address_delivery', models.CharField(max_length=150, verbose_name='Адресс доставки')),
                ('status', models.CharField(choices=[(1, 'Создан'), (2, 'Отменен'), (3, 'В пути'), (4, 'Завершен')], max_length=150, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['date_create'],
            },
        ),
        migrations.CreateModel(
            name='Chegue',
            fields=[
                ('date_print', models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи')),
                ('address_print', models.CharField(max_length=150, verbose_name='Адресс выдачи')),
                ('terminal', models.CharField(max_length=100, verbose_name='Номер терминала')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='place.order')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
                'ordering': ['terminal', 'date_print'],
            },
        ),
        migrations.CreateModel(
            name='Pos_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Сумма')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='place.order', verbose_name='Заказ')),
                ('thing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='place.things', verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
                'ordering': ['thing', 'order', 'price'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='thing',
            field=models.ManyToManyField(through='place.Pos_order', to='place.things'),
        ),
    ]
