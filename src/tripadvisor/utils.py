import re
from botasaurus import bt
from casefy import kebabcase

from unidecode import unidecode

def unicode_to_ascii(text):
    """
    Convert unicode text to ASCII, replacing special characters.
    """
    # Replacing 'ë' with 'e' and return the ASCII text
    return unidecode(text).replace("ë", "e")

def kebab_case(s):
    return kebabcase(s)

def unique_strings(lst):
    # Use a set to remove duplicates, then convert back to a list
    return list(dict.fromkeys(lst))


def sort_dict_by_keys(dictionary, keys):
    new_dict = {}
    
    try:
        for key in keys:
            new_dict[key] = dictionary[key]
    except:
        bt.write_json(dictionary, "Failed")
        raise Exception("Failed to sort dict by keys")
    return new_dict

default_browser_options = {
    "block_images": True,
    "reuse_driver": True,
    "keep_drivers_alive": True,
    "close_on_crash": True,  # When Ready for Production change to True
    "headless": True,        # When Ready change to True
    'output': None, # When Ready for Production Uncomment
}

# max 5 retries add
default_request_options = {
    "close_on_crash": True,  # When Ready for Production change to True
    'output': None, # When Ready for Production Uncomment
}