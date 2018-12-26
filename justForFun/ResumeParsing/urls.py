from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
                path('',views.index, name="root"),
                path('index/',views.index, name="index"),
                path('login/',views.loginView, name="login"),
            ] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
