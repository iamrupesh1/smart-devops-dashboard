terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 3.0.0"
    }
  }
}

provider "docker" {}

# Pull Nginx image
resource "docker_image" "nginx_img" {
  name = "nginx:latest"
}

# Create Nginx container
resource "docker_container" "nginx" {
  name  = "nginx"
  image = docker_image.nginx_img.image_id

  ports {
    internal = 80
    external = 8080
  }
}
