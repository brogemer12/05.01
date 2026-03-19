from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from .forms import ExamForm, GroupForm
from django.db.models import Q
from django.contrib.auth.models import Group

def exam_list(request):
    query = request.GET.get('q')
    exams = Exam.objects.filter(is_public=True).order_by('date')
    
    if query:
        exams = exams.filter(Q(title__icontains=query) | Q(users__username__icontains=query) | Q(groups__name__icontains=query)).distinct()
        
    return render(request, 'exams/exam_list.html', {'exams': exams})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exams/exam_form.html', {'form': form, 'title': 'Добавить новый экзамен'})

def exam_edit(request, key):
    exam = get_object_or_404(Exam, pk=key)
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'exams/exam_form.html', {'form': form, 'title': 'Редактировать экзамен'})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'exams/group_list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'exams/exam_form.html', {'form': form, 'title': 'Создать группу', 'back_url': 'group_list'})

def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'exams/exam_form.html', {'form': form, 'title': 'Редактировать группу', 'back_url': 'group_list'})
