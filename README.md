# the-economist

the-economist is a prototype Python service. This example has two main resources that create the following endpoints:

# Blueprints

## root.bp
* GET / || /health
  * return Restful** response
  * status code 200, and others params

## alive.bp
* GET /alive/ || /alive/health
  * return a response with Flask/app info
  * status code 200

## indecon.bp
* GET /indecon/
  * return descriptor "Entrega la información de las APIs publicadas por indecon"
* GET /indecon/last
  * return descriptor "API que entrega los últimos valores de todos los elementos"
* GET /indecon/values/elemento
  * return descriptor "API que entrega todos los valores de un elemento particular"
* GET /indecon/date/elemento/02-01-2020
  * return descriptor "API que entrega el valor de un elemento particular en una fecha en particular"



# Tested in: Google Kubernetes Engine

## Installation with Helm [+info](https://helm.sh/docs/helm/helm_install/)
* helm install helm-charts/ --generate-name
* helm install NAME_SERVICE helm-charts/ --set global.namespace=NAMESPACE

## Validation
* kubectl --namespace=NAMESPACE get all

## Delete
* helm uninstall NAME_SERVICE

## k8s examples manifests (review first)
* kubectl apply -f k8s/

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
* pip3 install -r src/requirements.txt
* python3 src/api.py
