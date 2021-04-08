from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'click'
]

test_requirements = [
]

setup(
    name='intercom',
    version='0.9',
    description="Distance finder for intercom",
    long_description=readme,
    author="Batuhan Ceylan",
    author_email='batuhan@batuhanceylan.com',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'intercom=intercom.intercom:intercom',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
