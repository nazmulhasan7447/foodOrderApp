# Generated by Django 3.2.11 on 2022-03-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0005_cookiepolicy_deliverypolicy_privacypolicy_refundpolicy_returnpolicy_securitypolicy_termsconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('check_in', models.CharField(default='', max_length=255)),
                ('check_out', models.CharField(default='', max_length=255)),
                ('attraction_one_name', models.CharField(default='', max_length=255)),
                ('attraction_one_distance', models.CharField(default='', max_length=255)),
                ('attraction_two_name', models.CharField(default='', max_length=255)),
                ('attraction_two_distance', models.CharField(default='', max_length=255)),
                ('map_link', models.TextField(default='')),
                ('ac', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.DeleteModel(
            name='CookiePolicy',
        ),
        migrations.DeleteModel(
            name='DeliveryPolicy',
        ),
        migrations.DeleteModel(
            name='PrivacyPolicy',
        ),
        migrations.RemoveField(
            model_name='productsubcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='RefundPolicy',
        ),
        migrations.DeleteModel(
            name='ReturnPolicy',
        ),
        migrations.DeleteModel(
            name='SecurityPolicy',
        ),
        migrations.DeleteModel(
            name='TermsConditions',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductSubCategory',
        ),
    ]
