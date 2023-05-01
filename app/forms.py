from django import forms
from django_select2 import forms as s2forms

from . import models
from .common_models import Distinct_Library_Layout, Distinct_SRA, Distinct_Sex, Distinct_Library_Selection, \
    Distinct_Assay_Type, Center_Name, Experiment_Name, Sample_Acc, Biosample, Organism, Bioproject, Country, Continent, \
    BreedSample, CultivarSample, EcotypeSample, IsolateSample, StrainSample


class LibraryLayoutWidget(s2forms.Select2MultipleWidget):
    queryset = Distinct_Library_Layout.objects.all().order_by('librarylayout')
    search_fields = [
        "librarylayout__icontains"
    ]


class SRAStudyWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_SRA.objects.all().order_by('sra_study')
    search_fields = [
        "sra_study__icontains"
    ]


class LibrarySelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Distinct_Library_Layout.objects.all()
    search_fields = [
        "librarylayout__icontains"
    ]


class CenterNameSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Center_Name.objects.all().order_by('center_name')
    search_fields = [
        "center_name__icontains"
    ]


class AccSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = models.Metadata.objects.all().order_by('acc')
    search_fields = [
        "acc__icontains"
    ]


class ExperimentSelectionWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Experiment_Name.objects.all().order_by('experiment')
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
        "isolate_sam__icontains"
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
    )
    sra_study = s2forms.forms.ModelMultipleChoiceField(
        label='SRA Study',
        required=False,
        queryset=Distinct_SRA.objects.all(),
        widget=SRAStudyWidget(attrs={'data-placeholder': '...starts with "SRP" or "ERP"',
                                     "data-minimum-input-length": 0}),
    )
    center_name = forms.ModelMultipleChoiceField(
        label='Center Name',
        required=False,
        queryset=Center_Name.objects.all(),
        widget=CenterNameSelectionWidget(attrs={'data-placeholder': '"Harvard University", "MIT"',
                                                "data-minimum-input-length": 0}),
    )
    experiment = forms.ModelMultipleChoiceField(
        label='Experiment ID',
        required=False,
        queryset=Experiment_Name.objects.all(),
        widget=ExperimentSelectionWidget(attrs={'data-placeholder': '...starts with "SRX" or "ERX"',
                                                "data-minimum-input-length": 0}),
    )
    sample_acc = forms.ModelMultipleChoiceField(
        label='Sample Acc',
        required=False,
        queryset=Sample_Acc.objects.all(),
        widget=SampleAccSelectionWidget(attrs={'data-placeholder': '...starts with "SRS" or "ERS"',
                                               "data-minimum-input-length": 0}),
    )
    biosample = forms.ModelMultipleChoiceField(
        label='Bio Sample',
        required=False,
        queryset=Biosample.objects.all(),
        widget=BiosampleSelectionWidget(attrs={'data-placeholder': '... starts with "SAMEA" or "SAMN"',
                                               "data-minimum-input-length": 0}),
    )
    organism = forms.ModelMultipleChoiceField(
        label='Organism',
        required=False,
        queryset=Organism.objects.all(),
        widget=OrganismSelectionWidget(attrs={'data-placeholder': '"oral", "skin", "gut"',
                                              "data-minimum-input-length": 0}),
    )
    bioproject = forms.ModelMultipleChoiceField(
        label='Bio Project',
        required=False,
        queryset=Bioproject.objects.all(),
        widget=BioprojectSelectionWidget(attrs={'data-placeholder': '...starts with "PRJEB", "PRJN"',
                                                "data-minimum-input-length": 0}),
    )
    geo_loc_name_country_calc = forms.ModelMultipleChoiceField(
        label='Country',
        required=False,
        queryset=Country.objects.all(),
        widget=CountrySelectionWidget(attrs={'data-placeholder': '"USA", "Japan"',
                                             "data-minimum-input-length": 0}),
    )
    geo_loc_name_country_continent_calc = forms.ModelMultipleChoiceField(
        label='Continent',
        required=False,
        queryset=Continent.objects.all(),
        widget=ContinentSelectionWidget(attrs={'data-placeholder': '"North America", "Oceania"',
                                               "data-minimum-input-length": 0}),
    )
    gender = forms.ModelMultipleChoiceField(
        label='Sex',
        required=False,
        queryset=Distinct_Sex.objects.all(),
        widget=SexSelectionWidget(attrs={'data-placeholder': '"male", "female" are only options',
                                         "data-minimum-input-length": 0}),
    )
    breed_sam = forms.ModelMultipleChoiceField(
        label='Breed Sample',
        required=False,
        queryset=BreedSample.objects.all(),
        widget=BreedSamWidget(attrs={'data-placeholder': '"Human", "unknown", "not applicable"',
                                     "data-minimum-input-length": 0}),
    )
    cultivar_sam = forms.ModelMultipleChoiceField(
        label='Cultivar Sample',
        required=False,
        queryset=CultivarSample.objects.all(),
        widget=CultivarSamWidget(attrs={'data-placeholder': 'unknown is the most common option',
                                        "data-minimum-input-length": 0}),
    )
    ecotype_sam = forms.ModelMultipleChoiceField(
        label='Ecotype Sample',
        required=False,
        queryset=EcotypeSample.objects.all(),
        widget=EcotypeSamWidget(attrs={'data-placeholder': 'unknown is the most common option',
                                       "data-minimum-input-length": 0}),
    )
    isolate_sam = forms.ModelMultipleChoiceField(
        label='Isolate Sample',
        required=False,
        queryset=IsolateSample.objects.all(),
        widget=IsolateSamWidget(attrs={'data-placeholder': '"Human", "stool", "oral cavity"',
                                       "data-minimum-input-length": 0}),
    )
    libraryselection = forms.ModelMultipleChoiceField(
        label='Library Selection',
        required=False,
        queryset=Distinct_Library_Selection.objects.all(),
        widget=LibrarySelectionWidget(attrs={'data-placeholder': '"PCR", "RT-PCR", "cDNA"',
                                             "data-minimum-input-length": 0}),
    )
    strain_sam = forms.ModelMultipleChoiceField(
        label='Strain Sample',
        required=False,
        queryset=StrainSample.objects.all(),
        widget=StrainSelectionWidget(attrs={'data-placeholder': 'unknown is the most common field',
                                            "data-minimum-input-length": 0}),
    )

    only_processed_studies = forms.BooleanField(
        label='Include only processed studies',
        required=False,
        label_suffix="",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    include_sra_studies = forms.BooleanField(
        label='Include SRA studies',
        required=False,
        initial=True,
        label_suffix="",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    include_private_studies = forms.BooleanField(
        label='Include my private studies',
        required=False,
        initial=True,
        label_suffix="",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = models.Metadata
        fields = ('librarylayout', 'sra_study', 'center_name', 'experiment', 'sample_acc', 'biosample',
                  'organism', 'bioproject', 'geo_loc_name_country_calc', 'geo_loc_name_country_continent_calc',
                  'gender', 'breed_sam', 'cultivar_sam', 'ecotype_sam', 'isolate_sam', 'libraryselection',
                  'strain_sam', 'only_processed_studies', 'include_sra_studies', 'include_private_studies')
