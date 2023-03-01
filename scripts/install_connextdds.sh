# Change Directory to Workspace
cd $HOME
mkdir -p dds-workspace
WORKSPACE="$HOME/dds-workspace"
cd $WORKSPACE

# download and install connextdds
mkdir ConnextDDS
cd ConnextDDS
wget https://s3.amazonaws.com/RTI/Bundles/6.1.1.8/Evaluation/rti_connext_dds-6.1.1.8-lm-x64Linux4gcc7.3.0.run
chmod +x rti_connext_dds-6.1.1.8-lm-x64Linux4gcc7.3.0.run
./rti_connext_dds-6.1.1.8-lm-x64Linux4gcc7.3.0.run

# Install pybind11
pip install pybind11

# Change Directory to Workspace
cd $WORKSPACE
# export connextdds home
export CONNEXTDDS_HOME="$HOME/dds-workspace/rti_connext_dds-6.1.1"
# clone connextdds-py
git clone https://github.com/rticommunity/connextdds-py.git
cd connextdds-py
# checkout the v0.1.5 tag for connextdds-py (6.1.1)
git checkout tags/v0.1.5 -b connextdds-py-6.1.1
# Build and Install ConnextDDS-Py
python configure.py --nddshome $CONNEXTDDS_HOME --jobs 4 x64Linux4gcc7.3.0
pip install .
