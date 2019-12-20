from django.contrib import admin
from .models import B_User, B_Manager, B_Zone, B_Section, B_Topic2Tag, B_Topic, B_Comment , B_Integral, B_Tag, B_Up


# Register your models here.

admin.site.register(B_User)
admin.site.register(B_Manager)
admin.site.register(B_Zone)
admin.site.register(B_Section)
admin.site.register(B_Topic)
admin.site.register(B_Comment)
admin.site.register(B_Tag)

