# echoMesh - Terraform Variable File
# Node deployment variables for sovereign field mesh network

project_name     = "echoMesh"
environment      = "field"
region           = "ap-southeast-2"
node_count       = 5
node_type        = "esp32"
auth_mode        = "dag_trustless"
mesh_protocol    = "LoRa"
gps_enabled      = false
encryption       = "ECC"
developer_alias  = "Internal_Vibe"

tags = {
  project   = "echoMesh"
  author    = "callum-m"
  identity  = "node0"
  presence  = "still"
  mode      = "emergent"
}