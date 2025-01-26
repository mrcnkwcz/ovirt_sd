"""
oVirt SD constants module.

Contains constants for discovery hosts and virtual machines and formatting labels.
"""

import ovirtsdk4.types as sdk_types

# General constants
META_LABEL_PREFIX = "__meta_"
OVIRT_LABEL_PREFIX = META_LABEL_PREFIX + "ovirt_"


# Host constants
OVIRT_DISCOVERY_HOST_FOLLOW = "affinity_labels,cluster,tags"
OVIRT_DISCOVERY_HOST_STATUSES = (
    sdk_types.HostStatus.ERROR,
    sdk_types.HostStatus.NON_OPERATIONAL,
    sdk_types.HostStatus.UP,
    sdk_types.HostStatus.NON_RESPONSIVE,
)

OVIRT_LABEL_HOST_ID = OVIRT_LABEL_PREFIX + "host_id"
OVIRT_LABEL_HOST_NAME = OVIRT_LABEL_PREFIX + "host_name"
OVIRT_LABEL_HOST_CLUSTER = OVIRT_LABEL_PREFIX + "host_cluster"
OVIRT_LABEL_HOST_STATUS = OVIRT_LABEL_PREFIX + "host_status"
OVIRT_LABEL_HOST_ADDRESS = OVIRT_LABEL_PREFIX + "host_address"
OVIRT_LABEL_HOST_TAG_PREFIX = OVIRT_LABEL_PREFIX + "host_tag_"
OVIRT_LABEL_HOST_AFFINITY_LABEL_PREFIX = OVIRT_LABEL_PREFIX + "host_affinity_label_"

# Vm constants
OVIRT_DISCOVERY_VM_FOLLOW = (
    "affinity_labels,cluster,template,reported_devices,tags,original_template"
)
OVIRT_DISCOVERY_VM_STATUSES = (
    sdk_types.VmStatus.IMAGE_LOCKED,
    sdk_types.VmStatus.MIGRATING,
    sdk_types.VmStatus.SAVING_STATE,
    sdk_types.VmStatus.UNKNOWN,
    sdk_types.VmStatus.UP,
)
OVIRT_LABEL_VM_ID = OVIRT_LABEL_PREFIX + "vm_id"
OVIRT_LABEL_VM_NAME = OVIRT_LABEL_PREFIX + "vm_name"
OVIRT_LABEL_VM_CLUSTER = OVIRT_LABEL_PREFIX + "vm_cluster"
OVIRT_LABEL_VM_STATUS = OVIRT_LABEL_PREFIX + "vm_status"
OVIRT_LABEL_VM_OS = OVIRT_LABEL_PREFIX + "vm_os"
OVIRT_LABEL_VM_TEMPLATE = OVIRT_LABEL_PREFIX + "vm_template"
OVIRT_LABEL_VM_ORIGINAL_TEMPLATE = OVIRT_LABEL_PREFIX + "vm_original_template"
OVIRT_LABEL_VM_FQDN = OVIRT_LABEL_PREFIX + "vm_fqdn"
OVIRT_LABEL_VM_IP_V4_PREFIX = OVIRT_LABEL_PREFIX + "vm_ip_v4_"
OVIRT_LABEL_VM_IP_V6_PREFIX = OVIRT_LABEL_PREFIX + "vm_ip_v6_"
OVIRT_LABEL_VM_TAG_PREFIX = OVIRT_LABEL_PREFIX + "vm_tag_"
OVIRT_LABEL_VM_AFFINITY_LABEL_PREFIX = OVIRT_LABEL_PREFIX + "vm_affinity_label_"
