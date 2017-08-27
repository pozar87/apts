from setuptools import setup 

import apts

#long_description = read('README.txt', 'CHANGES.txt')

setup(
    name='apts',
    version=apts.__version__,
    url='http://github.com/pozar87/apts/',
    license='Apache Software License',
    author='Łukasz Pożarlik',
    tests_require=['pytest'],
    install_requires=[''],
    #cmdclass={'test': PyTest},
    author_email='lpozarlik@gmail.com',
    description='Set of tools for automatic astrofotography images aqquisition and processing.',
    #long_description=long_description,
    packages=['apts'],
    include_package_data=True,
    platforms='any',
    #test_suite='sandman.test.test_sandman',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
