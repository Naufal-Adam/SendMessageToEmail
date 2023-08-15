from django.shortcuts import redirect, render
from .form import SendEmailForm
from .models import sendMail
from django.core.mail import EmailMessage

def send_test(request):
    mail = sendMail.objects.all()
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['nama']
            message = form.cleaned_data['pesan']
            from_email = form.cleaned_data['email']
            to_email = [form.cleaned_data['email_tujuan']]
            attachment = request.FILES['lampiran']
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=to_email,
            )
            email.attach(attachment.name, attachment.read(), attachment.content_type)
            email.send()
            form.save()
            return redirect('send_bro')
    else:
         form = SendEmailForm()
    return render(request, 'send.html', {'form': form, 'mail': mail})