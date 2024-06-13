from django.db import models

# Create your models here.

class hemnath(models.Model):
    STATUS_CHOICES = [
        ('work_completed', 'Work Completed -> LPO not yet received'),
        ('lpo_received', 'LPO received -> Work still pending'),
        ('not_invoiced', 'Not invoiced tasks'),
        ('invoiced', 'Invoiced tasks'),
    ]

    Area = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    EmailSubject = models.CharField(max_length=200)
    Client = models.CharField(max_length=200)
    Attention = models.CharField(max_length=200)
    SiteEng = models.CharField(max_length=200)
    ApprovedBy = models.CharField(max_length=200)
    registereddate = models.DateField()
    ApprovedDate = models.CharField(max_length=200)
    Approvedprice = models.CharField(max_length=200)
    QuotationRef = models.CharField(max_length=200)
    QTDate = models.CharField(max_length=200)
    UBSNo = models.CharField(max_length=200)
    property = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    Descriptions = models.CharField(max_length=200)
    AED = models.CharField(max_length=200)
    SRdate = models.CharField(max_length=200)
    LPO = models.CharField(max_length=200)
    LPORef = models.CharField(max_length=200)
    InvoiceRef = models.CharField(max_length=200)
    Invoice = models.CharField(max_length=200)
    REMARK = models.CharField(max_length=200)
    EmailLPO = models.CharField(max_length=200)
    Note = models.CharField(max_length=200)
    Status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=True,
        blank=True
    )
    
    
    def __str__(self) -> str:
        return super().__str__()