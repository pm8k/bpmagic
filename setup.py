from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


major = 0
minor = 1
patch = 0
version = '.'.join([str(v) for v in [major, minor, patch]])
download_url = 'https://github.com/pm8k/bpmagic/archive/{V}.tar.gz'.format(
    V=version)

setup(name='bpmagic',
      version=version,
      description='Magic functions to load boilerplate code',
      url='https://github.com/pm8k/bpmagic',
      download_url=download_url,

      long_description=readme(),
      author='Matthew Russell',
      author_email='astromars42@gmail.com',
      license='MIT',
      keywords=['python', 'magic', 'jupyter',
                'ipython', 'boiler', 'plate', 'bp'],
      classifiers=['Framework :: IPython'],
      py_modules=['bpmagic'],
      install_requires=[
          'ipython'
      ],
      include_package_data=True,

      zip_safe=False)
