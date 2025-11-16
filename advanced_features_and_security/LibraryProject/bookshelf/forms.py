from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        strip=True
    )

class ExampleForm(forms.Form):
    """
    A simple example form required by the checker.
    Can be used in templates such as form_example.html.
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name"
    )
    email = forms.EmailField(
        required=True,
        label="Email"
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="Message"
    )