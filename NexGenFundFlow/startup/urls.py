from . import views
from django.urls import path

app_name = 'startup'


urlpatterns = [
    path('create/',views.create_startup_view,name='create_startup_view'),
    path('brows/<startup_id>/',views.view_startup_profile_view,name='view_startup_profile_view'),
    path('edit/<startup_id>/',views.edit_startup_view,name='edit_startup_view'),
    path('<startup_id>/team/',views.team_view,name='team_view'),
    path('<startup_id>/add/team/',views.add_team_member_view,name='add_team_member_view'),
    path('all/<user_id>/',views.view_all_my_stratup_view,name='view_all_my_stratup_view'),
    path('<startup_id>/funding/create/',views.funding_round_view,name='funding_round_view'),
    path('<startup_id>/all/fund/',views.all_funding_round_view,name='all_funding_round_view'),
    path('view/startup/<startup_id>/requests/',views.view_funding_request,name='view_funding_request'),
    path('<request_id>/approved/request',views.approved_reqeust_view,name='approved_reqeust_view'),
    path('<request_id>/disapproved/request',views.disapproved_reqeust_view,name='disapproved_reqeust_view'),
    path('<startup_id>/funding/create/', views.all_funding_round_view, name='funding_round_view'),
    path('all/startup/request/<user_id>',views.view_all_funding_request,name='view_all_funding_request'),
    path('view/funding/round/request/<funding_id>/',views.funding_request_view,name='funding_request_view'),
    path('edit/members/<member_id>/',views.edit_member_profile_view,name='edit_member_profile_view'),
    path('delete/member/<member_id>/',views.delete_member_view,name='delete_member_view'),
    path('edit/member/<member_id>/',views.edit_member,name='edit_member'),
    path('startup/funding/request/<funding_id>',views.view_funding_requests,name='view_funding_requests')
]