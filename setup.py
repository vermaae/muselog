from setuptools import setup

VERSION = "1.8.2"

install_requires = [
    "pygelf>=0.4.1",
    "JSON-log-formatter>=0.2.0",
    "ddtrace>=0.22.0"  # This is the minimum version allowed as trace helpers weren't added until 0.22.0
]

setup(
    name="muselog",
    version=VERSION,
    description="themuse.com log utilities",
    zip_safe=False,

    packages=["muselog"],

    install_requires=install_requires,
    extras_require={
        "flask": ["Flask>=1.0.2"]
    }
)
