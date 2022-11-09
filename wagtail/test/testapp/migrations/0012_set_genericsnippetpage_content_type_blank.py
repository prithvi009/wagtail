# Generated by Django 4.1.2 on 2022-11-07 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("tests", "0011_modelwithnullableparentalkey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genericsnippetpage",
            name="snippet_content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="genericsnippetpage",
            name="snippet_object_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]