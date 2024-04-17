from django.urls import path
from django.urls.conf import include
from django.conf.urls.i18n import i18n_patterns
from myCV.views import cv_view, portfolio_details_view, send_email

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('send-email/', send_email, name='send_email'),
]

urlpatterns += i18n_patterns(
    path('', cv_view, name='cv_view'),
    path('portfolio-details/', portfolio_details_view, name='portfolio_details_view'),
)
