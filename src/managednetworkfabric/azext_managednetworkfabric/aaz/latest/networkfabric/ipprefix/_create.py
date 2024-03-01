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
    "networkfabric ipprefix create",
)
class Create(AAZCommand):
    """Create a Ip Prefix resource

    :example: Create a Ip Prefix
        az networkfabric ipprefix create --resource-group "example-rg" --location "westus3" --resource-name "example-ipprefix" --ip-prefix-rules "[{action:Permit,sequenceNumber:1234,networkPrefix:'1.1.1.0/24',condition:EqualTo,subnetMaskLength:24}]"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric ipprefix create --ip-prefix-rules "??"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/ipprefixes/{}", "2023-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the IP Prefix.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            help="Location of Azure region",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.annotation = AAZStrArg(
            options=["--annotation"],
            arg_group="Properties",
            help="Description for underlying resource.",
        )
        _args_schema.ip_prefix_rules = AAZListArg(
            options=["--ip-prefix-rules"],
            arg_group="Properties",
            help="The list of IP Prefix Rules.",
            required=True,
        )

        ip_prefix_rules = cls._args_schema.ip_prefix_rules
        ip_prefix_rules.Element = AAZObjectArg()

        _element = cls._args_schema.ip_prefix_rules.Element
        _element.action = AAZStrArg(
            options=["action"],
            help="Action to be taken on the configuration. Example: Permit.",
            required=True,
            enum={"Deny": "Deny", "Permit": "Permit"},
        )
        _element.condition = AAZStrArg(
            options=["condition"],
            help="Specify prefix-list bounds.",
            enum={"EqualTo": "EqualTo", "GreaterThanOrEqualTo": "GreaterThanOrEqualTo", "LesserThanOrEqualTo": "LesserThanOrEqualTo", "Range": "Range"},
        )
        _element.network_prefix = AAZStrArg(
            options=["network-prefix"],
            help="Network Prefix specifying IPv4/IPv6 packets to be permitted or denied. Example: 1.1.1.0/24.",
            required=True,
        )
        _element.sequence_number = AAZIntArg(
            options=["sequence-number"],
            help="Sequence to insert to/delete from existing route. Prefix lists are evaluated starting with the lowest sequence number and continue down the list until a match is made. Once a match is made, the permit or deny statement is applied to that network and the rest of the list is ignored.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )
        _element.subnet_mask_length = AAZStrArg(
            options=["subnet-mask-length"],
            help="SubnetMaskLength gives the minimum NetworkPrefix length to be matched. Possible values for IPv4 are 1 - 32 . Possible values of IPv6 are 1 - 128.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.IpPrefixesCreate(ctx=self.ctx)()
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

    class IpPrefixesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/ipPrefixes/{ipPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "ipPrefixName", self.ctx.args.resource_name,
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
                    "api-version", "2023-06-15",
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
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("annotation", AAZStrType, ".annotation")
                properties.set_prop("ipPrefixRules", AAZListType, ".ip_prefix_rules", typ_kwargs={"flags": {"required": True}})

            ip_prefix_rules = _builder.get(".properties.ipPrefixRules")
            if ip_prefix_rules is not None:
                ip_prefix_rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ipPrefixRules[]")
            if _elements is not None:
                _elements.set_prop("action", AAZStrType, ".action", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("condition", AAZStrType, ".condition")
                _elements.set_prop("networkPrefix", AAZStrType, ".network_prefix", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("sequenceNumber", AAZIntType, ".sequence_number", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("subnetMaskLength", AAZStrType, ".subnet_mask_length")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.ip_prefix_rules = AAZListType(
                serialized_name="ipPrefixRules",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            ip_prefix_rules = cls._schema_on_200_201.properties.ip_prefix_rules
            ip_prefix_rules.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.ip_prefix_rules.Element
            _element.action = AAZStrType(
                flags={"required": True},
            )
            _element.condition = AAZStrType()
            _element.network_prefix = AAZStrType(
                serialized_name="networkPrefix",
                flags={"required": True},
            )
            _element.sequence_number = AAZIntType(
                serialized_name="sequenceNumber",
                flags={"required": True},
            )
            _element.subnet_mask_length = AAZStrType(
                serialized_name="subnetMaskLength",
            )

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]