# Generated by Django 3.1.2 on 2020-11-04 15:26

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone'),
        ),
    ]
