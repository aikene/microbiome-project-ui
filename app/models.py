import os.path

from django.db import models
from django.contrib.auth.models import AbstractUser

from awscicd.settings import S3_PRIVATE_STUDIES_PATH

from awscicd import settings


class User(AbstractUser):
    email_notification = models.BooleanField(default=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return f"{self.email}"

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = 'app_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class History(models.Model):
    user_id = models.CharField(max_length=255)
    time_stamp = models.CharField(max_length=255)
    bioproject = models.TextField(blank=True, null=True)
    biosample = models.TextField(blank=True, null=True)
    breed_sam = models.TextField(blank=True, null=True)
    center_name = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    continent = models.TextField(blank=True, null=True)
    cultivar_sam = models.TextField(blank=True, null=True)
    ecotype_sam = models.TextField(blank=True, null=True)
    experiment = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    isolate_sam = models.TextField(blank=True, null=True)
    library_layout = models.TextField(blank=True, null=True)
    library_selection = models.TextField(blank=True, null=True)
    organism = models.TextField(blank=True, null=True)
    sample_acc = models.TextField(blank=True, null=True)
    sra_study = models.TextField(blank=True, null=True)
    strain_sam = models.TextField(blank=True, null=True)
    search_id = models.AutoField(primary_key=True)
    only_processed_studies = models.BooleanField()
    include_sra_studies = models.BooleanField()
    include_private_studies = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'history'


class Metadata(models.Model):
    acc = models.TextField(primary_key=True)
    assay_type = models.TextField(blank=True, null=True)
    center_name = models.TextField(blank=True, null=True)
    consent = models.TextField(blank=True, null=True)
    experiment = models.TextField(blank=True, null=True)
    sample_name = models.TextField(blank=True, null=True)
    instrument = models.TextField(blank=True, null=True)
    librarylayout = models.TextField(blank=True, null=True)
    libraryselection = models.TextField(blank=True, null=True)
    librarysource = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)
    sample_acc = models.TextField(blank=True, null=True)
    biosample = models.TextField(blank=True, null=True)
    organism = models.TextField(blank=True, null=True)
    sra_study = models.TextField(blank=True, null=True)
    releasedate = models.DateTimeField(blank=True, null=True)
    bioproject = models.TextField(blank=True, null=True)
    mbytes = models.IntegerField(blank=True, null=True)
    loaddate = models.TextField(blank=True, null=True)
    avgspotlen = models.IntegerField(blank=True, null=True)
    mbases = models.IntegerField(blank=True, null=True)
    library_name = models.TextField(blank=True, null=True)
    biosamplemodel_sam = models.TextField(blank=True, null=True)
    collection_date_sam = models.TextField(blank=True, null=True)
    geo_loc_name_country_calc = models.TextField(blank=True, null=True)
    geo_loc_name_country_continent_calc = models.TextField(blank=True, null=True)
    geo_loc_name_sam = models.TextField(blank=True, null=True)
    ena_first_public_run = models.TextField(blank=True, null=True)
    ena_last_update_run = models.TextField(blank=True, null=True)
    sample_name_sam = models.TextField(blank=True, null=True)
    datastore_filetype = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    jattr = models.TextField(blank=True, null=True)
    description_sam = models.TextField(blank=True, null=True)
    treatment_sam = models.TextField(blank=True, null=True)
    sample_type_sam = models.TextField(blank=True, null=True)
    isolation_source_sam = models.TextField(blank=True, null=True)
    health_state_sam = models.TextField(blank=True, null=True)
    genotype_sam = models.TextField(blank=True, null=True)
    disease_stage_sam = models.TextField(blank=True, null=True)
    disease_sam = models.TextField(blank=True, null=True)
    cell_type_sam = models.TextField(blank=True, null=True)
    birth_location_sam = models.TextField(blank=True, null=True)
    tissue_sam = models.TextField(blank=True, null=True)
    dev_stage_sam = models.TextField(blank=True, null=True)
    age_sam = models.TextField(blank=True, null=True)
    ecotype_sam = models.TextField(blank=True, null=True)
    cultivar_sam = models.TextField(blank=True, null=True)
    breed_sam = models.TextField(blank=True, null=True)
    strain_sam = models.TextField(blank=True, null=True)
    isolate_sam = models.TextField(blank=True, null=True)
    race_ethnicity = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadata'


class PostProcessorStudy(models.Model):
    id = models.TextField(primary_key=True)
    library_layout = models.CharField(max_length=100)
    feature_table_path = models.TextField()
    taxonomy_results_path = models.TextField()

    class Meta:
        managed = False
        db_table = 'post_processor_study'


class Results(models.Model):
    result_id = models.AutoField(primary_key=True)
    acc = models.CharField(max_length=255)
    taxon = models.CharField(max_length=1024, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    abundance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class Status(models.Model):
    acc = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_notification = models.BooleanField()
    public = models.BooleanField()
    status = models.SmallIntegerField()
    output_path = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status'
