from django.urls import path 
from django.conf import settings
from . import views 

urlpatterns = [
    path('', views.popular_featured, name='popular_featured'),
    path('chat', views.chat, name='chat'),
    path('final/', views.final, name='final'),
    path('Thanks/', views.Thanks, name='Thanks'),
    path('construction/', views.construction, name='construction'),
    path('jihudumie/', views.jihudumie, name='jihudumie'),
    path('complete/', views.complete, name='complete'),
    #path('toggle_bookmark/<int:property_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('Register/', views.Register, name='Register'),
    path('submit_inquiry/<int:property_id>/', views.submit_inquiry, name='submit_inquiry'),
    path('delete_inquiry/<int:id>/', views.delete_inquiry, name='delete_inquiry'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset_password/', views.reset_password, name='reset_password'),  
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('notifications/', views.notifications_view, name='notifications_view'),
    # path('notifications/mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('property_list/', views.property_list, name='property_list'),
    path('offer/', views.New_offer, name='New_offer'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('add_property/', views.add_property, name='add_property'),
    path('search_property/', views.search_property, name='search_property'),
]

