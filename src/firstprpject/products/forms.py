from django.forms import ModelForm, Form, CharField, TextInput, IntegerField, Textarea, forms , EmailField
from .models import Product


class ProductForm(ModelForm):
    # override default attributes
    title = CharField(min_length=1, widget=TextInput(attrs={
        'placeholder': ' title , please'
    }))

    description = CharField(min_length=1, widget=Textarea(attrs={
        'class': 'my-class',
        'rows': 20,
        'cols': 120,
        'id': 'my-id'
    }))
    emails = EmailField()
    price = IntegerField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    #   def clean_<field_name>():

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if not ("nadim" in title):
            raise forms.ValidationError(message="please enter title that contain nadim ")
        if not ('me' in title):
            raise forms.ValidationError(message="please enter title that contain me ")

        return title

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')

        if not email.endWith(".com"):
            raise forms.ValidationError("please enter a valid email")

        return email



class ProductRawForm(Form):
    title = CharField(min_length=1, widget=TextInput(attrs={
        'placeholder': 'enter title'
    }))
    description = CharField(min_length=1, widget=Textarea(attrs={
        'class': 'my-class',
        'rows': 20,
        'cols': 120,
        'id': 'my-id'
    }))
    price = IntegerField()
