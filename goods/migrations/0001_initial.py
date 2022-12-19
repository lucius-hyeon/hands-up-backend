# Generated by Django 4.1.3 on 2022-12-14 16:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=32)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('predict_price', models.IntegerField()),
                ('start_price', models.IntegerField()),
                ('high_price', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField()),
                ('start_time', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy_goods', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='like_goods', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_goods', to=settings.AUTH_USER_MODEL)),
                ('trade_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.tradechatroom')),
            ],
            options={
                'db_table': 'Goods',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goods/', validators=[django.core.validators.validate_image_file_extension])),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
            ],
            options={
                'db_table': 'GoodsImage',
            },
        ),
    ]