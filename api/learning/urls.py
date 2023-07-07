from django.urls import path
from .views import StudyPlanView, SectionView

app_name = 'learning'

urlpatterns = [
    path('studyplan', StudyPlanView.as_view(), name='study_plan_view'),
    path('section', SectionView.as_view(), name='section_view'),
]