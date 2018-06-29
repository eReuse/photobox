from setuptools import find_packages, setup

setup(
    name='ereuse-photobox',
    version='0.1dev1',
    packages=find_packages(),
    license='AGPLv3 License',
    description='Photobox.',
    scripts=['Scan.py'],
    url='https://github.com/eReuse/photobox',
    author='eReuse.org team',
    author_email='x.bustamante@ereuse.org',
    install_requires=[
        'boltons',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ]
)
