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
    "network perimeter profile access-rule show",
)
class Show(AAZCommand):
    """Gets the specified NSP access rule by name.

    :example: Get NSP access rule
        az network perimeter profile access-rule show -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2023-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecurityperimeters/{}/profiles/{}/accessrules/{}", "2023-07-01-preview"],
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
        _args_schema.access_rule_name = AAZStrArg(
            options=["-n", "--name", "--access-rule-name"],
            help="The name of the NSP access rule.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.perimeter_name = AAZStrArg(
            options=["--perimeter-name"],
            help="The name of the network security perimeter.",
            required=True,
            id_part="name",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="The name of the NSP profile.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NspAccessRulesGet(ctx=self.ctx)()
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

    class NspAccessRulesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}/profiles/{profileName}/accessRules/{accessRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accessRuleName", self.ctx.args.access_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkSecurityPerimeterName", self.ctx.args.perimeter_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2023-07-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )
            properties.direction = AAZStrType()
            properties.email_addresses = AAZListType(
                serialized_name="emailAddresses",
            )
            properties.fully_qualified_domain_names = AAZListType(
                serialized_name="fullyQualifiedDomainNames",
            )
            properties.network_security_perimeters = AAZListType(
                serialized_name="networkSecurityPerimeters",
                flags={"read_only": True},
            )
            properties.phone_numbers = AAZListType(
                serialized_name="phoneNumbers",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.subscriptions = AAZListType()

            address_prefixes = cls._schema_on_200.properties.address_prefixes
            address_prefixes.Element = AAZStrType()

            email_addresses = cls._schema_on_200.properties.email_addresses
            email_addresses.Element = AAZStrType()

            fully_qualified_domain_names = cls._schema_on_200.properties.fully_qualified_domain_names
            fully_qualified_domain_names.Element = AAZStrType()

            network_security_perimeters = cls._schema_on_200.properties.network_security_perimeters
            network_security_perimeters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_security_perimeters.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.perimeter_guid = AAZStrType(
                serialized_name="perimeterGuid",
                flags={"read_only": True},
            )

            phone_numbers = cls._schema_on_200.properties.phone_numbers
            phone_numbers.Element = AAZStrType()

            subscriptions = cls._schema_on_200.properties.subscriptions
            subscriptions.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.subscriptions.Element
            _element.id = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]