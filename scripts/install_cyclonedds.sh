# Change Directory to Workspace
cd $HOME
mkdir -p dds-workspace
WORKSPACE="$HOME/dds-workspace"
cd $WORKSPACE

# clone cyclonedds
git clone https://github.com/eclipse-cyclonedds/cyclonedds
# change directory to cyclonedds
echo "Changing directory to cyclonedds"
cd cyclonedds && mkdir build install && cd build
# make and install cyclonedds
echo "Building and installing cyclonedds"
cmake .. -DCMAKE_INSTALL_PREFIX=../install
cmake --build . --target install
# change directory to cyclonedds-workspace
echo "Changing directory to cyclonedds-workspace"
cd ..
# export cyclonedds home
# $WORKSPACE/cyclonedds/install
export CYCLONEDDS_HOME="$(pwd)/install"
# install cyclonedds-workspace
echo "Installing cyclonedds-workspace"
pip3 install git+https://github.com/eclipse-cyclonedds/cyclonedds-workspace
