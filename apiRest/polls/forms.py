from django import forms
 
class FormularioRegistro(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Correo Electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', max_length=100, widget=forms.PasswordInput)
 
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
 
        if password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')
 
        return cleaned_data

class FormularioLogin(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)
 
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data