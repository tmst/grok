from setuptools import setup, find_packages

setup(
    name='grok',
    version='0.9dev',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://svn.zope.org/grok/trunk',
    description='Grok: Now even cavemen can use Zope 3!',
    long_description=open('README.txt').read(),
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    license='ZPL',
    
    install_requires=['setuptools'],
)
