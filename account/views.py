import datetime
from urllib import request
from functions.functions import fillterbymonthanduser
from mymoudles.models import User, income,outro,debt
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 

class IndexView(TemplateView):
    template_name = "account/index.html"


class PanelView(LoginRequiredMixin,ListView):
    template_name = "account/panel.html"
    model = income
    context_object_name = "intro"
    def get_queryset(self):
        MyContent = super(PanelView, self).get_queryset()
        #this function do this => #return MyContent.filter(user= self.request.user,date__month=datetime.datetime.now().strftime("%m"))
        return fillterbymonthanduser(MyContent,self.request.user)
    
    #add another models
    def get_context_data(self, **kwargs):
        context = super(PanelView, self).get_context_data(**kwargs)
        context.update({
            'outro': fillterbymonthanduser(outro.objects, self.request.user),
            'debt': debt.objects.filter(user= self.request.user),
        })
        return context


class IncomeView(LoginRequiredMixin,DetailView):
    template_name = "account/incomedetail.html"
    model = income
    context_object_name = "obj"
    def get_queryset(self):
        MyContent = super(IncomeView, self).get_queryset()
        return MyContent.filter(user= self.request.user)


class OutroView(LoginRequiredMixin,DetailView):
    template_name = "account/outrodetail.html"
    model = outro
    context_object_name = "obj"
    def get_queryset(self):
        MyContent = super(OutroView, self).get_queryset()
        return MyContent.filter(user= self.request.user)


class DebtsView(LoginRequiredMixin,DetailView):
    template_name = "account/debtdetail.html"
    model = debt
    context_object_name = "obj"
    def get_queryset(self):
        MyContent = super(DebtsView, self).get_queryset()
        return MyContent.filter(user= self.request.user)


class IncomeAddView(LoginRequiredMixin,CreateView):
    model = income
    fields = ['name','valu']
    template_name = 'account/incomeadd.html'
    success_url = '/panel/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.datetime.now()
        return super(IncomeAddView, self).form_valid(form)


class OutroAddView(LoginRequiredMixin,CreateView):
    model = outro
    fields = ['name','valu']
    template_name = 'account/outroadd.html'
    success_url = '/panel/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.datetime.now()
        return super(OutroAddView, self).form_valid(form)


class DebtAddView(LoginRequiredMixin,CreateView):
    model = debt
    fields = ['name','allvalu','mounthvalu','finishtime']
    template_name = 'account/debtadd.html'
    success_url = '/panel/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DebtAddView, self).form_valid(form)


class IncomeListView(LoginRequiredMixin,ListView):
    model = income
    template_name = 'account/incomelist.html'
    context_object_name = "intro"

    def get_queryset(self):
            MyContent = super(IncomeListView, self).get_queryset()
            return MyContent.filter(user= self.request.user)


class OutroListView(LoginRequiredMixin,ListView):
    model = outro
    template_name = 'account/outrolist.html'
    context_object_name = "outro"

    def get_queryset(self):
            MyContent = super(OutroListView, self).get_queryset()
            return MyContent.filter(user= self.request.user)









