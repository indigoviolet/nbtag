default:
    just --list

build:
    hatch build

update_version_patch:
    hatch version patch

publish:
    hatch publish \
       --user __token__ -a $PYPI_UPLOAD_TOKEN

pipx_install:
    pipx install --force dist/conda_pip_minimal-$(poetry version | perl -lane 'print $F[1]')*.whl
