from django.utils import timezone

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from django.contrib.auth import get_user_model
#from .models import User

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_login(self):
    #     if self.username and self.password:
    #         raise forms.ValidationError("Password or Email Incorrect.")

class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone', 'profession', 'gender', 'blood', 'first_address', 'second_address',
                  'last_donation_date', 'age')
        widgets = {
            'last_donation_date': DateInput()
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False # send for admin approval
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone', 'profession', 'gender', 'blood', 'first_address', 'second_address')


class LastDonationChangeForm(UserChangeForm):
    this_year = timezone.now().year
    class Meta:
        model = User
        fields = ('last_donation_date',)

        widgets = {
            'last_donation_date': DateInput()
        }





# class RegisterForm(forms.ModelForm):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     # class Meta:
#     #     model = User
#     #     fields = ('email',)
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Username is Taken")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email
#
#     # def clean_password2(self):
#     #     # Check that the two password entries match
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise forms.ValidationError("Passwords don't match")
#     #     return password2




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'update')


class DonorForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone', 'blood', 'first_address', 'last_donation_date')
        widgets = {
            'last_donation_date': DateInput()
        }




















