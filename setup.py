try:
    from setuptools import setupt
except importError:
    from distutils.core import setup

config ={
    'descripton': 'Мой проект',
    'author': 'VK'
    'url': 'url address',
    'download_url': 'download url',
    'author_email': 'vk@vk.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'name': 'projectname'
}

setup(**config)
