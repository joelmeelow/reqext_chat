# Generated by Django 5.1.2 on 2024-10-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=255)),
                ('symptoms', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='chat_model',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chat_model',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chat_model',
            name='group_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='chat_model',
            name='messages',
            field=models.TextField(),
        ),
    ]
