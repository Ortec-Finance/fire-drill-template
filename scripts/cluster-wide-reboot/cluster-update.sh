#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'  # No Color

# Check if command-line arguments are provided
if [ -z "$1" ]; then
  read -p "Enter label key under spec.metadata.labels: " LABEL_KEY
else
  LABEL_KEY="$1"
fi

if [ -z "$2" ]; then
  read -p "Enter label value: " LABEL_VALUE
else
  LABEL_VALUE="$2"
fi

# Exit if LABEL_KEY or LABEL_VALUE is still empty after prompting
if [ -z "$LABEL_KEY" ] || [ -z "$LABEL_VALUE" ]; then
  echo -e "${RED}Both label key and value must be provided. Exiting.${NC}"
  exit 1
fi

# Get all machines with the specific label under spec.metadata.labels
machines=$(oc get machine -n openshift-machine-api -l "${LABEL_KEY}=${LABEL_VALUE}" -o=jsonpath="{.items[*].metadata.name}" | tr ' ' '\n' | sort -r -t- -k4,4 -k5,5 | tr '\n' ' ')

machine_count=$(echo "$machines" | wc -w)

declare -a processedMachines
rolloutProgress=1
for machine in $machines; do
  
  if [[ " ${processedMachines[@]} " =~ " ${machine} " ]]; then
    rolloutProgress=$((rolloutProgress+1))
    if [[ "$rolloutProgress" -eq "$machine_count" ]]; then
      echo "All machines have been rolled out"
      exit 1
    fi
    continue
  fi
  
  node_name=$(oc get machine ${machine} -n openshift-machine-api -o=jsonpath='{.status.nodeRef.name}')
  
  echo -e "${GREEN}Cordoning node $node_name associated with machine $machine...${NC}"
  oc adm cordon $node_name
  
  echo -e "${YELLOW}Draining node $node_name...${NC}"
  oc adm drain $node_name --ignore-daemonsets --delete-emptydir-data --force
  
  echo -e "${RED}Deleting machine $machine...${NC}"
  oc delete machine $machine -n openshift-machine-api

  # Wait for the machine count to get back to the original
  echo -e "${YELLOW}Waiting for a new machine to be created and its node to become Ready...${NC}"
  sleep 3
  newMachine=$(oc get machine -n openshift-machine-api -l "${LABEL_KEY}=${LABEL_VALUE}" --no-headers | grep -v "Running" | awk '{print $1}')
  processedMachines+=("${newMachine}")
  echo "Machine Created: $newMachine"
  i=1
  until [ "$(oc get machine -n openshift-machine-api -l "${LABEL_KEY}=${LABEL_VALUE}" -o=jsonpath="{.items[*].status.phase}" | grep -o "Running" | wc -w)" -eq "$machine_count" ]; do
    echo "$i: Waiting for $machine_count Zones to be Running.."
    i=$((i+1))
    sleep 10  # check every 10 seconds
  done
  
  # As machine names change, we need to refresh the machine list after each iteration.
  machines=$(oc get machine -n openshift-machine-api -l "${LABEL_KEY}=${LABEL_VALUE}" -o=jsonpath="{.items[*].metadata.name}")
  
  # Optional: Sleep for a while before updating the next machine/node
  sleep 60  # Wait for 1 minute; adjust as needed
done

echo -e "${GREEN}All machines (and associated nodes) with label under spec.metadata.labels ${LABEL_KEY}=${LABEL_VALUE} have been updated.${NC}"
