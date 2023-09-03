"""
URL configuration for nanovision project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    #all input form url
    path('company/login/', login, name='login'),
    path('company/course/entry', company_course_entry, name='company_course_entry'),
    path('company/empolys/user/entry/', company_empolys_user_entry, name='company_empolys_user_entry'),
    path('company/course/new/time/<str:id>/entry', company_course_new_time_entry, name='company_course_new_time_entry'),
    path('company/course/exist/time/<str:id>/delete', compay_course_exist_time_delete,
         name='compay_course_exist_time_delete'),
    path('company/course/exist/time/<str:id>/edit', company_course_exist_time_edit,
         name='company_course_exist_time_edit'),

    path('company/course/new/batch/<str:id>/entry', company_course_new_batch_entry, name='company_course_new_batch_entry'),
    path('company/course/exit/batch/<str:id>/delete', company_course_exist_batch_delete, name='company_course_exist_batch_delete'),
    path('company/course/exit/batch/<str:id>/edit', company_course_exist_batch_edit, name='company_course_exist_batch_edit'),

    path('company/course/new/document/<str:id>/entry', company_course_new_document_entry, name='company_course_new_document_entry'),
    path('company/course/exit/document/<str:id>/delete', company_course_exist_document_delete, name='company_course_exist_document_delete'),
    path('company/course/exit/document/<str:id>/edit', company_course_exist_document_edit, name='company_course_exist_document_edit'),
    path('company/course/document/submission/<str:id>/and/list/view', company_course_student_docment_submition_and_list_view, name='company_course_student_docment_submition_and_list_view'),



    path('company/expences/catagory/entry', company_expence_catagory_entry, name='company_expence_catagory_entry'),
    path('company/expences/catagory/<str:id>/delete', company_expences_catagory_delete, name='company_expences_catagory_delete'),
    path('company/expences/entry', company_expense_entry, name='company_expense_entry'),


    path('company/course/fees/list/<str:id>/view', company_course_fee_list_view, name='company_course_fee_list_view'),
    path('company/course/fees/<str:id>/entry/', company_course_new_fee_entry, name='company_course_new_fee_entry'),


    path('company/help/desk/number/entry', company_help_desk_number_entry, name='company_help_desk_number_entry'),



    path('company/student/payment/entry/', company_student_payment_entry, name='company_student_payment_entry'),
    path('company/student/payment/<str:id>/history/', company_student_payment_history, name='company_student_payment_history'),
    path('company/daily/income/history/', company_daily_income_history, name='company_daily_income_history'),


    path('company/student/payment/fine/entry', company_student_fine_entry, name='company_student_fine_entry'),
    path('company/student/payment/waiver/entry', company_student_waiver_entry, name='company_student_waiver_entry'),



    path('company/daily/exp/history/', company_daily_exp_history, name='company_daily_exp_history'),




#new account for student of user
    path('company/close/an/<str:id>/account/', company_close_an_account, name='company_close_an_account'),
    path('company/close/account/list', company_student_or_user_close_report, name='company_student_or_user_close_report'),
    path('company/create/an/account/', company_create_new_account, name='company_create_new_account'),
    path('company/create/an/account/<str:id>/online', company_create_new_account_online, name='company_create_new_account_online'),
    path('company/students/or/user/report', company_student_or_user_report, name='company_student_or_user_report'),
    path('company/students/or/user/<str:id>/details/view', company_student_details_view, name='company_student_details_view'),

    # all reporting form url

    path('company/course/list/view', company_course_list_view, name='company_course_list_view'),


    path('company/student/search/auto/with/ajax', company_student_search_with_ajax, name='company_student_search_with_ajax'),

]


