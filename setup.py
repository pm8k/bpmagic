from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


major = 0
minor = 1
patch = 2
version = '.'.join([str(v) for v in [major, minor, patch]])


setup(name='boilermagic',
      version=version,
      description='Magic functions to load boilerplate code',
      url='https://github.com/pm8k/boilermagic',
      download_url = 'https://github.com/pm8k/boilermagic/archive/0.1.2.tar.gz', # I'll explain this in a second

      long_description=readme(),
      author='Matthew Russell',
      author_email='astromars42@gmail.com',
      license='MIT',
      keywords=['python', 'magic', 'jupyter', 'ipython', 'boiler', 'plate'],

      packages=['boilermagic'],
        install_requires=[
          'ipython'
      ],
      include_package_data=True,

      zip_safe=False)