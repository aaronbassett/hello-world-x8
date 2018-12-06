from django.conf.urls import url
from conversation.views import NCCOView

app_name = "conversation"

urlpatterns = [url(r"^$", NCCOView.as_view(), name="ncco")]
