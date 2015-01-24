# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import django.core.validators
from django.conf import settings
import django_enumfield.enum
import django_enumfield.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=accounts.models.MemberType, choices=[(0, django_enumfield.enum.Value(b'GUEST', 0, 'Guest', accounts.models.MemberType)), (1, django_enumfield.enum.Value(b'ACTIVE', 1, 'Member', accounts.models.MemberType)), (2, django_enumfield.enum.Value(b'SUSPENDED', 2, 'Suspended', accounts.models.MemberType)), (3, django_enumfield.enum.Value(b'BANNED', 3, 'Banned', accounts.models.MemberType))])),
                ('display_name', models.CharField(null=True, max_length=32, help_text='Name to be displayed publicly.', blank=True, verbose_name='Display Name')),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_query_name='user', verbose_name='groups')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('service', django_enumfield.db.fields.EnumField(default=0, enum=accounts.models.ServiceType, choices=[(0, django_enumfield.enum.Value(b'EMAIL', 0, 'E-Mail', accounts.models.ServiceType)), (1, django_enumfield.enum.Value(b'FROGPANTS', 1, 'FrogPants', accounts.models.ServiceType)), (2, django_enumfield.enum.Value(b'TWITTER', 2, 'Twitter', accounts.models.ServiceType)), (3, django_enumfield.enum.Value(b'GOOGLE', 3, 'Google', accounts.models.ServiceType)), (4, django_enumfield.enum.Value(b'FACEBOOK', 4, 'Facebook', accounts.models.ServiceType)), (5, django_enumfield.enum.Value(b'SKYPE', 5, 'Skype', accounts.models.ServiceType)), (6, django_enumfield.enum.Value(b'REDDIT', 6, 'Reddit', accounts.models.ServiceType)), (7, django_enumfield.enum.Value(b'GITHUB', 7, 'GitHub', accounts.models.ServiceType)), (8, django_enumfield.enum.Value(b'YAHOO', 8, 'Yahoo!', accounts.models.ServiceType))])),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField(unique=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(null=True, help_text='date of birth', blank=True, verbose_name='birth date')),
                ('email_updates', models.BooleanField(default=False, help_text='Receive e-mail updates and newletters', verbose_name='e-mail updates')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='host',
            field=models.ManyToManyField(to='accounts.Host', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', blank=True, related_query_name='user', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
