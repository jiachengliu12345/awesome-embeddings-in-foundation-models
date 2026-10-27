#!/usr/bin/env python3
"""Check source references, language pairs, local links, and SVG files offline."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors=[]
    catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
    sources=catalog['sources']
    ids={s['id'] for s in sources}
    if len(ids)!=len(sources):
        errors.append('Duplicate source IDs')
    claims={c['id'] for c in catalog['claims']}
    for claim in catalog['claims']:
        if not set(claim['source_ids']).issubset(ids):
            errors.append(f'{claim["id"]}: missing claim source')
    for page in catalog['pages']:
        if set(page['paths'])!={'en','zh-CN'}:
            errors.append(f'{page["topic"]}: missing language')
        for path in page['paths'].values():
            if not (root/path).is_file():
                errors.append(f'Missing page: {path}')
        if not set(page.get('claim_ids',[])).issubset(claims):
            errors.append(f'{page["topic"]}: missing claim')
    for path in sorted(root.rglob('*.md')):
        if '.git' in path.parts:
            continue
        body=path.read_text(encoding='utf-8')
        if path.name.endswith('.zh-CN.md'):
            other=path.name.removesuffix('.zh-CN.md')+'.md'
        else:
            other=path.stem+'.zh-CN.md'
        if not (path.parent/other).is_file() or f']({other})' not in body:
            errors.append(f'{path.relative_to(root)}: missing equivalent-language link')
        refs=re.search(r'<!-- sources: (.*?) -->',body)
        if refs and not {s.strip() for s in refs.group(1).split(',') if s.strip()}.issubset(ids):
            errors.append(f'{path.relative_to(root)}: unknown source ID')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',body):
            parsed=urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not (path.parent/unquote(parsed.path)).exists():
                errors.append(f'{path.relative_to(root)}: missing link {target}')
    for path in (root/'assets').glob('*.svg'):
        try:
            svg=ET.fromstring(path.read_text(encoding='utf-8'))
            if not svg.get('viewBox') or svg.find('{http://www.w3.org/2000/svg}title') is None:
                errors.append(f'{path.name}: missing viewBox or title')
        except ET.ParseError as error:
            errors.append(f'{path.name}: {error}')
    if not (root/'explorer.html').is_file():
        errors.append('Missing storage calculator')
    return errors


if __name__=='__main__':
    errors=check()
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        raise SystemExit(1)
    print('Source references, bilingual pages, local links, and SVG files pass.')
