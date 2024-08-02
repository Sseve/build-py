import pathlib
import setuptools

path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()

setuptools.setup(
    name="setuptoolsdemo",
    version="0.0.1",
    description="打包示例",
    author="Sseve",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["setuptoolsdemo = setuptoolsdemo.main:main"]},
    install_requires=install_requires,
)

