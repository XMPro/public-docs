# Manage Access

Managing the access of users is important as it can improve the security of XMPro Objects. Permissions are given to users only based on what they need to do, for example, someone who only needs to view something can be given _read_ access. This can hide additional functionality that users do not need and also protect against unintentional tampering.&#x20;

Whether or not you can design a particular data stream, application, or other XMPro Objects is determined by the permissions that you have on it. The person that originally created the XMPro Object will be listed as the owner and can never lose his/her right to access it unless it is deleted. Other users can then be assigned read or read-and-write access.

{% embed url="https://www.youtube.com/watch?v=T-dr8cGbNoo" %}

## Grant Permissions

Granting permissions makes it easier for multiple users to collaborate on one particular XMPro Object. It also makes it easier to grant permissions to multiple users who are only allowed to view or read it without making changes, possibly to just give feedback or to discuss part of the XMPro Object.

### Permissions: Owner

The _Owner_ has full permission to make any changes required to the XMPro Object. The owner is also allowed to give other users access or change the permissions of existing users.

### Permissions: Co-Owner

The _Co-Owner_ has full permission to make any changes required to the XMPro Object. The Co-Owner is also allowed to give other users or change the permissions of existing users, except removing or changing the Owner's permissions.

### Permissions: Write

A person who has _Write_ access will be allowed to view, edit, publish and unpublish the XMPro Object.

### Permissions: Read

The _Read_ permission will allow a person to view the XMPro Object, but making any changes to the XMPro Object will be prohibited.

### Permission Matrix

| Permission/Operation | Owner | Co-Owner | Write | Read |
| -------------------- | ----- | -------- | ----- | ---- |
| View                 | ✓     | ✓        | ✓     | ✓    |
| Publish/Unpublish    | ✓     | ✓        | ✓     | ✗    |
| Edit                 | ✓     | ✓        | ✓     | ✗    |
| Delete               | ✓     | ✓        | ✗     | ✗    |
| Manage Versions      |       |          |       |      |
|   • View             | ✓     | ✓        | ✓     | ✓    |
|   • Create/Copy      | ✓     | ✓        | ✓     | ✗    |
|   • Delete           | ✓     | ✓        | ✗     | ✗    |
| Manage Access        | ✓     | ✓        | ✗     | ✗    |

![](<../.gitbook/assets/Access\_1 (1).png>)

![](<../.gitbook/assets/Access\_2 (2).png>)

![](<../.gitbook/assets/Access\_3 (2).png>)

## Actions on the Manage Access page

| **Action** | **Description**                                                       |
| ---------- | --------------------------------------------------------------------- |
| Add        | Adds a user.                                                          |
| Select     | Selects multiple users.                                               |
| Edit       | Edits the permissions of a particular user.                           |
| Cancel     | Discards any changes made to the user's permissions up to that point. |
| Delete     | Deletes a user.                                                       |

## Manage Run Access



{% hint style="warning" %}
For Apps, if a User has Design Access they will also automatically have access to run the App in view mode. However, for Recommendations, a User can only view Recommendation Alerts if they or their Business Role has Run Access, regardless of whether they have Design Access to the Recommendation.
{% endhint %}

![Run Access for the ACME Company and David only ](<../.gitbook/assets/image (574).png>)

## Business Roles (Company Administrator)

Business Roles are a hierarchical representation of the different areas of an organization. When managing access for XMPro Products, the Business Roles defined in Subscription Manager are used.

Business Roles are managed by the Administrator of a Company through the Users page.

![](<../.gitbook/assets/image (1209).png>)

All new users will automatically be added under the default 'All Employees' Business Role. Users can be moved, but not deleted from this list. A User can only be listed once underneath one Business Role.

![](<../.gitbook/assets/image (300).png>)

### Business Role of a User

Alternatively, a user's business role can also be managed from the user blade. See [Change Business Role](../administration/users/business-role-for-a-user.md).

<figure><img src="../.gitbook/assets/Users_Change Business Role.png" alt=""><figcaption></figcaption></figure>

### Sync Business Roles from Azure AD

If [Azure AD](../installation/3.-complete-installation/configure-sso-optional/sso-azure-ad.md) has been linked as your External Identity Provider, you can specify a claim name that Azure AD or the graph API will pass to Subscription Manager.&#x20;

When a user logs in, Subscription Manager will look at the value specified in this Claim and assign them to the Business Role with the same name.

[See the Sync Azure AD Role to SM's Business Role article for information on how to configure the claim name.](../installation/3.-complete-installation/configure-sso-optional/sso-azure-ad.md#sync-azure-ad-role-with-sms-business-role)

{% hint style="info" %}
If a Business Role with the same name doesn't exist, it will be created as a child under the default Business Role, 'All Employees'.
{% endhint %}

## Actions on the Manage Run Access page

| **Action** | **Description**                                                      |
| ---------- | -------------------------------------------------------------------- |
| Save       | Saves any changes made to the Manage Run Access up to this point.    |
| Discard    | Discards any changes made to the Manage Run Access up to this point. |

## Further Reading

* [How to Manage Access](../how-tos/manage-access.md)
