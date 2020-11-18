from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# relative import of forms
from .models import Quiz, Image, Answer, Question
from .forms import QuizForm


def create_quiz(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_quiz(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Quiz.objects.all()

    return render(request, "list_view.html", context)


def list_image(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Image.objects.all()

    return render(request, "explore_view.html", context)


def quiz_mode(request):
    answerTemp = Answer.objects.all()
    answers = []
    j = 1
    for a in answerTemp:
        if j < 4:
            answers.append(a)
        if j == 4:
            answers.append(a)
            break
        j = j + 1
    allImages = Image.objects.all()
    image_list = []
    for img in allImages:
        if img.question.id != 1:
            break
        image_list.append(img)
    page = request.GET.get('page', 1)
    page2 = request.GET.get('page', 1)
    paginator = Paginator(image_list, 2)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    temp = Image.objects.all()
    image_list2 = []
    i = 1
    for t in Image.objects.all():
        if i % 2 == 0:
            image_list2.append(t)
        i = i + 1

    paginator2 = Paginator(image_list2, 1)
    try:
        images2 = paginator2.page(page2)
    except PageNotAnInteger:
        images2 = paginator2.page(1)
    except EmptyPage:
        images2 = paginator2.page(paginator2.num_pages)
    return render(request, "quiz_mode.html", {'images': images, 'images2': images2, 'answers': answers})
