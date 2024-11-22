from django import forms
from .models import Category

class PostFilterForm(forms.Form):
    # title = forms.CharField(required=False, max_length=100)
    # category = forms.ChoiceField(choices=[('', 'All'), ('tech', 'Tech'), ('life', 'Life'), ('news', 'News')], required=False)
    # start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    search = forms.CharField(
        required=False,
        max_length=200,
        label='جستجو'
    )
    # query = forms.CharField(required=False, label="جستجو در عنوان", widget=forms.TextInput(attrs={'placeholder': 'عنوان پست...'}))
    # category = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple(attrs={
    #         "class": "form-check-input"
    #     }),
    #     label="دسته‌بندی"
    # )
