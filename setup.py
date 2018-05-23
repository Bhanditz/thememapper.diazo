from setuptools import setup, find_packages

setup(
    name='thememapper.diazo',
    version='0.2.1',
    description='thememapper module containing diazo server for development',
    long_description=open('README.rst').read(),
    author='Brandon Tilstra',
    author_email='tilstra@gmail.com',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['thememapper'],
    include_package_data=True,
    url='http://pypi.python.org/pypi/thememapper/',
    license='gpl',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet",
      ],
    install_requires=['Flask','tornado==3.1.0','diazo[wsgi]','wsgiproxy'],
    entry_points = {
    'console_scripts': [
                        'thememapper_diazo = thememapper.diazo.server:main'
                       ]
    },
    zip_safe=False
)
