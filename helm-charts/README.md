# the-economist APP

> the-economist is a prototype python service
> This example has two resources:
> * GET / > return a response whit { "hello": "world" } and status code 200
> * GET /alive > return a response with Flask info and status code 200

### Kubernetes manifests

Are included in this repo, in directory k8s. Create services with type ClusterIP/LoadBalancer*/NodePort, create a namespace and ingresses by service type to allow traffic to the deployments pod.

### Helm templating

The charts included in this repo, create a deployment, sample configuration is in values.yaml, Create services with type Ingress/NodePort, create a namespace and ingresses by service type to allow traffic to the deployments pod.


(*) Internal and External LoadBalancers
