from django import forms
from .models import sendMail

class SendEmailForm(forms.ModelForm):
    nama = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama'}),
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    )
    email_tujuan = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email tujuan'}),
    )
    pesan = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pesan'}),
    )
    lampiran = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-info'})
    )
    class Meta:
        model = sendMail
        fields = ['nama', 'email', 'pesan', 'email_tujuan', 'lampiran']
