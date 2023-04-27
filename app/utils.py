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
        
