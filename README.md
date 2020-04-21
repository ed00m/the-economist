# flask_api_rest_manifest

> api-python-helloworld is a simple python microservice. development with Flask and Restful library

# Google Kubernetes Engine

## Helm - Cluster access

* kubectl create serviceaccount -n kube-system tiller
* kubectl create clusterrolebinding tiller-binding --clusterrole=cluster-admin --serviceaccount kube-system:tiller
* helm init --service-account tiller

## Installation with Helm [+info](https://helm.sh/docs/helm/helm_install/)
* helm install helm-charts/ --generate-name
* helm install NAME_SERVICE helm-charts/ --set global.namespace=NAMESPACE

## Installation with kubectl
* kubectl apply -f k8s/

## Validation
* kubectl --namespace=NAMESPACE get all

## Delete
* helm uninstall NAME_SERVICE


## Docs
* [Helm Installation](https://thenewstack.io/how-to-install-the-helm-kubernetes-package-manager-on-ubuntu-server/)
* [Helm + GKE](https://medium.com/google-cloud/installing-helm-in-google-kubernetes-engine-7f07f43c536e)
