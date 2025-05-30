# echoMesh - Terraform Variable File
# Node deployment variables for sovereign field mesh network

environment         = "echo-field"
region              = "ap-southeast-2"
availability_zone   = "az-1"
instance_type       = "t3.micro"
node_count          = 3
mesh_id             = "echomesh-001"
enable_loRa_module  = true
enable_gps_sync     = true
enable_signal_cache = true
mesh_mode           = "loiter"
encryption_key_path = "/secrets/field-auth.key"
data_retention_days = 7
logging_level       = "minimal"
deploy_via_drone    = false # unless explicitly specified

tags = {
  project   = "echoMesh"
  author    = "callum-m"
  identity  = "node0"
  presence  = "still"
  mode      = "emergent"
}