# Install

## Subscription Manager

1. Start the installation process by running the _Subscription Manager.exe_ file, received from your XMPro.

![](<../../../.gitbook/assets/image (279).png>)

2. Click the "I Agree" button and press "Next"

![](<../../../.gitbook/assets/image (1069).png>)

3. Follow the instructions and when the installation is finished click "Close"

![](<../../../.gitbook/assets/image (467).png>)

{% hint style="info" %}
This "Setup" will install the installer you will use to install the database and website
{% endhint %}

4. When this initial installation is complete, open the start menu
5. Search for "XMPro Subscription Manager" and click on Run as Administrator

![](<../../../.gitbook/assets/image (1797).png>)

### **Component Choice**

6. When the installer launches, choose “Install” and click "Next"

![](<../../../.gitbook/assets/image (1288).png>)

7. Select the components that you would like to install and click "Next"

{% hint style="info" %}
If this is the first time you are installing Subscription Manager select both “Database” and “Web Application”
{% endhint %}

![](<../../../.gitbook/assets/image (1357).png>)

### Database

#### **Server**

8. Select the server instance to which you would like to connect

{% hint style="info" %}
If you already know the server instance name, it can be entered manually. Otherwise, use the refresh button on the right to load all available servers. Selecting the “Local Servers” check box will limit the search to the local network.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>



#### **Authentication Method**

9. Specify the authentication method that should be used: Windows or SQL

9.1. Windows Authentication: you may leave the options as is

{% hint style="warning" %}
**Warning:** Configure a service account that can be used for Windows authentication.
{% endhint %}

9.2. SQL authentication:

* Click the "Change" button
* Select the “Use SQL Authentication” option
* Enter the username and password of the SQL Server instance you’re connecting to

{% hint style="warning" %}
**Warning:** The SQL user must have permission to create databases on the server.
{% endhint %}

<figure><img src="../../../.gitbook/assets/POWiUeVksR.png" alt=""><figcaption></figcaption></figure>

**Database**

{% hint style="info" %}
The Database section allows you to configure if you would like to use an existing database or create a new one. Leaving the options as default will result in a new database being created.
{% endhint %}

To change the pre-populated name of the new database or to select to use an existing database:

10. Click the "Change" button
11. Make the changes needed by selecting the correct option
12. Specify the name of the new database or select an existing database from the drop-down

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Web Application

**DNS Name**

13. Verify if your DNS name is correct, if not, edit the value to contain the correct DNS name

{% hint style="info" %}
This is your fully qualified domain name (FQDN). Please find some examples below explaining the DNS name.

* https://localhost/xmprosubscriptionmanager
* https://vm-qa-win2022-2/xmprosubscriptionmanager
* https://demo.azurewebsites.com
{% endhint %}

| Complete Address                                 | DNS                    | Virtual Directory        |
| ------------------------------------------------ | ---------------------- | ------------------------ |
| https://localhost/xmprosubscriptionmanager       | localhost              | xmprosubscriptionmanager |
| https://vm-qa-win2022-2/xmprosubscriptionmanager | vm-qa-win2022-2        | xmprosubscriptionmanager |
| https://demo.azurewebsites.com                   | demo.azurewebsites.com |                          |

**Virtual Directory**

14. Select the parent site from the Web Site drop-down

{% hint style="info" %}
By default, the Virtual Directory name will be "xmprosubscriptionmanager" which will be created within IIS for the Subscription Manager site. If you wish to change the name you can specify it in the "Virtual Directory Name" text box.
{% endhint %}

15. Verify if the value in the content directory field is correct. If not, apply any changes needed

{% hint style="info" %}
By default, the option to create a sub-directory within the content directory is checked and you can specify a name in the “Sub-Directory” text box.
{% endhint %}

#### **Application Pool**

16. If you wish to change this name or use an existing application pool, click the Change button

