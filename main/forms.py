from django import forms
from django.conf import settings

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=100, help_text="Mention whether it's a Query or Report")
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    # def is_valid(self, form):
    #     body = {
    #         'your_name': form.cleaned_data['your_name'],
    #         'email': form.cleaned_data['email'],
    #         'subject': form.cleaned_data['subject'],
    #         'message': form.cleaned_data['message'],
    #     }
    #     email_body = f'Hi Admin/Team \n\n {body[message]} \n\n {body[your_name]}'
    #     try:
    #         send_email(body['subject'], email_body, body['email'], settings.FROM_EMAIL)
    #     except BadHeaderError:
    #         messages.error('Invalid header')
        
    #     return redirect('main:contact')

