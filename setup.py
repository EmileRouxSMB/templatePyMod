from setuptools import setup
import templatePyMod

setup(name='templatePyMod',
      version=templatePyMod.__version__,
      description="templatePyMod",
      long_description="templatePyMod",
      author="Ludovic Charleux, Emile Roux",
      author_email="emile.roux@univ-smb.fr",
      license="GPL v3",
      packages=["templatePyMod"],
      zip_safe=False,
      include_package_data=True,
      url="https://gitlab.com/xxx",
      install_requires=[
          "numpy",
          "scipy",
          "pandas",
      ],
      )
