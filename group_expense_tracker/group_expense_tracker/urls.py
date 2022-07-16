from django.contrib import admin
from django.urls import path
from .app.views import CreateNewGroup,GetBalanceExpense,AddExpenseToGroup,UpdateExpenseInGroup,DeleteExpenseInGroup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create', CreateNewGroup),
    path('api/add', AddExpenseToGroup),
    path('api/update', UpdateExpenseInGroup),
    path('api/delete', DeleteExpenseInGroup),
    path('api/balance', GetBalanceExpense),
]
    