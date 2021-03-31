from rest_framework.routers import SimpleRouter

from todos.views import TodoViewsSet

router = SimpleRouter()

router.register('', TodoViewsSet, basename='todos')

urlpatterns = router.urls