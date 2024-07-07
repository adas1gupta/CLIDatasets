from setuptools import setup, find_packages

setup(
    name='data-analyzer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'dask',
        'flask',
        'flask_sqlalchemy'
    ],
    entry_points='''
        [console_scripts]
        data-analyzer=data_analyzer.cli:cli
    ''',
)
