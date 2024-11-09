# myprofile/views.py
from django.shortcuts import render

def profile_view(request):
    context = {
        'name': 'Meenakshi Varma_ 2310080009',
        'degree': 'B.Tech in Artificial Intelligence & Data Science, KLH University',
        'bio': "AI & Data Science student focused on leveraging technology to drive innovation in healthcare and agriculture.",
        'email': 'meenakshisibyala@gmail.com',
        'phone': '+91 9327544123',
        'location': 'Hyderabad',
        'skills': [
            'Java - Intermediate',
            'Python - Advanced',
            'Machine Learning - Intermediate',
            'Data Analysis - Intermediate',
            'HTML & CSS - Intermediate',
            'SQL - Intermediate',
        ],
        'achievements': [
            'Participated in RoboRace - Robotics Competition',
            'Active Participant in Various Tech Events & Hackathons',
            'Anchored & Hosted College Events',
            'Cultural Incharge for SAC',
            'Volunteered for AI & Tech Workshops',
        ],
        'education': [
            'Schooling in Little Scholar\'s school',
            'Intermediate in Ignite',
            'B.Tech in AI & DS, KLH University',
        ],
        'projects': [
            {
                'name': 'Routine maker website',
                'description': 'Developed a PERSONAL CARE website which will help you to manage time',
                'link': 'https://github.com/meeenakshii/Projectpfsd2k24'
            }
        ],
        'contact': {
            'email': '2310080009@klh.edu.in',
            'phone': '+91 62093729837',
            'linkedin': 'https://www.linkedin.com/in/meenakshi-varma-807a00226/',
            'github': 'https://github.com/meeenakshii',
        },
    }
    return render(request, 'profile.html', context)
