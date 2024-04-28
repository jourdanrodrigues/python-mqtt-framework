from setuptools import find_packages, setup

setup(
    name="django-mqtt-framework",
    version="0.0.1",
    description="",
    author="Jourdan Rodrigues",
    author_email="thiagojourdan@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/jourdanrodrigues/django-mqtt-framework",
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        "django>=5.0",
        "paho-mqtt>=2.0",
    ],
)
