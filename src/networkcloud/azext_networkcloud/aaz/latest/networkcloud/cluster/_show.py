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
    "networkcloud cluster show",
)
class Show(AAZCommand):
    """Get properties of the provided cluster.

    :example: Get cluster
        az networkcloud cluster show --name "clusterName" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2025-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/clusters/{}", "2025-02-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the cluster.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ClustersGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}",
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
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
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
                    "api-version", "2025-02-01",
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
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _ShowHelper._build_schema_extended_location_read(_schema_on_200.extended_location)
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZIdentityObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType(
                nullable=True,
            )

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.aggregator_or_single_rack_definition = AAZObjectType(
                serialized_name="aggregatorOrSingleRackDefinition",
                flags={"required": True},
            )
            _ShowHelper._build_schema_rack_definition_read(properties.aggregator_or_single_rack_definition)
            properties.analytics_output_settings = AAZObjectType(
                serialized_name="analyticsOutputSettings",
            )
            properties.analytics_workspace_id = AAZStrType(
                serialized_name="analyticsWorkspaceId",
            )
            properties.available_upgrade_versions = AAZListType(
                serialized_name="availableUpgradeVersions",
                flags={"read_only": True},
            )
            properties.cluster_capacity = AAZObjectType(
                serialized_name="clusterCapacity",
                flags={"read_only": True},
            )
            properties.cluster_connection_status = AAZStrType(
                serialized_name="clusterConnectionStatus",
                flags={"read_only": True},
            )
            properties.cluster_extended_location = AAZObjectType(
                serialized_name="clusterExtendedLocation",
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_extended_location_read(properties.cluster_extended_location)
            properties.cluster_location = AAZStrType(
                serialized_name="clusterLocation",
            )
            properties.cluster_manager_connection_status = AAZStrType(
                serialized_name="clusterManagerConnectionStatus",
                flags={"read_only": True},
            )
            properties.cluster_manager_id = AAZStrType(
                serialized_name="clusterManagerId",
                flags={"read_only": True},
            )
            properties.cluster_service_principal = AAZObjectType(
                serialized_name="clusterServicePrincipal",
            )
            properties.cluster_type = AAZStrType(
                serialized_name="clusterType",
                flags={"required": True},
            )
            properties.cluster_version = AAZStrType(
                serialized_name="clusterVersion",
                flags={"required": True},
            )
            properties.command_output_settings = AAZObjectType(
                serialized_name="commandOutputSettings",
            )
            properties.compute_deployment_threshold = AAZObjectType(
                serialized_name="computeDeploymentThreshold",
            )
            properties.compute_rack_definitions = AAZListType(
                serialized_name="computeRackDefinitions",
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.hybrid_aks_extended_location = AAZObjectType(
                serialized_name="hybridAksExtendedLocation",
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_extended_location_read(properties.hybrid_aks_extended_location)
            properties.managed_resource_group_configuration = AAZObjectType(
                serialized_name="managedResourceGroupConfiguration",
            )
            properties.manual_action_count = AAZIntType(
                serialized_name="manualActionCount",
                flags={"read_only": True},
            )
            properties.network_fabric_id = AAZStrType(
                serialized_name="networkFabricId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.runtime_protection_configuration = AAZObjectType(
                serialized_name="runtimeProtectionConfiguration",
            )
            properties.secret_archive = AAZObjectType(
                serialized_name="secretArchive",
            )
            properties.secret_archive_settings = AAZObjectType(
                serialized_name="secretArchiveSettings",
            )
            properties.support_expiry_date = AAZStrType(
                serialized_name="supportExpiryDate",
                flags={"read_only": True},
            )
            properties.update_strategy = AAZObjectType(
                serialized_name="updateStrategy",
            )
            properties.vulnerability_scanning_settings = AAZObjectType(
                serialized_name="vulnerabilityScanningSettings",
            )
            properties.workload_resource_ids = AAZListType(
                serialized_name="workloadResourceIds",
                flags={"read_only": True},
            )

            analytics_output_settings = cls._schema_on_200.properties.analytics_output_settings
            analytics_output_settings.analytics_workspace_id = AAZStrType(
                serialized_name="analyticsWorkspaceId",
            )
            analytics_output_settings.associated_identity = AAZObjectType(
                serialized_name="associatedIdentity",
            )
            _ShowHelper._build_schema_identity_selector_read(analytics_output_settings.associated_identity)

            available_upgrade_versions = cls._schema_on_200.properties.available_upgrade_versions
            available_upgrade_versions.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.available_upgrade_versions.Element
            _element.control_impact = AAZStrType(
                serialized_name="controlImpact",
                flags={"read_only": True},
            )
            _element.expected_duration = AAZStrType(
                serialized_name="expectedDuration",
                flags={"read_only": True},
            )
            _element.impact_description = AAZStrType(
                serialized_name="impactDescription",
                flags={"read_only": True},
            )
            _element.support_expiry_date = AAZStrType(
                serialized_name="supportExpiryDate",
                flags={"read_only": True},
            )
            _element.target_cluster_version = AAZStrType(
                serialized_name="targetClusterVersion",
                flags={"read_only": True},
            )
            _element.workload_impact = AAZStrType(
                serialized_name="workloadImpact",
                flags={"read_only": True},
            )

            cluster_capacity = cls._schema_on_200.properties.cluster_capacity
            cluster_capacity.available_appliance_storage_gb = AAZIntType(
                serialized_name="availableApplianceStorageGB",
            )
            cluster_capacity.available_core_count = AAZIntType(
                serialized_name="availableCoreCount",
            )
            cluster_capacity.available_host_storage_gb = AAZIntType(
                serialized_name="availableHostStorageGB",
            )
            cluster_capacity.available_memory_gb = AAZIntType(
                serialized_name="availableMemoryGB",
            )
            cluster_capacity.total_appliance_storage_gb = AAZIntType(
                serialized_name="totalApplianceStorageGB",
            )
            cluster_capacity.total_core_count = AAZIntType(
                serialized_name="totalCoreCount",
            )
            cluster_capacity.total_host_storage_gb = AAZIntType(
                serialized_name="totalHostStorageGB",
            )
            cluster_capacity.total_memory_gb = AAZIntType(
                serialized_name="totalMemoryGB",
            )

            cluster_service_principal = cls._schema_on_200.properties.cluster_service_principal
            cluster_service_principal.application_id = AAZStrType(
                serialized_name="applicationId",
                flags={"required": True},
            )
            cluster_service_principal.password = AAZStrType(
                flags={"secret": True},
            )
            cluster_service_principal.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"required": True},
            )
            cluster_service_principal.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"required": True},
            )

            command_output_settings = cls._schema_on_200.properties.command_output_settings
            command_output_settings.associated_identity = AAZObjectType(
                serialized_name="associatedIdentity",
            )
            _ShowHelper._build_schema_identity_selector_read(command_output_settings.associated_identity)
            command_output_settings.container_url = AAZStrType(
                serialized_name="containerUrl",
            )

            compute_deployment_threshold = cls._schema_on_200.properties.compute_deployment_threshold
            compute_deployment_threshold.grouping = AAZStrType(
                flags={"required": True},
            )
            compute_deployment_threshold.type = AAZStrType(
                flags={"required": True},
            )
            compute_deployment_threshold.value = AAZIntType(
                flags={"required": True},
            )

            compute_rack_definitions = cls._schema_on_200.properties.compute_rack_definitions
            compute_rack_definitions.Element = AAZObjectType()
            _ShowHelper._build_schema_rack_definition_read(compute_rack_definitions.Element)

            managed_resource_group_configuration = cls._schema_on_200.properties.managed_resource_group_configuration
            managed_resource_group_configuration.location = AAZStrType()
            managed_resource_group_configuration.name = AAZStrType()

            runtime_protection_configuration = cls._schema_on_200.properties.runtime_protection_configuration
            runtime_protection_configuration.enforcement_level = AAZStrType(
                serialized_name="enforcementLevel",
            )

            secret_archive = cls._schema_on_200.properties.secret_archive
            secret_archive.key_vault_id = AAZStrType(
                serialized_name="keyVaultId",
                flags={"required": True},
            )
            secret_archive.use_key_vault = AAZStrType(
                serialized_name="useKeyVault",
            )

            secret_archive_settings = cls._schema_on_200.properties.secret_archive_settings
            secret_archive_settings.associated_identity = AAZObjectType(
                serialized_name="associatedIdentity",
            )
            _ShowHelper._build_schema_identity_selector_read(secret_archive_settings.associated_identity)
            secret_archive_settings.vault_uri = AAZStrType(
                serialized_name="vaultUri",
            )

            update_strategy = cls._schema_on_200.properties.update_strategy
            update_strategy.max_unavailable = AAZIntType(
                serialized_name="maxUnavailable",
            )
            update_strategy.strategy_type = AAZStrType(
                serialized_name="strategyType",
                flags={"required": True},
            )
            update_strategy.threshold_type = AAZStrType(
                serialized_name="thresholdType",
                flags={"required": True},
            )
            update_strategy.threshold_value = AAZIntType(
                serialized_name="thresholdValue",
                flags={"required": True},
            )
            update_strategy.wait_time_minutes = AAZIntType(
                serialized_name="waitTimeMinutes",
            )

            vulnerability_scanning_settings = cls._schema_on_200.properties.vulnerability_scanning_settings
            vulnerability_scanning_settings.container_scan = AAZStrType(
                serialized_name="containerScan",
            )

            workload_resource_ids = cls._schema_on_200.properties.workload_resource_ids
            workload_resource_ids.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_administrative_credentials_read = None

    @classmethod
    def _build_schema_administrative_credentials_read(cls, _schema):
        if cls._schema_administrative_credentials_read is not None:
            _schema.password = cls._schema_administrative_credentials_read.password
            _schema.username = cls._schema_administrative_credentials_read.username
            return

        cls._schema_administrative_credentials_read = _schema_administrative_credentials_read = AAZObjectType()

        administrative_credentials_read = _schema_administrative_credentials_read
        administrative_credentials_read.password = AAZStrType(
            flags={"secret": True},
        )
        administrative_credentials_read.username = AAZStrType(
            flags={"required": True},
        )

        _schema.password = cls._schema_administrative_credentials_read.password
        _schema.username = cls._schema_administrative_credentials_read.username

    _schema_extended_location_read = None

    @classmethod
    def _build_schema_extended_location_read(cls, _schema):
        if cls._schema_extended_location_read is not None:
            _schema.name = cls._schema_extended_location_read.name
            _schema.type = cls._schema_extended_location_read.type
            return

        cls._schema_extended_location_read = _schema_extended_location_read = AAZObjectType()

        extended_location_read = _schema_extended_location_read
        extended_location_read.name = AAZStrType(
            flags={"required": True},
        )
        extended_location_read.type = AAZStrType(
            flags={"required": True},
        )

        _schema.name = cls._schema_extended_location_read.name
        _schema.type = cls._schema_extended_location_read.type

    _schema_identity_selector_read = None

    @classmethod
    def _build_schema_identity_selector_read(cls, _schema):
        if cls._schema_identity_selector_read is not None:
            _schema.identity_type = cls._schema_identity_selector_read.identity_type
            _schema.user_assigned_identity_resource_id = cls._schema_identity_selector_read.user_assigned_identity_resource_id
            return

        cls._schema_identity_selector_read = _schema_identity_selector_read = AAZObjectType()

        identity_selector_read = _schema_identity_selector_read
        identity_selector_read.identity_type = AAZStrType(
            serialized_name="identityType",
        )
        identity_selector_read.user_assigned_identity_resource_id = AAZStrType(
            serialized_name="userAssignedIdentityResourceId",
            nullable=True,
        )

        _schema.identity_type = cls._schema_identity_selector_read.identity_type
        _schema.user_assigned_identity_resource_id = cls._schema_identity_selector_read.user_assigned_identity_resource_id

    _schema_rack_definition_read = None

    @classmethod
    def _build_schema_rack_definition_read(cls, _schema):
        if cls._schema_rack_definition_read is not None:
            _schema.availability_zone = cls._schema_rack_definition_read.availability_zone
            _schema.bare_metal_machine_configuration_data = cls._schema_rack_definition_read.bare_metal_machine_configuration_data
            _schema.network_rack_id = cls._schema_rack_definition_read.network_rack_id
            _schema.rack_location = cls._schema_rack_definition_read.rack_location
            _schema.rack_serial_number = cls._schema_rack_definition_read.rack_serial_number
            _schema.rack_sku_id = cls._schema_rack_definition_read.rack_sku_id
            _schema.storage_appliance_configuration_data = cls._schema_rack_definition_read.storage_appliance_configuration_data
            return

        cls._schema_rack_definition_read = _schema_rack_definition_read = AAZObjectType()

        rack_definition_read = _schema_rack_definition_read
        rack_definition_read.availability_zone = AAZStrType(
            serialized_name="availabilityZone",
        )
        rack_definition_read.bare_metal_machine_configuration_data = AAZListType(
            serialized_name="bareMetalMachineConfigurationData",
        )
        rack_definition_read.network_rack_id = AAZStrType(
            serialized_name="networkRackId",
            flags={"required": True},
        )
        rack_definition_read.rack_location = AAZStrType(
            serialized_name="rackLocation",
        )
        rack_definition_read.rack_serial_number = AAZStrType(
            serialized_name="rackSerialNumber",
            flags={"required": True},
        )
        rack_definition_read.rack_sku_id = AAZStrType(
            serialized_name="rackSkuId",
            flags={"required": True},
        )
        rack_definition_read.storage_appliance_configuration_data = AAZListType(
            serialized_name="storageApplianceConfigurationData",
        )

        bare_metal_machine_configuration_data = _schema_rack_definition_read.bare_metal_machine_configuration_data
        bare_metal_machine_configuration_data.Element = AAZObjectType()

        _element = _schema_rack_definition_read.bare_metal_machine_configuration_data.Element
        _element.bmc_connection_string = AAZStrType(
            serialized_name="bmcConnectionString",
            flags={"read_only": True},
        )
        _element.bmc_credentials = AAZObjectType(
            serialized_name="bmcCredentials",
            flags={"required": True},
        )
        cls._build_schema_administrative_credentials_read(_element.bmc_credentials)
        _element.bmc_mac_address = AAZStrType(
            serialized_name="bmcMacAddress",
            flags={"required": True},
        )
        _element.boot_mac_address = AAZStrType(
            serialized_name="bootMacAddress",
            flags={"required": True},
        )
        _element.machine_details = AAZStrType(
            serialized_name="machineDetails",
        )
        _element.machine_name = AAZStrType(
            serialized_name="machineName",
        )
        _element.rack_slot = AAZIntType(
            serialized_name="rackSlot",
            flags={"required": True},
        )
        _element.serial_number = AAZStrType(
            serialized_name="serialNumber",
            flags={"required": True},
        )

        storage_appliance_configuration_data = _schema_rack_definition_read.storage_appliance_configuration_data
        storage_appliance_configuration_data.Element = AAZObjectType()

        _element = _schema_rack_definition_read.storage_appliance_configuration_data.Element
        _element.admin_credentials = AAZObjectType(
            serialized_name="adminCredentials",
            flags={"required": True},
        )
        cls._build_schema_administrative_credentials_read(_element.admin_credentials)
        _element.rack_slot = AAZIntType(
            serialized_name="rackSlot",
            flags={"required": True},
        )
        _element.serial_number = AAZStrType(
            serialized_name="serialNumber",
            flags={"required": True},
        )
        _element.storage_appliance_name = AAZStrType(
            serialized_name="storageApplianceName",
        )

        _schema.availability_zone = cls._schema_rack_definition_read.availability_zone
        _schema.bare_metal_machine_configuration_data = cls._schema_rack_definition_read.bare_metal_machine_configuration_data
        _schema.network_rack_id = cls._schema_rack_definition_read.network_rack_id
        _schema.rack_location = cls._schema_rack_definition_read.rack_location
        _schema.rack_serial_number = cls._schema_rack_definition_read.rack_serial_number
        _schema.rack_sku_id = cls._schema_rack_definition_read.rack_sku_id
        _schema.storage_appliance_configuration_data = cls._schema_rack_definition_read.storage_appliance_configuration_data


__all__ = ["Show"]
