from django.shortcuts import render
from django.db.models import Min, Max, Q
from .models import Employee, JobHistory, Department


def home(request):
    return render(request, 'home.html')


def pola_bintang_page(request):
    n_input = request.GET.get('n')
    result = []
    if n_input and n_input.isdigit():
        n = int(n_input)
        for i in range(n):
            row = ""
            for j in range(n):
                if i == j or i + j == n - 1:
                    row += "*"
                else:
                    row += " "
            result.append(row)
    return render(request, 'bintang.html', {'result': result, 'n': n_input})

def report_karyawan_page(request):
    dept_id = request.GET.get('dept_id')
    emp_id = request.GET.get('emp_id')
    
    context = {}

  
    if emp_id:
        context['riwayat'] = JobHistory.objects.filter(employee_id=emp_id).select_related('job', 'employee')

  
    if dept_id:
    
        stats = Employee.objects.filter(department_id=dept_id).aggregate(low=Min('salary'), high=Max('salary'))
        context['stats'] = stats
        
       
        context['pegawai_khusus'] = Employee.objects.filter(
            department_id=dept_id
        ).filter(
            Q(salary=stats['low']) | Q(salary=stats['high'])
        ).select_related('job', 'department')

    return render(request, 'report.html', context)