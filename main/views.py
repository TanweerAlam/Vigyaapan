from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


from .models import Main
from jobs.models import Job
from .forms import ContactForm
from django.conf import settings



# Create your views here.

class IndexView(TemplateView):
    template_name = "main/index.html"
    # extra_context = {'jobs': Job.objects.filter(is_published=True).values('post_title')}
    # extra_context = {'site' : Main.objects.get(page__icontains="home")}
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['site'] = Main.objects.get(page__icontains="home")
        context['job_notifications'] = Job.objects.filter(is_published=True).order_by('-created_on').values('post_title', 'slug')[:10]
        context['job_by_results'] = Job.objects.filter( result_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')[:10]
        context['featured_jobs'] = Job.objects.filter(is_featured=True, is_published=True).order_by('-updated_on').values('post_title', 'slug')[:10]
        context['job_by_admitcards'] = Job.objects.filter(admit_card_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')[:10]
        context['job_syllabus'] = Job.objects.filter(syllabus_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')[:10]

        return context
    

class AboutView(TemplateView):
    template_name = "main/about.html"
    extra_context = {'site' : Main.objects.get(page__icontains="about")}
    
# class ContactView(FormView):
#     template_name = "main/contact.html"
#     form_class = ContactForm
#     # extra_context = {'site' : Main.objects.get(page__icontains="contact")}

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             body = {
#                 'your_name': form.cleaned_data['your_name'],
#                 'email': form.cleaned_data['email'],
#                 'subject': form.cleaned_data['subject'],
#                 'message': form.cleaned_data['message'],
#             }
#             email_body = f'Hi Admin/Team \n\n {body['message']} \n\n {body['your_name']}'
#             try:
#                 send_email(body['subject'], email_body, body['email'], settings.FROM_EMAIL)
#             except BadHeaderError:
#                 messages.error('Invalid header')
#             # return self.form_valid(form)
#             return redirect('main:contact')
#         else:
#             return self.form_invalid(form)


@csrf_exempt
def contactView(request):
    site = Main.objects.get(page__icontains="contact")
    form = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_body = f'Hi Admin/Team \n\n {message} \n\n {your_name}'

            try:
                send_mail(subject, email_body, 'tanweeralam1312@gmail.com', ('tannumystic@gmail.com',))
                messages.success(request, "Your email was sent to the admins.")
            except BadHeaderError:
                messages.error('Invalid header')
            
            return redirect('main:contact')
    
    form = ContactForm()
    return render(request, 'main/contact.html', {'site': site, 'form': form})