from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def register(request):

    success = False

    if request.method == 'POST':

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():

            Student.objects.create(

                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                dob=form.cleaned_data['dob'],
                gender=form.cleaned_data['gender'],

                department=form.cleaned_data['department'],
                year=form.cleaned_data['year'],
                roll_number=form.cleaned_data['roll_number'],

                address=form.cleaned_data['address'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],

                technical_skills=', '.join(
                    form.cleaned_data['technical_skills']
                ),

                learning_mode=form.cleaned_data['learning_mode'],

                resume=request.FILES['resume'],

                about=form.cleaned_data['about']
            )

            success = True
            form = StudentForm()

    else:

        form = StudentForm()

    return render(request, 'register.html', {
        'form': form,
        'success': success
    })