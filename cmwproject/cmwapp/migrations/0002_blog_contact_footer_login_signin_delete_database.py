# Generated by Django 4.2.3 on 2023-08-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmwapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=30)),
                ('Pic', models.ImageField(blank=True, upload_to='')),
                ('des', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('con_no', models.IntegerField()),
                ('mes_sage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('hello', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_nm', models.CharField(max_length=30)),
                ('l_nm', models.CharField(max_length=30)),
                ('e_mai', models.CharField(max_length=10)),
                ('p_word', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_nam', models.CharField(max_length=30)),
                ('l_nam', models.CharField(max_length=30)),
                ('e_ma', models.CharField(max_length=10)),
                ('pa_word', models.CharField(max_length=35)),
                ('p', models.CharField(max_length=35)),
            ],
        ),
        migrations.DeleteModel(
            name='database',
        ),
    ]
