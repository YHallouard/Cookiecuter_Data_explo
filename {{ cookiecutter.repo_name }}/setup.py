from setuptools import setup, find_packages
from os import path

with open('README.md', 'r') as fh:
    long_description = fh.read()

required_setup = ['pytest-runner',
                  'wheel',
                  'flake8']
required_tests = ['pytest',
                  'pytest-cov',
                  'treon']

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

required_install = [x.strip() for x in all_reqs]
__version__ = 'init'
exec(open('{{ cookiecutter.repo_name }}/version.py').read())

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version=__version__,
    description="{{ cookiecutter.description }}",
    author='{{ cookiecutter.author_name }}',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['pytest-runner', 'wheel', 'flake8'],
    tests_require=['pytest', 'pytest-cov', 'treon'],
    install_requires=all_reqs,
    license='{% if cookiecutter.open_source_license == "MIT" %}MIT\
    {% elif cookiecutter.open_source_license == "BSD-3-Clause" %}BSD-3{% endif %}',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
