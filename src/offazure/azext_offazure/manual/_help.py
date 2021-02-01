# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps

helps['offazure'] = """
    type: group
    short-summary: Manage on-premise resources for migrate.
"""

helps['offazure hyperv'] = """
    type: group
    short-summary: Manage Hyper-V on-premise resources.
"""

helps['offazure hyperv cluster'] = """
    type: group
    short-summary: Manage Hyper-V cluster
"""

helps['offazure hyperv cluster list'] = """
    type: command
    short-summary: "Get all clusters on the on-premise site."
    examples:
      - name: List clusters by site
        text: |-
               az offazure hyperv cluster list --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv cluster show'] = """
    type: command
    short-summary: "Get the details of a Hyper-V cluster."
    examples:
      - name: Get a cluster
        text: |-
               az offazure hyperv cluster show --cluster-name MyClusterName --resource-group \
                 MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv host'] = """
    type: group
    short-summary: Manage Hyper-V host
"""

helps['offazure hyperv host list'] = """
    type: command
    short-summary: "Get all hosts on the on-premise site."
    examples:
      - name: List hosts by site
        text: |-
               az offazure hyperv host list --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv host show'] = """
    type: command
    short-summary: "Get the details of a Hyper-V host."
    examples:
      - name: Get a host
        text: |-
               az offazure hyperv host show --host-name MyHostName --resource-group \
                 MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv machine'] = """
    type: group
    short-summary: Manage Hyper-V machine
"""

helps['offazure hyperv machine list'] = """
    type: command
    short-summary: "List all machines on the on-premise site."
    examples:
      - name: List machines by site
        text: |-
               az offazure hyperv machine list --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv machine show'] = """
    type: command
    short-summary: "Get the details of a machine."
    examples:
      - name: Get a machine.
        text: |-
               az offazure hyperv machine show --machine-name MyMachineName --resource-group \
                 MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv run-as-account'] = """
    type: group
    short-summary: Manage Hyper-V run-as-account
"""

helps['offazure hyperv run-as-account list'] = """
    type: command
    short-summary: "List all run-as-accounts on the on-premise site."
    examples:
      - name: List run-as-accounts by site
        text: |-
               az offazure hyperv run-as-account list --resource-group MyResourceGroup \
                 --site-name MySiteName
"""

helps['offazure hyperv run-as-account show'] = """
    type: command
    short-summary: "Get the details of a run-as-account."
    examples:
      - name: Get a run-as-account.
        text: |-
               az offazure hyperv run-as-account show --account-name MyAccount --resource-group \
                 MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv site'] = """
    type: group
    short-summary: Manage Hyper-V site
"""

helps['offazure hyperv site show'] = """
    type: command
    short-summary: "Get the details of a site."
    examples:
      - name: Get a Hyper-V site
        text: |-
               az offazure hyperv site show --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure hyperv site create'] = """
    type: command
    short-summary: "Create a Hyper-V site."
    parameters:
      - name: --identity
        short-summary: "Service principal identity details used by agent for communication to the service."
        long-summary: |
            Usage: --identity tenant-id=XX application-id=XX object-id=XX audience=XX \
aad-authority=XX raw-cert-data=XX

            tenant-id: Tenant Id for the service principal with which the on-premise management/data plane components \
would communicate with our Azure services.
            application-id: Application/client Id for the service principal with which the on-premise management/data \
plane components would communicate with our Azure services.
            object-id: Object Id of the service principal with which the on-premise management/data plane components \
would communicate with our Azure services.
            audience: Intended audience for the service principal.
            aad-authority: AAD Authority URL which was used to request the token for the service principal.
            raw-cert-data: Raw certificate data for building certificate expiry flows.
      - name: --agent
        short-summary: "On-premises agent details."
        long-summary: |
            Usage: --agent key-vault-uri=XX key-vault-id=XX

            key-vault-uri: Key vault URI.
            key-vault-id: Key vault ARM Id.
    examples:
      - name: Create a Hyper-V site
        text: |-
               az offazure hyperv site create --resource-group MyResourceGroup --site-name MySiteName \
                 --location centralus
