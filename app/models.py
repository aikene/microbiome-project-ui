from django.db import models
from django.contrib.auth.models import AbstractUser

from awscicd import settings


# Create your models here.
class User(AbstractUser):

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return f"{self.email}"

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = 'app_user'


class History(models.Model):
    user_id = models.CharField(max_length=255)
    time_stamp = models.CharField(max_length=255)
    task_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'history'


class Metadata(models.Model):
    acc = models.TextField(unique=True, primary_key=True, verbose_name='Run ID')
    assay_type = models.TextField(blank=True, null=True)
    center_name = models.TextField(blank=True, null=True, verbose_name="Center Name")
    consent = models.TextField(blank=True, null=True)
    experiment = models.TextField(blank=True, null=True)
    sample_name = models.TextField(blank=True, null=True)
    instrument = models.TextField(blank=True, null=True)
    librarylayout = models.TextField(blank=True, null=True, verbose_name='Library Layout')
    libraryselection = models.TextField(blank=True, null=True)
    librarysource = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)
    sample_acc = models.TextField(blank=True, null=True)
    biosample = models.TextField(blank=True, null=True)
    organism = models.TextField(blank=True, null=True)
    sra_study = models.TextField(blank=True, null=True, verbose_name="SRA Study ID")
    releasedate = models.DateTimeField(blank=True, null=True)
    bioproject = models.TextField(blank=True, null=True)
    mbytes = models.IntegerField(blank=True, null=True)
    loaddate = models.TextField(blank=True, null=True)
    avgspotlen = models.IntegerField(blank=True, null=True)
    mbases = models.IntegerField(blank=True, null=True)
    library_name = models.TextField(blank=True, null=True)
    biosamplemodel_sam = models.TextField(blank=True, null=True)
    collection_date_sam = models.TextField(blank=True, null=True)
    geo_loc_name_country_calc = models.TextField(blank=True, null=True, verbose_name="Country")
    geo_loc_name_country_continent_calc = models.TextField(blank=True, null=True, verbose_name="Continent")
    geo_loc_name_sam = models.TextField(blank=True, null=True)
    ena_first_public_run = models.TextField(blank=True, null=True)
    ena_last_update_run = models.TextField(blank=True, null=True)
    sample_name_sam = models.TextField(blank=True, null=True)
    datastore_filetype = models.TextField(blank=True, null=True)
    jattr = models.TextField(blank=True, null=True)
    race_sam = models.TextField(blank=True, null=True)
    body_site_sam = models.TextField(blank=True, null=True)
    source_name_sam = models.TextField(blank=True, null=True)
    bytes = models.TextField(blank=True, null=True)
    tissue_sam = models.TextField(blank=True, null=True)
    cell_type_sam = models.TextField(blank=True, null=True)
    sex_calc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadata'


class Results(models.Model):
    acc = models.CharField(max_length=255)
    taxon = models.TextField(blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    abundance = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class Status(models.Model):
    acc = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'
