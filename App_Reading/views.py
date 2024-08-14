from django.shortcuts import render, redirect
from .models import Story

def reading(request):
    english_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    selected_english_level = request.GET.get('english_level', None)
    selected_title = request.GET.get('title', None)
    
    titles = Story.objects.none()
    story = None
    
    if selected_english_level:
        titles = Story.objects.filter(english_level=selected_english_level).values_list('title', flat=True).distinct()
    
    if selected_title:
        try:
            story = Story.objects.get(title=selected_title, english_level=selected_english_level)
        except Story.DoesNotExist:
            story = None
    
    context = {
        'english_levels': english_levels,
        'selected_english_level': selected_english_level,
        'titles': titles,
        'selected_title': selected_title,
        'story': story
    }
    return render(request, 'reading.html', context)