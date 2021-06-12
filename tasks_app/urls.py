from django.urls import path
from tasks_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    # todo: delete V
    path('request_test', views.sample_http_resp, name='sample_http_resp'),
    path('AFK', views.AFK, name='AFK'),
    path('tasks/add_new', views.add_new, name='add_new'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
