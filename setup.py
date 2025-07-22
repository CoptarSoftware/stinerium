from setuptools import setup, find_packages

setup(
    name='test_library',
    version='0.0.7',
    description='Core Test Library '
                'This library extends Selenium with custom actions, allowing separation of business and technical logic in automated tests.'
                'Through its abstraction layer, tests become more readable, maintainable, and can be written in a business-friendly language '
                'without direct use of raw Selenium methods.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sebastian Jadczak',
    author_email='Sebastian-Jadczak@wp.pl',
    url='https://github.com/CoptarSoftware',
    packages=find_packages(),
    install_requires=[
        'selenium==4.28.1',
        'dacite==1.8.1',
        'setuptools==75.8.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12'
)
