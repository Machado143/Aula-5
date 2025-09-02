from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Farmacia.urls')),
]
=======
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Farmacia.urls')),
]
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
