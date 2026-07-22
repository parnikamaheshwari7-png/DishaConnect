from django.shortcuts import render
from . models import Category, Question
# Create your views here.

def general_advice(request):
    categories=Category.objects.all()

    context={
        "categories":categories
    }

    return render(request, "guidance/general_advice.html", context)


def category_questions(request, category_id):

    category = Category.objects.get(id=category_id)

    questions = Question.objects.filter(
        category=category,
        is_active=True
    )

    context = {
        "category": category,
        "questions": questions,
    }

    return render(
        request,
        "guidance/category_questions.html",
        context
    )

from django.shortcuts import get_object_or_404

def question_answer(request, question_id):

    question = get_object_or_404(
        Question,
        id=question_id,
        is_active=True
    )

    related_questions = Question.objects.filter(
        category=question.category,
        is_active=True
    ).exclude(
        id=question.id
    )[:5]

    context = {
        "question": question,
        "related_questions": related_questions,
    }

    return render(
        request,
        "guidance/question_answer.html",
        context
    )

def ai_guidance(request):
    return render(request, "guidance/ai_guidance.html")


def ask_guide(request):
    return render(request, "guidance/ask_guide.html")