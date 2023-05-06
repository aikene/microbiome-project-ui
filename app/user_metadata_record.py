class UserMetadataRecord:
    def __init__(self, run_id):
        self.run_id = run_id                # Run ID (Acc)
        self.contents = None                # Contents dictionary
        self.forward_fastq = None           # File name w/o extension
        self.forward_fastq_f_name = None    # File name with extension
        self.forward_fastq_file = None      # File object
        self.reverse_fastq = None           # File name w/o extension
        self.reverse_fastq_f_name = None    # File name with extension
        self.reverse_fastq_file = None      # File object
