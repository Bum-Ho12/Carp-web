from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns= [
    path('',views.bookView,name='book'),
    path('book_json_format/',views.BookView,name='bookS'),
    path('notificaton/',views.notificationView,name='notification'),
    path('notification_json_format/',views.NotificationView,name='notificationS'),
    path('activity/',views.activityView, name='activity'),
    path('activity_json_format/',views.ActivityView,name='activityS'),
    path('album/',views.albumView, name='album'),
    path('album_json_format/',views.AlbumView,name='albumS'),
    path('booklist/',views.bookList, name='bookls'),
    path('activitylist/',views.activityList, name='activityls'),
    path('albumlist/',views.albumList, name='albumls'),
    path('notificationlist/',views.notificationList, name='notificationls'),
    path('book/<int:pk>/', views.bookDetail,name='bookdl'),
    path('activity/<int:pk>/', views.activityDetail,name='activitydl'),
    path('album/<int:pk>/', views.albumDetail,name='albumdl'),
    path('notification/<int:pk>/', views.notificationDetail,name='notificationdl'),
    path('book_update/<int:pk>/', views.bookUpdate,name='bookup'),
    path('activity_update/<int:pk>/', views.activityUpdate,name='activityup'),
    path('album_update/<int:pk>/', views.albumUpdate,name='albumup'),
    path('notification_update/<int:pk>/', views.notificationUpdate,name='notificationup'),
    path('book_delete/<int:pk>/', views.bookDelete,name='bookdel'),
    path('activity_delete/<int:pk>/', views.activityDelete,name='activitydel'),
    path('album_delete/<int:pk>/', views.albumDelete,name='albumdel'),
    path('notification_delete/<int:pk>/', views.notificationDelete,name='notificationdel'),

]

urlpatterns= format_suffix_patterns(urlpatterns)
