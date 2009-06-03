from setuptools import setup, find_packages

setup(
    name = 'dzenlog-link',
    version = '0.1.2',
    description = 'This is a simple application to post links to the dzenlog.',
    keywords = 'django apps blogging dzenlog',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-dzenlog-link/',
    install_requires = ['django-dzenlog>=0.2.7'],
    dependency_links = ['http://pypi.aartemenko.com/'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(exclude=['example*']),
    package_data = {
        'templates': ['*.html'],
    },
    include_package_data = True,
    zip_safe = False,
)

