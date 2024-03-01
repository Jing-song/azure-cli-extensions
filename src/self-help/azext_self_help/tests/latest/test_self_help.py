# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer, KeyVaultPreparer
from msrestazure.tools import resource_id
import uuid


class SelfHelpScenario(ScenarioTest):

    @ResourceGroupPreparer()
    @KeyVaultPreparer()
    def test_help_discoverysolutions(self, resource_group, key_vault):

        self.kwargs.update({
            'scope': resource_id(resource_group=resource_group,
                                 subscription=self.get_subscription_id(),
                                 name=key_vault,
                                 namespace='Microsoft.KeyVault',
                                 type='vaults'),
            'filter': "\"ProblemClassificationId eq '00000000-0000-0000-0000-000000000000'\""
        })

        list_solution_discovery_result = self.cmd(
            'self-help discovery-solution list --scope {scope} --filter {filter}', checks=[
                self.check(
                    '[0].type', 'Microsoft.Help/discoverySolutions', case_sensitive=False)
            ]).get_output_in_json()
        self.assertTrue(list_solution_discovery_result is not None)
        self.assertTrue(len(list_solution_discovery_result) >= 1)
        self.assertTrue("type" in list_solution_discovery_result[0])
        self.assertTrue("name" in list_solution_discovery_result[0])
        self.assertTrue("id" in list_solution_discovery_result[0])

    @ResourceGroupPreparer()
    @KeyVaultPreparer()
    def test_help_diagnostics(self, resource_group, key_vault):

        # Create diagnostic for keyVault resource.
        diagnostic_name = self.create_random_name(prefix='cli_test', length=15)
        self.kwargs.update({
            'scope': resource_id(resource_group=resource_group,
                                 subscription=self.get_subscription_id(),
                                 name=key_vault,
                                 namespace='Microsoft.KeyVault',
                                 type='vaults'),
            'diagnostic-name': diagnostic_name,
            'insights': "[{solutionId:Demo2InsightV2}]"
        })

        create_diagnostic_result = self.cmd(
            "self-help diagnostic create --diagnostic-name {diagnostic-name}  --insights {insights} --scope {scope}", checks=[
                self.check('name', '{diagnostic-name}'),
                self.check('type', 'Microsoft.Help/Diagnostics'),
            ])
        create_diagnostic_result = create_diagnostic_result.get_output_in_json()
        self.assertTrue(create_diagnostic_result is not None)
        self.assertTrue(create_diagnostic_result["acceptedAt"] is not None)

        # Get diagnostic for keyVault resource.
        get_diagnostic_result = self.cmd(
            "self-help diagnostic show --diagnostic-name {diagnostic-name} --scope {scope}", checks=[
                self.check('name', '{diagnostic-name}'),
                self.check('type', 'Microsoft.Help/Diagnostics'),
            ])
        get_diagnostic_result = get_diagnostic_result.get_output_in_json()
        self.assertTrue(get_diagnostic_result is not None)
        self.assertTrue(get_diagnostic_result["acceptedAt"] is not None)

    def test_help_check_name_diagnostics(self):

        # Check diagnostic name availability.
        self.kwargs.update({
            'scope': resource_id(subscription=self.get_subscription_id()),
            'diagnostic-name': self.create_random_name(prefix='cli_test', length=15),
        })

        self.cmd(
            "self-help check-name-availability --scope {scope} --name {diagnostic-name} --type 'Microsoft.Help/diagnostics'", checks=[
                self.check('nameAvailable', 'True'),])
        
    def test_help_check_name_solutions(self):

        # Check solution name availability.
        self.kwargs.update({
            'scope': resource_id(subscription=self.get_subscription_id()),
            'solution-name': self.create_random_name(prefix='cli_test', length=15),
        })

        self.cmd(
            "self-help check-name-availability --scope {scope} --name {solution-name} --type 'Microsoft.Help/solutions'", checks=[
                self.check('nameAvailable', 'True'),])
    
    def test_help_check_name_troubleshooters(self):

        # Check troubleshooter name availability.
        self.kwargs.update({
            'scope': resource_id(subscription=self.get_subscription_id()),
            'troubleshooter-name': str(uuid.uuid4())
        })

        self.cmd(
            "self-help check-name-availability --scope {scope} --name {troubleshooter-name} --type 'Microsoft.Help/troubleshooters'", checks=[
                self.check('nameAvailable', 'True'),])
    

    @ResourceGroupPreparer()
    @KeyVaultPreparer()
    def test_help_solutions(self, resource_group, key_vault):

        # Create solution for keyVault resource.
        solution_name = self.create_random_name(prefix='cli_test', length=15)
        self.kwargs.update({
            'scope': resource_id(resource_group=resource_group,
                                 subscription=self.get_subscription_id(),
                                 name=key_vault,
                                 namespace='Microsoft.KeyVault',
                                 type='vaults'),
            'solution-name': solution_name,
            'trigger-criteria': "[{name:solutionid,value:Demo2InsightV2}]",
            'update-trigger-criteria': "[{name:ReplacementKey,value:<!--56ee7509-92e1-4b9e-97c2-dda53065294c-->}]",
            'parameters': '{}',
            'update-parameters': '{SearchText:CanNotRDP,SymptomId:KeyVaultVaultNotFoundInsight}'
        })

        create_solution_result = self.cmd(
            "self-help solution create --solution-name {solution-name}  --trigger-criteria {trigger-criteria} --parameters {parameters} --scope {scope}", checks=[
                self.check('name', '{solution-name}'),
                self.check('type', 'Microsoft.Help/Solutions')])
        create_solution_result = create_solution_result.get_output_in_json()
        self.assertTrue(create_solution_result is not None)
        self.assertTrue(create_solution_result["id"] is not None)
        self.assertTrue(create_solution_result["name"] is not None)

        # Get solution for keyVault resource.
        get_solution_result = self.cmd(
            "self-help solution show --solution-name {solution-name} --scope {scope}", checks=[
                self.check('name', '{solution-name}'),
                self.check('type', 'Microsoft.Help/Solutions')])
        get_solution_result = get_solution_result.get_output_in_json()
        self.assertTrue(get_solution_result is not None)
        self.assertTrue(get_solution_result["id"] is not None)
        self.assertTrue(get_solution_result["name"] is not None)

        # Update solution for keyVault resource.
        update_solution_result = self.cmd(
            "self-help solution update --solution-name {solution-name} --trigger-criteria {update-trigger-criteria} --parameters {update-parameters} --scope {scope}", checks=[
                self.check('name', '{solution-name}'),
                self.check('type', 'Microsoft.Help/Solutions')])
        update_solution_result = update_solution_result.get_output_in_json()
        self.assertTrue(update_solution_result is not None)
        self.assertTrue(update_solution_result["id"] is not None)
        self.assertTrue(update_solution_result["name"] is not None)


    @ResourceGroupPreparer()
    @KeyVaultPreparer()
    def test_help_troubleshooters(self, resource_group, key_vault):

        # Create solution for keyVault resource.
        resourceId = resource_id(resource_group=resource_group,
                                 subscription=self.get_subscription_id(),
                                 name=key_vault,
                                 namespace='Microsoft.KeyVault',
                                 type='vaults')
        self.kwargs.update({
            'scope': resourceId,
            'troubleshooter-name': 'f81d4fae-7dec-11d0-a765-00a0c91e6bf5',
            'solution-id': 'e104dbdf-9e14-4c9f-bc78-21ac90382231',
            'parameters': '{ResourceUri:' + resourceId + '}',
            'responses': '[]'
        })

        create_troubleshooter_result = self.cmd(
            "self-help troubleshooter create --troubleshooter-name {troubleshooter-name}  --solution-id {solution-id} --parameters {parameters} --scope {scope}", checks=[
                self.check('name', '{troubleshooter-name}'),
                self.check('type', 'troubleshooters')])
        create_troubleshooter_result = create_troubleshooter_result.get_output_in_json()
        self.assertTrue(create_troubleshooter_result is not None)
        self.assertTrue(create_troubleshooter_result["id"] is not None)
        self.assertTrue(create_troubleshooter_result["name"] is not None)
        self.assertTrue(create_troubleshooter_result["steps"] is not None)


        # Get solution for keyVault resource.
        get_troubleshooter_result = self.cmd(
            "self-help troubleshooter show --troubleshooter-name {troubleshooter-name} --scope {scope}", checks=[
                self.check('name', '{troubleshooter-name}'),
                self.check('type', 'troubleshooters')])
        get_troubleshooter_result = get_troubleshooter_result.get_output_in_json()
        self.assertTrue(get_troubleshooter_result is not None)
        self.assertTrue(get_troubleshooter_result["id"] is not None)
        self.assertTrue(get_troubleshooter_result["name"] is not None)
        self.assertTrue(get_troubleshooter_result["steps"] is not None)

        self.kwargs.update({'step-id': get_troubleshooter_result["steps"][0]["id"]})

        # End troubleshooter for keyVault resource.
        self.cmd(
            "self-help troubleshooter end --troubleshooter-name {troubleshooter-name} --scope {scope}")
        
        # Restart troubleshooter for keyVault resource.
        restart_troubleshooter_result = self.cmd(
            "self-help troubleshooter restart --troubleshooter-name {troubleshooter-name} --scope {scope}")
        restart_troubleshooter_result = restart_troubleshooter_result.get_output_in_json()
        self.assertTrue(restart_troubleshooter_result is not None)

        # Continue troubleshooter for keyVault resource.
        self.cmd("self-help troubleshooter continue --troubleshooter-name {troubleshooter-name} --step-id {step-id} --responses {responses} --scope {scope}")
