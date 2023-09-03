from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import Group
from datetime import *
from django.db.models import Avg, Count, Min, Sum, Q, F
from dateutil.relativedelta import relativedelta



class Account:
    def __init__(self, account):
        self.account=account# 
    
    def account_close_and_month_count(self):
        try:
            close_date=self.account.student_user_close.date.date()
        except:
            close_date=datetime.now().date()
        cal_date=relativedelta(close_date, self.account.date.date())
        
        if self.account.course.payment_system:
            return 1
        else:
            return cal_date.month# 12 months

    def waivers(self):
        amount=self.account.course_student_waiver_set.all().aggregate(Sum('amount'))['amount__sum']
        if amount:
            return amount
        else:
            return 0
    
    def fines(self):
        amount=self.account.course_student_penalti_set.all().aggregate(Sum('amount'))['amount__sum']
        if amount:
            return amount
        else:
            return 0

    def paid_amount(self):
        amount=self.account.payment_receive_set.all().aggregate(Sum('amount'))['amount__sum']
        if amount:
            return amount+self.waivers()
        else:
            return self.waivers()

    def actual_fee(self):# with and with out fee
        course_fee=self.account.course_fee.amount
        discount=self.account.discount
        fee=course_fee-discount
        month=self.account_close_and_month_count()
        return month*fee+self.fines()
    
    def due(self):
        due=self.actual_fee()-self.paid_amount()
        return due

    

# class Document(Account):
#     def __init__(self, account):
#         super()__init__(account)

    