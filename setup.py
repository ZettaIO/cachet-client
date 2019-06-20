from setuptools import setup


setup(
    name="cachet-client",
    version="1.0.0",
    description="Administation client for the Cachet status project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/zettaio/cachet-client",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    maintainer="Einar Forselv",
    maintainer_email="eforselv@gmail.com",
    packages=['cachetclient', 'cachetclient.v1'],
    include_package_data=True,
    keywords=['cachet', 'client'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=[
        'requests==2.21.0'
    ],
    entry_points={'console_scripts': [
        'cachet = cachetclient.cli:execute_from_command_line',
    ]},
)
