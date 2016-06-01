from distutils.core import setup

LONG_DESC = '''This is a more elaborate description of the package'''

setup(
    name = 'acmepack',
    packages = [name],
    version = '0.1',
    long_description=LONG_DESC,
    description = 'Python package skeleton',
    author = 'Alex Railean',
    author_email = 'a.railean@dekart.com',
    keywords = ['python', 'tutorial'],
    license = 'BSD',
    classifiers = [
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License'
      ],
    # provide your external dependencies here as a list of strings
    install_requires=[
        #'reyaml',
      ]
)

