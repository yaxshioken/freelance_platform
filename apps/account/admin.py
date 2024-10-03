from django.contrib import admin

from apps.account.models import Account, AccountInfo, Notifications


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_filter = ('is_active','role')
    list_display = ('username','phone','is_active')
    search_fields = ('username','phone')
@admin.register(AccountInfo)
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ('id','bio','profession','technologies','account','is_visible')
    list_filter = ('is_visible',)
    search_fields = ('technologies','profession','account')

@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id','message','is_read','type','account','url')
    list_filter = ('is_read','type')


