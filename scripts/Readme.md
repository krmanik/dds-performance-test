# Build and Install Python DDS

## Eclipse CycloneDDS

### Build CycloneDDS for Python

```sh
./scripts/install_cyclonedds.sh 
```

## eProsima FastDDS

### Build FastDDS for Python

```sh
./scripts/install_fastdds.sh 
```

## OpenDDS

### Build OpenDDS for Python

```sh
./scripts/install_opendds.sh 
```

## Clean

```sh
cd $WORKSPACE
rm -r <name of dds project>
# e.g. rm -r cyclonedds
```

## Set environment var

Set environment var before running tests.

```sh
WORKSPACE="$HOME/dds-workspace"

# for cyclonedds
export CYCLONEDDS_HOME=$WORKSPACE/cyclonedds/install

# for fastdds
source $WORKSPACE/fastdds_python_ws/install/setup.sh

# for opendds
source $WORKSPACE/OpenDDS/setenv.sh

# for connextdds
export CONNEXTDDS_HOME="$WORKSPACE/rti_connext_dds-6.1.1"
```
