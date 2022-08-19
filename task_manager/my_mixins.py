from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class MyLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                self.request,
                messages.ERROR,
                _("You are not autorized! Please sign in."),
            )
            return redirect("/login")

        return super().dispatch(request, *args, **kwargs)


class MyUserPassesTestMixin(UserPassesTestMixin):

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            messages.add_message(
                self.request,
                messages.ERROR,
                (self.no_permission_message),
            )
            return redirect(self.no_permission_url)
        return super().dispatch(request, *args, **kwargs)
