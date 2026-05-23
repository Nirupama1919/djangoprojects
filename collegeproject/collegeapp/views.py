

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def colleges(request):

    colleges_list = ['SVEW', 'VIT', 'BVRICE']

    return render(request, 'colleges.html', {
        'colleges': colleges_list
    })

def students(request):

    students_data = [
        {'sno': 1, 'name': 'Asha', 'branch': 'CSE', 'age': 17},
        {'sno': 2, 'name': 'Ravi', 'branch': 'ECE', 'age': 20},
        {'sno': 3, 'name': 'Sneha', 'branch': 'IT', 'age': 18},
    ]

    return render(request, 'students.html', {
        'students': students_data
    })
def address(request):
    return render(request, 'address.html')