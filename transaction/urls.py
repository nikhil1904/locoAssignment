from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls import url

# Modules
from .views import TransactionViewSet, TransactionTypesView, TransactionSumView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'/transaction', TransactionViewSet, basename="transactions")
# router.register(r'/types', views.TransactionTypesView, basename="types")

urlpatterns = [
    path('', include(router.urls)),
    path('/types/<str:type>', TransactionTypesView.as_view()),
    path('/sum/<int:transaction_id>', TransactionSumView.as_view())
]

# urlpatterns = router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
