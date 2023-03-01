# Change Directory to Workspace
cd $HOME
mkdir -p dds-workspace
WORKSPACE="$HOME/dds-workspace"
cd $WORKSPACE

# clone opendds
git clone https://github.com/OpenDDS/OpenDDS.git
# change directory to opendds
echo "Changing directory to OpenDDS"
cd OpenDDS
echo "Building and installing OpenDDS"
./configure
make

echo "Setting environment variables"
source setenv.sh

cd ..
# clone python opendds
git clone https://github.com/OpenDDS/pyopendds.git
# change directory to python opendds
echo "Changing directory to pyopendds"
cd pyopendds
# Build and Install PyOpenDDS
echo "Building and installing pyopendds"
pip install .
