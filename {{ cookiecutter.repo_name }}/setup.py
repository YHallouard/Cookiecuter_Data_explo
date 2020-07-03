from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

required = ['Sphinx',
            'flake8',
            'Flask',
            'matplotlib',
            'Keras',
            'numpy<1.19.0',
            'opencv-python',
            'pandas',
            'Pillow',
            'scikit-image',
            'scikit-learn',
            'tensorflow',
            'tqdm',
            'grpcio==1.27.2',
            'imantics',
            'shapely',
            'tqdm',
            'mlflow',
            'geopandas']

__version__ = 'init'
exec(open('src/version.py').read())

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version=__version__,
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['pytest-runner', 'wheel', 'flake8'],
    tests_require=['pytest', 'pytest-cov', 'treon'],
    install_requires=required,
    license='{% if cookiecutter.open_source_license == "MIT" %}MIT\
    {% elif cookiecutter.open_source_license == "BSD-3-Clause" %}BSD-3{% endif %}',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
