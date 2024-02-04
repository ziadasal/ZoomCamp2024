terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.1.0"
    }
  }
}

provider "local" {}

resource "local_file" "example" {
  content  = "Hello, GitHub Codespaces!"
  filename = "output.txt"
}
