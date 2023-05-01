from django.db import models


class Distinct_Gender(models.Model):
    gender = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gender_view'

    def __str__(self):
        return self.gender or ''


class Distinct_Library_Layout(models.Model):
    librarylayout = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_layout_view'

    def __str__(self):
        return self.librarylayout or ''

class Distinct_Library_Selection(models.Model):
    libraryselection = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_selection_view'

    def __str__(self):
        return self.libraryselection or ''


class Distinct_SRA(models.Model):
    sra_study = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sra_view'

    def __str__(self):
        return self.sra_study or ''


class Center_Name(models.Model):
    center_name = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'center_name_view'

    def __str__(self):
        return self.center_name or ''


class Distinct_Assay_Type(models.Model):
    sra_study = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sra_view'

    def __str__(self):
        return self.sra_study or ''


class Experiment_Name(models.Model):
    experiment = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experiment_name_view'

    def __str__(self):
        return self.experiment or ''


class Sample_Acc(models.Model):
    sample_acc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sample_acc_view'

    def __str__(self):
        return self.sample_acc or ''


class Biosample(models.Model):
    biosample = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'biosample_view'

    def __str__(self):
        return self.biosample or ''


class Organism(models.Model):
    organism = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organism_view'

    def __str__(self):
        return self.organism or ''


class Bioproject(models.Model):
    bioproject = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bioproject_view'

    def __str__(self):
        return self.bioproject or ''


class Country(models.Model):
    geo_loc_name_country_calc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'country_view'

    def __str__(self):
        return self.geo_loc_name_country_calc or ''


class Continent(models.Model):
    geo_loc_name_country_continent_calc = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'continent_view'

    def __str__(self):
        return self.geo_loc_name_country_continent_calc or ''


class BreedSample(models.Model):
    breed_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'breed_sam_view'

    def __str__(self):
        return self.breed_sam or ''


class CultivarSample(models.Model):
    cultivar_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cultivar_sam_view'

    def __str__(self):
        return self.cultivar_sam or ''


class EcotypeSample(models.Model):
    ecotype_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecotype_sam_view'

    def __str__(self):
        return self.ecotype_sam or ''


class IsolateSample(models.Model):
    isolate_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'isolate_sam_view'

    def __str__(self):
        return self.isolate_sam or ''


class StrainSample(models.Model):
    strain_sam = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'strain_sam_view'

    def __str__(self):
        return self.strain_sam or ''
