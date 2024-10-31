from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Home view that doesn't require login
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, "Thank you for your message!")
        return redirect('home')
    return render(request, 'contact.html')

def reporting_form(request):
    return render(request, 'reporting_form.html')

def submit_report(request):
    if request.method == 'POST':
        sales_figures = request.POST.get('salesFigures')
        region = request.POST.get('region')
        products = request.POST.get('products')

        if not sales_figures or not region or not products:
            messages.error(request, "Please fill in all fields.")
            return redirect('reporting_form')

        # Store report data temporarily in session
        if 'reports' not in request.session:
            request.session['reports'] = []
        
        request.session['reports'].append({
            'sales_figures': sales_figures,
            'region': region,
            'products': products
        })
        request.session.modified = True  # Ensure session is saved
        messages.success(request, "Report submitted successfully!")
        return redirect('dashboard')

    return HttpResponse("Method not allowed", status=405)

def dashboard(request):
    # Retrieve reports from session
    reports = request.session.get('reports', [])
    return render(request, 'dashboard.html', {'reports': reports})

def sales_data(request):
    """Return sales data in JSON format."""
    sales_data = request.session.get('reports', [])
    return JsonResponse({'sales_data': sales_data})
