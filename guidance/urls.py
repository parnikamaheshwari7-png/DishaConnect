from django.urls import path
from . import views

urlpatterns=[
    path("", views.general_advice, name="general_advice"),
     path(
        "category/<int:category_id>/",
        views.category_questions,
        name="category_questions"
    ),
    path(
    "question/<int:question_id>/",
    views.question_answer,
    name="question_answer"
),
path(
    "ai-guidance/",
    views.ai_guidance,
    name="ai_guidance"
),

path(
    "ask-guide/",
    views.ask_guide,
    name="ask_guide"
),
]