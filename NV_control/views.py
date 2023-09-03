from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Avg, Count, Min, Sum, Q, F

from .Data_Query import *
# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'login.html',{"wrong":"wrong"})
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect(login)


@login_required(login_url='company/login/')
def home(request):
    company=request.user.c_name
    context={
        'cn':company
    }
    return render(request, 'base.html', context)

@login_required(login_url='company/login/')
def company_course_entry(request):
    if request.method=='POST':
        course_full_name=request.POST.get('course_full_name')
        course_short_name=request.POST.get('course_short_name')
        course_code=request.POST.get('course_code')
        number_of_classes=request.POST.get('number_of_classes')
        payment_system=request.POST.get('payment_system')
        Course.objects.create(
                              c_name=request.user.c_name,
                              course_name=course_full_name,
                              short_name=course_short_name,
                              code=course_code,
                              number_of_class=number_of_classes,
                              payment_system= True if payment_system else False
                              )

    return render(request, 'entry/course_entry.html', {'success':"success"})

@login_required(login_url='company/login/')
def company_course_new_time_entry(request, id):# course table id
    obj_course=Course.objects.get(id=id)
    context={
        'course':obj_course
        }
    if request.method=='POST':
        starting_time=request.POST.get('starting_time')
        ending_time=request.POST.get('ending_time')
        obj_course.course_time_set.create(c_name=request.user.c_name,
                                          s_time=starting_time,
                                          e_time=ending_time
                                          )
    return render(request, 'entry/time/course_time.html', context)

@login_required(login_url='company/login/')
def company_course_exist_time_edit(request, id):# course time table id
    obj_course_time=Course_Time.objects.get(id=id)
    context={
        'time': obj_course_time
    }
    if request.method=='POST':
        starting_time=request.POST.get('starting_time')
        ending_time=request.POST.get('ending_time')
        obj_course_time.s_time=starting_time
        obj_course_time.e_time=ending_time
        obj_course_time.save()
        return redirect(company_course_new_time_entry, obj_course_time.course.id)
    return render(request, 'entry/time/course_edit_time.html', context)

@login_required(login_url='company/login/')
def compay_course_exist_time_delete(request, id):# course time table id
    obj_course_time=Course_Time.objects.get(id=id)
    course_id=obj_course_time.course.id
    obj_course_time.delete()
    return redirect(company_course_new_time_entry,course_id)#render(request, '')

@login_required(login_url='company/login/')
def company_course_list_view(request):
    course=request.user.c_name.course_set.all()
    context={
        'courses':course
    }
    return render(request, 'report/course_list_view.html', context)

@login_required(login_url='company/login/')
def company_course_new_batch_entry(request, id):
    obj_course=Course.objects.get(id=id)
    context={
        "course":obj_course
    }
    if request.method=='POST':
        batch=request.POST.get('batch')
        obj_course.course_batch_set.create(c_name=request.user.c_name,
                                           batch=batch)
    return render(request,'entry/batch/course_batch_entry.html',context)

@login_required(login_url='company/login/')
def company_course_exist_batch_delete(request, id):#course batch table id
    obj_course_batch=Course_Batch.objects.get(id=id)
    course_id=obj_course_batch.course.id
    obj_course_batch.delete()
    return redirect(company_course_new_batch_entry, course_id)

@login_required(login_url='company/login/')
def company_course_exist_batch_edit(request, id):#course batch table id
    obj_batch=Course_Batch.objects.get(id=id)
    context={
        'batch':obj_batch
    }
    if request.method=='POST':
        batch=request.POST.get('batch')
        obj_batch.batch=batch
        obj_batch.save()
        return redirect(company_course_new_batch_entry, obj_batch.course.id)
    return render(request, 'entry/batch/course_edit_batch.html', context)


