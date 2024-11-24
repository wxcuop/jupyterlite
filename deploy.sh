#!/bin/bash
export NODE_VERSION=18
#Deploy.sh for netlify

#yum install wget -y

wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

export PATH="$PWD/bin:$PATH"
export MAMBA_ROOT_PREFIX="$PWD/micromamba"

# Initialize Micromamba shell
#./bin/micromamba shell init -s bash -p $MAMBA_ROOT_PREFIX
./bin/micromamba shell init -s bash -r $MAMBA_ROOT_PREFIX
# Source Micromamba environment directly
eval "$(./bin/micromamba shell hook -s bash)"

# Activate the Micromamba environment
micromamba create -n jupyterenv python=3.12 -c conda-forge -y
micromamba activate jupyterenv
micromamba install conda-forge::nodejs #needed to build webr
# install the dependencies
python -m pip install -r requirements.txt

# build the JupyterLite site
jupyter lite --version
jupyter lite build --contents content --output-dir dist
