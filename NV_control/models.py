from django.db import models
from django.contrib.auth.models import AbstractUser


class Company_Name(models.Model):
    c_full_name=models.CharField(max_length=500)
    c_short_name=models.CharField(max_length=500)
    logo=models.ImageField(upload_to='media /company/logo/')
    location=models.TextField(max_length=800)
    date=models.DateTimeField(auto_now_add=True)
    # active

    def __str__(self):
        return f'{self.c_short_name} {self.date}'

class Office_User(AbstractUser):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=150, null=True)
    name_english=models.CharField(max_length=150, null=True)
    date_of_bath=models.DateField(null=True)
    father_name=models.CharField(max_length=250, null=True)
    mother_name=models.CharField(max_length=250,null=True)
    present_address=models.TextField(max_length=500, null=True)
    cell_number_1=models.CharField(max_length=15, null=True)
    cell_number_2=models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.c_name} {self.name} {self.cell_number_1} {self.cell_number_2}'




# Create your models here.

class Company_Active(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.c_name} {self.datetime}'

class Company_Deactive(models.Model):
    c_name=models.OneToOneField(Company_Active, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.c_name} {self.datetime}'



class Company_Help_Desk(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    l_education=models.CharField(max_length=255)
    degination=models.CharField(max_length=100)
    number=models.CharField(max_length=15)

    def _str_(self):
        return f'{self.c_name} {self.name} {self.number}'

class Company_Expense_Catagory(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    exp_name=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.c_name} {self.exp_name}'

class Company_Expense(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    exp_id=models.CharField(max_length=25, null=True)
    catagory=models.ForeignKey(Company_Expense_Catagory, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=255)
    details=models.TextField(max_length=1000)
    amount=models.FloatField()
    entry_by=models.ForeignKey(Office_User, on_delete=models.DO_NOTHING)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.c_name} {self.catagory} {self.amount}'

class Course(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=150)
    short_name=models.CharField(max_length=150)
    code=models.CharField(max_length=25)
    number_of_class=models.PositiveIntegerField()
    payment_system=models.BooleanField(default=False)# True = fix False = monthly
    active=models.BooleanField(default=False)# varify by super admin
    date=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return f'{self.c_name} {self.course_name} {self.payment_system}'

class Course_Feese(models.Model):
    c_name=models.ForeignKey(Company_Name,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    amount=models.FloatField()
    max_discount=models.FloatField(null=True)# it belog to max descount parsentis (%)

    def _str_(self):
        return f'{self.c_name} {self.date} {self.course} {self.amount}'

class Course_Necessary_Document(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    document_name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    mandatory=models.BooleanField(default=True)

    def _str_(self):
        return f'{self.c_name} {self.course} {self.document_name}'

class Course_Day(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    day_name=models.CharField(max_length=30)

    def _str_(self):
        return f'{self.c_name} {self.course} {self.day_name}'

class Course_Time(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    s_time=models.TimeField()
    e_time=models.TimeField(null=True)

    def _str_(self):
        return f'{self.c_name} {self.course} {self.s_time}'

class Course_Batch(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    batch=models.CharField(max_length=50)

    def _str_(self):
        return f'{self.c_name} {self.course} {self.batch}'

class Student_User(models.Model):
    #backend neacessary info
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    course_fee=models.ForeignKey(Course_Feese, on_delete=models.CASCADE)

    date=models.DateTimeField(auto_now_add=True)
    discount=models.FloatField(default=0)
    #my company necessary info but optional
    course_day=models.ForeignKey(Course_Day, on_delete=models.CASCADE, null=True)
    course_time=models.ForeignKey(Course_Time, on_delete=models.CASCADE, null=True)
    course_batch=models.ForeignKey(Course_Batch, on_delete=models.CASCADE, null=True)


    #personal info
    student_id=models.CharField(max_length=150, null=True)
    name_english=models.CharField(max_length=150, null=True)
    name_bangla=models.CharField(max_length=250, null=True)
    nich_name=models.CharField(max_length=250, null=True)
    date_of_bath=models.DateField(null=True)
    blood_group=models.CharField(max_length=5, null=True)
    father_name=models.CharField(max_length=250, null=True)
    mother_name=models.CharField(max_length=250,null=True)
    father_occupation=models.CharField(max_length=250, null=True)
    present_address=models.TextField(max_length=500, null=True)
    cell_number_student=models.CharField(max_length=15)
    cell_number_guardian=models.CharField(max_length=15)

    def _str_(self):
        return f'{self.c_name} {self.name_english} {self.cell_number_student}'


class Student_User_Close(models.Model):
    student=models.OneToOneField(Student_User, on_delete=models.CASCADE)
    remarks=models.TextField(max_length=750, null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} {self.date.date()}'

class Payment_Receive(models.Model):
    c_name=models.ForeignKey(Company_Name, on_delete=models.CASCADE)
    student=models.ForeignKey(Student_User, on_delete=models.CASCADE)
    amount=models.FloatField()
    reveive_by=models.CharField(max_length=80)
    payment_id=models.CharField(max_length=50)

    date=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.payment_id} {self.amount} {self.date}'

class Course_Student_Documents_Submited(models.Model):
    student=models.OneToOneField(Student_User, on_delete=models.CASCADE)
    document=models.ManyToManyField(Course_Necessary_Document)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} {self.document.count()} {self.date.date()}'

class Course_Student_Penalti(models.Model):
    student=models.ForeignKey(Student_User, on_delete=models.DO_NOTHING)
    amount=models.FloatField()
    remarks=models.TextField(max_length=750)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} {self.amount}'

class Course_Student_Waiver(models.Model):
    student=models.ForeignKey(Student_User, on_delete=models.DO_NOTHING)
    amount=models.FloatField()
    remarks=models.TextField(max_length=750)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} {self.amount}'