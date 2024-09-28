from django.contrib import admin
from feedback_and_queries.models import FeedBack
# Register your models here.


@admin.register(FeedBack)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','ratings','feedback_text']
