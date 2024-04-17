from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.mail import send_mail
from django.http import JsonResponse


def cv_view(request):
    return render(request, 'base.html')


@xframe_options_exempt
def portfolio_details_view(request):
    return render(request, 'portfolio_details.html')


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject,
                f'De la: {name}\nE-mail: {email}\nMesaj: {message}',
                email,
                ['contact@adrian-dolca.ro'],
                fail_silently=False,
            )
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
