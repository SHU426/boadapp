from django.contrib import admin

from board.models import SredModel
from .models import SredModel,Sred_msg_post
# Register your models here.
class SredMsgList(admin.StackedInline):
    model = Sred_msg_post
    extra = 5

class SredAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [SredMsgList]

    list_display = ('id','title','created_at')

admin.site.register(SredModel,SredAdmin)