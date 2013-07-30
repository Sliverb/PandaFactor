from django.forms import CharField, ChoiceField, Form, Textarea, TextInput

class CreateJobForm(Form):
    title = CharField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}));
    duration = CharField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}));
    location = CharField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}));
    
    IS_PAID_CHOICES = ((1, 'Paid'), (2, 'Unpaid'))
    is_paid = ChoiceField(choices=IS_PAID_CHOICES)
    
    description = CharField(widget=Textarea)

    