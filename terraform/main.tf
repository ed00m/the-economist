provider "google" {
    credentials = file("account.json")
    project     = var.project
    region      = var.region
    zone        = var.location
}

resource "google_compute_network" "default" {
    name                    = var.network_name
    auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "default" {
    name                     = var.network_name
    ip_cidr_range            = var.ip_cidr_range
    network                  = google_compute_network.default.self_link
    region                   = var.region
    private_ip_google_access = true
}

data "google_client_config" "current" {}

data "google_container_engine_versions" "default" {
    location = var.location
}

resource "google_container_cluster" "default" {
    name               = var.cluster_name
    location           = var.location
    initial_node_count = var.initial_node_count
    min_master_version = data.google_container_engine_versions.default.latest_master_version
    network            = google_compute_subnetwork.default.name
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

resource "google_container_node_pool" "default_preemptible_nodes" {
    name       = var.default_preemptible_nodes
    location   = var.location
    cluster    = google_container_cluster.default.name
    node_count = var.initial_node_count

    management {
        auto_repair = true
    }

    node_config {
        preemptible  = true
        machine_type = var.machine_type

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
}

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
