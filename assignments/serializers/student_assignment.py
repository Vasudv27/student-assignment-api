from rest_framework import serializers
from assignments.models import StudentAssignment


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssignment
        fields = [
            'id',
            'auto_id',
            'student_name',
            'assignment_title',
            'description',
            'due_date',
            'status',
            'date_added',
            'date_updated',
        ]
        read_only_fields = ['id', 'auto_id', 'date_added', 'date_updated']