@login_required(login_url='company/login/')
def company_course_new_document_entry(request, id):# course table id
    obj_course=Course.objects.get(id=id)
    context={
        'course':obj_course
    }
    if request.method=='POST':
        document_name=request.POST.get('document_name')
        mandatory=request.POST.get('mandatory')
        Course_Necessary_Document.objects.create(c_name=request.user.c_name,
                                                 course=obj_course,
                                                 document_name=document_name,
                                                 mandatory= True if bool(mandatory) else False)
    return render(request, 'entry/document/course_document_entry.html', context)

@login_required(login_url='company/login/')
def company_course_exist_document_delete(request, id):#Course_Necessary_Document table id
    obj_cnd=Course_Necessary_Document.objects.get(id=id)
    course_id=obj_cnd.course.id
    obj_cnd.delete()
    return redirect(company_course_new_document_entry, course_id)

@login_required(login_url='company/login/')
def company_course_exist_document_edit(request, id):#Course_Necessary_Document table id
    obj_cnd=Course_Necessary_Document.objects.get(id=id)
    context={
        "document":obj_cnd
    }
    if request.method=='POST':
        document_name=request.POST.get('document_name')
        mandatory=request.POST.get('mandatory')
        obj_cnd.document_name=document_name
        obj_cnd.mandatory=True if bool(mandatory) else False
        obj_cnd.save()
        return redirect(company_course_new_document_entry, obj_cnd.course.id)
    return render(request, 'entry/document/course_edit_document.html', context)

@login_required(login_url='company/login/')
def company_course_student_docment_submition_and_list_view(request, id):#Student_User table id
    obj_stu=Student_User.objects.get(id=id)
    submiter_docs=Course_Student_Documents_Submited.objects.filter(student=obj_stu).last()#obj_stu.course_student_documents_submited.document.all().values_list('id', flat=True)
    doc_list=obj_stu.course.course_necessary_document_set.all()
    # print(submiter_docs.document.all().count())
    context={
        'student':obj_stu,
        'submited_docs': submiter_docs.document.all().values_list('id', flat=True) if submiter_docs.document.all() else None
    }
    if request.method=='POST':
        if submiter_docs:
            check_csds=submiter_docs
        else:
            check_csds=Course_Student_Documents_Submited(student=obj_stu)
            check_csds.save()
        for i in range(1, doc_list.count()+1):
            doc=request.POST.get(f'doc{i}')
            if bool(doc):
                obj_doc=doc_list[i-1]
                check_csds.document.add(obj_doc)
            else:
                continue
    return render(request, 'entry/document/student_doc_submite_entrry_and_view.html', context)



@login_required(login_url='company/login/')
def company_course_fee_list_view(request,id):# course table id
    obj_course=Course.objects.get(id=id)
    context={
        'course':obj_course
    }
    return render(request,'course_fee/course_fee_list.html', context)


@login_required(login_url='company/login/')
def company_expence_catagory_entry(request):
    if request.method=='POST':
        exp_catagory=request.POST.get('exp_name')
        Company_Expense_Catagory.objects.create(c_name=request.user.c_name,
                                                exp_name=exp_catagory)

    return render(request, 'entry/expencse/company_expencse_catagory_entry.html')


@login_required(login_url='company/login/')
def company_expences_catagory_delete(request, id):
    Company_Expense_Catagory.objects.get(id=id).delete()
    return redirect(company_expence_catagory_entry)



@login_required(login_url='company/login/')
def company_course_new_fee_entry(request,id):# course fee table id
    obj_courser_fee=Course_Feese.objects.get(id=id)
    context={
        'fee':obj_courser_fee
    }
    if request.method=='POST':
        amount=request.POST.get('amount')
        max_discount=request.POST.get('max_discount')
        Course_Feese.objects.create(c_name=request.user.c_name,
                                    course=obj_courser_fee.course,
                                    amount=amount,
                                    max_discount=max_discount)
        return redirect(company_course_fee_list_view, obj_courser_fee.course.id)
    return render(request, 'course_fee/course_fee_entry.html', context)

