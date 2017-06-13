from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import UpdateView

from companies.models import CompanyForm, Company


@login_required
def add(request):
    company_form = CompanyForm()
    return render(request, 'companies/add.html', {'CompanyForm': company_form})


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'companies/index.html'
    context_object_name = 'companies'

    def get_queryset(self):
        """
        :return: all the companies created by current user ordered by creation date
        """
        user_id = self.request.user.id
        return Company.objects.filter(user_id__exact=user_id).order_by('-creation_date')


@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'companies/update.html'
    form_class = CompanyForm
    success_url = '/companies/'


@login_required
def save(request):
    if request.POST:
        current_user = request.user
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.user_id = current_user.id
            new_company.save()

        return HttpResponseRedirect(reverse('companies:index'))

    return HttpResponse("Passed confirmed did not get the post")


@login_required
def update(request, pk=None):
    obj = get_object_or_404(Company, pk=pk)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            return redirect('/companies/')
    return render(request, 'companies/update.html', {'form': form})


@login_required
def delete(request, pk=None):
    if request.method == 'GET':
        obj = get_object_or_404(Company, pk=pk)
        obj.delete()
        return redirect('/companies/')
