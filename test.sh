#!/bin/bash


echo '#### Create Python3 Virtual Environment ####'

VIRTUAL_ENV_NAME='cabral-devops'
python3 -m venv $VIRTUAL_ENV_NAME


echo '#### Activate Virtual Environment ####'

source $VIRTUAL_ENV_NAME/bin/activate


echo '#### Install Requirements ####'
pip3 install -r ./requirements.txt



#############Jump to that Path##############
cd /var/lib/jenkins/workspace/$JOB_NAME/



echo '#### Run tests ####'

python -m unittest


echo '#### Deactivate Virtual Environment and Exit Shell Command Line ####'

deactivate
exit
