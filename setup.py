from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize(
        [
            "cython_naive_impl.py",
            "cython_impl.py"
        ],
        compiler_directives={'language_level' : "3"}
    )
)
