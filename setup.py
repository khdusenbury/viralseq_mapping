"""Setup script for ``rsview``."""

import sys
from os import path
try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

# Check that using Python 3
if not (sys.version_info[0] == 3):
    raise RuntimeError('rsview requires Python 3.x\n'
            'You are using Python {0}.{1}'.format(
            sys.version_info[0], sys.version_info[1]))

# get metadata, which is specified in another file
metadata = {}
with open('./rsview/_metadata.py') as f:
    lines = [line for line in f.readlines() if not line.isspace()]
for dataname in ['version', 'author', 'url']:
    for line in lines:
        entries = line.split('=')
        assert len(entries) == 2, "Failed to parse metadata:\n%s" % line
        if entries[0].strip() == '__%s__' % dataname:
            if dataname in metadata:
                raise ValueError("Duplicate metadata for %s" % dataname)
            else:
                metadata[dataname] = entries[1].strip()[1 : -1]
    assert dataname in metadata, "Failed to find metadata for %s" % dataname

with open('README.md') as f:
    readme = f.read()

# main setup command
setup(
    name = 'rsview',
    version = metadata['version'],
    author = metadata['author'],
    url = metadata['url'],
    description = 'Mapping of RSV sequences based on Genbank submissions.' \
                  'Correlation of genotypes with childhood pneumonia deaths.',
    long_description = readme,
    license = 'MIT License',
    install_requires = ['biopython', 'country_converter', 'plotly', 'pandas'],
    packages=find_packages(exclude=['docs', 'tests']),
    package_dir = {'RSView':'rsview'},
    scripts = ['rsview/seq_download.py',
               'rsview/genotype.py',
               'rsview/map_rsv.py',
               'rsview/health_download.py',
               'rsview/parsearguments.py',
               'rsview/plot_rsv.py',
               'rsview/plot_correlation.py'
                ]
)
