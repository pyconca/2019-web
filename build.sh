#!/bin/bash

# Going to print some fancy text to make this easy to identify in netlify logs
echo -e "\n"
echo -e "\n"
echo -e "\n"
echo -e "\n"
echo -e "\n"
echo "------------------------------------------------------------------------"
echo "BUILD START"
echo "------------------------------------------------------------------------"

# Print the version of the tools we are using
echo "Python version"
python --version
echo "Node version"
node --version
echo "NPM version"
npm --version
echo "PIP version"
pip --version

# install NPM dependencies
npm install

# install PIP dependencies
pip install -r requirements.txt

nikola build

nikola build  # we need to run this twice to pick up gulp/sass stuff


echo "------------------------------------------------------------------------"
echo "BUILD COMPLETED SUCCESSFULLY!"
echo "------------------------------------------------------------------------"
