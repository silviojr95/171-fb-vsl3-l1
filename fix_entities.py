import os

base = r'c:\Users\silvi\OneDrive\Documentos\Antigravity landers\171-fb-vsl3-l1'

with open(os.path.join(base, 'dark', 'index.html'), 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<!-- Styles -->', '<!-- Styles (LIGHT THEME) -->')
content = content.replace('href="css/style.css"', 'href="css/style-light.css"')

with open(os.path.join(base, 'light', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print('Done. light/index.html synced from dark, only CSS link swapped.')
