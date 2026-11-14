"""Rebuild the portable page using only Python's standard library."""
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parent
template = (root / 'page-template.html').read_text(encoding='utf-8')
fragment = (root / 'player-source.html').read_text(encoding='utf-8')
placeholder = '__GENESIS_PLAYER_FRAGMENT__'
if template.count(placeholder) != 1:
    raise ValueError('Expected one player placeholder in the page template')
output = template.replace(placeholder, escape(fragment, quote=True))
(root / 'index.html').write_text(output, encoding='utf-8')
print('Built index.html:', len(output.encode('utf-8')), 'bytes')
