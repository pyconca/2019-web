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
python --version
node --version
npm --version
pip --version

echo "default $BUILD_TOKEN and $TOKEN_2"

echo "hope those environment variables printed"


echo "------------------------------------------------------------------------"
echo "BUILD COMPLETED SUCCESSFULLY!"
echo "------------------------------------------------------------------------"