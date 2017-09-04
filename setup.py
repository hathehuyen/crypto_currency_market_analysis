from setuptools import setup, find_packages
setup(
    name = 'ccma',
    version = '1.0.0',
    long_description = __doc__,
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'pandas',
        'mongoengine',
        'requests==2.18.4'
    ]
)