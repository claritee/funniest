from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)