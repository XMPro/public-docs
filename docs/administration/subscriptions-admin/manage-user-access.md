# Manage User Access

{% hint style="warning" %}
Please note that this section is intended for Administrative users. No other type of user is allowed to manage a Company's Subscriptions.
{% endhint %}

## **Adding Users to a Subscription**

Follow the steps below to give access to a product for a user in a company other than XMPro.

1. Open the Subscriptions page from the left-hand menu.
2. Click on the product the user needs access to.
3. Click the Users button in the command bar.
4. Click on _Add_.
5. Select the user from the drop-down.
6. Select a role for the user.
7. Select the rights the selected user needs on the product.
8. Click _Save_.
9. The user will receive an email that access has been granted for the selected product.

![](<../../.gitbook/assets/image (616).png>)

## Approve User Access Request

If there is [no Auto Approval or Default Subscription](setup-auto-approvals-default-subscriptions.md) setup, the Admin needs to approve a user's Access Request.&#x20;

If someone in your company lodged an access request for a product, an email will be sent to all Company Administrators within your company. The first available person with an administrative role within the Subscription Manager can approve the request. To approve an access request for a user, please follow the steps below.

1. Open the Subscriptions page from the left-hand menu.
2. Select the product for which the access request was lodged. A counter next to the product name will indicate the number of pending access requests you have for that product.
3. Click on _Access Requests_.
4. Click on the name of the user that lodged the request.
5. Select the role that the user should have on the product from the drop-down, for example, “_General User_“.
6. Select the rights the user should have on the product, for example, the [rights and roles for Data Stream Designer](manage-user-access.md#data-stream-designer-rights-and-roles) or [rights and roles for the App Designer](manage-user-access.md#app-designer-rights-and-roles).
7. Click _Save_.
8. The user who lodged the request will receive an email notifying him/ her that they have been granted access to the product.

![](<../../.gitbook/assets/image (266).png>)

## **Editing Rights and Access for a User**

If you need to edit rights for a user or a user’s role on a product, follow the steps below.

1. Open the Subscriptions page from the left-hand menu.
2. Select the product that you are looking to change a user's rights or access.
3. Click Users in the command bar to open the Users page.
4. Select the user whose rights or role you would like to change on a product.
5. Make any changes to the role of the selected user, as required.
6. Make any changes to the rights of the selected user, as required.
7. Click _Save._

![](<../../.gitbook/assets/image (1379).png>)

{% hint style="info" %}
Advise the user to sign out and back in again for the changes to take effect.
{% endhint %}

## **Removing Access for a User**

If you need to remove access for a user on a product, follow the steps below.

1. Open the Subscriptions page from the left-hand menu.
2. Select the product that you are looking to revoke a user's access.
3. Click Users in the command bar to open the Users page.
4. Select the user whose rights or role you would like to change on a product.
5. Click _Revoke Access_.
6. Confirm that you would like to remove access for the selected user on the selected product by clicking _Yes._

![](<../../.gitbook/assets/image (1103).png>)

## Data Stream Designer Rights and Roles <a href="#data-stream-designer-rights-and-roles" id="data-stream-designer-rights-and-roles"></a>

Several rights are maintained in Subscription Manager for Data Stream Designer. Each of these rights represents an aspect of the Data Stream Designer system that a user is allowed to see or access. Persons with administrative rights in Subscription Manager manage all rights.&#x20;

### Data Stream Designer Rights

The table below lists the rights that can be assigned to a user.

<table><thead><tr><th width="252">Right</th><th>Description</th></tr></thead><tbody><tr><td>CreateAgent</td><td>Allows for an <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/agent/@drafts">Agent</a> to be uploaded.</td></tr><tr><td>CreateCategory</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/category/@drafts">Category</a> to be created.</td></tr><tr><td>CreateCollection</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/collection/@drafts">Collection</a> to be created.</td></tr><tr><td>CreateUseCase</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/data-stream/@drafts">Data Stream</a> to be created, in which a user can create a Data Stream.</td></tr><tr><td>DeleteAgent</td><td>Allows for an Agent to be deleted.</td></tr><tr><td>DeleteCategory</td><td>Allows for a Category to be deleted.</td></tr><tr><td>DeleteCollection</td><td>Allows for a Collection to be deleted.</td></tr><tr><td>DeleteUseCase</td><td>Allows for a Data Stream to be deleted.</td></tr><tr><td>DesignUseCase</td><td>Allows for changes to be made to a Data Stream. This right allows a user to save changes to a Data Stream, as well as configure or delete Agents in a Data Stream. This right also allows for a user to copy a version of the Stream.</td></tr><tr><td>DisconnectCollectionHosts</td><td>Allows for the user to disconnect <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/collection/@drafts">Stream Hosts.</a>​</td></tr><tr><td>EditAgent</td><td>Allows for an Agent to be edited. This includes managing the versions available in Data Stream Designer for the Agent.</td></tr><tr><td>EditBusinessCase</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/how-tos/data-streams/use-business-case-and-notes/@drafts">Business Case</a> to be edited.</td></tr><tr><td>EditCategory</td><td>Allows for Categories to be edited.</td></tr><tr><td>EditCollection</td><td>Allows for a Collection to be edited.</td></tr><tr><td>EditNotes</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/how-tos/data-streams/use-business-case-and-notes/@drafts">Notes</a> to be edited.</td></tr><tr><td>EditUseCase</td><td>Allows for a Data Stream to be edited.</td></tr><tr><td>LiveView</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/how-tos/data-streams/use-live-view/@drafts">Live Data</a> from a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/how-tos/publish/@drafts">published Data Stream</a> to be viewed.</td></tr><tr><td>ManageVariables</td><td>Allows for the management of <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/variable/@drafts">Variables</a>.</td></tr><tr><td>PublishUseCase</td><td>Allows for a user to publish a Data Stream.</td></tr><tr><td>RevokeCollectionKey</td><td>Allows for a Collection key to be replaced with a new key.</td></tr><tr><td>SetHostLogLevel</td><td>Allows you to change the Host Log Levels between Info or Trace. <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/collection/@drafts">See the Collection and Stream Host article for more information.</a>​</td></tr><tr><td>ShareUseCase</td><td>Allows for Data Streams to be shared.</td></tr><tr><td>ViewAgent</td><td>Allows for a list of Agents to be viewed.</td></tr><tr><td>ViewCategory</td><td>Allows for a Category to be viewed.</td></tr><tr><td>ViewCollection</td><td>Allows for a Collection to be viewed.</td></tr><tr><td>ViewHostLogs</td><td>Allows for the ability to view logs created for Stream Hosts that are running.</td></tr><tr><td>ViewHosts</td><td>Allows for a list of the available Stream Hosts to be viewed.</td></tr><tr><td>ViewUseCase</td><td>Allows for a Data Stream to be viewed.</td></tr></tbody></table>

### Data Stream Designer Default Roles

A user is assigned a role and each role has appropriate rights for that function enabled.&#x20;

The table below illustrates which rights are included with each of the default roles. These default roles can be amended by the global administrator - who can also add new roles.

<table data-full-width="false"><thead><tr><th width="253">Right</th><th data-type="checkbox">Administrator</th><th data-type="checkbox">User</th></tr></thead><tbody><tr><td>CreateAgent</td><td>true</td><td>false</td></tr><tr><td>CreateCategory</td><td>true</td><td>false</td></tr><tr><td>CreateCollection</td><td>true</td><td>false</td></tr><tr><td>CreateUseCase</td><td>true</td><td>true</td></tr><tr><td>DeleteAgent</td><td>true</td><td>false</td></tr><tr><td>DeleteCategory</td><td>true</td><td>false</td></tr><tr><td>DeleteCollection</td><td>true</td><td>false</td></tr><tr><td>DeleteUseCase</td><td>true</td><td>true</td></tr><tr><td>DesignUseCase</td><td>true</td><td>true</td></tr><tr><td>DisconnectCollectionHosts</td><td>true</td><td>false</td></tr><tr><td>EditAgent</td><td>true</td><td>false</td></tr><tr><td>EditBusinessCase</td><td>true</td><td>true</td></tr><tr><td>EditCategory</td><td>true</td><td>false</td></tr><tr><td>EditCollection</td><td>true</td><td>false</td></tr><tr><td>EditNotes</td><td>true</td><td>true</td></tr><tr><td>EditUseCase</td><td>true</td><td>true</td></tr><tr><td>LiveView</td><td>true</td><td>true</td></tr><tr><td>ManageVariables</td><td>true</td><td>false</td></tr><tr><td>PublishUseCase</td><td>true</td><td>true</td></tr><tr><td>RevokeCollectionKey</td><td>true</td><td>false</td></tr><tr><td>SetHostLogLevel</td><td>true</td><td>false</td></tr><tr><td>ShareUseCase</td><td>true</td><td>true</td></tr><tr><td>ViewAgent</td><td>true</td><td>true</td></tr><tr><td>ViewCategory</td><td>true</td><td>true</td></tr><tr><td>ViewCollection</td><td>true</td><td>true</td></tr><tr><td>ViewHostLogs</td><td>true</td><td>false</td></tr><tr><td>ViewHosts</td><td>true</td><td>false</td></tr><tr><td>ViewUseCase</td><td>true</td><td>true</td></tr></tbody></table>

## ‌App Designer Rights and Roles

‌Several App Designer rights are maintained in Subscription Manager. Each of these rights represents an aspect of the App Designer system that a user is allowed to see or access. Persons with administrative rights in Subscription Manager manage all rights.&#x20;

### App Designer Rights

The table below lists the rights that can be assigned to a user.

<table><thead><tr><th width="255">Right</th><th>Description</th></tr></thead><tbody><tr><td>CreateApp</td><td>Allows for an <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/application/@drafts">Application</a> to be created.</td></tr><tr><td>CreateCategory</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/category/@drafts">Category</a> to be created.</td></tr><tr><td>CreateConnector</td><td>Allows for a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/connector/@drafts">Connector</a> to be created.</td></tr><tr><td>DeleteApp</td><td>Allows for an Application to be deleted.</td></tr><tr><td>DeleteAppFile</td><td>Allows for an <a href="../../concepts/application/app-files.md">App File</a> to be deleted.</td></tr><tr><td>DeleteCategory</td><td>Allows for a Category to be deleted</td></tr><tr><td>DeleteConnector</td><td>Allows for a Connector to be deleted.</td></tr><tr><td>DesignForm</td><td>Allows for changes to be made to a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/recommendation/form/@drafts">Form</a>. This right allows a user to add, edit, and delete Forms. If a user has the DesignRecommendation right they are able to select Forms for Rules, but not add, edit, or delete a Form.</td></tr><tr><td>DesignRecommendation</td><td>Allows for changes to be made to a <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/recommendation/@drafts">Recommendation</a>. This right allows a user to save changes to a Recommendation.</td></tr><tr><td>EditApp</td><td>Allows for an Application to be edited.</td></tr><tr><td>EditCategory</td><td>Allows for a Category to be edited.</td></tr><tr><td>EditConnector</td><td>Allows for a Connector to be edited.</td></tr><tr><td>ManageAccess</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/manage-access/@drafts">Design and Run Access</a> to Apps to be managed.</td></tr><tr><td>ManageAppConnections</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/application/data-integration#connection/@drafts">Connections</a> to be added, edited, and deleted.</td></tr><tr><td>ManageConnector<br>Categories</td><td>Allows for categories of Connectors to be added, edited, and deleted.</td></tr><tr><td>ManageRecommendation<br>Access</td><td>Allows for Design and Run Access to Recommendations to be managed.</td></tr><tr><td>ManageRecommendation<br>Categories</td><td>Allows for categories of Recommendations to be added, edited, and deleted.</td></tr><tr><td>ManageTemplate</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/application/template/@drafts">Templates</a> to be added, edited, and deleted.</td></tr><tr><td>ManageVariables</td><td>Allows for <a href="https://app.gitbook.com/@xmpro/s/xmpro-platform/~/drafts/-McRQI6uAA2BN6b_t2j4/variable/@drafts">Variables</a> to be added, edited, and deleted</td></tr><tr><td>UploadAppFile</td><td>Allows for an App File to be uploaded.</td></tr><tr><td>ViewApp</td><td>Allows for the user to view Applications in runtime mode.</td></tr><tr><td>ViewAppBar</td><td>Allows for the left menu bar to be viewed.</td></tr><tr><td>ViewCategory</td><td>Allows for Categories to be viewed.</td></tr><tr><td>ViewConnector</td><td>Allows for Connectors to be viewed.</td></tr><tr><td>ViewRecommendationAlert</td><td>Allows for Recommendation Alerts to be viewed.</td></tr><tr><td>ViewTemplate</td><td>Allows for Templates to be viewed.</td></tr></tbody></table>

### App Designer Default Roles

A user is assigned a role and each role has appropriate rights for that function enabled.&#x20;

The table below illustrates which rights are included with each of the default roles. These default roles can be amended by the global administrator - who can also add new roles.

<table data-full-width="false"><thead><tr><th width="253">Right</th><th width="146" data-type="checkbox">Administrator</th><th data-type="checkbox">Design User</th><th data-type="checkbox">User</th></tr></thead><tbody><tr><td>CreateApp</td><td>true</td><td>true</td><td>false</td></tr><tr><td>CreateCategory</td><td>true</td><td>false</td><td>false</td></tr><tr><td>CreateConnector</td><td>true</td><td>false</td><td>false</td></tr><tr><td>DeleteApp</td><td>true</td><td>true</td><td>false</td></tr><tr><td>DeleteAppFile</td><td>true</td><td>true</td><td>true</td></tr><tr><td>DeleteCategory</td><td>true</td><td>false</td><td>false</td></tr><tr><td>DeleteConnector</td><td>true</td><td>false</td><td>false</td></tr><tr><td>DesignForm</td><td>true</td><td>true</td><td>false</td></tr><tr><td>DesignRecommendation</td><td>true</td><td>true</td><td>false</td></tr><tr><td>EditApp</td><td>true</td><td>true</td><td>false</td></tr><tr><td>EditCategory</td><td>true</td><td>false</td><td>false</td></tr><tr><td>EditConnector</td><td>true</td><td>false</td><td>false</td></tr><tr><td>ManageAccess</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ManageAppConnections</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ManageConnector<br>Categories</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ManageRecommendation<br>Access</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ManageRecommendation<br>Categories</td><td>true</td><td>false</td><td>false</td></tr><tr><td>ManageTemplate</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ManageVariables</td><td>true</td><td>false</td><td>false</td></tr><tr><td>UploadAppFile</td><td>true</td><td>true</td><td>true</td></tr><tr><td>ViewApp</td><td>true</td><td>true</td><td>true</td></tr><tr><td>ViewAppBar</td><td>true</td><td>true</td><td>true</td></tr><tr><td>ViewCategory</td><td>true</td><td>true</td><td>true</td></tr><tr><td>ViewConnector</td><td>true</td><td>true</td><td>false</td></tr><tr><td>ViewRecommendationAlert</td><td>true</td><td>true</td><td>true</td></tr><tr><td>ViewTemplate</td><td>true</td><td>true</td><td>false</td></tr></tbody></table>

## ‌AI Rights and Roles

One right is maintained in Subscription Manager for XMPro AI. It represents an aspect of the AI system that a user is allowed to see or access. Persons with administrative rights in Subscription Manager manage it.&#x20;

### AI Rights

The table below lists the right that can be assigned to a user.

<table><thead><tr><th width="252">Right</th><th>Description</th></tr></thead><tbody><tr><td>Access Jupyter</td><td>Allows for XMPro Notebook to be accessed.</td></tr></tbody></table>

### AI Default Roles

A user is assigned a role and each role has appropriate rights for that function enabled.&#x20;

The table below illustrates which rights are included with each of the default roles. These default roles can be amended by the global administrator - who can also add new roles.

<table><thead><tr><th width="252">Right</th><th data-type="checkbox">Administrator</th></tr></thead><tbody><tr><td>Access Jupyter</td><td>true</td></tr></tbody></table>

## ‌XMPro Notebook Rights and Roles

Access rights for XMPro Notebook are controlled in Jupyter, not Subscription Manager.
