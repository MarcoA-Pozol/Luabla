# Generated by Django 5.1.1 on 2024-10-20 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CN_Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('hsk_level', models.CharField(max_length=5)),
                ('is_shareable', models.BooleanField(default=False)),
                ('language', models.CharField(default='Chinese', max_length=30)),
                ('downloads', models.IntegerField(default=0)),
                ('image', models.ImageField(default='deck_images/default_deck_image.jpg', upload_to='deck_images/')),
                ('cards_cuantity', models.IntegerField(default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cn_deck_author', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(related_name='cn_deck_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CN_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hanzi', models.CharField(max_length=40)),
                ('pinyin', models.CharField(max_length=120)),
                ('meaning', models.CharField(max_length=200)),
                ('example_phrase', models.CharField(max_length=200, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cn_card_author', to=settings.AUTH_USER_MODEL)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cn_deck', to='Chinese.cn_deck')),
            ],
        ),
    ]