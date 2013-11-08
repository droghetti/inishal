__author__ = 'droghetti'
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    #@user_passes_test(lambda u: u.groups.filter(name='Manager').count() == 0, login_url='/console/accounts/login')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)