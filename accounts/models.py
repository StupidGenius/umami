"""

The MIT License (MIT)

Copyright (c) 2011-2015 Mark Rogaski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from __future__ import unicode_literals

from django.db import models
from django_enumfield import enum
from django.contrib.auth.models import AbstractUser, UserManager


class MemberStatus(enum.Enum):
    GUEST = 0
    ACTIVE = 1
    SUSPENDED = 2
    BANNED = 3

    labels = {
        GUEST: 'Guest',
        ACTIVE: 'Member',
        SUSPENDED: 'Suspended',
        BANNED: 'Banned',
    }


class Member(AbstractUser):
    """Extended User model."""
    status = enum.EnumField(MemberStatus, default=MemberStatus.GUEST)
    host = models.ManyToManyField('Host', null=True, blank=True)
    display_name = models.CharField(max_length=32,
        null=True, blank=True, verbose_name=u'Display Name',
        help_text=u'Name to be displayed publicly.') 

    def __unicode__(self):
        try:
            if self.display_name:
                return u'%s (%s)' % (self.username, self.display_name)
            elif self.first_name or self.last_name:
                name = ' '.join(self.first_name, self.last_name)
                return u'%s (%s)' % (self.username, name.capwords)
        except:
            pass
        return self.username
            

class Host(models.Model):
    address = models.GenericIPAddressField(blank=False, unique=True,
        db_index=True)

    def __unicode__(self):
        return self.address


