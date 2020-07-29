# terraform - Provider
provider "kubernetes" {
    version = "~> 1.10.0"
    host    = google_container_cluster.default.endpoint
    token   = data.google_client_config.current.access_token
    client_certificate = base64decode(
        google_container_cluster.default.master_auth[0].client_certificate,
    )
    client_key = base64decode(
        google_container_cluster.default.master_auth[0].client_key
    )
    cluster_ca_certificate = base64decode(
        google_container_cluster.default.master_auth[0].cluster_ca_certificate,
    )
}

# Kubernetes Engine - Namespace
resource "kubernetes_namespace" "default" {
    metadata {
        name = var.kubernetes_namespace
    }
}

# Kubernetes Engine - Workload Deployment
resource "kubernetes_deployment" "default" {
    metadata {
        name = var.kubernetes_deployment
        namespace = kubernetes_namespace.default.metadata[0].name
        labels = {
            app = var.kubernetes_deployment
        }
    }

    spec {
        replicas = var.kubernetes_deployment_replicas

        selector {
            match_labels = {
                app = var.kubernetes_deployment
            }
        }

        template {
            metadata {
                labels = {
                    app = var.kubernetes_deployment
                }
            }

            spec {
                container {
                    image = var.kubernetes_container_image
                    name  = var.kubernetes_deployment

                    resources {
                        limits {
                            cpu    = "0.5"
                            memory = "512Mi"
                        }
                        requests {
                            cpu    = "250m"
                            memory = "50Mi"
                        }
                    }

                    liveness_probe {
                        http_get {
                            path = "/alive"
                            port = 3000

                            http_header {
                                name  = "X-Project"
                                value = var.kubernetes_deployment
                            }
                        }

                        initial_delay_seconds = 15
                        period_seconds        = 1
                    }
                }
            }
        }
    }
}

# Kubernetes Engine - Service
resource "kubernetes_service" "default" {
    metadata {
        namespace = kubernetes_namespace.default.metadata[0].name
        name      = var.kubernetes_service
    }

    spec {
        selector = {
            app = var.kubernetes_deployment
        }

        session_affinity = "ClientIP"

        port {
            protocol    = "TCP"
            port        = 80
            target_port = 3000
        }

        type             = "LoadBalancer"
        load_balancer_ip = google_compute_address.default.address
    }
}

# Environment - Output
output "load-balancer-ip" {
    value = google_compute_address.default.address
}
