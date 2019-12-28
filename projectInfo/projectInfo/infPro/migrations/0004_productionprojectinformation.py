# Generated by Django 2.2.3 on 2019-07-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infPro', '0003_auto_20190702_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionProjectInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Application_Owner', models.CharField(blank=True, max_length=1000, null=True)),
                ('Support_Team_Group_Name', models.CharField(blank=True, max_length=1000, null=True)),
                ('Application_Server_Name', models.CharField(blank=True, max_length=1000, null=True)),
                ('Application_Server_IP', models.CharField(blank=True, max_length=1000, null=True)),
                ('Server_OS_Version', models.CharField(blank=True, max_length=1000, null=True)),
                ('Database_Server_Name', models.CharField(blank=True, max_length=1000, null=True)),
                ('Database_Server_IP', models.CharField(blank=True, max_length=1000, null=True)),
                ('Database_Name', models.CharField(blank=True, max_length=1000, null=True)),
                ('Database_Version', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
