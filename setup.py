try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description' : 'Getting info from the browser', 
        'author': 'Bar Amber', 
        'url': 'URL to get it at.',
        'download_url': 'Where to doownload it.',
        'author_email': 'barhalaf7@gmail.com',
        'version': '0.1.0', 
        'install_requires': ['nose'],
        'packages': ['ex51'], 
        'scripts': [],
        'name': 'ex51'
        }
setup(**config)

