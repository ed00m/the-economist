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

resource "kubernetes_namespace" "develop" {
    metadata {
        name = "develop"
    }
}

resource "google_compute_address" "default" {
    name   = var.network_name
    region = var.region
}

resource "kubernetes_service" "the-economist" {
    metadata {
        namespace = kubernetes_namespace.develop.metadata[0].name
        name      = "the-economist"
    }

    spec {
        selector = {
            run = "the-economist"
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

resource "kubernetes_replication_controller" "the-economist" {
    metadata {
        name      = "the-economist"
        #namespace = kubernetes_namespace.develop.metadata[0].name

        labels = {
            run = "the-economist"
        }
    }

    spec {
        selector = {
            run = "the-economist"
        }

        template {
            container {
                image = "ed00m/the-economist:v0.3.1"
                name  = "the-economist"

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
            }
        }
    }
}

output "load-balancer-ip" {
    value = google_compute_address.default.address
}
