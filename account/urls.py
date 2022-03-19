from unicodedata import name
from django.urls import path
from .views import IndexView,PanelView,IncomeView,OutroView,DebtsView,IncomeAddView,OutroAddView,DebtAddView,IncomeListView,OutroListView
from django.contrib.auth import views 
from django.urls import path
urlpatterns = [
    path('', IndexView.as_view()),
    path('panel/', PanelView.as_view(),name='panel'),
    path('incomes/<int:pk>',IncomeView.as_view(),name="incomesdetail"),
    path('outro/<int:pk>', OutroView.as_view(),name="outrosdetail"),
    path('debts/<int:pk>', DebtsView.as_view(),name="debtsdetail"),
    path('IncomeAdd/', IncomeAddView.as_view(),name="incomeadd"),
    path('OutroAdd/', OutroAddView.as_view(),name="outroadd"),
    path('DebtAdd/', DebtAddView.as_view(),name="debtadd"),
    path('IncomeList/', IncomeListView.as_view(),name="incomelist"),
    path('OutroList/', OutroListView.as_view(),name="outrolist")
]

urlpatterns += [ path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]