#!/bin/bash
#export NODE_VERSION=18
#Deploy.sh for netlify

#yum install wget -y

wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

export PATH="$PWD/bin:$PATH"
export MAMBA_ROOT_PREFIX="$PWD/micromamba"
mkdir -p .mamba/pkgs
chmod -R u+w .mamba
# Initialize Micromamba shell
#./bin/micromamba shell init -s bash -p $MAMBA_ROOT_PREFIX
./bin/micromamba shell init -s bash -r $MAMBA_ROOT_PREFIX
micromamba config set use_lockfiles false
# Source Micromamba environment directly
eval "$(./bin/micromamba shell hook -s bash)"

# Activate the Micromamba environment
micromamba create -n jupyterenv python=3.12 -c conda-forge -y
micromamba activate jupyterenv
micromamba install conda-forge::nodejs #needed to build webr

# install the dependencies
python -m pip install -r requirements.txt
#python -m pip install git+https://github.com/r-wasm/jupyterlite-webr-kernel.git
# build the JupyterLite site
jupyter lite --version
#jupyter lite build --contents content --output-dir dist --pyodide https://github.com/pyodide/pyodide/releases/download/0.27.5/pyodide-0.27.5.tar.bz2
jupyter lite build --contents content --output-dir dist 
