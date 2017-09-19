# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.formsets import BaseFormSet
from django.forms.formsets import formset_factory
from apps.users.multiform import MultiFormsView
from multi_form_view import MultiModelFormView

from .forms import RegistrationAdminForm
from .forms import RegistrationAttendantForm
from .forms import AddressForm

from .models import Admin, Address


def home(request):
    return render(request, 'users/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:home')
    return logout(request, *args, **kwargs)


class RegistrationAdminView(MultiModelFormView):
    form_classes = {
        'registration_admin_form' : RegistrationAdminForm,
        'address_form' : AddressForm,
    }
    record_id = None
    template_name = 'users/registerStaff.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationAdminView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        self.admin_id = self.kwargs.get('admin_id', None)
        try:
            admin = Admin.objects.get(id=self.admin_id)
        except Admin.DoesNotExist:
            admin = None
        return {
            'registration_admin_form': admin,
            'address_form': admin.address if admin else None,
        }

    def get_success_url(self):
        return reverse('users:login')

    def forms_valid(self, forms):
        admin = forms['registration_admin_form'].save(commit=False)
        admin.address = forms['address_form'].save()
        admin.save()
        return super(RegistrationAdminView, self).forms_valid(forms)
    '''
    form_class = RegistrationAdminForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')

    form_classes = {'address': AddressForm,
                    'admin': RegistrationAdminForm}

    def get_address_initial(self):
        return {'email':''}

    def get_admin_initial(self):
        return {'email':''}

    def get_context_data(self, **kwargs):
        context = super(RegistrationAdminView, self).get_context_data(**kwargs)
        context.update({"teste": 'teste',
                        "teste": 'teste'})
        return context

    def address_form_valid(self, form):
        print (form)
        user = form.save(self.request)
        return form.address(self.request, redirect_url=self.get_success_url())

    def admin_form_valid(self, form):
        print (form)
        print ("\\\\\\")
        user = form.save(self.request)
        return form.admin(self.request, user, self.get_success_url())
    '''

class RegistrationAttendantView(CreateView):
    form_class = RegistrationAttendantForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')