@login_required(login_url='company/login/')
def company_empolys_user_entry(request):
    context={
        'groups':Group.objects.all()
    }
    if request.method=='POST':
        e_ename=request.POST.get('e_ename')
        e_bname=request.POST.get('e_bname')
        email=request.POST.get('email')
        date_of_bath=request.POST.get('date_of_bath')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        present_address=request.POST.get('present_address')
        call_number1=request.POST.get('call_number1')
        call_number2=request.POST.get('call_number2')
        group=request.POST.get('group')# bring id
        obj_group=Group.objects.get(id=group)
        new=Office_User(
                        c_name=request.user.c_name,
                        username=email, email=email,
                        name=e_ename,name_english=e_bname,
                        date_of_bath=date_of_bath,
                        father_name= father_name,
                        mother_name=mother_name,
                        present_address=present_address,
                        cell_number_1=call_number1,
                        cell_number_2=call_number2
                        )
        new.save()
        new.set_password(f'{request.user.c_name.c_short_name}')
        context['success']='success'
        new.groups.add(obj_group)
        return render(request, 'entry/empoly_entry.html', context)
    return render(request, 'entry/empoly_entry.html', context)

@login_required(login_url='company/login/')
def company_help_desk_number_entry(request):
    if request.method=='POST':
        h_name = request.POST.get('h_name')
        last_education = request.POST.get('last_education')
        degination = request.POST.get('degination')
        phone_number = request.POST.get('phone_number')
        Company_Help_Desk.objects.create(
            c_name=request.user.c_name,
            name=h_name,
            l_education=last_education,
            degination=degination,
            number=phone_number
        )
    return render(request, 'entry/help_desk_number_entry.html', {'success':"success"})

def student_id_genarat(request):
    last_student=request.user.c_name.student_user_set.filter(date__year=datetime.now().date().year,
                                                             date__month=datetime.now().date().month).last()
    if bool(last_student):
        last_id=int(last_student.student_id[-4:])+1
        last_final_id=f'{last_id}'.zfill(4)
        full_and_final_id=f'{request.user.c_name.c_short_name}' \
                          f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id
    else:
        last_final_id=f'{1}'.zfill(4)
        full_and_final_id=f'{request.user.c_name.c_short_name}' \
                          f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id



        # Student_User.objects.filter(c_name=request.user.c_name)

# @login_required(login_url='company/login/')
# def new_student_or_user_entry(request):
#
#     return render(request, 'entry/student/new_student.html')

@login_required(login_url='company/login/')
def company_create_new_account(request):# it is new students
    if request.method=='POST':
        name_in_englis=request.POST.get('name_in_englis')
        name_in_bangla=request.POST.get('name_in_bangla')
        nich_name=request.POST.get('nich_name')
        date_of_bath=request.POST.get('date_of_bath')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        father_occupation=request.POST.get('father_occupation')
        present_address=request.POST.get('present_address')
        cell_number_student=request.POST.get('cell_number_student')
        cell_number_guardian=request.POST.get('cell_number_guardian')
        #admission info
        course=request.POST.get('course')# bring id
        obj_course=Course.objects.get(id=course)
        batch=request.POST.get('batch')# bring id
        obj_batch=Course_Batch.objects.get(id=batch)
        time=request.POST.get('stime')# bring id
        obj_time=Course_Time.objects.get(id=time)
        discount=request.POST.get('discount')# discount amount

        # student_id=f'{request.user.c_name.c_short_name}{datetime.now().strftime("%y")}'.zfill(4)
        student_id = student_id_genarat(request)

        new=Student_User(c_name=request.user.c_name,
                     student_id=student_id,
                     course=obj_course,
                     course_fee=obj_course.course_feese_set.last(),
                     course_time=obj_time,
                     course_batch=obj_batch,
                     discount=discount,
                     name_english=name_in_englis,
                     name_bangla=name_in_bangla,
                     nich_name=nich_name,
                     date_of_bath=date_of_bath,
                     blood_group=blood_group,
                     father_name=father_name,
                     mother_name=mother_name,
                     father_occupation=father_occupation,
                     present_address=present_address,
                     cell_number_student=cell_number_student,
                     cell_number_guardian=cell_number_guardian,
                     )
        new.save()
        return render(request, 'student/new_account_entry.html', {'success':'success'})
    return render(request, 'student/new_account_entry.html')


