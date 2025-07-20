from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assignments.views.student_assignment import StudentAssignmentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'assignments', StudentAssignmentViewSet, basename='studentassignment')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
