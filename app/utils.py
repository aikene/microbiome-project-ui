def validate_password(password):
    min_length = 8

    if len(password) < min_length:
        return False, f'Your password must be at least {min_length} characters long.'

    if password.isnumeric():
        return False, f'Your password cannot be entirely numeric.'

    return True, 'Your password has been updated successfully.'
