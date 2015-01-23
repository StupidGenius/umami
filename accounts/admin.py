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

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin

from accounts.models import Member, Profile
from accounts.forms import MemberCreationForm, MemberChangeForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class MemberAdmin(UserAdmin):
    save_on_top = True
    list_display = ('id',
                    'username',
                    'status',
                    'display_name',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'is_staff',
                    'is_superuser')
    filter_horizontal = ['groups', 'user_permissions']
    readonly_fields = ['password', 'last_login', 'date_joined', 'host']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('display_name', 'first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('status', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Audit', {'fields': ('host',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    inlines = (ProfileInline,)
    list_filter = ['status', 'is_active', 'is_staff', 'is_superuser']
    list_display_links = ['username']
    ordering = ['id']
    search_fields = ['username', 'display_name', 'first_name', 'last_name', 'email']
    form = MemberChangeForm
    add_form = MemberCreationForm
    change_password_form = AdminPasswordChangeForm

    def get_urls(self):
        from django.conf.urls import patterns
        return patterns('',
            (r'^(\d+)/password/$', self.admin_site.admin_view(self.user_change_password))) + super(MemberAdmin, self).get_urls()


admin.site.register(Member, MemberAdmin)


