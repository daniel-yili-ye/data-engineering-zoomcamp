variable "credentials" {
  description = "Credentials"
  default     = "credentials.json"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-437503"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcp_storage_name" {
  description = "Bucket Storage Name"
  default     = "terraform-demo-437503-bucket"
}

variable "gcp_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}