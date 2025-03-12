# Elastic Overload

This application will overload any elastic search cluster by deploying an army of log spammers.

You can adjust the amount of spam by changing the replicas in the `deployment.yaml`

1. Build the `/app`
2. Push it to your Container Registry
3. Adjust `kustomization.yaml` to apply the right image url