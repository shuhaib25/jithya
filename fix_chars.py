# Fix garbled encoding characters in HTML/CSS/JS files
import re

files = [
    r'c:\Users\USER\Downloads\Craftivo\Craftivo\index.html',
    r'c:\Users\USER\Downloads\Craftivo\Craftivo\assets\css\main.css',
    r'c:\Users\USER\Downloads\Craftivo\Craftivo\assets\js\main.js',
]

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        original = content

        # Remove/replace garbled em dash variants
        content = content.replace('\u00c3\u00a2\u00e2\u0082\u00ac\u00e2\u0080\u0094', ' ')
        content = content.replace('\u00c3\u00a2\u00e2\u0082\u00ac\u00e2\u20ac', ' ')
        content = content.replace('&mdash;', ' ')

        # Remove garbled apostrophe/quote variants
        content = content.replace('\u00c3\u00a2\u00e2\u0082\u00ac\u00e2\u201e\u00a2', "'")
        content = content.replace('\u00c3\u00a2\u00e2\u0082\u00ac\u00e2\u0084\u00a2', "'")

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Fixed: ' + filepath)
        else:
            print('No changes needed: ' + filepath)
    except Exception as e:
        print('Error on ' + filepath + ': ' + str(e))
