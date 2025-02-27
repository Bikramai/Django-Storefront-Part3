from django.core.exceptions import ValidationError



def validate_file_size(value):
    max_size_kb = 1024

    if value.size > max_size_kb * 1024:
        raise ValidationError(f'Files cannot be larger than {max_size_kb} KB!')