def company_create_new_account_online(request, id):# company id table
    company=Company_Name.objects.get(id=id)
    context={
        'company':company
    }
    if request.method=='POST':
        name_in_englis=request.POST.get('name_in_englis')
        name_in_bangla=request.POST.get('name_in_bangla')
        nich_name=request.POST.get('nich_name')
        date_of_bath=request.POST.get('date_of_bath')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        father_occupation=request.POST.get('father_occupation')
        present_address=request.POST.get('present_address')
        cell_number_student=request.POST.get('cell_number_student')
        cell_number_guardian=request.POST.get('cell_number_guardian')
        #admission info
        course=request.POST.get('course')# bring id
        obj_course=Course.objects.get(id=course)
        batch=request.POST.get('batch')# bring id
        obj_batch=Course_Batch.objects.get(id=batch)
        time=request.POST.get('stime')# bring id
        obj_time=Course_Time.objects.get(id=time)
        # discount=request.POST.get('discount')# discount amount

        # student_id=f'{request.user.c_name.c_short_name}{datetime.now().strftime("%y")}'.zfill(4)
        student_id = student_id_genarat(request)

        new=Student_User(c_name=request.user.c_name,
                     student_id=student_id,
                     course=obj_course,
                     course_fee=obj_course.course_feese_set.last(),
                     course_time=obj_time,
                     course_batch=obj_batch,
                    #  discount=discount,
                     name_english=name_in_englis,
                     name_bangla=name_in_bangla,
                     nich_name=nich_name,
                     date_of_bath=date_of_bath,
                     blood_group=blood_group,
                     father_name=father_name,
                     mother_name=mother_name,
                     father_occupation=father_occupation,
                     present_address=present_address,
                     cell_number_student=cell_number_student,
                     cell_number_guardian=cell_number_guardian,
                     )
        new.save()

        return render(request, 'student/student_account_online_entry.html', context)
    return render(request, 'student/student_account_online_entry.html', context)



@login_required(login_url='company/login/')
def company_close_an_account(request, id):# student_user table id 
    obj_stu=Student_User.objects.get(id=id)
    context={
        'student':obj_stu
    }
    if request.method=='POST':
        remarks=request.POST.get('remarks')
        Student_User_Close.objects.create(student=obj_stu, remarks=remarks)
        context['successfull']="successfully account is close"
    return render(request, 'student/student_account_close.html', context)


@login_required(login_url='company/login/')
def company_student_or_user_close_report(request):
    close_accounts=Student_User_Close.objects.filter(student__c_name=request.user.c_name)
    context={
        'accounts':close_accounts
    }
    return render(request, 'student/close_student_list.html', context)



@login_required(login_url='company/login/')
def company_student_or_user_report(request):
    students=Student_User.objects.filter(c_name=request.user.c_name)
    output={}
    for stu in students:
        acc=Account(stu)
        output[stu]=acc.actual_fee()
    context={
        'students':output
    }
    return render(request, 'student/student_list.html', context)


@login_required(login_url='company/login/')
def company_student_details_view(request, id):# student_user table id
    obj_student=Student_User.objects.get(id=id)
    acc=Account(obj_student)
    context={
        'student':acc
    }
    return render(request, 'student/student_details.html', context)



