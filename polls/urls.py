from django.urls import path

from . import views

#modificado en tuto part 4
'''
app_name='polls'  #agregamos un namespace por si tenemos luego mas apps aparte de polls
urlpatterns = [
    path('',views.index, name='index'),
    
    #the 'name' value as called by the {% url %} template tag
    path('/<int:question_id>/', views.detail, name='detail'),

    path('/<int:question_id>/results/', views.results, name='results'),

    path('/<int:question_id>/vote/', views.vote, name='vote'),
]
'''

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
     path('/music', views.model_form_upload, name='music'),
       path('/musicToHear', views.IndexView2.as_view(), name='musicToHear'),
]