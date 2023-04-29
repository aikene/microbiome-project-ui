from import_export import resources
from .models import Metadata

class DataUploader(resources.ModelResource):   # <- added by nlandi
    class Meta:
        skip_unchanged = True
        model = Metadata