def payment_id_genarat(request):
    last_id=request.user.c_name.payment_receive_set.filter(date__year=datetime.now().date().year,
                                                               date__month=datetime.now().date().month).last()
    if bool(last_id):
        last_payment_id = int(last_id.payment_id[-4:]) + 1
        last_final_id = f'{last_payment_id}'.zfill(4)
        full_and_final_id = f'{request.user.c_name.c_short_name}-P-' \
                            f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id
    else:
        last_final_id = f'{1}'.zfill(4)
        full_and_final_id = f'{request.user.c_name.c_short_name}-P-' \
                            f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id



@login_required(login_url='company/login/')
def company_student_payment_entry(request):
    if request.method=='POST':
        student_id=request.POST.get('student_id')
        obj_student= Student_User.objects.get(
            c_name=request.user.c_name,
            student_id=student_id.upper()
                )    #request.user.c_name.student_user_set.get(student_id=student_id.upper())
        # obj_sudent=Student_User.objects.get(c_name=request)
        # student_name=request.POST.get('student_name')
        amount=request.POST.get('amount')
        payment_id=payment_id_genarat(request)
        obj_student.payment_receive_set.create(c_name=request.user.c_name,
                                              amount=amount,
                                              reveive_by=request.user.username,
                                              payment_id=payment_id)
        # print(student_id, student_name, amount)

        context={
            'successfull':f"successfull entry payment Payment\n"
                          f" ID {payment_id} and Amount {amount}"
        }
        return render(request, 'entry/payment/payment_entry.html', context)
    return render(request, 'entry/payment/payment_entry.html')



@login_required(redirect_field_name='login')
def company_daily_income_history(request):
    historis=Payment_Receive.objects.filter(c_name=request.user.c_name,
                                            date__date=datetime.now().date())
    courses=request.user.c_name.course_set.filter(active=True)
    context={
        'historis':historis,
        'courses':courses,
    }
    if request.method=='POST':
        courses=request.POST.get('courses')# bring id
        tdate=request.POST.get('tdate')
        fdate=request.POST.get('fdate')
        historis = Payment_Receive.objects.filter(c_name=request.user.c_name)
        if tdate and fdate:
            historis=historis.filter(date__date__range=[datetime.strptime(fdate, '%Y-%m-%d').date(),
                                                        datetime.strptime(tdate, '%Y-%m-%d').date()])
        elif fdate:
            historis = historis.filter(date__date__range=[datetime.strptime(fdate, '%Y-%m-%d').date(),
                                                          datetime.now().date()])
        elif tdate:
            historis = historis.filter(date__date=tdate)
        if courses!="All":
            historis = historis.filter(student__course__id=courses)
        context['historis'] = historis
        return render(request, 'report/payment/company_user_daily_income.html', context)
    return render(request, 'report/payment/company_user_daily_income.html', context)


@login_required(redirect_field_name='login')
def company_daily_exp_history(request):
    exp_history=request.user.c_name.company_expense_set.filter(date__date=datetime.now().date())
    context={
        'historis':exp_history
    }
    if request.method=='POST':
        exp_catagory=request.POST.get('exp_catagory')
        fdate=request.POST.get('fdate')
        tdate=request.POST.get('tdate')

        if tdate and fdate:
            historis=historis.filter(date__date__range=[datetime.strptime(fdate, '%Y-%m-%d').date(),
                                                        datetime.strptime(tdate, '%Y-%m-%d').date()])
        elif fdate:
            historis = historis.filter(date__date__range=[datetime.strptime(fdate, '%Y-%m-%d').date(),
                                                          datetime.now().date()])
        elif tdate:
            historis = historis.filter(date__date=tdate)
        if courses!="All":
            historis = historis.filter(student__course__id=courses)
        context['historis'] = historis

        return render(request, 'report/expense/company_user_daily_exp.html', context)
    return render(request, 'report/expense/company_user_daily_exp.html', context)


@login_required(redirect_field_name='login')
def company_student_payment_history(request, id):# student user table id
    obj_acount=Student_User.objects.get(id=id)
    acc=Account(obj_acount)

    payments=Payment_Receive.objects.filter(c_name=request.user.c_name, student__id=id)
    context={
        'payments':payments,
        'student':Student_User.objects.get(id=id)
    }
    return render(request, 'report/payment/student_user_payment_history.html',context)


