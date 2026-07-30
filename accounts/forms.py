from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Expertise


class RegisterForm(UserCreationForm):

    role = forms.ChoiceField(
        choices=[
            (CustomUser.Roles.USER, "Seek Guidance"),
            (CustomUser.Roles.GUIDE, "Become a Guide"),
        ],
        widget=forms.RadioSelect(attrs={
            "class": "role-radio",
        }),
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
        widget=forms.CheckboxSelectMultiple(attrs={
            "class": "expertise-checkboxes",
        }),
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
                "placeholder": "First name",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
            }),

            "mobile_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Mobile number (optional)",
            }),
        }

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "mobile_number": "Mobile Number",
            "role": "How would you like to join?",
            "qualification": "Highest Qualification",
            "experience_years": "Years of Experience",
            "bio": "About You",
            "languages_known": "Languages Known",
            "linkedin_url": "LinkedIn Profile",
            "password1": "Password",
            "password2": "Confirm Password",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Create a strong password",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Re-enter your password",
        })
        self.fields["mobile_number"].required = False


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
