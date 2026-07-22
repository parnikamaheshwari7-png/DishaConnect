from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Expertise


class RegisterForm(UserCreationForm):

    role = forms.ChoiceField(
        choices=[
            (CustomUser.Roles.USER, "User"),
            (CustomUser.Roles.GUIDE, "Guide"),
        ],
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    qualification = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Highest Qualification"
        })
    )

    experience_years = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Years of Experience"
        })
    )

    expertise = forms.ModelMultipleChoiceField(
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Tell us about yourself"
        })
    )

    languages_known = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "English, Hindi, Sanskrit"
        })
    )

    linkedin_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "LinkedIn Profile URL (Optional)"
        })
    )

    class Meta:
        model = CustomUser

        fields = (
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "role",
            "qualification",
            "experience_years",
            "expertise",
            "bio",
            "languages_known",
            "linkedin_url",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "mobile_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Mobile Number"
            }),
        }


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"
            }
        )
    )