import requests
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from assignments.models import StudentAssignment
from assignments.serializers.student_assignment import StudentAssignmentSerializer
from .permissions import ReadOnlyOrAuthenticated


class StudentAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = StudentAssignment.active_objects.all()
    permission_classes = [ReadOnlyOrAuthenticated] 

    def perform_create(self, serializer):
        instance = serializer.save()
        self.trigger_webhook(instance, event="create")

    def perform_update(self, serializer):
        instance = serializer.save()
        self.trigger_webhook(instance, event="update")

    def destroy(self, request, *args, **kwargs):
        """Soft delete instead of actual delete"""
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def trigger_webhook(self, instance, event):
        webhook_url = "https://webhook.site/a736290f-3e19-4eea-a64d-289cac5ad1f1"  

        payload = {
            "event": event,
            "student_name": instance.student_name,
            "assignment_title": instance.assignment_title,
            "status": instance.status,
        }

        try:
            requests.post(webhook_url, json=payload, timeout=5)
        except requests.exceptions.RequestException as e:
            # Log or handle error as needed
            print(f"Webhook failed: {e}")


