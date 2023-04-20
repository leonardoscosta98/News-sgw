# Generated by Django 3.1.3 on 2023-04-20 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_sistema', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
            },
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('imagem_fundo', models.ImageField(blank=True, null=True, upload_to='imagens/', verbose_name='imagem de fundo')),
                ('data_expiracao', models.DateField(blank=True, null=True)),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sistema')),
            ],
            options={
                'verbose_name': 'Aviso',
                'verbose_name_plural': 'Avisos',
            },
        ),
    ]
