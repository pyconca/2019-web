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

# Start gulp build process
gulp build


echo "------------------------------------------------------------------------"
echo "BUILD COMPLETED SUCCESSFULLY!"
echo "------------------------------------------------------------------------"
