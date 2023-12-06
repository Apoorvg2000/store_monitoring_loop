"""
Admin registrations for the store monitoring application.
This file contains admin site registrations for model classes,
enabling Django's admin interface to handle these models.
"""

from django.contrib import admin
from .models import StoreReport, StoreStatusLog, StoreTimezone, StoreTiming

# Register your models here.

# The StoreReport model is registered with the admin site to enable administrators
# to manage report instances directly through the admin interface.
admin.site.register(StoreReport)
# The StoreTiming model is registered with the admin site to allow administrators
# to edit store timing details such as open and close times.
admin.site.register(StoreTiming)
# The StoreStatusLog model is registered to track changes in store status over time,
# providing admins with a historical view of store statuses.
admin.site.register(StoreStatusLog)
# The StoreTimezone model is registered with the admin site to manage timezone information
# for each store, ensuring accurate time-based data representation.
admin.site.register(StoreTimezone)

