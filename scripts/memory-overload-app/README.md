# MEMORY EATER
This Python application will eat the amount of megabytes that it is assigned to by a `curl` command
To use this, go into the pods terminal and `curl -X POST http://localhost:8000/consume/22000`
You can also `curl -X POST http://localhost:8000/release` to release the memory that has been consumed

You can modify the Taints and Tolerations as well as the Resource requests and limits from the `kustomization.yaml`

1. Build the `/app`
2. Push it to your Container Registry
3. Adjust `kustomization.yaml` to apply the right image url