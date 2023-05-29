from django.urls import path
from rest_framework import routers
from calendar_app.views import GoogleCalendarInitView, GoogleCalendarRedirectView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path(
        "rest/v1/calendar/init/", GoogleCalendarInitView.as_view(), name="calendar-init"
    ),
    path(
        "rest/v1/calendar/redirect/",
        GoogleCalendarRedirectView.as_view(),
        name="calendar-redirect",
    ),
]
