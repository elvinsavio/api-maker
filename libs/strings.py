import re

def sanitize_folder_name(name):
    # Define a regular expression pattern for valid folder names
    # This allows alphanumeric characters, dashes, and underscores
    valid_chars = re.compile(r'[^a-zA-Z0-9_\-]')
    
    # Replace invalid characters with an underscore
    sanitized_name = valid_chars.sub('_', name)
    
    # Strip leading and trailing whitespace
    sanitized_name = sanitized_name.strip()
    
    # Ensure the folder name is not empty
    if not sanitized_name:
        raise ValueError("Input cannot be empty")
    
    return sanitized_name