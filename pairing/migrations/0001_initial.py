# Generated by Django 4.1.6 on 2023-03-30 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('brothers', models.ManyToManyField(related_name='brother', to='pairing.brother')),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField()),
                ('week_end', models.DateField()),
                ('brother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pairing.brother')),
                ('pledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pairing.pledge')),
            ],
        ),
        migrations.AddField(
            model_name='brother',
            name='new_members',
            field=models.ManyToManyField(related_name='pledge', to='pairing.pledge'),
        ),
    ]
