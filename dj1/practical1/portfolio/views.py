from django.shortcuts import render

projects = [
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio built with Django to showcase my projects.",
        "image": "images/prj1.png",
        "github_link": "NONE",
        
    },
    {
        "title": "Finance Analytics Dashboard",
        "description": "A dashboard for visualizing financial data and analytics using matplotlib and seaborn.",
        "image": "images/prj2.png",
        "github_link": "https://github.com/Harshit10032006/Finance-Analytics-Dashboard",
        
    },
    {
        "title": "Device Price Prediction",
        "description": "A machine learning model to predict device prices based on their specifications.",
        "image": "images/prj3.png",
        "github_link": "https://github.com/Harshit10032006/Device_price_prediction",
       
    },
    {
        "title": "RAG-Based DBMS AI Teaching Assistant",
        "description": "An AI-powered teaching assistant for database management systems, leveraging Retrieval-Augmented Generation (RAG) techniques.",
        "image": "images/prj4.png",
        "github_link": "https://github.com/Harshit10032006/RAG-Based-DBMS-AI-Teaching-Assistant",
     
    },
]

def home(request):
    return render(request, 'home.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')