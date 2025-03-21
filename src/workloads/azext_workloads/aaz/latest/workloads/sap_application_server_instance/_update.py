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
    "workloads sap-application-server-instance update",
)
class Update(AAZCommand):
    """Update the SAP Application Server Instance resource. This will be used by service only. PUT by end user will return a Bad Request error.
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/sapvirtualinstances/{}/applicationinstances/{}", "2024-09-01"],
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
        _args_schema.application_instance_name = AAZStrArg(
            options=["-n", "--name", "--application-instance-name"],
            help="The name of SAP Application Server instance resource.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^.*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sap_virtual_instance_name = AAZStrArg(
            options=["--vis-name", "--sap-virtual-instance-name"],
            help="The name of the Virtual Instances for SAP solutions resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9]{2}$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Properties",
            help="Gets or sets the Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SapApplicationServerInstancesUpdate(ctx=self.ctx)()
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

    class SapApplicationServerInstancesUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/applicationInstances/{applicationInstanceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "applicationInstanceName", self.ctx.args.application_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "sapVirtualInstanceName", self.ctx.args.sap_virtual_instance_name,
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
                    "api-version", "2024-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.dispatcher_status = AAZStrType(
                serialized_name="dispatcherStatus",
                flags={"read_only": True},
            )
            properties.errors = AAZObjectType(
                flags={"read_only": True},
            )
            properties.gateway_port = AAZIntType(
                serialized_name="gatewayPort",
                flags={"read_only": True},
            )
            properties.health = AAZStrType(
                flags={"read_only": True},
            )
            properties.hostname = AAZStrType(
                flags={"read_only": True},
            )
            properties.icm_http_port = AAZIntType(
                serialized_name="icmHttpPort",
                flags={"read_only": True},
            )
            properties.icm_https_port = AAZIntType(
                serialized_name="icmHttpsPort",
                flags={"read_only": True},
            )
            properties.instance_no = AAZStrType(
                serialized_name="instanceNo",
                flags={"read_only": True},
            )
            properties.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            properties.kernel_patch = AAZStrType(
                serialized_name="kernelPatch",
                flags={"read_only": True},
            )
            properties.kernel_version = AAZStrType(
                serialized_name="kernelVersion",
                flags={"read_only": True},
            )
            properties.load_balancer_details = AAZObjectType(
                serialized_name="loadBalancerDetails",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.subnet = AAZStrType(
                flags={"read_only": True},
            )
            properties.vm_details = AAZListType(
                serialized_name="vmDetails",
                flags={"read_only": True},
            )

            errors = cls._schema_on_200.properties.errors
            errors.properties = AAZObjectType()
            _UpdateHelper._build_schema_error_definition_read(errors.properties)

            load_balancer_details = cls._schema_on_200.properties.load_balancer_details
            load_balancer_details.id = AAZStrType(
                flags={"read_only": True},
            )

            vm_details = cls._schema_on_200.properties.vm_details
            vm_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vm_details.Element
            _element.storage_details = AAZListType(
                serialized_name="storageDetails",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.virtual_machine_id = AAZStrType(
                serialized_name="virtualMachineId",
                flags={"read_only": True},
            )

            storage_details = cls._schema_on_200.properties.vm_details.Element.storage_details
            storage_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vm_details.Element.storage_details.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )

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


class _UpdateHelper:
    """Helper class for Update"""

    _schema_error_definition_read = None

    @classmethod
    def _build_schema_error_definition_read(cls, _schema):
        if cls._schema_error_definition_read is not None:
            _schema.code = cls._schema_error_definition_read.code
            _schema.details = cls._schema_error_definition_read.details
            _schema.message = cls._schema_error_definition_read.message
            return

        cls._schema_error_definition_read = _schema_error_definition_read = AAZObjectType()

        error_definition_read = _schema_error_definition_read
        error_definition_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_definition_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_definition_read.message = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_definition_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_definition_read(details.Element)

        _schema.code = cls._schema_error_definition_read.code
        _schema.details = cls._schema_error_definition_read.details
        _schema.message = cls._schema_error_definition_read.message


__all__ = ["Update"]
