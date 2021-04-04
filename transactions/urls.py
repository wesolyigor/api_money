from django.urls import path
from rest_framework.routers import SimpleRouter

from transactions.views import AccountViewSet, TransactionViewSet, StatsView

router = SimpleRouter()

router.register('v1/accounts', AccountViewSet, basename='accounts')
router.register('v1/transactions', TransactionViewSet, basename='transactions')

urlpatterns = router.urls

# app_name = 'transactions'

urlpatterns += [
    path('v1/stats/', StatsView.as_view()),
    # path('v1/accounts/', AccountViewSet.as_view(), name='accounts')
]
