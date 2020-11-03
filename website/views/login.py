from django.contrib.auth.views import LoginView
from rest_framework.authtoken.models import Token


class Login(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        self.request.session["token"] = Token.objects.get_or_create(user=self.request.user)[0].key
        return super().get_success_url()
