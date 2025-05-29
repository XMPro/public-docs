---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Azure

This document will guide you through how to set up the Azure infrastructure and deploy the XMPro Platform.

* [Install](azure.md#install)
* [Upgrade](azure.md#upgrade)
* [Uninstall](azure.md#uninstall)

## Architecture

The following deployment diagram shows an example architecture and the necessary resources for the XMPro platform in Microsoft Azure.

![Fig 1: Example XMPro architecture in Azure](<../../.gitbook/assets/Azure_Architecture_as of Nov 11,2024x1.png>)

Set up of Cloud Stream Host, Master Data, [Azure Cache](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-dotnet-how-to-use-azure-redis-cache), or [Twilio](broken-reference) is optional and is dependent on client requirements. As a result, these resources will be excluded from this deployment.

## Prerequisites

In order to proceed with the deployment, you are required to complete the steps in the **1. Preparation** guide:

1. Select Azure resources that meet the [**hardware** requirements](broken-reference) and [**software** requirements](broken-reference).
2. Follow the [certificate and communication steps](broken-reference) for an [SMTP Account](broken-reference) (Recommended).

As well as having:

* Azure portal administrative access
* Access to Subscription and Resource group

## Install

This section provides information about installing the XMPro platform from scratch in Azure.

1. Log on to the Azure Portal [https://portal.azure.com/](https://portal.azure.com/) (with Company Administrator access)
2. In the search bar type “Deploy” and select “Deploy a custom template”

![](../../.gitbook/assets/Azure-ARMTemplate-Search.PNG)

3\. Click "Build your own template in the editor"

![](<../../.gitbook/assets/image (146).png>)

4\. Download the file from the link provided below:

{% file src="../../.gitbook/assets/mainTemplate_v4.4.19.json" %}

5\. Select "Load File" and then Open the downloaded "mainTemplate\_\[Version].json"

![](../../.gitbook/assets/Azure-ARMTemplate-Upload.PNG)

6\. Once loaded, click Save - do not change the template.

![](../../.gitbook/assets/Azure-ARMTemplate-Save.PNG)

7\. Complete the form.

{% hint style="danger" %}
* Enter the username in the correct format i.e. firstname.lastname@companyname.onxmpro.com
* The following special characters are **not** supported in the passwords: `` ` ' \ $ @ ``
* Take note of the passwords used as this will not be displayed again and they are required later.
{% endhint %}

![](../../.gitbook/assets/Azure-ARMTemplate-Form.PNG)

8\. Verify the information is correct and click Create.

![](<../../.gitbook/assets/image (338).png>)

After successful deployment, the following items have been installed:

* Subscription Manager
* Data Stream Designer
* App Designer
* Stream Host

Proceed to [Restart the App Services](azure.md#restarting-app-services) after they are all deployed.

### Restarting App Services

This step explains how to restart your app services in the Azure Portal.

1. Type “Resource groups” in the search bar and select “Resource groups”.

![](../../.gitbook/assets/Azure-ARMTemplate-Restart-1.PNG)

2\. Search for the Resource Group created during installation and select it.

![](../../.gitbook/assets/Azure-ARMTemplate-Restart-2.PNG)

3\. Select Subscription Manager, Data Stream Designer, and App Designer and restart the applications.

![](../../.gitbook/assets/Restart_3.png)

4\. The below GIF shows how to restart your app service.

![](../../.gitbook/assets/PI2GwPRNfr.gif)

### Logins

<table><thead><tr><th width="426">User</th><th width="133.59649122807014">Type</th><th>Password</th></tr></thead><tbody><tr><td>admin@xmpro.onxmpro.com</td><td>Super Admin</td><td>as entered during setup</td></tr><tr><td>firstname.lastname@companyname.onxmpro.com</td><td>Admin</td><td>as entered during setup</td></tr></tbody></table>

### Request a License

A new company is created as part of the installation process but needs a valid license to work.

{% hint style="info" %}
Login using the Super Admin account **admin@xmpro.onxmpro.com**.
{% endhint %}

1\. Click Company in the left menu to open the Companies page.\
2\. Click on the Company.\
3\. Click on the Subscriptions gauge to open the Subscriptions page.\
4\. Click on a Subscription.\
5\. Click the Update License button in the command bar.\
6\. Click _Generate a license request_, enter the number of days, and submit.\
7\. When you have received the license from [XMPro support](http://xmpro.com/support/), upload it.\
8\. Click Save.

This sends a request to XMPro for an App Designer license for this Company.

![](<../../.gitbook/assets/image (1434).png>)

{% hint style="danger" %}
The _Generate a license request_ link will only work if SMTP was set up during installation.
{% endhint %}

9\. Change the Product to Data Stream Designer from the list and request another license

{% hint style="info" %}
Licenses are given on an individual basis by the [XMPro support team](http://xmpro.com/support/).
{% endhint %}

When you have received a license for each product through an email sent to the email address given during installation, follow the steps below to upload the license for both App Designer and Data Stream Designer.

![](../../.gitbook/assets/License_3.png)

### Next Step: Complete Installation

The installation of the XMPro Platform is now complete but before you can use the platform, some steps are needed to set up the environment. Further instructions about the configuration can be found below:

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

## Upgrade

{% hint style="danger" %}
Before beginning the upgrade, back up databases using [this](https://docs.microsoft.com/en-us/azure/azure-sql/database/database-export#the-azure-portal) guide.
{% endhint %}

Follow the same steps as a new [Install](azure.md#install) to upgrade your XMPro platform\*\*.\*\* Make sure to:

* Download and use the latest "mainTemplate\_\[Version].json".
* Before deploying, stop the SM App Service to avoid file locking issues during MSDeploy.
* Use the same Resource Group and credentials used during the **original** Install when completing the Custom deployment form.

<figure><img src="../../.gitbook/assets/Azure-ARMTemplate-Upgrade.PNG" alt=""><figcaption></figcaption></figure>

## Known Issues

### Notebook Upgrades with ARM Deployments

When upgrading XMPro instances that use AI Notebooks installed via ARM deployments, you may encounter known issues with the automated upgrade process. These issues primarily affect the Notebook components during ARM-based upgrades.

#### **Impact and Scope**

* This issue affects users who deploy via ARM and already have AI Notebooks installed
* The issue primarily appears during upgrades to version 4.4.18 and later
* The problem involves compatibility between the ARM template and current Azure implementation

#### **Workaround: Manual Notebook Deployment**

While automated Notebook upgrades via ARM deployments may fail, you can successfully upgrade Notebooks using the following manual deployment process:

#### **Prerequisites**

1. Bash terminal
2. Azure CLI 2
3. Helm 3.X

#### **Manual Deployment Steps**

1. **Login and validate connection to the correct subscription**

```
az login
az account show
```

2. **Find the name of the AKS resource**

```
az aks list -o table
```

3. **Merge the AKS cluster into kubeconfig**

```
az aks get-credentials -n <aks resource name> -g <resource group>
```

4. **Check the kubectl is connected to the AKS instance**

```
kubectl config current-context
```

5. **Find the helm deployment**

```
helm list -n prod
```

6. **Check the helm deployment values and save to values.yml**

```
helm get values xmpro-notebooks -n prod > values.yml | sed -i '1d' values.yml
```

7. **Remove the first line "USER-SUPPLIED VALUES:"**

```
sed -i '1d' values.yml
```

8. **Observe the singleuser section in values.yml**

```
singleuser:
  image:
    name: <registry>/base-jupyter-notebook
    tag: <release-version>
```

9. **Set the following values**

* `<registry>` = xmpro.azurecr.io
* `<release-version>` = the desired release tag version e.g. 4.4.18

10. **Deploy the values upgrade using Helm**

```
helm upgrade --cleanup-on-fail --install xmpro-notebooks jupyterhub/jupyterhub --namespace prod --create-namespace
```

11. **Wait for the deployment to complete**
12. **Verify the deployment**

```
helm list -n prod
```

13. **Verify the values are set correctly**

```
helm get values xmpro-notebooks -n prod
```

14. **Verify the pods status**

```
kubectl get pods -n prod
```

15. **If required, forcefully restart the notebook pods**

```
kubectl delete pods --all -n prod
```

### Issues

### **1. Notebook URLs are mismatched**

The URLs for notebook should be in sync in all the places:

* AI AppService > Environment Vars > xmpro:aidesigner:jupyterUrl
* SM DB dbo.ProductUrls > Notebook Url
* Helm Chart Release > xmpro-notebook > values
* `kubectl describe svc proxy-public -n prod` > annotations > service.beta.kubernetes.io/azure-dns-label-name

#### Troubleshooting <a href="#user-content-troubleshooting" id="user-content-troubleshooting"></a>

```
// az login to the subscription
```

**Connect to the aks instance**

```
az aks list -o table
az aks get-credentials -g <resource-group> -n <aks-instance-name-from-above>
kubectl config set-context <aks-instance-name-from-above>
kubectl config current-context
```

**Get helm deployment details**

```bash
helm ls -n prod
helm get values xmpro-notebooks -n prod
// check the notebook URLs
```

**Get proxy public annotations**

```
kubectl get svc -n prod
kubectl describe svc proxy-public -n prod
// check the service.beta.kubernetes.io/azure-dns-label-name annotation
```

**Check the SQL database**

```
az resource list -g <resource-group> -o table
az sql server show -g <resource-group> -n <sql-server-instance-name-from-above>
// check the SM DB dbo.ProductUrls > Notebook Url
```

**Force restart all pods**

```
kubectl get pods -n prod
kubectl delete pods --all -n prod
```

### 2. Access Denied to Storage Account

After a Notebook upgrade, launching a Jupyter Hub user instance may result in an error such as;

```
MountVolume.MountDevice failed for volume "pvc-64bd7714-7c0e-45ca-88cc-c1bdf816108e": rpc error: code = Internal desc = volume(MC_armupgrade_aks-armup-xmpro-001_centralus#nfs0f17de3935cc49c2ae46#pvc-64bd7714-7c0e-45ca-88cc-c1bdf816108e##prod#) mount "nfs0f17de3935cc49c2ae46.blob.core.windows.net:/nfs0f17de3935cc49c2ae46/pvc-64bd7714-7c0e-45ca-88cc-c1bdf816108e" on "/var/lib/kubelet/plugins/kubernetes.io/csi/blob.csi.azure.com/fd5793275cbf92e1d702e30d03bcf1634564e3690e3b635a763e814f5e09c29/globalmount" failed with mount failed: exit status 1 Mounting command: mount Mounting arguments: -t aznfs -o nconnect=4,sec=sys,vers=3,nolock nfs0f17de3935cc49c2ae46.blob.core.windows.net:/nfs0f17de3935cc49c2ae46/pvc-64bd7714-7c0e-45ca-88cc-c1bdf816108e /var/lib/kubelet/plugins/kubernetes.io/csi/blob.csi.azure.com/fd5793275cbf92e1d702e30d03bcf1634564e3690e3b635a763e814f5e09c29/globalmount Output: [0mmount.nfs: access denied by server while mounting 10.161.100.100:/nfs0f17de3935cc49c2ae46/pvc-64bd7714-7c0e-45ca-88cc-c1bdf816108e[0m [2;31mMount failed![0[0m Please refer to http://aka.ms/blobmounterror for possible causes and solutions for mount errors.
```

Follow the appropriate instructions on the link [http://aka.ms/blobmounterror](http://aka.ms/blobmounterror)  to fix up the reported error.

These particular steps deal with the [Access denied by the server](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/mounting-azure-blob-storage-container-fail#nfs-error2) error.

## Uninstall

This section provides information about uninstalling the XMPro platform from Azure.

1. Open the resource group where XMPro is installed
2. Click Delete resource group

![](../../.gitbook/assets/Delete_1.png)

3\. Enter the name of the resource group and click _Delete_

![](../../.gitbook/assets/Azure-ARMTemplate-Delete.PNG)
