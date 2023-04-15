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


