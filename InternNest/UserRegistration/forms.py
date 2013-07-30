from django.forms import CharField, EmailField, Form, HiddenInput, IntegerField, PasswordInput, TextInput, ValidationError, widgets

class LoginForm(Form):
    email = EmailField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    password = CharField(widget=PasswordInput(attrs={'class':'textboxWithPlaceholder'}))
   
    # Additional validation logic
    def clean(self):
        cleaned_data = super(Form, self).clean()
       
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')
        if email and email2:
            if email != email2:
                message = 'The entered emails do not match'
                self._errors['email2'] = self.error_class([message])
                del cleaned_data['email2']
            elif get_user_model().objects.filter(email=email).count() != 0:
                message = 'That email is already registered'
                self._errors['email'] = self.error_class([message])
                del cleaned_data['email']
            
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if (password and password2) and (password != password2):
            message = 'The entered passwords do not match'
            self._errors['password2'] = self.error_class([message])
            del cleaned_data['password2']
        
        return cleaned_data
    
class RegisterUserForm(Form):
    first_name = CharField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}));
    last_name = CharField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}));
    email = EmailField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    email2 = EmailField(max_length=100, widget=TextInput(attrs={'class':'textboxWithPlaceholder'}))
    password = CharField(widget=PasswordInput(attrs={'class':'textboxWithPlaceholder'}))
    password2 = CharField(widget=PasswordInput(attrs={'class':'textboxWithPlaceholder'}))
    
    # Additional validation logic
    def clean(self):
        cleaned_data = super(Form, self).clean()
       
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')
        if email and email2:
            if email != email2:
                message = 'The entered emails do not match'
                self._errors['email2'] = self.error_class([message])
                del cleaned_data['email2']
            elif get_user_model().objects.filter(email=email).count() != 0:
                message = 'That email is already registered'
                self._errors['email'] = self.error_class([message])
                del cleaned_data['email']
            
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if (password and password2) and (password != password2):
            message = 'The entered passwords do not match'
            self._errors['password2'] = self.error_class([message])
            del cleaned_data['password2']
        
        return cleaned_data