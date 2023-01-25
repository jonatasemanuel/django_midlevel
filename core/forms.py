from django import forms
from django.core.mail.message import EmailMessage
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E- mail', max_length=120)
    topic = forms.CharField(label='Topic', max_length=60)
    message = forms.CharField(label='Message', widget=forms.Textarea())
    
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        topic = self.cleaned_data['topic']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nE- mail: {email}\nTopi: {topic}\nMessage: {message}'

        mail = EmailMessage(
                subject='E- mail sended by django_mid system',
                body=content,
                from_email='jonatassilvaemanuel@gmail.com',
                to=['jonatassilvaemanuel@gmail.com', ],
                headers={'Reply-To': email}
                )
        mail.send()

