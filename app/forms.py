from django import forms
from django_select2 import forms as s2forms

from . import models
from .common_models import Distinct_Library_Layout, Distinct_SRA, Distinct_Sex, Distinct_Library_Selection, \
    Distinct_Assay_Type, Center_Name, Experiment_Name, Sample_Acc, Biosample, Organism, Bioproject, Country, Continent, \
    BreedSample, CultivarSample, EcotypeSample, IsolateSample, StrainSample


class LibraryLayoutWidget(s2forms.ModelSelect2MultipleWidget):
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


class StrainSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = StrainSample.objects.all()
    search_fields = [
        "strain_sam__icontains"
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


class SexSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_Sex.objects.all()
    search_fields = [
        "gender__icontains"
    ]


class BreedSamWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = BreedSample.objects.all()
    search_fields = [
        "breed_sam__icontains"
    ]


class CultivarSamWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = CultivarSample.objects.all()
    search_fields = [
        "cultivar_sam__icontains"
    ]


class EcotypeSamWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = EcotypeSample.objects.all()
    search_fields = [
        "ecotype_sam__icontains"
    ]


class IsolateSamWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = IsolateSample.objects.all()
    search_fields = [
        "iosolate_sam__icontains"
    ]


class LibrarySelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_Library_Selection.objects.all()
    search_fields = [
        "libraryselection__icontains"
    ]


class MetadataForm(forms.ModelForm):
    librarylayout = forms.ModelMultipleChoiceField(
        label='Library Layout',
        required=False,
        queryset=Distinct_Library_Layout.objects.all(),
        widget=LibraryLayoutWidget(attrs={'data-placeholder': '"Single" and "Paired" are only options',
                                     "data-minimum-input-length": 0}),
        initial=Distinct_Library_Layout.objects.all(),
    )
    sra_study = s2forms.forms.ModelMultipleChoiceField(
        label='SRA Study',
        required=False,
        queryset=Distinct_SRA.objects.all(),
        widget=SRAStudyWidget(attrs={'data-placeholder': 'SRA Studies typically start with "SRP" or "ERP"',
                                     "data-minimum-input-length": 0}),
        initial=Distinct_SRA.objects.all()[:10],
    )
    center_name = forms.ModelMultipleChoiceField(
        label='Center Name',
        required=False,
        queryset=Center_Name.objects.all(),
        widget=CenterNameSelectionWidget(attrs={'data-placeholder': 'Example Center Name is "MIT"',
                                     "data-minimum-input-length": 0}),
        initial='UNIVERSITY OF CALIFORNIA SAN DIEGO MICROBIOME INIT'
    )
    experiment = forms.ModelMultipleChoiceField(
        label='Experiment ID',
        required=False,
        queryset=Experiment_Name.objects.all(),
        widget=ExperimentSelectionWidget(attrs={'data-placeholder': 'Experiments start with "SRX" or "ERX"',
                                     "data-minimum-input-length": 0}),
        initial='SRX2986493'
    )
    sample_acc = forms.ModelMultipleChoiceField(
        label='Sample Acc',
        required=False,
        queryset=Sample_Acc.objects.all(),
        widget=SampleAccSelectionWidget(attrs={'data-placeholder': 'Acc start with "SRS" or "ERS"',
                                     "data-minimum-input-length": 0}),
        initial='SRS8610790'
    )
    biosample = forms.ModelMultipleChoiceField(
        label='Bio Sample',
        required=False,
        queryset=Biosample.objects.all(),
        widget=BiosampleSelectionWidget(attrs={'data-placeholder': 'Biosample starts with "SAMEA" or "SAMN"',
                                     "data-minimum-input-length": 0}),
        initial='SAMN18350539'
    )
    organism = forms.ModelMultipleChoiceField(
        label='Organism',
        required=False,
        queryset=Organism.objects.all(),
        widget=OrganismSelectionWidget(attrs={'data-placeholder': 'Organisms include "oral", "skin", "gut"',
                                     "data-minimum-input-length": 0}),
        initial='metagenome'
    )
    bioproject = forms.ModelMultipleChoiceField(
        label='Bio Project',
        required=False,
        queryset=Bioproject.objects.all(),
        widget=BioprojectSelectionWidget(attrs={'data-placeholder': 'Bioprojects start with "PRJEB", "PRJN"',
                                     "data-minimum-input-length": 0}),
        initial='PRJEB36635'
    )
    geo_loc_name_country_calc = forms.ModelMultipleChoiceField(
        label='Country',
        required=False,
        queryset=Country.objects.all(),
        widget=CountrySelectionWidget(attrs={'data-placeholder': 'Countries...',
                                     "data-minimum-input-length": 0}),
        initial='USA'
    )
    geo_loc_name_country_continent_calc = forms.ModelMultipleChoiceField(
        label='Continent',
        required=False,
        queryset=Continent.objects.all(),
        widget=ContinentSelectionWidget(attrs={'data-placeholder': 'Continents...',
                                     "data-minimum-input-length": 0}),
        initial='North America'
    )
    gender = forms.ModelMultipleChoiceField(
        label='Sex',
        required=False,
        queryset=Distinct_Sex.objects.all(),
        widget=SexSelectionWidget(attrs={'data-placeholder': 'Sex fields include "male", "female"',
                                     "data-minimum-input-length": 0}),
        initial=['male', 'female']
    )
    breed_sam = forms.ModelMultipleChoiceField(
        label='Breed Sample',
        required=False,
        queryset=BreedSample.objects.all(),
        widget=BreedSamWidget(attrs={'data-placeholder': 'Breed fields include "Human", "unknown", "not applicable"',
                                     "data-minimum-input-length": 0}),
        initial='Human'
    )
    cultivar_sam = forms.ModelMultipleChoiceField(
        label='Cultivar Sample',
        required=False,
        queryset=CultivarSample.objects.all(),
        widget=CultivarSamWidget(attrs={'data-placeholder': '...',
                                     "data-minimum-input-length": 0}),
        initial='unknown'
    )
    ecotype_sam = forms.ModelMultipleChoiceField(
        label='Ecotype Sample',
        required=False,
        queryset=EcotypeSample.objects.all(),
        widget=EcotypeSamWidget(attrs={'data-placeholder': '...',
                                     "data-minimum-input-length": 0}),
        initial='unknown'
    )
    isolate_sam = forms.ModelMultipleChoiceField(
        label='Isolate Sample',
        required=False,
        queryset=IsolateSample.objects.all(),
        widget=IsolateSamWidget(attrs={'data-placeholder': 'Isolate fields include "Human", "stool", "oral cavity"',
                                     "data-minimum-input-length": 0}),
        initial='Bacteria'
    )
    libraryselection = forms.ModelMultipleChoiceField(
        label='Library Selection',
        required=False,
        queryset=Distinct_Library_Selection.objects.all(),
        widget=LibrarySelectionWidget(attrs={'data-placeholder': 'Library Selection fields include "PCR",'
                                                                 '"RT-PCR", "cDNA"',
                                     "data-minimum-input-length": 0}),
        initial='PCR'
    )
    strain_sam = forms.ModelMultipleChoiceField(
        label='Strain Sample',
        required=False,
        queryset=StrainSample.objects.all(),
        widget=StrainSelectionWidget(attrs={'data-placeholder': '...',
                                     "data-minimum-input-length": 0}),
        initial='complex microbiome'
    )

    class Meta:
        model = models.Metadata
        fields = ('librarylayout', 'sra_study', 'center_name', 'experiment', 'sample_acc', 'biosample',
                  'organism', 'bioproject', 'geo_loc_name_country_calc', 'geo_loc_name_country_continent_calc',
                  'gender', 'breed_sam', 'cultivar_sam', 'ecotype_sam', 'isolate_sam', 'libraryselection', 'strain_sam')
