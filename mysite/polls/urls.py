from django.urls import path
from . import views

#app_name sirve para distinguir las diferentes url
#que pueden existir en un proyecto django
#en este caso solo hay una apliación: poll
#sin embargo, pueden existir varias más en un proyecto
#muchas de las cuales pueden tener las mismas urls
#por eso es necesario especificar un namespace (app_name)
#para saber qué url cargar en cada template

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
