#!/bin/bash
FOLDER="$(cd "$(dirname "$0")" && pwd)"
rm -rf ${FOLDER}/env
conda create --yes -p ${FOLDER}/env python=3.6.0 pandas matplotlib

# install cvxpy
conda install --yes -c cvxgrp cvxpy

# pip install -r requirements.txt
