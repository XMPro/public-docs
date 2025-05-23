# SSO - ADFS

In this article, we will look at how to set up AD FS so that it can be used as an external identity provider for Subscription Manager, allowing single sign-on capability between AD FS and Subscription Manager.

Follow the steps below:

## IIS&#x20;

&#x20; 1\. Navigate to the location in IIS where Subscription Manager was installed.

{% hint style="info" %}
You can right-click on the application name in IIS and choose “_Explore_“.
{% endhint %}

![](https://docs.xmpro.com/wp-content/uploads/2019/05/open-sub-mgr-app.png)

&#x20; 2\. Open the _web.config_ file.

![](https://docs.xmpro.com/wp-content/uploads/2019/05/open-web-config.png)

&#x20; 3\. Scroll down to the “_xmpro_” section.&#x20;

{% hint style="info" %}
It might be encrypted, which will require you to decrypt it first. For instructions, please refer to the [How to encrypt and decrypt a web.config file](https://docs.xmpro.com/knowledge-base-2/how-to-encrypt-and-decrypt-a-web-config-file/) Knowledge Base article.
{% endhint %}

&#x20; 4\. Under the “_identityProviders_” element, add a new element called “_adfs_”.

&#x20; 5\. Specify the metadata address of your AD FS, as per the image below:

<figure><img src="../../../.gitbook/assets/SSO_ADFS_web_config_metadata_address.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Set the correct URL for the metadataAddress value. An example of how the URL might look is “_https://adfs.domain.com/federationmetadata/2007-06/federationmetadata.xml_“.&#x20;

Verify your URL by browsing to it in a browser.&#x20;
{% endhint %}

&#x20; 6\. Copy the “_baseUrl_” value in the web.config - you will need it later in this guide.

<figure><img src="../../../.gitbook/assets/SSO_AzureAD_web_config_baseUrl.png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Warning**: you will use this value to create a relying party trust between the Subscription Manager application and AD FS
{% endhint %}

## Server Manager

&#x20; 1\. Log on to your AD FS server and go to Tools –> AD FS Management&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/open-ad-fs-management.png)

### Relying Party Trust&#x20;

&#x20;2\. Click _Add Relying Party Trust_

![](https://docs.xmpro.com/wp-content/uploads/2019/05/click-on-add-relying-trust.png)

&#x20; 3\. Select _Claims aware_ and click Start&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/select-claims-aware.png)

&#x20; 4\. Select _Enter data about the relying party manually_ and click Next&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/add-data-manually.png)

&#x20; 5\. Choose a display name and click Next and Next again&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/choose-a-display-name.png)

&#x20; 6\. Select _Enable support for the WS-Federation Passive protocol_, add the URL and click Next

{% hint style="info" %}
This is the base URL you copied from the web.config file.&#x20;
{% endhint %}

![](https://docs.xmpro.com/wp-content/uploads/2019/05/wsf-protocol.png)

&#x20; 7\. Add the identifier for the application. Use the URL for Subscription Manager

&#x20; 8\. Add the URL and click Next&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/unique-identifier.png)

&#x20; 9\. Choose an access control policy and click Next. Continue to the last screen&#x20;

{% hint style="info" %}
For this article, we are going to choose _Permit everyone_
{% endhint %}

![](https://docs.xmpro.com/wp-content/uploads/2019/05/access-control-policy.png)

### Claims Issuance Policy &#x20;

10\. Select _Configure claims issuance policy for this application_ and finish&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/last-screen.png)

&#x20; 11\. In the AD FS Management window, click _Edit Claim Issuance Policy…_ and click _Add Rule_&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/edit-claim-insurance-policy.png)

&#x20; 12\. In the _Claim rule template_ drop-down, select _Send LDAP Attributes as Claims_ and click Next&#x20;

![](https://docs.xmpro.com/wp-content/uploads/2019/05/LDAP.png)

&#x20; 13\. Choose a name for the rule and map the claims  &#x20;

![](<../../../.gitbook/assets/Edit Rule.png>)

![](https://docs.xmpro.com/wp-content/uploads/2019/05/Choose-a-name-for-the-rule.png)

## Login to Subscription Manager using AD FS

Now you should be ready. If you navigate to the Subscription Manager application, you will see the AD FS login option. Log in with your AD FS credentials.&#x20;

{% hint style="info" %}
You will be asked to link your account when you sign in for the first time. If so, fill in your information and click Link Account &#x20;
{% endhint %}

![](https://docs.xmpro.com/wp-content/uploads/2019/05/add-adfs-credentials.png)

![](https://docs.xmpro.com/wp-content/uploads/2019/05/adfs-button.png)
