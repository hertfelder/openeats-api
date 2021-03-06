# Generated by Django 2.0.1 on 2018-01-29 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_auto_20180106_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Course'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Cuisine'),
        ),
        migrations.AlterField(
            model_name='subrecipe',
            name='child_recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_recipe', to='recipe.Recipe'),
        ),
        migrations.AlterField(
            model_name='subrecipe',
            name='parent_recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_recipe', to='recipe.Recipe'),
        ),
    ]