"""

helps['offazure hyperv site delete'] = """
    type: command
    short-summary: "Delete a Hyper-V site."
    examples:
      - name: Delete a Hyper-V site.
        text: |-
               az offazure hyperv site delete --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure vmware'] = """
    type: group
    short-summary: Manage VMware on-premise resources.
"""

helps['offazure vmware machine'] = """
    type: group
    short-summary: Manage VMware machine
"""

helps['offazure vmware machine list'] = """
    type: command
    short-summary: "List all machines on the on-premise site."
    examples:
      - name: List VMware machines by site
        text: |-
               az offazure vmware machine list --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure vmware machine show'] = """
    type: command
    short-summary: "Get the details of a machine."
    examples:
      - name: Get a VMware machine.
        text: |-
               az offazure vmware machine show --name MyMachineName --resource-group MyResourceGroup \
                 --site-name MySiteName
"""

helps['offazure vmware run-as-account'] = """
    type: group
    short-summary: Manage VMware run-as-account
"""

helps['offazure vmware run-as-account list'] = """
    type: command
    short-summary: "List all run-as-accounts on the on-premise site."
    examples:
      - name: List VMware run-as-accounts by site.
        text: |-
               az offazure vmware run-as-account list --resource-group MyResourceGroup \
                 --site-name MySiteName
"""

helps['offazure vmware run-as-account show'] = """
    type: command
    short-summary: "Get the details of a run-as-account."
    examples:
      - name: Get a VMware run-as-account.
        text: |-
               az offazure vmware run-as-account show --account-name MyAccountName --resource-group \
                 MyResourceGroup --site-name MySiteName
"""

helps['offazure vmware site'] = """
    type: group
    short-summary: Manage VMware site
"""

helps['offazure vmware site show'] = """
    type: command
    short-summary: "Get the details of a VMware site."
    examples:
      - name: Get a VMware site
        text: |-
               az offazure vmware site show --resource-group MyResourceGroup --name MySiteName \
"""

helps['offazure vmware site create'] = """
    type: command
    short-summary: "Create a site for VMware resources."
    parameters:
      - name: --identity
        short-summary: "Service principal identity details used by agent for communication to the service."
        long-summary: |
            Usage: --identity tenant-id=XX application-id=XX object-id=XX audience=XX \
aad-authority=XX raw-cert-data=XX

            tenant-id: Tenant Id for the service principal with which the on-premise management/data plane components \
would communicate with our Azure services.
            application-id: Application/client Id for the service principal with which the on-premise management/data \
plane components would communicate with our Azure services.
            object-id: Object Id of the service principal with which the on-premise management/data plane components \
would communicate with our Azure services.
            audience: Intended audience for the service principal.
            aad-authority: AAD Authority URL which was used to request the token for the service principal.
            raw-cert-data: Raw certificate data for building certificate expiry flows.
      - name: --agent
        short-summary: "On-premises agent details."
        long-summary: |
            Usage: --agent key-vault-uri=XX key-vault-id=XX

            key-vault-uri: Key vault URI.
            key-vault-id: Key vault ARM Id.
    examples:
      - name: Create a VMware site
        text: |-
               az offazure vmware site create -g MyResourceGroup --site-name MySiteName --location centralus
"""

helps['offazure vmware site delete'] = """
    type: command
    short-summary: "Delete a VMware site."
    examples:
      - name: Delete a VMware site
        text: |-
               az offazure vmware site delete --resource-group MyResourceGroup --name MySiteName
"""

helps['offazure vmware vcenter'] = """
    type: group
    short-summary: Manage VMware vCenter
"""

helps['offazure vmware vcenter list'] = """
    type: command
    short-summary: "List all vCenters on the on-premise site."
    examples:
      - name: List VMware vCenters by site
        text: |-
               az offazure vmware vcenter list --resource-group MyResourceGroup --site-name MySiteName
"""

helps['offazure vmware vcenter show'] = """
    type: command
    short-summary: "Get the details of a vCenter."
    examples:
      - name: Get a VMware vCenter.
        text: |-
               az offazure vmware vcenter show --resource-group MyResourceGroup --site-name MySiteName \
                 --name MyVCenterName
"""