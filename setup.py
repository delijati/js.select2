from setuptools import setup, find_packages
import os

version = '3.3'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (read('README.md')
                    + '\n' +
                    read('js', 'select2', 'test_select2.js.txt')
                    + '\n' +
                    read('CHANGES.txt'))

setup(name='js.select2',
      version=version,
      description="Fanstatic packaging of select2",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Josip Delic',
      author_email='delijati@delijati.net',
      url="https://github.com/delijati/js.select2",
      license='BSD',
      packages=find_packages(),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['fanstatic',
                        'setuptools',
                        ],
      entry_points={'fanstatic.libraries':
                    ['select2 = js.select2:library',
                     ],
                    },
      )
