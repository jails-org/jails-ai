#!/usr/bin/env python3
"""Bundle shared standards into independently installable jails-ai skills."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    sources = sorted((root / 'standards').glob('*.md'))
    stale = []

    for entrypoint in sorted((root / 'skills').glob('*/SKILL.md')):
        for source in sources:
            target = entrypoint.parent / 'references' / 'standards' / source.name
            content = (
                '<!-- Generated from standards/' + source.name
                + ' by scripts/sync_standards.py. Do not edit directly. -->\n\n'
                + source.read_text(encoding='utf-8')
            )
            if target.exists() and target.read_text(encoding='utf-8') == content:
                continue
            if args.check:
                stale.append(str(target.relative_to(root)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding='utf-8')
                print('Updated ' + str(target.relative_to(root)))

    if stale:
        parser.exit(1, 'Outdated bundled standards:\n' + '\n'.join(stale) + '\n')
    if args.check:
        print('Bundled standards are current.')


if __name__ == '__main__':
    main()
