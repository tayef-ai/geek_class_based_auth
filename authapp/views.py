from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LoginView
from .forms import ChangePasswordForm, ResetPasswordForm, PasswordSetForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
# Create your views here.
class MyLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')

        return super().dispatch(request, *args, **kwargs)
    authentication_form=LoginForm

@login_required(login_url="/login/")
def dashboardview(request):
    user = request.user
    email = user.email
    return render(request, 'registration/dashboard.html', {'user': user, 'email': email})

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class ChangePView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/changepassword.html'
    form_class=ChangePasswordForm
    success_url = '/dashboard/'
    success_message = "Password updated successfully"

class ResetPasswordView(PasswordResetView):
    template_name = 'registration/resetpassword.html'
    form_class=ResetPasswordForm
    # success_url = '/dashboard/'
    # success_message = "Password updated successfully"

class PasswordSetView(PasswordResetConfirmView):
    template_name = 'registration/passwordset.html'
    form_class=PasswordSetForm
    # success_url = '/dashboard/'
    # success_message = "Password updated successfully"