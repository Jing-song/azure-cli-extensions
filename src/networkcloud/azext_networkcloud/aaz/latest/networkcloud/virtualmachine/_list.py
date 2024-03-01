# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkcloud virtualmachine list",
    is_preview=True,
)
class List(AAZCommand):
    """List virtual machines in the provided resource group or subscription.

    :example: List virtual machines for resource group
        az networkcloud virtualmachine list --resource-group "resourceGroupName"

    :example: List virtual machines for subscription
        az networkcloud virtualmachine list
    """

    _aaz_info = {
        "version": "2023-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.networkcloud/virtualmachines", "2023-10-01-preview"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/virtualmachines", "2023-10-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.VirtualMachinesListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.VirtualMachinesListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VirtualMachinesListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/virtualMachines",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.admin_username = AAZStrType(
                serialized_name="adminUsername",
                flags={"required": True},
            )
            properties.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
                flags={"read_only": True},
            )
            properties.bare_metal_machine_id = AAZStrType(
                serialized_name="bareMetalMachineId",
                flags={"read_only": True},
            )
            properties.boot_method = AAZStrType(
                serialized_name="bootMethod",
            )
            properties.cloud_services_network_attachment = AAZObjectType(
                serialized_name="cloudServicesNetworkAttachment",
                flags={"required": True},
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.cpu_cores = AAZIntType(
                serialized_name="cpuCores",
                flags={"required": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.isolate_emulator_thread = AAZStrType(
                serialized_name="isolateEmulatorThread",
            )
            properties.memory_size_gb = AAZIntType(
                serialized_name="memorySizeGB",
                flags={"required": True},
            )
            properties.network_attachments = AAZListType(
                serialized_name="networkAttachments",
            )
            properties.network_data = AAZStrType(
                serialized_name="networkData",
            )
            properties.placement_hints = AAZListType(
                serialized_name="placementHints",
            )
            properties.power_state = AAZStrType(
                serialized_name="powerState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.ssh_public_keys = AAZListType(
                serialized_name="sshPublicKeys",
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
                flags={"required": True},
            )
            properties.user_data = AAZStrType(
                serialized_name="userData",
            )
            properties.virtio_interface = AAZStrType(
                serialized_name="virtioInterface",
            )
            properties.vm_device_model = AAZStrType(
                serialized_name="vmDeviceModel",
            )
            properties.vm_image = AAZStrType(
                serialized_name="vmImage",
                flags={"required": True},
            )
            properties.vm_image_repository_credentials = AAZObjectType(
                serialized_name="vmImageRepositoryCredentials",
            )
            properties.volumes = AAZListType(
                flags={"read_only": True},
            )

            cloud_services_network_attachment = cls._schema_on_200.value.Element.properties.cloud_services_network_attachment
            cloud_services_network_attachment.attached_network_id = AAZStrType(
                serialized_name="attachedNetworkId",
                flags={"required": True},
            )
            cloud_services_network_attachment.default_gateway = AAZStrType(
                serialized_name="defaultGateway",
            )
            cloud_services_network_attachment.ip_allocation_method = AAZStrType(
                serialized_name="ipAllocationMethod",
                flags={"required": True},
            )
            cloud_services_network_attachment.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            cloud_services_network_attachment.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )
            cloud_services_network_attachment.mac_address = AAZStrType(
                serialized_name="macAddress",
                flags={"read_only": True},
            )
            cloud_services_network_attachment.network_attachment_name = AAZStrType(
                serialized_name="networkAttachmentName",
            )

            network_attachments = cls._schema_on_200.value.Element.properties.network_attachments
            network_attachments.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.network_attachments.Element
            _element.attached_network_id = AAZStrType(
                serialized_name="attachedNetworkId",
                flags={"required": True},
            )
            _element.default_gateway = AAZStrType(
                serialized_name="defaultGateway",
            )
            _element.ip_allocation_method = AAZStrType(
                serialized_name="ipAllocationMethod",
                flags={"required": True},
            )
            _element.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            _element.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )
            _element.mac_address = AAZStrType(
                serialized_name="macAddress",
                flags={"read_only": True},
            )
            _element.network_attachment_name = AAZStrType(
                serialized_name="networkAttachmentName",
            )

            placement_hints = cls._schema_on_200.value.Element.properties.placement_hints
            placement_hints.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.placement_hints.Element
            _element.hint_type = AAZStrType(
                serialized_name="hintType",
                flags={"required": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )
            _element.scheduling_execution = AAZStrType(
                serialized_name="schedulingExecution",
                flags={"required": True},
            )
            _element.scope = AAZStrType(
                flags={"required": True},
            )

            ssh_public_keys = cls._schema_on_200.value.Element.properties.ssh_public_keys
            ssh_public_keys.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ssh_public_keys.Element
            _element.key_data = AAZStrType(
                serialized_name="keyData",
                flags={"required": True},
            )

            storage_profile = cls._schema_on_200.value.Element.properties.storage_profile
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
                flags={"required": True},
            )
            storage_profile.volume_attachments = AAZListType(
                serialized_name="volumeAttachments",
            )

            os_disk = cls._schema_on_200.value.Element.properties.storage_profile.os_disk
            os_disk.create_option = AAZStrType(
                serialized_name="createOption",
            )
            os_disk.delete_option = AAZStrType(
                serialized_name="deleteOption",
            )
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
                flags={"required": True},
            )

            volume_attachments = cls._schema_on_200.value.Element.properties.storage_profile.volume_attachments
            volume_attachments.Element = AAZStrType()

            vm_image_repository_credentials = cls._schema_on_200.value.Element.properties.vm_image_repository_credentials
            vm_image_repository_credentials.password = AAZStrType(
                flags={"secret": True},
            )
            vm_image_repository_credentials.registry_url = AAZStrType(
                serialized_name="registryUrl",
                flags={"required": True},
            )
            vm_image_repository_credentials.username = AAZStrType(
                flags={"required": True},
            )

            volumes = cls._schema_on_200.value.Element.properties.volumes
            volumes.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class VirtualMachinesListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetworkCloud/virtualMachines",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.admin_username = AAZStrType(
                serialized_name="adminUsername",
                flags={"required": True},
            )
            properties.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
                flags={"read_only": True},
            )
            properties.bare_metal_machine_id = AAZStrType(
                serialized_name="bareMetalMachineId",
                flags={"read_only": True},
            )
            properties.boot_method = AAZStrType(
                serialized_name="bootMethod",
            )
            properties.cloud_services_network_attachment = AAZObjectType(
                serialized_name="cloudServicesNetworkAttachment",
                flags={"required": True},
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.cpu_cores = AAZIntType(
                serialized_name="cpuCores",
                flags={"required": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.isolate_emulator_thread = AAZStrType(
                serialized_name="isolateEmulatorThread",
            )
            properties.memory_size_gb = AAZIntType(
                serialized_name="memorySizeGB",
                flags={"required": True},
            )
            properties.network_attachments = AAZListType(
                serialized_name="networkAttachments",
            )
            properties.network_data = AAZStrType(
                serialized_name="networkData",
            )
            properties.placement_hints = AAZListType(
                serialized_name="placementHints",
            )
            properties.power_state = AAZStrType(
                serialized_name="powerState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.ssh_public_keys = AAZListType(
                serialized_name="sshPublicKeys",
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
                flags={"required": True},
            )
            properties.user_data = AAZStrType(
                serialized_name="userData",
            )
            properties.virtio_interface = AAZStrType(
                serialized_name="virtioInterface",
            )
            properties.vm_device_model = AAZStrType(
                serialized_name="vmDeviceModel",
            )
            properties.vm_image = AAZStrType(
                serialized_name="vmImage",
                flags={"required": True},
            )
            properties.vm_image_repository_credentials = AAZObjectType(
                serialized_name="vmImageRepositoryCredentials",
            )
            properties.volumes = AAZListType(
                flags={"read_only": True},
            )

            cloud_services_network_attachment = cls._schema_on_200.value.Element.properties.cloud_services_network_attachment
            cloud_services_network_attachment.attached_network_id = AAZStrType(
                serialized_name="attachedNetworkId",
                flags={"required": True},
            )
            cloud_services_network_attachment.default_gateway = AAZStrType(
                serialized_name="defaultGateway",
            )
            cloud_services_network_attachment.ip_allocation_method = AAZStrType(
                serialized_name="ipAllocationMethod",
                flags={"required": True},
            )
            cloud_services_network_attachment.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            cloud_services_network_attachment.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )
            cloud_services_network_attachment.mac_address = AAZStrType(
                serialized_name="macAddress",
                flags={"read_only": True},
            )
            cloud_services_network_attachment.network_attachment_name = AAZStrType(
                serialized_name="networkAttachmentName",
            )

            network_attachments = cls._schema_on_200.value.Element.properties.network_attachments
            network_attachments.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.network_attachments.Element
            _element.attached_network_id = AAZStrType(
                serialized_name="attachedNetworkId",
                flags={"required": True},
            )
            _element.default_gateway = AAZStrType(
                serialized_name="defaultGateway",
            )
            _element.ip_allocation_method = AAZStrType(
                serialized_name="ipAllocationMethod",
                flags={"required": True},
            )
            _element.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            _element.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )
            _element.mac_address = AAZStrType(
                serialized_name="macAddress",
                flags={"read_only": True},
            )
            _element.network_attachment_name = AAZStrType(
                serialized_name="networkAttachmentName",
            )

            placement_hints = cls._schema_on_200.value.Element.properties.placement_hints
            placement_hints.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.placement_hints.Element
            _element.hint_type = AAZStrType(
                serialized_name="hintType",
                flags={"required": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )
            _element.scheduling_execution = AAZStrType(
                serialized_name="schedulingExecution",
                flags={"required": True},
            )
            _element.scope = AAZStrType(
                flags={"required": True},
            )

            ssh_public_keys = cls._schema_on_200.value.Element.properties.ssh_public_keys
            ssh_public_keys.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ssh_public_keys.Element
            _element.key_data = AAZStrType(
                serialized_name="keyData",
                flags={"required": True},
            )

            storage_profile = cls._schema_on_200.value.Element.properties.storage_profile
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
                flags={"required": True},
            )
            storage_profile.volume_attachments = AAZListType(
                serialized_name="volumeAttachments",
            )

            os_disk = cls._schema_on_200.value.Element.properties.storage_profile.os_disk
            os_disk.create_option = AAZStrType(
                serialized_name="createOption",
            )
            os_disk.delete_option = AAZStrType(
                serialized_name="deleteOption",
            )
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
                flags={"required": True},
            )

            volume_attachments = cls._schema_on_200.value.Element.properties.storage_profile.volume_attachments
            volume_attachments.Element = AAZStrType()

            vm_image_repository_credentials = cls._schema_on_200.value.Element.properties.vm_image_repository_credentials
            vm_image_repository_credentials.password = AAZStrType(
                flags={"secret": True},
            )
            vm_image_repository_credentials.registry_url = AAZStrType(
                serialized_name="registryUrl",
                flags={"required": True},
            )
            vm_image_repository_credentials.username = AAZStrType(
                flags={"required": True},
            )

            volumes = cls._schema_on_200.value.Element.properties.volumes
            volumes.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]