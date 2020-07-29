# terraform - Provider
provider "google" {
    credentials = file("account.json")
    project     = var.project
    region      = var.region
    zone        = var.zone
}
# Provider -Client
data "google_client_config" "current" {}

# Network - VPC
resource "google_compute_network" "default" {
    name                    = var.network_name
    auto_create_subnetworks = false
}

# Network - Subnet
resource "google_compute_subnetwork" "default" {
    name                     = "${var.network_name}-${var.zone}"
    ip_cidr_range            = var.subnetwork_cidr_range
    network                  = google_compute_network.default.self_link
    region                   = var.region
    private_ip_google_access = true
}
