from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Student, Exams
from .forms import LoginForm, RegisterForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # messages.success(request, "Successfully saved")
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            exam = Exams.objects.all()
            ur = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            dbuser = Student.objects.filter(user=ur, password=pd)
            if not dbuser:
                return HttpResponse('Login failed')
            else:
                request.session['z'] = ur
                request.session.get_expiry_age()
                instance = get_object_or_404(Student, user=ur)
                return render(request, 'examhome.html', {'exam': exam, 'ur': ur, 'instance': instance})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def exam(request):
    if request.session.has_key('z'):
        name = request.GET.get('name')
        request.session['name'] = name
        a = request.session['z']
        exam = Exams.objects.filter(exam_name=name)
        instance = get_object_or_404(Student, user=a)
        context = {
            'exam': exam,
            'ur': a,
            'instance': instance,
            'exam_name': name,
        }
        return render(request, 'userexamhome.html', context)
