
from rest_framework.routers import DefaultRouter
from subscription.views import SubscriptionViewSet
from subscription.apps import SubscriptionConfig

app_name = SubscriptionConfig.name

router = DefaultRouter()
router.register(r'course', SubscriptionViewSet, basename='subscription')


urlpatterns = [

]+router.urls