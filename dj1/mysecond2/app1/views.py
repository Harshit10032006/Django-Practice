from multiprocessing import context

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class View :
    def __init__ (self,age,name,gender):
        self.age = age
        self.name = name
        self.gender = gender
    
def home (request):
        context={'name':'Johnny','age':20,'gender':'Male',
                 'skills':['Python','Django','React'],
                 'user':View(30,'John','Male'),
                 'app1':{
                     'title':'My First App',
                     'content':'This is my first app using Django framework',
                     'created_at':'2023-01-01',
                 }}
        return render(request,'home.html',context)


def control(request):
    content = {
        "company": "GameVerse Studios",
        "role": "Backend Django Developer Intern",
        "location": "Remote",
        "experience": "Fresher",
        "salary": "₹6 - ₹10 LPA",

        "requirements": [
            "Good knowledge of Python",
            "Basic understanding of Django",
            "Knowledge of HTML & CSS",
            "Basic SQL knowledge",
            "Understanding of Git & GitHub",
            "Problem-solving skills"
        ],

        "skills": [
            "Python",
            "Django",
            "REST API",
            "Git",
            "HTML",
            "CSS",
            "JavaScript"
        ],

        "benefits": [
            "Work From Home",
            "Flexible Working Hours",
            "Learning Budget",
            "Performance Bonus",
            "Certificate of Internship"
        ]
    }

   
    return render(request,'controlflow.html',content)