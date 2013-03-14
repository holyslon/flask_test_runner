"""
Flask-TestRunner
--------------

Add Class run Flask app in test Environment


"""
import sys
from setuptools import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# https://github.com/pypa/virtualenv/pull/259)
try:
    import multiprocessing
except ImportError:
    pass

install_requires = ['Flask']

setup(
    name='Flask-TestRunner',
    version='0.0.1-dev',
    url='http://github.com/holyslon/flask_test_runner',
    license='BSD',
    author='Anton Onikiichuk',
    author_email='anton@onikiychuk.com',
    description='Add Class run Flask app in test Environment',
    long_description=__doc__,
    packages=[
        'flask_test_runner'
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)