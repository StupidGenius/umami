# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import timezone_field.fields
import django_enumfield.db.fields
import django_enumfield.enum
from django.conf import settings
import django.core.validators
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=75)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('status', django_enumfield.db.fields.EnumField(choices=[(0, django_enumfield.enum.Value(b'GUEST', 0, 'Guest', accounts.models.MemberType)), (1, django_enumfield.enum.Value(b'ACTIVE', 1, 'Member', accounts.models.MemberType)), (2, django_enumfield.enum.Value(b'SUSPENDED', 2, 'Suspended', accounts.models.MemberType)), (3, django_enumfield.enum.Value(b'BANNED', 3, 'Banned', accounts.models.MemberType))], default=0, enum=accounts.models.MemberType)),
                ('display_name', models.CharField(help_text='Name to be displayed publicly.', null=True, verbose_name='Display Name', max_length=32, blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_name='user_set')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', django_enumfield.db.fields.EnumField(choices=[(0, django_enumfield.enum.Value(b'EMAIL', 0, 'E-Mail', accounts.models.ServiceType)), (1, django_enumfield.enum.Value(b'FROGPANTS', 1, 'FrogPants', accounts.models.ServiceType)), (2, django_enumfield.enum.Value(b'TWITTER', 2, 'Twitter', accounts.models.ServiceType)), (3, django_enumfield.enum.Value(b'GOOGLE', 3, 'Google', accounts.models.ServiceType)), (4, django_enumfield.enum.Value(b'FACEBOOK', 4, 'Facebook', accounts.models.ServiceType)), (5, django_enumfield.enum.Value(b'SKYPE', 5, 'Skype', accounts.models.ServiceType)), (6, django_enumfield.enum.Value(b'REDDIT', 6, 'Reddit', accounts.models.ServiceType)), (7, django_enumfield.enum.Value(b'GITHUB', 7, 'GitHub', accounts.models.ServiceType)), (8, django_enumfield.enum.Value(b'YAHOO', 8, 'Yahoo!', accounts.models.ServiceType))], default=0, enum=accounts.models.ServiceType)),
                ('address', models.CharField(max_length=256)),
                ('public', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.GenericIPAddressField(unique=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='UTC')),
                ('email_updates', models.BooleanField(verbose_name='e-mail updates', help_text='Receive e-mail updates and newletters', default=False)),
                ('birth_date', models.DateField(null=True, verbose_name='birth date', help_text='date of birth', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='host',
            field=models.ManyToManyField(null=True, to='accounts.Host', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_query_name='user', blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set'),
            preserve_default=True,
        ),
    ]
