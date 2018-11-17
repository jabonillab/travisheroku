from setuptools import setup

setup(
    name='clikpik',
    packages=['clikpik'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Testing',
        'Flask-SQLAlchemy',
        'psycopg2'
    ],
)