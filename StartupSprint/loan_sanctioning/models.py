from django.db import models

class Loan(models.Model):
    LOAN_STATUS_CHOICE = [
        ('',''),
        ('pending', 'pending'),
        ('done', 'done'),
        ('rejected', 'rejected'),
    ]
    application = models.OneToOneField('application_generation.Application', on_delete=models.CASCADE, related_name='Loans')
    loan_principal_amount = models.FloatField(default=0, blank=True)
    loan_tenure = models.FloatField(default=0, blank=True),
    interest_rate = models.FloatField(default=0, blank=True)
    total_amount_and_processing_fees = models.FloatField(default=0, blank=True)
    installment = models.IntegerField(default=0, blank=True)
    maturity_date = models.DateField(default="2000-12-12", blank=True)
    sanction_letter = models.FileField(upload_to='customer/loan/', default=0, blank=True)
    status = models.CharField(max_length=250, choices=LOAN_STATUS_CHOICE, default=0, blank=True)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        return f"self.id"
    

class Vendor(models.Model):
    application = models.ForeignKey('application_generation.Application', on_delete=models.CASCADE, related_name="Vendors")
    name= models.CharField(max_length=250, default=0, blank=True)
    vendor_type = models.CharField(max_length=250, default=0, blank=True)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=25, default=0, blank=True)
    city = models.CharField(max_length=250, default=0, blank=True)
    state = models.CharField(max_length=250, default=0, blank=True)
    country = models.CharField(max_length=250, default=0, blank=True)
    pin_code = models.IntegerField(default=0, blank=True) 
    mobile = models.CharField(max_length=10, default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='customer/vendor/', default=0, blank=True) 
    current_account_no = models.CharField(max_length=25, default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
        return f"{self.id}"

class Transaction(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=200, verbose_name='Signature', blank=True, null=True)
    transaction_by = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name="user_transactions", blank=True, null=True) 
    transaction_time = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=20)
    loan = models.ForeignKey(Loan, on_delete=models.DO_NOTHING, related_name="loan_transactions")