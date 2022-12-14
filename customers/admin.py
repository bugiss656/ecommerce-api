from django.contrib import admin
from .models import (
    CustomerProfile,
    Address
)


admin.site.register(CustomerProfile)
admin.site.register(Address)