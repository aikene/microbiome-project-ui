from django import forms
from django_select2 import forms as s2forms

from . import models
from .common_models import Distinct_Library_Layout, Distinct_SRA, Distinct_Sex, Distinct_Library_Selection, \
    Distinct_Assay_Type, Center_Name, Experiment_Name, Sample_Acc, Biosample, Organism, Bioproject, Country, \
    Continent


# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Upload
#         fields = ('file', 'uploaded_at', )


class LibraryLayoutWidget(s2forms.Select2MultipleWidget):
    queryset = Distinct_Library_Layout.objects.all()
    search_fields = [
        "librarylayout__icontains"
    ]


class SRAStudyWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_SRA.objects.all()
    search_fields = [
        "sra_study__icontains"
    ]


class LibrarySelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_Library_Layout.objects.all()
    search_fields = [
        "librarylayout__icontains"
    ]


class CenterNameSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Center_Name.objects.all()
    search_fields = [
        "center_name__icontains"
    ]


class AccSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = models.Metadata.objects.all()
    search_fields = [
        "acc__icontains"
    ]


class ExperimentSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Experiment_Name.objects.all()
    search_fields = [
        "experiment__icontains"
    ]


class SampleAccSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Sample_Acc.objects.all()
    search_fields = [
        "sample_acc__icontains"
    ]


class BiosampleSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Biosample.objects.all()
    search_fields = [
        "biosample__icontains"
    ]


class OrganismSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Organism.objects.all()
    search_fields = [
        "organism__icontains"
    ]


class BioprojectSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Bioproject.objects.all()
    search_fields = [
        "bioproject__icontains"
    ]


class CountrySelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Country.objects.all()
    search_fields = [
        "geo_loc_name_country_calc__icontains"
    ]


class ContinentSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Continent.objects.all()
    search_fields = [
        "geo_loc_name_country_continent_calc__icontains"
    ]


class MetadataForm(forms.ModelForm):
    librarylayout = forms.ModelMultipleChoiceField(
        label='Library Layout',
        required=False,
        queryset=Distinct_Library_Layout.objects.all(),
        widget=LibraryLayoutWidget(),
        # initial=Distinct_Library_Layout.objects.all(),
    )
    sra_study = forms.ModelMultipleChoiceField(
        label='SRA Study',
        required=False,
        queryset=Distinct_SRA.objects.all(),
        widget=SRAStudyWidget,
        # initial='DRP000316'
    )
    center_name = forms.ModelMultipleChoiceField(
        label='Center Name',
        required=False,
        queryset=Center_Name.objects.all(),
        widget=CenterNameSelectionWidget,
        # initial='UNIVERSITY OF CALIFORNIA SAN DIEGO MICROBIOME INIT'
    )
    experiment = forms.ModelMultipleChoiceField(
        label='Experiment ID',
        required=False,
        queryset=Experiment_Name.objects.all(),
        widget=ExperimentSelectionWidget,
        # initial='SRX2986493'
    )
    sample_acc = forms.ModelMultipleChoiceField(
        label='Sample Acc',
        required=False,
        queryset=Sample_Acc.objects.all(),
        widget=SampleAccSelectionWidget,
        # initial='SRS8610790'
    )
    biosample = forms.ModelMultipleChoiceField(
        label='Bio Sample',
        required=False,
        queryset=Biosample.objects.all(),
        widget=BiosampleSelectionWidget,
        # initial='SAMN18350539'
    )
    organism = forms.ModelMultipleChoiceField(
        label='Organism',
        required=False,
        queryset=Organism.objects.all(),
        widget=OrganismSelectionWidget,
        # initial='metagenome'
    )
    bioproject = forms.ModelMultipleChoiceField(
        label='Bio Project',
        required=False,
        queryset=Bioproject.objects.all(),
        widget=BioprojectSelectionWidget,
        # initial='PRJEB36635'
    )
    geo_loc_name_country_calc = forms.ModelMultipleChoiceField(
        label='Country',
        required=False,
        queryset=Country.objects.all(),
        widget=CountrySelectionWidget,
        # initial='USA'
    )
    geo_loc_name_country_continent_calc = forms.ModelMultipleChoiceField(
        label='Continent',
        required=False,
        queryset=Continent.objects.all(),
        widget=ContinentSelectionWidget,
        # initial='North America'
    )

    class Meta:
        model = models.Metadata
        fields = ('librarylayout', 'sra_study', 'center_name', 'experiment', 'sample_acc', 'biosample',
                  'organism', 'bioproject', 'geo_loc_name_country_calc', 'geo_loc_name_country_continent_calc')
