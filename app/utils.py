import csv
import logging
import os
import shutil
import copy

logger = logging.getLogger('django')

from .user_metadata_record import UserMetadataRecord

from django.core.files.storage import FileSystemStorage


def validate_password(password):
    min_length = 8

    if len(password) < min_length:
        return False, f'Your password must be at least {min_length} characters long.'

    if password.isnumeric():
        return False, f'Your password cannot be entirely numeric.'

    return True, 'Your password has been updated successfully.'


def stringify_list(lst):
    if lst is None:
        return None

    return ','.join(lst)


def convert_str_to_list(str):
    return str.split(',')


def update_session_list(request,key, runId, add=1):
    # Get the session variable
    session_list = request.session.get(key, [])

    # Check if the input runId value is in the list
    if runId in session_list:
        # Remove the input runId value from the list
        if add == 0:
            session_list.remove(runId)
    else:
        # Add the input runId value to the list
        if add == 1:
            session_list.append(runId)

    # Update the session variable
    request.session[key] = session_list


def clear_session_list(request,key):
    request.session[key] = []
        

def populate_user_metadata_records(fastq_files, metadata_records, previous_run_ids):
    fastq_files_copy = {key: value for key, value in fastq_files.items()}
    for metadata_record in metadata_records:

        library_layout = metadata_record.contents.get('Library Layout', '').upper()
        if library_layout != 'SINGLE' and library_layout != 'PAIRED':
            success = False
            msg = 'Library Layout must be either SINGLE or PAIRED.'
            return success, msg, metadata_records

        run_id = metadata_record.contents.get('Run ID', '')
        if run_id == '':
            success = False
            msg = 'Invalid metadata! Missing run id in metadata.'
            return success, msg, metadata_records

        if run_id in previous_run_ids:
            success = False
            msg = f'Run ID {run_id} already exists.'
            return success, msg, metadata_records

        if library_layout == 'SINGLE':
            if run_id not in fastq_files_copy:
                success = False
                msg = f'Missing sequence file: {run_id}.fastq'
                return success, msg, metadata_records

            metadata_record.forward_fastq = run_id
            metadata_record.forward_fastq_f_name = fastq_files_copy[run_id][0]
            metadata_record.forward_fastq_file = fastq_files_copy[run_id][1]

            fastq_files_copy.pop(run_id)
        else:
            run_id_1 = f'{run_id}_1'
            run_id_2 = f'{run_id}_2'

            if run_id_1 not in fastq_files_copy:
                success = False
                msg = f'Missing sequence file: {run_id_1}.fastq'
                return success, msg, metadata_records
            if run_id_2 not in fastq_files_copy:
                success = False
                msg = f'Missing sequence file: {run_id_2}.fastq'
                return success, msg, metadata_records

            metadata_record.forward_fastq = run_id_1
            metadata_record.forward_fastq_f_name = fastq_files_copy[run_id_1][0]  # file name w/ extension
            metadata_record.forward_fastq_file = fastq_files_copy[run_id_1][1]    # file object

            metadata_record.reverse_fastq = run_id_2
            metadata_record.reverse_fastq_f_name = fastq_files_copy[run_id_2][0]  # file name w/ extension
            metadata_record.reverse_fastq_file = fastq_files_copy[run_id_2][1]    # file object

            fastq_files_copy.pop(run_id_1)
            fastq_files_copy.pop(run_id_2)

    if fastq_files_copy:
        if len(fastq_files_copy) > 3:
            missing_metadata_runs = ', '.join(list(fastq_files_copy)[:3]) + ' ...'
        else:
            missing_metadata_runs = ', '.join(list(fastq_files_copy)[:3]) + '.'

        success = False
        msg = f'Missing run ids in metadata: {missing_metadata_runs}'
        return success, msg, metadata_records

    success = True
    msg = ''
    return success, msg, metadata_records


def get_metadata_from_csv(csv_file):
    field_names = {'Run ID', 'Library Layout', 'Center Name', 'Experiment ID', 'Biosample', 'Organism', 'Bioproject',
                   'Country', 'Continent', 'Sample Name', 'Sample Title', 'Sample Type', 'Breed Sample',
                   'Cultivar Sample',
                   'Ecotype Sample', 'Isolate Sample', 'Library Selection', 'Strain Sample', 'Strain', 'Age',
                   'Dev Stage',
                   'Gender', 'Tissue', 'Birth Location', 'Cell Type', 'Collection Date', 'Disease', 'Disease Stage',
                   'Genotype',
                   'Health State', 'Isolation Source', 'Treatment', 'Description'}
    metadata_records = []

    if not os.path.isfile(csv_file):
        msg = f'Please provide a metadata csv file.'
        success = False
        return success, msg, metadata_records

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        run_ids = set()
        for i, row in enumerate(reader):
            # Validate field names
            if i == 0:
                for k in row.keys():
                    if k not in field_names:
                        msg = f'Invalid metadata format! {k} is not a valid column name.'
                        success = False
                        return success, msg, metadata_records

            # Check library layout
            library_layout = row.get('Library Layout', '').upper()
            if library_layout != 'SINGLE' and library_layout != 'PAIRED':
                msg = 'Invalid metadata! Library Layout must be either SINGLE or PAIRED.'
                success = False
                return success, msg, metadata_records

            # Check run id
            run_id = row.get('Run ID', '')
            if run_id == '':
                msg = 'Invalid metadata! Missing run id in metadata.'
                success = False
                return success, msg, metadata_records

            if run_id in run_ids:
                msg = 'Invalid metadata! Duplicate run ids found.'
                success = False
                return success, msg, metadata_records

            user_metadata_record = UserMetadataRecord(run_id)
            user_metadata_record.contents = row

            metadata_records.append(user_metadata_record)

        if metadata_records:
            msg = ''
            success = True
        else:
            msg = 'Please fill in the metadata csv.'
            success = False

        return success, msg, metadata_records


def create_dir(directory):
    """
    Create a new directory. Overwrite if it already exists.
    """
    remove_dir(directory)
    os.makedirs(directory)


def remove_dir(directory):
    """
    Delete the given directory if it exists.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)


def create_txt(file_path, contents=''):
    """
    Create a text file if it doesn't already exist.
    """
    if os.path.isfile(file_path):
        return

    try:
        with open(file_path, 'w') as f:
            if contents:
                f.write(contents)
    except Exception as e:
        raise ValueError(f'Unable to create {file_path}. {str(e)}')


def save_file(folder, file_name, file):
    logger.info("Inside save_file function.")
    try:
        fs = FileSystemStorage(location=folder)
        fs.save(file_name, file)
    except Exception as e:
        logger.info("ERROR!")
        logger.info(str(e))
