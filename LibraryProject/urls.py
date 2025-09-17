path('relationship_app/', include('relationship_app.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]
