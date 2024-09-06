from django.db import models


class Application(models.Model):
    EMPLOYMENT_CHOICE = [
        ('',''),
        ('self_employed', 'self_employed'),
        ('salaried', 'salaried')
    ]
    BUSINESS_TYPE = [
        ('',''),
        ('manufacturing', 'manufacturing'),
        ('service', 'service'),
        ('trading', 'trading')
    ]
    APPLICATION_STATUS = [
        ('',''),
        ('generated', 'generated'),
        ('document_verified', 'document_verified'),
        ('sanctioned', 'sanctioned'),
        ('disbursed', 'disbursed'),
        ('rejected', 'rejected')
    ]

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='applications')
    aadhaar_no = models.CharField(max_length=12, default=0, blank=True)
    pan_no = models.CharField(max_length=10, default=0, blank=True)
    type_of_employment = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICE, default=0, blank=True)
    business_title = models.CharField(max_length=250, default=0, blank=True)
    business_type = models.CharField(max_length=250, choices=BUSINESS_TYPE, default=0, blank=True)
    business_address = models.TextField(default=0, blank=True)
    gst_registration_no = models.CharField(max_length=50, default=0, blank=True)
    business_license_no = models.CharField(max_length=50, default=0, blank=True)
    expected_average_annual_turnover = models.CharField(max_length=250, default=0, blank=True)
    years_in_current_business = models.IntegerField(default=0, blank=True)
    collateral = models.CharField(max_length=250, default=0, blank=True)
    status = models.CharField(max_length=250, default='', choices=APPLICATION_STATUS)
    application_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)
    credit_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"
    

class Guarantor(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'fenale'),
        ('transgender', 'transgender')
    ]
    application = models.ForeignKey('application_generation.Application', on_delete=models.CASCADE, related_name='guarantors')
    relation_with_customer = models.CharField(max_length=250, default=0, blank=True)
    name = models.CharField(max_length=150, default=0, blank=True)
    dob= models.DateField(default="1992-12-12", blank=True)
    gender = models.CharField(max_length= 50, default=0, blank=True, choices=GENDER_CHOICES)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=250, default= 0, blank=True)
    city = models.CharField(max_length=50, default=0, blank=True)
    state = models.CharField(max_length = 50, default=0, blank=True)
    country = models.CharField(max_length=250, default= 0 , blank=True)
    pin_code = models.IntegerField(default = 0, blank=True)
    mobile = models.CharField(max_length=10, default=0, blank=True)
    photo = models.ImageField(upload_to='customer/guarantor/', default=0, blank=True)
    profession = models.CharField(max_length=250, default=0, blank=True)
    income_certificate = models.FileField(upload_to='customer/guarantor/', default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    current_account_no = models.CharField(max_length=20, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='customer/guarantor/', default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
        return f'{self.id}'


class Document(models.Model):
    DOCUMENT_STATUS_CHOICE = [ 
        ('', ''),
        ('pending', 'pending'),
        ('done', 'done'),
        ('rejected', 'rejected')
    ]

    application = models.OneToOneField('application_generation.Application', on_delete=models.CASCADE, related_name='documents')
    aadhaar_card = models.FileField(upload_to='customer/document/', default=0, blank=True) 
    pan_card = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_address_proof_or_copy_of_rent_agreement = models.FileField(upload_to='customer/document/', default=0, blank=True)
    electricity_bill = models.FileField(upload_to='customer/document/', default=0, blank=True)
    msme_certificate = models.FileField(upload_to='customer/document/', default=0, blank=True)
    gst_certificate = models.FileField(upload_to='customer/document/', default=0, blank=True)
    udyog_aadhaar_registration = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_license = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_plan_or_proposal = models.FileField(upload_to='customer/documents', default=0, blank=True )
    three_year_itr_with_balance_sheet = models.FileField(upload_to='customer/document/', default=0, blank=True)
    collateral_document = models.FileField(upload_to='customer/document/', default=0, blank=True)
    stamp_duty = models.FileField(upload_to='customer/document/', default=0, blank=True)
    status = models.CharField(max_length=250, choices=DOCUMENT_STATUS_CHOICE, default=0, blank=True)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        return f'{self.id}'