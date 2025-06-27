import re

def replacer(match):
    # Check if the 'bold_match' group captured something
    if match.group('bold_match'):
        # Extract the content inside the **...**
        # We slice [2:-2] to remove the leading and trailing "**"
        content = match.group('bold_match')[2:-2]
        return f'<strong>{content}</strong>'
    # Check if the 'newline_match' group captured something
    elif match.group('newline_match'):
        return '<br/>'
    else:
        # This case should ideally not happen if the pattern is comprehensive
        return match.group(0) # Return the original match if neither group captured

def sharp_text(string):
    pattern = re.compile(r'(?P<bold_match>\*\*.*?\*\*)|(?P<newline_match>\n)')
    return re.sub(pattern, replacer, string)