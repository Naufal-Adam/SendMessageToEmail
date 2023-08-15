from email.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import SendEmailForm
from django.core.mail import send_mail
from .models import sendMail

# Create your views here.
def send_test(request):
    mail = sendMail.objects.all()
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['nama']
            message = form.cleaned_data['pesan']
            from_email = form.cleaned_data['email']
            to_email = [form.cleaned_data['email_tujuan']]
            email = EmailMessage(subject, message, from_email, to_email)
            attachment = request.FILES.get('lampiran')
            if attachment:
                email.attach(attachment.name, attachment.read(), mimetype=attachment.content_type)
                email.send()
            form.save()
            return redirect('send_bro')
    else:
        form = SendEmailForm()
    return render(request, 'send.html', {'form': form, 'mail': mail})