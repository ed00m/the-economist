# api-python-helloworld APP

> api-python-helloworld is a simple python microservice
> This example has two resources:
> * GET / > return a response whit { "hello": "world" } and status code 200
> * GET /alive > return a response with Flask info and status code 200

### Kubernetes manifests

Are included in this repo, in directory k8s

### Helm templating

The charts included in this repo, create a deployment with 2 replicas, the number of replicas are in values.yaml, create services with type ClusterIP/LoadBalancer*/NodePort, create a namespace and ingresses by service type to allow traffic to the deployments pod.

(*) Internal and External LoadBalancers
