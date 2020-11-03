# Generated by Django 2.1.3 on 2020-11-03 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='articolo',
            name='giornalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articoli', to='news.Giornalista'),
        ),
    ]
