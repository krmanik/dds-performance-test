# Change Directory to Workspace
cd $HOME
mkdir -p dds-workspace
WORKSPACE="$HOME/dds-workspace"
# Change directory to the location where the colcon workspace will be created
echo -e "Change directory to $WORKSPACE"
cd $WORKSPACE

# install required packages
echo -e "Installing required packages"
sudo apt update -y
sudo apt install -y swig libpython3-dev libasio-dev libtinyxml2-dev

# build and install Fast DDS
# Create workspace directory
echo -e "Changing directory to $WORKSPACE"
mkdir -p fastdds_python_ws/src
cd fastdds_python_ws
# Get workspace setup file
echo -e "Getting workspace setup file"
wget https://raw.githubusercontent.com/eProsima/Fast-dds-workspace/main/fastdds_python.repos
# Download repositories
echo -e "Downloading repositories"
vcs import src < fastdds_python.repos
# Build the workspace
echo -e "Building the FastDDS"
colcon build

# source before running tests
# source ~/dds-workspace/fastdds_python_ws/install/setup.sh
