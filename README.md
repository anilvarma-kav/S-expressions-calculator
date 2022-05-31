S-expression calculator
=======================
For full details on this problem refer to https://gist.github.com/rraval/2ef5e2ff228e022653db2055fc12ea9d


Requirements
=======================
1. Python3

How to run(MacOS or Linux)
=======================

**Step 1:** Download the repository uisng 

```
virtualenv -p <path_to_python2.7> <env_name>
```

*NOTE : the above command assumes that the python3 is installed in the system.*

**Step 2:** Activate the virtual environment

```
source <env_name>/bin/activate
```
*The name of the activated environment will appear on the left of the prompt.* 

**Step 3:** Install the HOME package outside virtual environment but make sure that the virtual environment is active

```
pip install git+https://github.com/ListerLab/HOME.git

or

git clone https://github.com/ListerLab/HOME.git
cd ./HOME
pip install -r requirements.txt
python setup.py install
```
***For conda users**
```
git clone https://github.com/ListerLab/HOME.git
cd ./HOME
conda env create    *assuming the conda environment is activated and R is already installed in it*
source activate HOMEenv
python setup.py install
```
