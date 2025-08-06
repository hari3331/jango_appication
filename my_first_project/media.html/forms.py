from django import forms
class Contact_form(models.Model):
    name = forms.CharField(required=False)
    email=forms.EmailField(label="Enter Your Emai0l")
    feedback=forms.CharField(widget=forms.Textarea)
