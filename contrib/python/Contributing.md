# Contributing to `Huntela`

## Building Release 

1. Go to the Python project's root directory `contrib/python`.
1. Delete the `dist` directory if it exists, to clean up all existing builds.
1. Open `huntela/setup.py` and bump up the `VERSION`.
1. Run the setup script to generate the package files `python huntela/setup.py sdist bdist_wheel`.
1. Finally, upload the generated bits to PyPI `twine upload dist/*`.
