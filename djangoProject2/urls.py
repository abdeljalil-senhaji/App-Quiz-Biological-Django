"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Quiz_Biological.views import create_quiz, list_quiz, list_image, quiz_mode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addQuiz/', create_quiz, name='create_view'),
    path('listQuiz/', list_quiz, name='list_view'),
    path('listImages/', list_image, name='explore_view'),
    path('quizMode/', quiz_mode, name='quiz_mode'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
