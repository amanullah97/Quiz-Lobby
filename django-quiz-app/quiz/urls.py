from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user, signup_view, Homeview, contact_message, Application_Form_View, Application_Message
from django.urls import path


urlpatterns = [         url(regex=r'^$', view=index.as_view(), name='index'),
                        url(regex=r'^home/$', view=Homeview.as_view(), name='home'),
                        url(regex=r'^application/$', view=Application_Form_View.as_view(), name='application_form'),
                        url(regex=r'^application_message/$', view=Application_Message.as_view(), name='application_message'),
                        url(regex=r'^contact/$', view=contact_message, name='contact_message'),
                        url(regex=r'^signup/$', view=signup_view, name='signup'),
                        url(regex=r'^login/$', view=login_user, name='login'),
                        url(regex=r'^logout/$', view=logout_user, name='logout'),
                        url(regex=r'^quizzes/$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                        url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                        url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                        url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                        url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                        url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                        url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                        url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),


]