{% hint style="info" %}
By default, a new application pool will be created when installing the site. The new application pool will have the same name as the name specified in the “Application Pool Name” field.
{% endhint %}

17. Either select the “Create a new Application Pool” or “Use an existing Application Pool” option

{% hint style="info" %}
If you choose “Create a new Application Pool”, give it an appropriate name. If you choose “Use an existing Application Pool”, select an existing application pool from the drop-down.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

#### **Security Account**

18. Select a security account that can be used

{% hint style="info" %}
The default option is “Local System”, which is a built-in security account. You can either change it by selecting a different built-in security account from the drop-down or by specifying your own security account.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Warning**: If you selected Windows authentication to connect to the database, you must choose “Specify your own Security Account” and provide the correct credentials. The service account must have batch logon rights enabled. More Information on how to set up a custom application pool in IIS as well as steps on how to enable batch logon rights can be found in this [**link**](https://docs.xmpro.com/knowledge-base-2/setting-up-a-custom-application-pool-so-that-windows-authentication-can-be-used-when-installing-xmpro-enabling-batch-logon-rights-for-a-user/).
{% endhint %}

### SMTP

19. Enter the SMTP details referenced in the [**1. Preparation**](../../1.-preparation.md#smtp-account) guide.\
    By default, the "Enable Email Notification" is checked.

{% hint style="info" %}
SMTP can be disabled by unchecking the "Enable Email Notification" checkbox if you don't want to receive email notifications. If at a later stage email notifications are needed, the installer can be run again to add SMTP functionality.
{% endhint %}

![](<../../../.gitbook/assets/image (1381).png>)

{% hint style="danger" %}
**Warning:** You are required to set up an SMTP account. Failing to do so will make registering new users very cumbersome.

Check your connection to the email server using the "Test SMTP settings" button.
{% endhint %}

### Certificates

During the installation process, you will be asked to upload two certificates: a signing certificate and an encryption certificate. You may use the same certificate for both options. The instructions on how to create a certificate can be found in the [Installing Prerequisites](prerequisites.md) guide.

#### **Signing Certificate**

20. Start by browsing to a suitable _.pfx_ certificate file. Specify the password for the certificate
21. Use the dropdown to select "Subject Name"

{% hint style="info" %}
It is recommended that you choose “LocalMachine” as the Location for the signing certificate.
{% endhint %}

![](<../../../.gitbook/assets/image (356).png>)

#### **Encryption Certificate**

22. Start by browsing to a suitable _.pfx_ certificate file. Specify the password for the certificate
23. Use the dropdown to select "Subject Name"

{% hint style="info" %}
It is recommended that you choose “LocalMachine” as the Location for the encryption certificate.
{% endhint %}

![](<../../../.gitbook/assets/image (1431).png>)

{% hint style="warning" %}
**Warning:** Both certificates must contain a private key.
{% endhint %}

### Final Steps

24. Continue through the wizard, confirm the installation and the components will be installed

![](<../../../.gitbook/assets/image (1658).png>)

{% hint style="warning" %}
**Warning:** Note the username and password on the last screen of the installer. This user has been created during installation as Subscription Manager itself needs at least one user in the system. Without it, you cannot add other users.

Change the password of the default user to a new, secure password after logging in for the first time.
{% endhint %}

### Accessing the Website

#### **Using Web Browser**

25. Access the website by putting the URL into your browser

{% hint style="info" %}
The format of the URL will be as follows: “_https://yourdnsname/virtualdirectoryname/_”
{% endhint %}

![](<../../../.gitbook/assets/image (1728).png>)

### Obtaining an Installation Profile

To install the Data Stream Designer and App Designer, you will need an Installation Profile.

26. Navigate to the XMPro Subscription Manager site as above using the Global Admin Login Details&#x20;
27. Go to the Subscription Manager page

<figure><img src="../../../.gitbook/assets/Home Image Current.jfif" alt=""><figcaption></figcaption></figure>

28. Click Products in the menu and click the Installation Profile button

![](<../../../.gitbook/assets/image (179).png>)

29. Enter a File Key and press OK to download the file

{% hint style="warning" %}
**Warning:** Remember the file key as it is needed when installing Data Stream Designer and App Designer.
{% endhint %}

![](<../../../.gitbook/assets/image (1020).png>)

### Optional: IIS User Permissions

If you’ve chosen to use a **custom service account** during installation, you may have to perform an extra step. An error may be shown after logging into Subscription Manager, even after giving the _IIS\_USRS_ group permission on the signing certificate private keys. The error would be as follow: “_We could not grant you access to the requested subscription. There was an unexpected error_“. The logs would also contain the following error: “_System.Security.Cryptography.CryptographicException: Keyset does not exist_“.

To solve this issue, use this [**article**](https://docs.xmpro.com/knowledge-base-2/how-to-grant-permission-to-iis-user-on-xmpro-identity-service-signing-certificate/) as a guideline to grant access for the Application Pool Identity (in some cases a domain account) on the signing certificate private keys.

## Data Stream Designer

1. Start the installation process by running the _Data Stream Designer.exe_ that you've received from XMPro.

![](<../../../.gitbook/assets/image (1624).png>)

2. Click the "I Agree" button and press "Next"​

![](<../../../.gitbook/assets/image (970).png>)

3. Follow the instructions and when the installation is finished click "Close"

![](<../../../.gitbook/assets/image (1463).png>)

4. When this initial installation is complete, open the start menu
5. Search for "Data Stream Designer" and click on Run as Administrator

![](<../../../.gitbook/assets/image (907).png>)

### Component Choice

6. When the installer launches, choose “Install”

![](<../../../.gitbook/assets/image (815).png>)

7. Select the components that you would like to install

{% hint style="info" %}
If this is the first time you are installing the Data Stream Designer, it is highly recommended that you select both “Database” and “Web Application”.
{% endhint %}

![](<../../../.gitbook/assets/image (120).png>)

### Database

#### **Server**

8. Select the server instance you would like to connect to.

{% hint style="info" %}
If you already know the server instance name, it can be entered manually. Otherwise, use the refresh button on the right to load all available servers. Selecting the “Local Servers” check box will limit the search to the local network.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### **Authentication Method**

9. Specify the authentication method that should be used: Windows or SQL

9.1. Windows Authentication: you may leave the options as is

{% hint style="warning" %}
**Warning:** Configure a service account that can be used for Windows authentication.
{% endhint %}

9.2. SQL Authentication:

* To connect to the database using SQL Server authentication, click the "Change" button
* Select the “Use SQL Authentication” option
* Enter the username and password of the SQL Server instance you’re connecting to

{% hint style="warning" %}
**Warning:** The SQL user must have permission to create databases on the server.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

**Database**

{% hint style="info" %}
The Database section allows you to configure if you would like to use an existing database or create a new one. Leaving the options as default will result in a new database being created.
{% endhint %}

To change the pre-populated name of the new database or to select to use an existing database:

10. Click the "Change" button and select the appropriate option
11. Specify the name of the new database or select an existing database from the drop-down

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

### Encryption Upgrade

If you are upgrading from 4.0 to 4.1+, you will be shown the Encryption Upgrade Settings page. This will assist you in migrating existing Server Variables to the new method of encryption.

{% hint style="warning" %}
To upgrade existing Server Variables, the details of the **Subscription Manager** database are required, **not** the **Data Stream Designer** database (provided on the previous page).
{% endhint %}

#### Upgrade Server Variables?

12. Tick to automatically upgrade the Server Variables. It is recommended, but not required.\
    None of the other settings on this page are required if you choose not to upgrade.

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### Server

13. Select the server instance you want to connect to

#### Authentication Method

14. Specify the authentication method that should be used: Windows or SQL

#### Database

15. Select the **Subscription Manager** database and click Next

### Web Application

**DNS Name**

16. Verify if your DNS name is correct. If not, edit the value to contain the correct DNS name

{% hint style="info" %}
This is your fully qualified domain name (FQDN). Please find some examples below explaining the DNS name.

* https://localhost/datastreams
* https://vm-qa-win2022-2/datastreams
* https://demo.azurewebsites.com
{% endhint %}

| Complete Address                                 | DNS                    | Virtual Directory |
| ------------------------------------------------ | ---------------------- | ----------------- |
| https://localhost/xmprosubscriptionmanager       | localhost              | datastreams       |
| https://vm-qa-win2022-2/xmprosubscriptionmanager | vm-qa-win2022-2        | datastreams       |
| https://demo.azurewebsites.com                   | demo.azurewebsites.com |                   |

**Virtual Directory**

17. Select the parent site from the Web Site drop-down

{% hint style="info" %}
By default, the Virtual Directory name will be "DataStreams" which will be created within IIS for the Data Stream site. If you wish to change the name you can specify it in the "Virtual Directory Name" text box.
{% endhint %}

18. Verify the value in the content directory field. If incorrect, apply any changes needed

{% hint style="info" %}
By default, the option to create a sub-directory within the content directory is checked and you can specify a name in the “Sub-Directory” text box.
{% endhint %}

#### Application Pool

19. If you wish to change the name or use an existing application pool, click the Change button

{% hint style="info" %}
By default, a new application pool will be created when installing the site. The new application pool will have the same name as the name specified in the “Application Pool Name” field.
{% endhint %}

20. Either select the “Create a new Application Pool” or “Use an existing Application Pool” option

{% hint style="info" %}
If you choose “Create a new Application Pool”, give it an appropriate name. If you choose “Use an existing Application Pool”, select an existing application pool from the drop-down.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

#### **Security Account**

21. Select "Local System" as the security account.

{% hint style="info" %}
The two options available to choose from are using a built-in security account or specifying your own security account.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Warning**: If you selected Windows authentication to connect to the database, you must choose “Specify your own Security Account” and provide the correct credentials. The service account must have batch logon rights enabled. More Information on how to set up a custom application pool in IIS as well as steps on how to enable batch logon rights can be found in this [**link**](https://docs.xmpro.com/knowledge-base-2/setting-up-a-custom-application-pool-so-that-windows-authentication-can-be-used-when-installing-xmpro-enabling-batch-logon-rights-for-a-user/).
{% endhint %}

### Installation Profile

22. Click the Browse button to upload an installation profile for Subscription Manager
23. Select a file and click "Next"

{% hint style="info" %}
This file ensures the Data Stream Designer contains the correct details for the Subscription Manager instance you would like to use. The file can be obtained through the [steps outlined previously in this tutorial](install.md#obtaining-an-installation-profile).
{% endhint %}

![](<../../../.gitbook/assets/image (1723).png>)

24. After you press "Next", authenticate yourself using Subscription Manager credentials

![](<../../../.gitbook/assets/image (766).png>)

{% hint style="warning" %}
**Warning:** If you are unable to sign in at this step, please follow this [**link**](prerequisites.md) to disable Internet Explorer Enhanced Security Configuration.
{% endhint %}

### Final Steps

25. Continue through the wizard, confirm the installation and the components will be installed

## App Designer

1. Start the installation process by running the _App Designer.exe_ file that you've received from XMPro.

![](<../../../.gitbook/assets/image (1631).png>)

2. Click the "I Agree" button and press "Next"

![](<../../../.gitbook/assets/image (189).png>)

3. Follow the instructions and click "Close" when the installation is finished

![](<../../../.gitbook/assets/image (869).png>)

{% hint style="info" %}
This "Setup" will install the installer you will use to install the database and website
{% endhint %}

4. When this initial installation is complete, open the start menu
5. Search for "App Designer" and click on Run as Administrator

![](<../../../.gitbook/assets/image (222).png>)

### **Component Choice**

6. When the installer launches, choose “Install” and click "Next"

![](<../../../.gitbook/assets/image (1438).png>)

7. Select the components that you would like to install and click "Next"

{% hint style="info" %}
If this is the first time you are installing Subscription Manager, it is highly recommended that you select both “Database” and “Web Application”.
{% endhint %}

![](<../../../.gitbook/assets/image (323).png>)

### Database

#### **Server**

8. Select the server instance you would like to connect to

{% hint style="info" %}
If you already know the server instance name, it can be entered manually. Otherwise, use the refresh button on the right to load all available servers. Selecting the “Local Servers” check box will limit the search to the local network.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### **Authentication Method**

9. Specify the authentication method that should be used: Windows or SQL

9.1. Windows Authentication: you may leave the options as is

{% hint style="warning" %}
**Warning:** Configure a service account that can be used for Windows authentication
{% endhint %}

9.2. SQL Authentication:

* Click the "Change" button
* Select the “Use SQL Authentication” option
* Enter the username and password of the SQL Server instance you’re connecting to

{% hint style="warning" %}
**Warning:** The SQL user must have permission to create databases on the server.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

**Database**

{% hint style="info" %}
The Database section allows you to configure if you would like to use an existing database or create a new one. Leaving the options as default will result in a new database being created.
{% endhint %}

To change the pre-populated name of the new database or to select to use an existing database:

10. Click the "Change" button and select the appropriate option
11. Specify the name of the new database or select an existing database from the drop-down

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

### Encryption Upgrade

If you are upgrading from 4.0 to 4.1 or greater, you will be shown the Encryption Upgrade Settings page. This will assist you in migrating existing Server Variables and Connector settings to the new method of encryption.

{% hint style="warning" %}
To upgrade existing Server Variables, the details of the **Subscription Manager** database is required, **not** the **Data Stream Designer** database (provided on the previous page).
{% endhint %}

#### App Designer Encryption Key

12. Enter the App Designer Encryption Key

{% hint style="info" %}
To find the App Designer Encryption Key, inspect the appsettings.json file in the web server files. It will be found under the JSON path "xmpro.appDesigner.encryptionKey".

If that path does not exist, it is stored in a cloud-service key vault. Search for the "xmpro.keyVault" JSON object for the details required to find the encryption key.

Documentation for the [Azure](install.md#server) and [Amazon](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key vaults have been linked for convenience.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

#### Upgrade Server Variables?

13. Tick to automatically upgrade the Server Variables. It is recommended, but not required.\
    None of the other settings on this page are required if you choose not to upgrade.

#### Server

14. Select the server instance you want to connect to

#### Authentication Method

15. Specify the authentication method that should be used: Windows or SQL

#### Database

16. Select the **Subscription Manager** database and click Next

### Web Application

**DNS Name**

17. Verify if your DNS name is correct, if not, edit the value to contain the correct DNS name

{% hint style="info" %}
This is your fully qualified domain name (FQDN). Please find some examples below explaining the DNS name.

* https://localhost/xmprosubscriptionmanager
* https://vm-qa-win2022-2/xmprosubscriptionmanager
* https://demo.azurewebsites.com
{% endhint %}

| https://localhost/xmprosubscriptionmanager       | localhost              | xmprosubscriptionmanager |
| ------------------------------------------------ | ---------------------- | ------------------------ |
| https://vm-qa-win2022-2/xmprosubscriptionmanager | vm-qa-win2022-2        | xmprosubscriptionmanager |
| https://demo.azurewebsites.com                   | demo.azurewebsites.com |                          |

**Virtual Directory**

18. Select the parent site from the Web Site drop-down

{% hint style="info" %}
By default, the Virtual Directory name will be "AppDesigner" which will be created within IIS for the Data Stream site. If you wish to change the name you can specify it in the "Virtual Directory Name" text box.
{% endhint %}

19. Verify if the value in the content directory field is correct. If not, apply any changes needed

{% hint style="info" %}
By default, the option to create a sub-directory within the content directory is checked and you can specify a name in the “Sub-Directory” text box.
{% endhint %}

#### **Application Pool**

20. If you wish to change this name or use an existing application pool, click the Change button

{% hint style="info" %}
By default, a new application pool will be created when installing the site. The new application pool will have the same name as the name specified in the “Application Pool Name” field.
{% endhint %}

21. Either select the “Create a new Application Pool” or “Use an existing Application Pool” option

{% hint style="info" %}
If you choose “Create a new Application Pool”, give it an appropriate name. If you choose “Use an existing Application Pool”, select an existing application pool from the drop-down.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

#### **Security Account**

22. Select "Local System" as the security account

{% hint style="info" %}
You can either change it by selecting a different built-in security account from the drop-down or by specifying your own security account.\\
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Warning**: If you selected Windows authentication to connect to the database, you must choose “Specify your own Security Account” and provide the correct credentials. The service account must have batch logon rights enabled. More Information on how to set up a custom application pool in IIS as well as steps on how to enable batch logon rights can be found [i](https://docs.xmpro.com/knowledge-base-2/setting-up-a-custom-application-pool-so-that-windows-authentication-can-be-used-when-installing-xmpro-enabling-batch-logon-rights-for-a-user/)n this [**link**](https://docs.xmpro.com/knowledge-base-2/setting-up-a-custom-application-pool-so-that-windows-authentication-can-be-used-when-installing-xmpro-enabling-batch-logon-rights-for-a-user/).
{% endhint %}

### Integration Details

23. Type in the URL of Data Stream designer in the text box

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

### SMTP

24. Enter the SMTP settings referenced in the [**1. Preparation**](../../1.-preparation.md#smtp-account) guide.\
    By default, the "Enable Email Notification" is checked.

{% hint style="info" %}
SMTP can be disabled by unchecking the "Enable Email Notification" checkbox if you don't want to receive email notifications. If at a later stage email notifications are needed, the installer can be run again to add SMTP functionality.
{% endhint %}

![](<../../../.gitbook/assets/image (164).png>)

{% hint style="warning" %}
**Warning:** You are required to set up an SMTP account. Failing to do so will make registering new users very cumbersome.

It is highly recommended to check your connection to the email server using the "Test SMTP settings" button.
{% endhint %}

### Twilio (Optional)

25. Enter the Twilio details referenced in the [**1. Preparation**](../../1.-preparation.md#twilio-optional) guide. If you don't want SMS notifications you can select "None" from the "Select Provider" dropdown.

![](<../../../.gitbook/assets/image (51).png>)

### Installation Profile

26. Click the Browse button to upload an installation profile for Subscription Manager
27. Select a file and click "Next"

{% hint style="info" %}
This file ensures the App Designer contains the correct details for the Subscription Manager instance you would like to use. The file used can be obtained through the [steps outlined previously in this tutorial](install.md#obtaining-an-installation-profile).

The Installation Profile generated for Data Stream Installer can be used in this step.
{% endhint %}

![](<../../../.gitbook/assets/image (507).png>)

28. After you press "Next", authenticate yourself using Subscription Manager credentials

![](<../../../.gitbook/assets/image (412).png>)

{% hint style="warning" %}
**Warning:** If you are unable to sign in at this step, please follow this [**link**](prerequisites.md) to disable Internet Explorer Enhanced Security Configuration.
{% endhint %}

### Final Steps

29. Continue through the wizard, confirm the installation and the components will be installed

## Next Step: Complete Installation

The installation of the XMPro Platform is now complete, but there are some environment setup steps before you can use the platform. Please click the below link for further instructions:

{% content-ref url="../../3.-complete-installation" %}
[3.-complete-installation](../../3.-complete-installation)
{% endcontent-ref %}
