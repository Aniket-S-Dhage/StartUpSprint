from django.db import models

class Defaulter(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='defaulters')
    default_amount = models.FloatField(default=0, blank=True)
    pending_since_date = models.DateField(default='2000-12-12', blank=True)

    def __str__(self):
        return f"{self.id}"
    

class Installment(models.Model):
    INSTALLMENT_CHOICES = {
        ('',''),
        ('ok','ok'),
        ('pending','pending'),
        ('late','late'),
    }
    loan = models.ForeignKey('loan_sanctioning.Loan', on_delete=models.CASCADE, related_name='installments')
    remaining_amount = models.FloatField(default=0.0, blank=True)
    installment_no = models.IntegerField(default=0, blank=True)
    monthly_installment_amount = models.FloatField(default=0.0, blank=True)
    installment_expected_date = models.DateField(default="2000-12-12", blank=True)
    installment_paid_date = models.DateField(default="2000-12-12", blank=True)
    penalty_amount = models.FloatField(default=0.0, blank=True)
    status = models.CharField(max_length=100, blank=True, choices=INSTALLMENT_CHOICES, default='pending')

    def __str__(self):
        return f"{self.id}"
    


class Disbursement(models.Model):

    PAYMENT_CHOICES = [
        ('',''),
        ('neft', 'neft'),
        ('rtgs', 'rtgs'),
        ('imps', 'imps'),
    ]
    DISBURSEMENT_CHOICES = [
        ('',''),
        ('pending', 'pending'),
        ('disbursed', 'disbursed'),
    ]
    loan = models.OneToOneField('loan_sanctioning.Loan', on_delete=models.CASCADE, related_name="disbursements")
    insurance_doc = models.FileField(upload_to='customer/disbursement', default=0, blank=True)
    payment_mode = models.CharField(max_length=250, default=0, blank=True, choices=PAYMENT_CHOICES)
    net_disbursed_amount = models.FloatField(default=0, blank=True)
    disbursed_to_account_no = models.CharField(max_length=25, default=0, blank=True)
    receipt_doc = models.FileField(upload_to='customer/disbursement', default=0, blank=True)
    status = models.CharField(max_length=250, default=0 , blank=True, choices=DISBURSEMENT_CHOICES)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.id}"