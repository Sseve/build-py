from setuptools import setup, find_packages


setup(
    name="demo",
    version="0.0.1",
    description="示例项目",
    maintainer="Sseve",
    author="Sseve",
    url="github.com/Sseve/build-py/demo",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["demo = demo.main:main"]},
    package_data={"": [".env.demo"]},
    install_requires=["python-dotenv==1.0.1"],
)