@login_required(redirect_field_name='login')
def company_student_waiver_entry(request):
    print('fuck you function')
    if request.method=='POST':
        print('hello i am post')
        student_id=request.POST.get('student_id')
        obj_student=Student_User.objects.get(c_name=request.user.c_name,
                                            student_id=student_id.upper())

        amount=request.POST.get('amount')
        remarks=request.POST.get('remarks')
        obj_student.course_student_waiver_set.create(amount=amount,remarks=remarks)
        # print('hello there i am working', student_id, amount, remarks)
        context={
            'successfull':"Waiver entry successfully"
        }
        return render(request, 'entry/payment/waiver/student_waiver_entry.html', context)
    return render(request, 'entry/payment/waiver/student_waiver_entry.html')


@login_required(redirect_field_name='login')
def company_student_fine_entry(request):
    if request.method=='POST':
        student_id=request.POST.get('student_id')
        obj_student=Student_User.objects.get(c_name=request.user.c_name,
                                            student_id=student_id.upper())

        amount=request.POST.get('amount')
        remarks=request.POST.get('remarks')
        obj_student.course_student_penalti_set.create(amount=amount,remarks=remarks)
        context={
            'successfull':"Waiver entry successfully"
        }
        return render(request, 'entry/payment/fine/student_fine_entry.html', context)
    return render(request, 'entry/payment/fine/student_fine_entry.html')




def exp_id_genarat(request):
    last_id=request.user.c_name.company_expense_set.filter(date__year=datetime.now().date().year,
                                                               date__month=datetime.now().date().month).last()
    if bool(last_id):
        last_payment_id = int(last_id.payment_id[-4:]) + 1
        last_final_id = f'{last_payment_id}'.zfill(4)
        full_and_final_id = f'{request.user.c_name.c_short_name}-E-' \
                            f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id
    else:
        last_final_id = f'{1}'.zfill(4)
        full_and_final_id = f'{request.user.c_name.c_short_name}-E-' \
                            f'{datetime.now().strftime("%y")}{datetime.now().strftime("%m")}{last_final_id}'
        return full_and_final_id

@login_required(redirect_field_name='login')
def company_expense_entry(request):
    expence_catagory=request.user.c_name.company_expense_catagory_set.all()
    context={
        'exp_cat':expence_catagory,
        'ra':[i for i in range(1,8)]
    }

    if request.method=="POST":
        exp_id=exp_id_genarat(request)

        for i in range(1, 8):
            exp_catagory=request.POST.get(f"exp_catagory{i}")
            title=request.POST.get(f"title{i}")
            details=request.POST.get(f"details{i}")
            amount=request.POST.get(f"amount{i}")
            
            print(exp_catagory, title, details, amount, exp_id)

            if exp_catagory=='None':
                continue
            
            obj_exp_cata=Company_Expense_Catagory.objects.get(id=exp_catagory)
            Company_Expense.objects.create(c_name=request.user.c_name,
            title=title, details=details, amount=amount,catagory=obj_exp_cata,
            entry_by=request.user, exp_id=exp_id
            )
            context["successfull"]=f"Successfully entry\
            EXP id is : {exp_id}"
        return render(request, 'entry/expencse/company_expense_entry.html', context)
    return render(request, 'entry/expencse/company_expense_entry.html', context)


@login_required(redirect_field_name='login')
def company_student_search_with_ajax(request):
    # print('she is calling me succesfully')
    student_id = request.POST.get('s_or_u_id', None)
    # print(student_id,'here i am ')
    obj_student=Student_User.objects.filter(c_name=request.user.c_name,
                                            student_id=student_id.upper())
    # print(obj_student.count())
    context={
        'obj_student': list(obj_student.values())
    }
    return JsonResponse(context)

