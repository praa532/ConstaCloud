from django.urls import path
from .views import HomePage, HomePage2,GetStudentsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage, name='home'),
    path('home/', HomePage2, name='home2'),
    path('getstudents/', GetStudentsView.as_view(), name='get_students'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)