"""
oVirt Service Discovery module
"""
import ovirtsdk4 as sdk
import ovirtsdk4.types as sdk_types

from ovirt_sd.constants import (
    OVIRT_DISCOVERY_VM_FOLLOW,
    OVIRT_DISCOVERY_VM_STATUSES,
    OVIRT_LABEL_VM_ID,
    OVIRT_LABEL_VM_NAME,
    OVIRT_LABEL_VM_CLUSTER,
    OVIRT_LABEL_VM_STATUS,
    OVIRT_LABEL_VM_OS,
    OVIRT_LABEL_VM_TEMPLATE,
    OVIRT_LABEL_VM_ORIGINAL_TEMPLATE,
    OVIRT_LABEL_VM_FQDN,
    OVIRT_LABEL_VM_IP_V4_PREFIX,
    OVIRT_LABEL_VM_IP_V6_PREFIX,
    OVIRT_LABEL_VM_TAG_PREFIX,
    OVIRT_LABEL_VM_AFFINITY_LABEL_PREFIX,
)

from ovirt_sd.constants import (
    OVIRT_DISCOVERY_HOST_FOLLOW,
    OVIRT_DISCOVERY_HOST_STATUSES,
    OVIRT_LABEL_HOST_ID,
    OVIRT_LABEL_HOST_NAME,
    OVIRT_LABEL_HOST_CLUSTER,
    OVIRT_LABEL_HOST_STATUS,
    OVIRT_LABEL_HOST_TAG_PREFIX,
    OVIRT_LABEL_HOST_AFFINITY_LABEL_PREFIX,
)


class ServiceDiscovery:
    """Base discovery"""

    def __init__(self, connection: sdk.Connection):
        """Init Service Discovery"""
        self.connection = connection

    def connect(self) -> sdk.Connection:
        """Connect to Engine"""
        return self.connection

    def disconnect(self) -> None:
        """Disconnect from Engine"""
        self.connection.close()

    def get_targets_group(self):
        """
        Get targets groups.
        If there were no targets or they did not match the search, an empty list is returned.
        """
        targets_group = []
        for d in self._discover():
            targets = self._get_targets(d)
            if not targets:
                continue
            targets_group.append(targets)
        return targets_group

    def _discover(self) -> list:
        """Return a list of discovered objects."""
        raise NotImplementedError

    def _get_targets(self, o) -> dict:
        """Return a targets from discovered objects."""
        raise NotImplementedError


class HostsServiceDiscovery(ServiceDiscovery):
    """Discovery virtualization hosts class."""

    def _discover(self) -> list[sdk_types.Host]:
        """Discovery virtualization hosts."""
        return (
            self.connection.system_service()
            .hosts_service()
            .list(follow=OVIRT_DISCOVERY_HOST_FOLLOW)
        )

    def _get_targets(self, o) -> dict:
        """
        Get targets from virtualization hosts.
        If the host parameters do not meet the conditions, it returns an empty dictionary.
        """
        targets = [o.address]
        labels = {
            OVIRT_LABEL_HOST_ID: o.id,
            OVIRT_LABEL_HOST_NAME: o.name,
            OVIRT_LABEL_HOST_CLUSTER: o.cluster.name,
            OVIRT_LABEL_HOST_STATUS: o.status.name,
            **{f"{OVIRT_LABEL_HOST_TAG_PREFIX}{t.name}": "true" for t in o.tags},
            **{
                f"{OVIRT_LABEL_HOST_AFFINITY_LABEL_PREFIX}{a.name}": "true"
                for a in o.affinity_labels
            },
        }
        if targets and o.status in OVIRT_DISCOVERY_HOST_STATUSES:
            return {
                "targets": targets,
                "labels": labels,
            }
        return {}


class VMServiceDiscovery(ServiceDiscovery):
    """Discovery virtual machines class."""

    def _discover(self) -> list[sdk_types.Vm]:
        """Discovery virtual machines."""
        return (
            self.connection.system_service()
            .vms_service()
            .list(follow=OVIRT_DISCOVERY_VM_FOLLOW)
        )

    def _get_targets(self, o: sdk_types.Vm) -> dict:
        """
        Get targets from virtual machine.
        If the VM parameters do not meet the conditions, it returns an empty dictionary.
        """
        targets = []
        ips = [
            ip.address
            for device in o.reported_devices
            if device.ips
            for ip in device.ips
        ]
        ips_v4 = [ip for ip in ips if "." in ip]
        ips_v6 = [ip for ip in ips if ":" in ip]
        if ips_v4:
            targets = [ips_v4[0]]
        elif ips_v6:
            targets = [ips_v6[0]]
        else:
            return {}
        labels = {
            OVIRT_LABEL_VM_ID: o.id,
            OVIRT_LABEL_VM_NAME: o.name,
            OVIRT_LABEL_VM_CLUSTER: o.cluster.name,
            OVIRT_LABEL_VM_STATUS: o.status.name,
            OVIRT_LABEL_VM_OS: o.os.type,
            OVIRT_LABEL_VM_TEMPLATE: o.template.name,
            OVIRT_LABEL_VM_ORIGINAL_TEMPLATE: o.original_template.name,
            OVIRT_LABEL_VM_FQDN: o.fqdn,
            **{f"{OVIRT_LABEL_VM_IP_V4_PREFIX}{i}": ip for i, ip in enumerate(ips_v4)},
            **{f"{OVIRT_LABEL_VM_IP_V6_PREFIX}{i}": ip for i, ip in enumerate(ips_v6)},
            **{f"{OVIRT_LABEL_VM_TAG_PREFIX + t.name}": "true" for t in o.tags},
            **{
                f"{OVIRT_LABEL_VM_AFFINITY_LABEL_PREFIX}{a.name}": "true"
                for a in o.affinity_labels
            },
        }
        if targets and o.status in OVIRT_DISCOVERY_VM_STATUSES:
            return {
                "targets": targets,
                "labels": labels,
            }
        return {}
