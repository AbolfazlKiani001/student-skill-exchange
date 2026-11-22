from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Skill, contactmessage, StudentProfile


def skill_list(request):
    skills = Skill.objects.all()

    return render(request, 'skills/skill_list.html', {
        'skills': skills
    })


def skill_detail(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    return render(request, 'skills/skill_detail.html', {
        'skill': skill
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('skill_list')

        return render(request, 'skills/login.html', {
            'error': 'نام کاربری یا رمز عبور اشتباه است.'
        })

    return render(request, 'skills/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        email = request.POST.get('email', '').strip()
        major = request.POST.get('major', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        terms = request.POST.get('terms')

        if not all([first_name, last_name, username, student_id,
                    email, major, password, confirm_password]):
            return render(request, 'skills/register.html', {
                'error': 'تمام فیلدها را تکمیل کنید.'
            })

        if not terms:
            return render(request, 'skills/register.html', {
                'error': 'باید قوانین سامانه را بپذیرید.'
            })

        if password != confirm_password:
            return render(request, 'skills/register.html', {
                'error': 'رمزهای عبور یکسان نیستند.'
            })

        if len(password) < 8:
            return render(request, 'skills/register.html', {
                'error': 'رمز عبور باید حداقل ۸ کاراکتر باشد.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'skills/register.html', {
                'error': 'این نام کاربری قبلاً ثبت شده است.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'skills/register.html', {
                'error': 'این ایمیل قبلاً ثبت شده است.'
            })

        if User.objects.filter(studentprofile__student_id=student_id).exists():
            return render(request, 'skills/register.html', {
                'error': 'این شماره دانشجویی قبلاً ثبت شده است.'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        StudentProfile.objects.create(
            user=user,
            student_id=student_id,
            major=major
        )

        return redirect('login')

    return render(request, 'skills/register.html')


def about(request):
    return render(request, 'skills/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            contactmessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            return render(request, 'skills/contact.html', {
                'success': 'پیام شما با موفقیت ثبت شد.'
            })

        return render(request, 'skills/contact.html', {
            'error': 'لطفاً تمام فیلدها را تکمیل کنید.'
        })

    return render(request, 'skills/contact.html')
# Create your views here.
