from courses.models import Course
from django.shortcuts import render
def index(request):
    courses=Course.objects.all()
    context={'courses':courses}
    context['custom_theme']=getDefaultCustomize()
    students={}
    for course in courses:
        students2=list(map(lambda x:x.last_name[0].upper()+x.last_name[1:]+" "+x.first_name[0].upper(),course.students.filter(is_staff=False).order_by("last_name","first_name")))
        students[course.title]=students2
    context['students']=students
    return render(request,"index.html",context)