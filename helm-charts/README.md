# the-economist

> the-economist is a prototype python service
> This example has two main resources that create the following endpoints:
> * GET / || /health > return a Restful** response, status code 200, and others params
> * GET /alive/ || /alive/* > return a response with Flask/app info and status code 200

# Google Kubernetes Engine

## Helm - Cluster access

* kubectl create serviceaccount -n kube-system tiller
* kubectl create clusterrolebinding tiller-binding --clusterrole=cluster-admin --serviceaccount kube-system:tiller
* helm init --service-account tiller

## Installation with Helm [+info](https://helm.sh/docs/helm/helm_install/)
* helm install helm-charts/ --generate-name
* helm install NAME_SERVICE helm-charts/ --set global.namespace=NAMESPACE

## Validation
* kubectl --namespace=NAMESPACE get all

## Delete
* helm uninstall NAME_SERVICE


## Docs
* [Helm Installation](https://thenewstack.io/how-to-install-the-helm-kubernetes-package-manager-on-ubuntu-server/)
* [Helm + GKE](https://medium.com/google-cloud/installing-helm-in-google-kubernetes-engine-7f07f43c536e)


(*) Internal and External LoadBalancers

(**) From a wrapper decorator


# Local development

## Environment
* Linux variables:
    * export FLASK_ENV="develop"
    * export FLASK_DEBUG=true

## Runtime
* pip3 install -r src/requeriments.txt
* python3 src/api.py
