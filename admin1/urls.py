from django.contrib import admin
from django.urls import path,include,reverse
from django.views.generic import RedirectView
from admin1 import views
from django.urls import path
from analytics.views import DataAnalyticsAPIView,DataAnalytics2APIView,userAPIView,salesExAPIView
from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views
from .middleware import LoginRedirectMiddleware



from .views import register, success,upload_csv,admin_dashboard,user_login,client_admin_dashboard,sales_dashboard,Please_upload_csv,analytics_dash,data_analytics_view,team,usermanagement,billing_summary,team_scorecard,header,teamleaderdetails,sales_ex,sales_analytics_view,sales_table,vechicledetails,unique_sales,unique_tl
from django.urls import path, include




urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/   ", RedirectView.as_view(url='/admin/logout/')),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    # path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    # path("admin/", user_login,name='admin'),
    # path('upload-csv/', upload_csv, name='upload'),
    path('admin1/', admin_dashboard, name='admin_dashboard'),
    path('sales_homepage/', sales_dashboard, name='sales_homepage'),
    # path('user_role/', views.user_dashboard, name='user_dashboard'),
    path('client_admin/', client_admin_dashboard, name='client_admin_dashboard'),
    path('Upload-csv/', upload_csv, name='upload1'),
    path('api/data/', DataAnalyticsAPIView.as_view(), name='get_data'),
    path('dashboard/', TemplateView.as_view(template_name='admin1/templates/dashboard.html'), name='dashboard'),
    path('analytics/', views.analytics_dash, name='Analytics'),
    # path('data-analytics/',data_analytics_view, name='data-analytics2'),
    path('logout/', views.logout_view, name='logout'),
    path('team_leader/',team,name="upload1"),
    path('api/data2/', DataAnalytics2APIView.as_view(), name='get_data'),
    path('usermanagement/',views.usermanagement, name='um'),
    path('billing_summary/',views.billing_summary, name='billing'),
    path('header/',views.header, name='header'),
    # path('api/user/', userAPIView.as_view(), name='registration-api'),
    path('team_scorecard/',views.team_scorecard,name='user_dashboard'),
    path('teamleaderdetails/',views.teamleaderdetails,name='teamleader_details'),
    path('sales_ex/',sales_ex,name='upload1'),
    path('api/sales',salesExAPIView.as_view(),name='get_data'),
    path('salesanalytics/',views.sales_analytics_view,name='sales_dashboard'),
    path('sales_table/',views.sales_table,name='sales_table'),
    path('vechicle_table/',views.vechicledetails,name='vechicle_table'),
    path('unique_tl/',views.unique_tl,name='uniquetl.html'),
    path('uniquesales_ex/',views.unique_sales,name='uniquesales_ex.html'),



]