import re

string = """
Welcome back! Absolutely, let's pick up right where we left off and continue our Arabic learning journey.\n\nWe are currently in **Stage 1: Foundation Strengthening**, and we were just beginning **Day 4** of our daily plan.\n\nLast time, we introduced 10 new vocabulary words, including some professions and other useful terms:\n\n1.  مهندس (muhandis) - Engineer (masculine)\n2.  مهندسة (muhandisah) - Engineer (feminine)\n3.  مترجم (mutarjim) - Translator (masculine)\n4.  مترجمة (mutarjimah) - Translator (feminine)\n5.  طالب (talib) - Student (masculine) (review)\n6.  طالبة (talibah) - Student (feminine) (review)\n7.  درس (dars) - Lesson\n8.  جامعة (jami\\'ah) - University (feminine word)\n9.  عمل (amal) - Work / Job\n10. شغل (shughl) - Work / Job (common in spoken Arabic, similar to amal)\n\nYour task was to:\n\n1.  Read these new words aloud several times, paying close attention to the masculine and feminine pairs and the ة (taa marbuta) that signals femininity.\n2.  Based on the spelling, identify which of the new singular nouns (درس, جامعة, عمل, شغل) are feminine.\n\nPlease let me know which of these nouns you identify as feminine!\n\n[PROGRESS: Stage 1 - Vocabulary Day 4]
"""

# Define the callback function that will determine the replacement
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

new_text = sharp_text(string)
with open("new_text.txt",'w') as file:
    file.write(new_text)
