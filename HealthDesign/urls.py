from django.conf.urls import url
from . import views

app_name = 'HealthDesign'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<demographics_id>[0-9]+)/$', views.detail, name='detail'),

    # HealthDesign/add-demographics/
    url(r'add-demographics/$', views.demographics_create, name='demographics-add'),

    # HealthDesign/3/update-demographics/
    url(r'(?P<demographics_id>[0-9]+)/update-demographics/$', views.demographics_update, name='demographics-update'),

    # HealthDesign/3/delete-demographics/
    url(r'(?P<demographics_id>[0-9]+)/delete-demographics/$', views.demographics_delete, name='demographics-delete'),

    # HealthDesign/2/add-guardian/
    url(r'(?P<demographics_id>[0-9]+)/add-guardian/$', views.guardian_create, name='guardian-add'),

    # HealthDesign/2/3/update-guardian/
    url(r'(?P<demographics_id>[0-9]+)/(?P<guardian_id>[0-9]+)/update-guardian/$', views.guardian_update, name='guardian-update'),

    # HealthDesign/3/2/delete-guardian/
    url(r'(?P<demographics_id>[0-9]+)/(?P<guardian_id>[0-9]+)/delete-guardian/$', views.guardian_delete, name='guardian-delete'),

    # HealthDesign/2/add-provider/
    url(r'(?P<demographics_id>[0-9]+)/add-provider/$', views.provider_create, name='provider-add'),

    # HealthDesign/2/1/update-provider/
    url(r'(?P<demographics_id>[0-9]+)/(?P<provider_id>[0-9]+)/update-provider/$', views.provider_update, name='provider-update'),

    # HealthDesign/3/2/delete-provider/
    url(r'(?P<demographics_id>[0-9]+)/(?P<provider_id>[0-9]+)/delete-provider/$', views.provider_delete, name='provider-delete'),

    # HealthDesign/2/add-allergies/
    url(r'(?P<demographics_id>[0-9]+)/add-allergies/$', views.allergies_create, name='allergies-add'),

    # HealthDesign/2/1/update-allergies/
    url(r'(?P<demographics_id>[0-9]+)/(?P<allergies_id>[0-9]+)/update-allergies/$', views.allergies_update, name='allergies-update'),

    # HealthDesign/3/2/delete-allergies/
    url(r'(?P<demographics_id>[0-9]+)/(?P<allergies_id>[0-9]+)/delete-allergies/$', views.allergies_delete, name='allergies-delete'),

    # HealthDesign/2/add-immunizations/
    url(r'(?P<demographics_id>[0-9]+)/add-immunizations/$', views.immunizations_create, name='immunizations-add'),

    # HealthDesign/2/4/update-immunizations/
    url(r'(?P<demographics_id>[0-9]+)/(?P<immunizations_id>[0-9]+)/update-immunizations/$', views.immunizations_update, name='immunizations-update'),

    # HealthDesign/3/2/delete-immunizations/
    url(r'(?P<demographics_id>[0-9]+)/(?P<immunizations_id>[0-9]+)/delete-immunizations/$', views.immunizations_delete, name='immunizations-delete'),

    # HealthDesign/2/add-medication/
    url(r'(?P<demographics_id>[0-9]+)/add-medication/$', views.medication_create, name='medication-add'),

    # HealthDesign/2/5/update-medication/
    url(r'(?P<demographics_id>[0-9]+)/(?P<medication_id>[0-9]+)/update-medication/$', views.medication_update, name='medication-update'),

    # HealthDesign/3/2/delete-medication/
    url(r'(?P<demographics_id>[0-9]+)/(?P<medication_id>[0-9]+)/delete-medication/$', views.medication_delete, name='medication-delete'),

    # HealthDesign/2/add-careplan/
    url(r'(?P<demographics_id>[0-9]+)/add-careplan/$', views.careplan_create, name='careplan-add'),

    # HealthDesign/2/6/update-careplan/
    url(r'(?P<demographics_id>[0-9]+)/(?P<careplan_id>[0-9]+)/update-careplan/$', views.careplan_update, name='careplan-update'),

    # HealthDesign/3/2/delete-careplan/
    url(r'(?P<demographics_id>[0-9]+)/(?P<careplan_id>[0-9]+)/delete-careplan/$', views.careplan_delete, name='careplan-delete'),

    # HealthDesign/2/add-encounters/
    url(r'(?P<demographics_id>[0-9]+)/add-encounters/$', views.encounters_create, name='encounters-add'),

    # HealthDesign/2/1/update-encounters/
    url(r'(?P<demographics_id>[0-9]+)/(?P<encounters_id>[0-9]+)/update-encounters/$', views.encounters_update, name='encounters-update'),

    # HealthDesign/3/2/delete-encounters/
    url(r'(?P<demographics_id>[0-9]+)/(?P<encounters_id>[0-9]+)/delete-encounters/$', views.encounters_delete, name='encounters-delete'),

    # HealthDesign/2/add-problemlist/
    url(r'(?P<demographics_id>[0-9]+)/add-problemlist/$', views.problemlist_create, name='problemlist-add'),

    # HealthDesign/2/2/update-problemlist/
    url(r'(?P<demographics_id>[0-9]+)/(?P<problemlist_id>[0-9]+)/update-problemlist/$', views.problemlist_update, name='problemlist-update'),

    # HealthDesign/3/2/delete-problemlist/
    url(r'(?P<demographics_id>[0-9]+)/(?P<problemlist_id>[0-9]+)/delete-problemlist/$', views.problemlist_delete, name='problemlist-delete'),

    # HealthDesign/2/add-procedures/
    url(r'(?P<demographics_id>[0-9]+)/add-procedures/$', views.procedures_create, name='procedures-add'),

    # HealthDesign/2/1/update-procedures/
    url(r'(?P<demographics_id>[0-9]+)/(?P<procedures_id>[0-9]+)/update-procedures/$', views.procedures_update, name='procedures-update'),

    # HealthDesign/3/2/delete-procedures/
    url(r'(?P<demographics_id>[0-9]+)/(?P<procedures_id>[0-9]+)/delete-procedures/$', views.procedures_delete, name='procedures-delete')
]
