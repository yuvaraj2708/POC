from django.shortcuts import render,redirect,get_object_or_404
from .models import *
import csv
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import logout
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    # Custom logout logic here, if needed
    logout(request)
    return redirect('login')

@login_required
def index(request):
    if request.method == 'POST':  # Ensure the method is checked correctly
        Area = request.POST.get('Area')
        Category = request.POST.get('Category')
        EmailSubject = request.POST.get('EmailSubject')
        Client = request.POST.get('Client')
        Attention = request.POST.get('Attention')
        SiteEng = request.POST.get('SiteEng')
        ApprovedBy = request.POST.get('ApprovedBy')
        registereddate = request.POST.get('registereddate')
        ApprovedDate = request.POST.get('ApprovedDate')
        Approvedprice = request.POST.get('Approvedprice')
        QuotationRef = request.POST.get('QuotationRef')
        QTDate = request.POST.get('QTDate')
        UBSNo = request.POST.get('UBSNo')
        property = request.POST.get('property')
        unit = request.POST.get('unit')
        Descriptions = request.POST.get('Descriptions')
        AED = request.POST.get('AED')
        Status = request.POST.get('Status')
        SRdate = request.POST.get('SRdate')
        LPO = request.POST.get('LPO')
        LPORef = request.POST.get('LPORef')
        InvoiceRef = request.POST.get('InvoiceRef')
        Invoice = request.POST.get('Invoice')
        REMARK = request.POST.get('REMARK')
        EmailLPO = request.POST.get('EmailLPO')
        Note = request.POST.get('Note')

        # Save the data to the database
        new_entry = hemnath(
            Area=Area,
            Category=Category,
            EmailSubject=EmailSubject,
            Client=Client,
            Attention=Attention,
            SiteEng=SiteEng,
            ApprovedBy=ApprovedBy,
            registereddate=registereddate,
            ApprovedDate=ApprovedDate,
            Approvedprice=Approvedprice,
            QuotationRef=QuotationRef,
            QTDate=QTDate,
            UBSNo=UBSNo,
            property=property,
            unit=unit,
            Descriptions=Descriptions,
            AED=AED,
            Status=Status,
            SRdate=SRdate,
            LPO=LPO,
            LPORef=LPORef,
            InvoiceRef=InvoiceRef,
            Invoice=Invoice,
            REMARK=REMARK,
            EmailLPO=EmailLPO,
            Note=Note
        )
        new_entry.save()
        return redirect('viewdata')  # Redirect to a success page

    return render(request, 'index.html')

@login_required
def viewdata(request):
    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')

    # Retrieve all records if no filter is applied
    views = hemnath.objects.all()

    # Apply filters if from_date and to_date are provided
    if from_date_str and to_date_str:
        # Assuming the date format is 'YYYY-MM-DD'
        views = views.filter(registereddate__range=[from_date_str, to_date_str])

    return render(request, 'viewdata.html', {'views': views})

@login_required
def download_filtered_data(request):
    # Retrieve filter parameters from request
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    # Query your model with the filter parameters
    filtered_data = hemnath.objects.filter(registereddate__range=(from_date, to_date))

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filtered_data.csv"'

    # Write CSV headers
    writer = csv.writer(response)
    writer.writerow(['ID', 'Area', 'Category', 'Email Subject', 'Client', 'Attention', 'Site Eng', 'Approved By','Registered Date', 'Approved Date', 'Approved price.', 'Quotation Ref', 'QT Date', 'UBS No', 'Property', 'Unit', 'Descriptions', 'AED', 'Status', 'SR date', 'LPO', 'LPO Ref', 'Invoice Ref#', 'Invoice', 'REMARK', 'Email LPO', 'Note'])  # Add your column headers here

    # Write CSV rows
    for item in filtered_data:
        writer.writerow([item.id, item.Area, item.Category, item.EmailSubject, item.Client, item.Attention, item.SiteEng, item.ApprovedBy, item.registereddate, item.ApprovedDate, item.Approvedprice, item.QuotationRef, item.QTDate, item.UBSNo, item.property, item.unit, item.Descriptions, item.AED, item.Status, item.SRdate, item.LPO, item.LPORef, item.InvoiceRef, item.Invoice, item.REMARK, item.EmailLPO, item.Note])  # Add your fields here

    return response



@login_required
def edit_view(request, id):
    Hemnath = get_object_or_404(hemnath, id=id)
    if request.method == 'POST':
        Hemnath.Area = request.POST.get('Area')
        Hemnath.Category = request.POST.get('Category')
        Hemnath.EmailSubject = request.POST.get('EmailSubject')
        Hemnath.Client = request.POST.get('Client')
        Hemnath.Attention = request.POST.get('Attention')
        Hemnath.SiteEng = request.POST.get('SiteEng')
        Hemnath.ApprovedBy = request.POST.get('ApprovedBy')
        Hemnath.registereddate = request.POST.get('registereddate')
        Hemnath.ApprovedDate = request.POST.get('ApprovedDate')
        Hemnath.Approvedprice = request.POST.get('Approvedprice')
        Hemnath.QuotationRef = request.POST.get('QuotationRef')
        Hemnath.QTDate = request.POST.get('QTDate')
        Hemnath.UBSNo = request.POST.get('UBSNo')
        Hemnath.property = request.POST.get('property')
        Hemnath.unit = request.POST.get('unit')
        Hemnath.Descriptions = request.POST.get('Descriptions')
        Hemnath.AED = request.POST.get('AED')
        Hemnath.Status = request.POST.get('Status')
        Hemnath.SRdate = request.POST.get('SRdate')
        Hemnath.LPO = request.POST.get('LPO')
        Hemnath.LPORef = request.POST.get('LPORef')
        Hemnath.InvoiceRef = request.POST.get('InvoiceRef')
        Hemnath.Invoice = request.POST.get('Invoice')
        Hemnath.REMARK = request.POST.get('REMARK')
        Hemnath.EmailLPO = request.POST.get('EmailLPO')
        Hemnath.Note = request.POST.get('Note')
        Hemnath.save()
        return redirect('index')

    return render(request, 'edit.html', {'Hemnath': Hemnath})

@login_required
def delete_view(request, id):
    Hemnath = get_object_or_404(hemnath, id=id)
    if request.method == 'POST':
        Hemnath.delete()
        return redirect('index')
    return render(request, 'delete.html', {'Hemnath': Hemnath})

@login_required
def work_completed(request):
    work_completed_data = hemnath.objects.filter(Status='work_completed')
    return render(request, 'work_completed.html', {'work_completed_data': work_completed_data})

@login_required
def lpo_received(request):
    lpo_received_data = hemnath.objects.filter(Status='lpo_received')
    return render(request, 'lpo_received.html', {'lpo_received_data': lpo_received_data})

@login_required
def not_invoiced_tasks(request):
    not_invoiced_data = hemnath.objects.filter(Status='not_invoiced')
    return render(request, 'not_invoiced_tasks.html', {'not_invoiced_data': not_invoiced_data})

@login_required
def invoiced_tasks(request):
    invoiced_data = hemnath.objects.filter(Status='invoiced')
    return render(request, 'invoiced_tasks.html', {'invoiced_data': invoiced_data})