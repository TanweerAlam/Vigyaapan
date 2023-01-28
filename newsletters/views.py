from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.sites.models import Site

# Create your views here.
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
def new(request):
    #
    form = None
    #
    if request.method == 'POST':
        #
        form = SubscriberForm(request.POST)
        if form.is_valid():
            sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
            is_exist = len(Subscriber.objects.filter(email=request.POST['email']))
            if is_exist:
                messages.error(request, 'Email already exists! Check mailbox and confirm it...')
                # redirect
            else:
                sub.save()
                # from_email=settings.FROM_EMAIL,
                # to_email=sub.email,
                # subject='Newsletter Confirmation',
                # html_message='Thank you for signing up for my email newsletter! \
                #     Please complete the process by \
                #     <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                #     confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                #                                         sub.email,
                #                                         sub.conf_num)
                # current_site = Site.objects.get_current()

                message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject='Newsletter Confirmation',
                    html_content='Thank you for signing up for my email newsletter! \
                        Please complete the process by \
                        <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                        confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                            sub.email,
                                                            sub.conf_num)
                )
                # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                # response = sg.send(message)

                try:
                    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                    response = sg.send(message)
                    print(response)
                    # send_mail(subject, html_message, from_email, (to_email,), fail_silently=False)
                    messages.success(request, "Subscription email has been sent...")
                except:
                    messages.error(request, "Something's wrong with the subscription system...")

                return HttpResponseRedirect(reverse('main:index'))
                # return render(request, 'main/index', {'email': sub.email, 'action': 'added', 'subscriber_form': SubscriberForm()})

        else:
            messages.error(request, "Something went wrong. Try later...")
            # return render(request, 'main/index.html', {'form': SubscriberForm()})
    return HttpResponseRedirect(reverse('main:index'))
        #
        # sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        # sub.save()
        # message = Mail(
        #     from_email=settings.FROM_EMAIL,
        #     to_emails=sub.email,
        #     subject='Newsletter Confirmation',
        #     html_content='Thank you for signing up for my email newsletter! \
        #         Please complete the process by \
        #         <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
        #         confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
        #                                             sub.email,
        #                                             sub.conf_num)
        # )
    #     sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    #     response = sg.send(message)
    #     return render(request, 'newsletters/newsletters.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    # else:
    #     return render(request, 'newsletters/newsletters.html', {'form': SubscriberForm()})


def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'newsletters/newsletters.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'newsletters/newsletters.html', {'email': sub.email, 'action': 'denied'})


def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.conf_num:
        sub.delete()
        return render(request, 'newsletters/newsletters.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'newsletters/newsletters.html', {'email': sub.email, 'action': 'denied'})
