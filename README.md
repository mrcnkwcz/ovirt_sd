# oVirt Service Discovery
Collection for oVirt environments

## Targets
### Host
- `__address__`: Address of the host. Can be IP or FQDN of the host
- `__meta_ovirt_host_id`: ID of the host
- `__meta_ovirt_host_name`: Name of the host
- `__meta_ovirt_host_cluster`: Name of the cluster
- `__meta_ovirt_host_status`: Status of the host
- `__meta_ovirt_host_address`: Address of the host
- `__meta_ovirt_host_tag_<tagname>`: `true` for each tag assigned to the host
- `__meta_ovirt_host_affinity_label_<labelname>`: `true` for each affinity label assigned to the host

### Virtual machine
- `__address__`: Address of the VM. Can be IPv4 or IPv6
- `__meta_ovirt_vm_id`:  ID of the VM
- `__meta_ovirt_vm_name`: Name of the VM
- `__meta_ovirt_vm_cluster`: Name of the cluster 
- `__meta_ovirt_vm_status`: Status of the VM
- `__meta_ovirt_vm_os`: OS of the VM
- `__meta_ovirt_vm_template`: Template of the VM
- `__meta_ovirt_vm_original_template`: Original template of the VM
- `__meta_ovirt_vm_fqdn`: FQDN of the VM
- `__meta_ovirt_vm_ip_v4_<number>`: IPv4 address for each IP address on VM
- `__meta_ovirt_vm_ip_v6_<number>`: IPv6 address for each IP address on VM
- `__meta_ovirt_vm_tag_<tagname>`: `true` for each tag assigned to the VM
- `__meta_ovirt_vm_affinity_label_<labelname>`: `true` for each affinity label assigned to the VM

## Env
- `OVIRT_URL`: URL Engine. Example: "https://engine.infra.example/ovirt-engine/api"
- `OVIRT_USERNAME`: Username with domain for authentication. Example: "api@internal" or "api@internalsso"
- `OVIRT_PASSWORD`: Password for user
- `OVIRT_INSECURE`: A boolean flag if the server TLS certificate should be checked. Default value is `False`
- `OVIRT_SD_TIMEOUT`: Time (in seconds) during which the connection to the server must be established. Default value is `60`
- `OVIRT_SD_PORT`: HTTP SD port

## Licenses
* Apache 2.0

## Authors
* Martsinkevich Artur (@mrcnkwcz)
