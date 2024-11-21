import pathlib
import setuptools


path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()


setuptools.setup(
    name="example",
    version="0.0.1",
    description="打包示例",
    author="Sseve",
    include_package_data=True,  # 项目包含: MANIFEST.in, 打包命令:python setup.py sdist
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["example = example.__main__:main"]},
    install_requires=install_requires,
)
