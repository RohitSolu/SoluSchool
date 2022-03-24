from django.urls import path
# from django.contrib import auth
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home, name="home"),
    #Auth
    path('signup',views.SignUp.as_view(),name='signup'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    #Student
    path('home/student_1/<int:id>',views.student_1,name="student_1"),
    path('home/student_1/addstudent',views.addStudent,name="add_student"),
    path('home/student_1/update/<int:pk>/', views.student_update,name='student_update'),
    path('home/student_1/delete/<int:pk>/', views.student_delete,name='student_delete'),

    #Subject
    path('home/subject/<int:id>', views.subject,name='subject'),
    path('home/subject/addsubject',views.addSubject,name="add_subject"),
    path('home/subject/update/<int:pk>/', views.subject_update,name='subject_update'),
    path('home/subject/delete/<int:pk>/', views.subject_delete,name='subject_delete'),

    #Result
    path('home/result_1/<int:id>', views.result_1,name='result_1'),
    path('home/result_1/addresult', views.addResult,name='add_result'),
    #Search
    path('home/search', views.searchview,name='search'),
    #Marksheet
    path('home/result_1/marksheet/<int:roll_no>',views.marksheet,name='marksheet'),
    #Dashboard
    path('home/dashboard',views.DashboardView.as_view(),name='dashboard'),
    #Issuer
    path('home/issuer',views.issuer,name='issuer'),
    path('home/issuer/issuer_update/<int:id>',views.issuer_update,name='issuer_update')
   
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)