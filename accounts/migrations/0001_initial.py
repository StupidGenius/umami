# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import django_enumfield.enum
import django_enumfield.db.fields
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=accounts.models.MemberStatus, choices=[(0, django_enumfield.enum.Value(b'GUEST', 0, b'Guest', accounts.models.MemberStatus)), (1, django_enumfield.enum.Value(b'ACTIVE', 1, b'Member', accounts.models.MemberStatus)), (2, django_enumfield.enum.Value(b'SUSPENDED', 2, b'Suspended', accounts.models.MemberStatus)), (3, django_enumfield.enum.Value(b'BANNED', 3, b'Banned', accounts.models.MemberStatus))])),
                ('display_name', models.CharField(help_text='Name to be displayed publicly.', max_length=32, null=True, verbose_name='Display Name', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
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
        migrations.AddField(
            model_name='member',
            name='host',
            field=models.ManyToManyField(to='accounts.Host', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
