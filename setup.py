from setuptools import setup

try:
    import enum  # noqa
    extra_requires = []
except ImportError:
    extra_requires = ['enum34']

REQUIRES = ['marshmallow>=2.0.0'] + extra_requires


with open('README.md', 'r') as f:
    readme = f.read()

with open('CHANGELOG', 'r') as f:
    changelog = f.read()


if __name__ == '__main__':
    setup(
        name='marshmallow-enum',
        version='1.4',
        author='Alec Nikolas Reiter',
        author_email='alecreiter@gmail.com',
        description='Enum field for Marshmallow',
        long_description=readme + '\n\n' + changelog,
        package_data={'': ['LICENSE']},
        include_package_data=True,
        license='MIT',
        packages=['marshmallow_enum'],
        install_requires=REQUIRES,
    )
