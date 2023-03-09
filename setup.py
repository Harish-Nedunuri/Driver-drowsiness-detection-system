#!/usr/bin/env src

"""The setup script."""

from setuptools import setup, find_packages
import json

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('package.json', 'r') as f:
    module_setup = json.load(f)
    module_name = module_setup['module_name']
    module_version = module_setup['module_version']
    module_description = module_setup['module_description']
    module_tasks = module_setup['tasks']

setup(
    name=module_name,
    version=module_version,
    description=module_description,
    long_description=readme,
    author='Harish Nedunuri',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.8, <3.9",
    install_requires=requirements,
    package_data={
        '': ['requirements.txt']
    },
    include_package_data=True,
    packages=find_packages(include=[module_name, module_name + '.*', 'package.json']),
    zip_safe=False,
    entry_points={
        'scripts': [f'{module_name}.{task}={module_name}.{task}.entry:main' for task in module_tasks]
    }
)
