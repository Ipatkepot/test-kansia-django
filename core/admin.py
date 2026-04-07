from django.contrib import admin
from .models import Job, Department, Employee, JobHistory

# Daftarkan semua model biar muncul di dashboard admin
admin.site.register(Job)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(JobHistory)