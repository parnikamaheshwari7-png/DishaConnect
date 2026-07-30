from django import forms

from guidance.models import Category

from .models import UserQuery


class AskGuideForm(forms.ModelForm):

    class Meta:
        model = UserQuery
        fields = ("category", "title", "description", "is_anonymous")
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Brief summary of your question",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Describe your question in detail so our guides can help you better.",
            }),
            "is_anonymous": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
        self.fields["category"].empty_label = "Select a guidance category"
