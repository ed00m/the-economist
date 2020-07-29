# GKE - Cluster engine versions
data "google_container_engine_versions" "default" {
    location = var.zone
}

# GKE - Cluster
resource "google_container_cluster" "default" {
    name               = var.cluster_name
    location           = var.zone
    initial_node_count = var.cluster_initial_node_count
    min_master_version = data.google_container_engine_versions.default.latest_master_version
    network            = google_compute_network.default.name
    subnetwork         = google_compute_subnetwork.default.name

    # We can't create a cluster with no node pool defined, but we want to only use
    # separately managed node pools. So we create the smallest possible default
    # node pool and immediately delete it.
    remove_default_node_pool = true

    master_auth {
        username = ""
        password = ""

        client_certificate_config {
            issue_client_certificate = false
        }
    }

    // Use legacy ABAC until these issues are resolved:
    //   https://github.com/mcuadros/terraform-provider-helm/issues/56
    //   https://github.com/terraform-providers/terraform-provider-kubernetes/pull/73
    enable_legacy_abac = true

    // Wait for the GCE LB controller to cleanup the resources.
    // Wait for the GCE LB controller to cleanup the resources.
    provisioner "local-exec" {
        when    = destroy
        command = "sleep 90"
    }
}

# GKE - Node Pool
resource "google_container_node_pool" "default" {
    name       = var.node_pool_preemptible
    location   = var.zone
    cluster    = google_container_cluster.default.name
    node_count = var.cluster_initial_node_count

    management {
        auto_repair = true
    }

    node_config {
        preemptible  = true
        machine_type = var.cluster_node_machine_type

        metadata = {
            disable-legacy-endpoints = "true"
        }

        oauth_scopes = [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ]
    }

    # cluster_autoscaling {
    #     enabled = true
    #
    #     resource_limits {
    #         maximum       = (known after apply)
    #         minimum       = (known after apply)
    #         resource_type = (known after apply)
    #     }
    # }
}

# Environment - Output
output "network" {
    value = google_compute_subnetwork.default.network
}

output "subnetwork_name" {
    value = google_compute_subnetwork.default.name
}

output "cluster_name" {
    value = google_container_cluster.default.name
}

output "cluster_region" {
    value = var.region
}

output "cluster_location" {
    value = google_container_cluster.default.location
}
