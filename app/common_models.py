from django.db import models


class Distinct_Sex(models.Model):
    sex_calc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sex_calc_view'


class Distinct_Library_Layout(models.Model):
    librarylayout = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_layout_view'


class Distinct_Library_Selection(models.Model):
    libraryselection = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_selection_view'


class Distinct_SRA(models.Model):
    sra_study = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sra_view'


class Center_Name(models.Model):
    center_name = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'center_name_view'


class Distinct_Assay_Type(models.Model):
    sra_study = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sra_view'


class Experiment_Name(models.Model):
    experiment = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experiment_name_view'


class Sample_Acc(models.Model):
    sample_acc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sample_acc_view'


class Biosample(models.Model):
    biosample = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'biosample_view'


class Organism(models.Model):
    organism = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organism_view'


class Bioproject(models.Model):
    bioproject = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bioproject_view'


class Country(models.Model):
    geo_loc_name_country_calc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'country_view'


class Continent(models.Model):
    geo_loc_name_country_continent_calc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'continent_view'


class BreedSample(models.Model):
    breed_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'breed_sam_view'


class CultivarSample(models.Model):
    cultivar_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cultivar_sam_view'


class EcotypeSample(models.Model):
    ecotype_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecotype_sam_view'


class IsolateSample(models.Model):
    iosolate_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iosolate_sam_view'


class StrainSample(models.Model):
    strain_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'strain_sam_view'
