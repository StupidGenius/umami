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

from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _

from accounts.models import Member


class MemberCreationForm(forms.ModelForm):
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[A-Za-z0-9_.+-]+$', help_text=_("Required. 30 characters or fewer. Letters, digits and ./+/-/_ only."),
        error_messages={'invalid': _("This value may contain only letters, numbers and ./+/-/_ characters.")}
    )
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('username',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Member.objects.get(username=username)
        except Member.DoesNotExist:
            return username
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MemberCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class MemberChangeForm(forms.ModelForm):
    class MemberChangeForm(forms.ModelForm):
        username = forms.RegexField(
            label=_("Username"), max_length=30, regex=r'^[A-Za-z0-9_.+-]+$',
            help_text=_("Required. 30 characters or fewer. Letters, digits and ./+/-/_ only."),
            error_messages={'invalid': _("This value may contain only letters, numbers and ./+/-/_ characters.")})
        password = ReadOnlyPasswordHashField(label=_("Password"),
            help_text=_("Raw passwords are not stored, so there is no way to see "
                        "this user's password, but you can change the password "
                        "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Member
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MemberChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial['password']


