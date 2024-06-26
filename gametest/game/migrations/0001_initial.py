# Generated by Django 3.2 on 2024-01-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamecategory', models.CharField(choices=[('fps', 'FPS'), ('music', '音楽ゲーム'), ('open', 'オープンワールド'), ('puzzle', 'パズルゲーム')], max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phonedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('apple', 'Apple'), ('samsung', 'Samsung'), ('google', 'Google'), ('sony', 'SONY'), ('oppo', 'OPPO'), ('xiaomi', 'Xiaomi'), ('asus', 'ASUS'), ('motorola', 'Motolora'), ('redmagic', 'Redmagic'), ('nothing', 'Nothing')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('displaysize', models.FloatField()),
                ('soc', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
            ],
        ),
    ]
