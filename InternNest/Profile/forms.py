from django.forms import CharField, EmailField, Form, TextInput


class ContactInfoForm(Form):
    phone = CharField(max_length=100, required=False, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    email = EmailField(max_length=254, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    address = CharField(max_length=100, required=False, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    