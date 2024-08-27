from django.urls import path
from .views import BudgetListView, BudgetDetailView, BudgetCreateView, BudgetUpdateView, BudgetItemUpdateView, export_budget_report, BudgetDeleteView

urlpatterns = [
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('budgets/add/', BudgetCreateView.as_view(), name='budget-add'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget-edit'),
    path('budgets/<int:pk>/items/', BudgetItemUpdateView.as_view(), name='budget-item-update'), 
    path('budgets/export/<int:pk>/', export_budget_report, name='budget-export'),
    path('<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget-delete'),

]
