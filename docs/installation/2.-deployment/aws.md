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

# AWS

## Architecture

The following deployment diagram shows an example architecture and the necessary resources for the XMPro platform in AWS.

<figure><img src="../../.gitbook/assets/AWS_Architecture_as of March 1,2024x1.png" alt=""><figcaption><p>Fig 1: Example XMPro architecture in AWS</p></figcaption></figure>

The solution is deployed as an auto-scaling Elastic Beanstalk Application with 3 environments:

* SM – Subscription Manager
* AD – Application Designer
* DS – Data Stream Designer & API

These environments use Redis for a centralized Cache and RDS for database storage.

All data transfers are done via HTTPS and the SSL certificates are managed in AWS Certificate Manager.

There are two accounts set up: one for production and one for non-production. Both of these environments follow the above architecture and deployment.

## Prerequisites

In order to proceed with the deployment, you are required to complete the steps in the **1. Preparation** guide:

1. Meet the [**hardware** requirements](../install.md#hardware-requirements)
2. Install the [**software** requirements](../install.md#software-requirements)
3. Follow the [certificate and communication steps](../install.md#preparation-steps)&#x20;

{% hint style="info" %}
**Two SSL Certificates are required**

1. An SSL Certificate in AWS Certificate Manager, used by IIS (See the [Appendix](aws.md#ssl-certificate-in-certificate-manager) guide).\

2. An SSL Certificate, used by the SM instance (added to the [S3 Bucket](aws.md#create-s3-bucket) during the installation).\
   Create or ask your administrator for an SSL certificate with the correct DNS name. A self-signed certificate is good enough. There are many ways to generate this certificate, one of which is described in the above [1. Preparation](../install.md#https-ssl-certificate) guide. Please note the file names **must** be called **ssl.pfx** and **ssl.password.txt**.
{% endhint %}

**Resources**&#x20;

We are going to be deploying the following resources, please ensure you have the desired domain names ready.

1. SQL RDS
2. Parameter Store
3. Elastic Beanstalk Application
4. Elastic Beanstalk Environment – Subscription Manager
5. Elastic Beanstalk Environment – App Designer
6. Elastic Beanstalk Environment – Data Stream Designer & API

An example of preferred domain names is as follows; each set is for a specific account as per the architecture diagram.

For production:

* https://sm-xmpro․_**domain**_․com
* https://ad-xmpro․_**domain**_․com
* https://ds-xmpro․_**domain**_․com

For non-production:

* https://sm-nonprod-xmpro․_**domain**_․com
* https://ad-nonprod-xmpro․_**domain**_․com
* https://ds-nonprod-xmpro․_**domain**_․com

Log on to the [AWS Management Console](https://console.aws.amazon.com/) and switch to the region you want to deploy the solution in, you will need Administrative rights to the subscription to complete the deployment.

## ElastiCache

Search for **ElastiCache** in the _**Services**_ dropdown and select it.

1. Click the _Get Started Now_ button from the screen that opens.

![](<../../.gitbook/assets/image (359).png>)

![](<../../.gitbook/assets/image (275).png>)

2\. Make sure _Redis_ is selected, click create.

![](<../../.gitbook/assets/image (701).png>)

3\. Provide a name for the cache, select the size and leave the rest of the Redis options as defaults.

![](<../../.gitbook/assets/image (1363).png>)

4\. Provide the _Subnet_ information and select the VPC to deploy Redis in.

![](<../../.gitbook/assets/image (315).png>)

5\. Click _Create_ to complete the Redis configuration and create the cache.

![](<../../.gitbook/assets/image (1686).png>)

6\. Once created, select **EC2** from _**Services,**_ and under _Network & Security_ click Security Groups.

7\. Edit the default security group and add _Redis Port 6379_ to the Inbound rules.

![](<../../.gitbook/assets/image (1621).png>)

8\. Make a note of the Redis endpoint as it will be used later within the Redis Connection string.

![](<../../.gitbook/assets/image (1613).png>)

{% hint style="info" %}
Note:

* Currently, SignalR doesn’t support Redis Clusters [https://docs.microsoft.com/en-us/aspnet/signalr/overview/performance/scaleout-with-redis](https://docs.microsoft.com/en-us/aspnet/signalr/overview/performance/scaleout-with-redis)
* Sticky Sessions must be used for SignalR [https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-6.0](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-6.0)
{% endhint %}

## Amazon RDS Creation

In the AWS Management Console choose **RDS** under _**Database**_ in the _**Services**_ drop-down.

1. Click _Databases_ and then click _Create database._

![](<../../.gitbook/assets/image (216).png>)

2\. Select _Easy Create_, _SQL Server,_ and the desired Tier for the database instance.

![](<../../.gitbook/assets/image (1584).png>)

3\. Provide the _DB instance Identifier_, _Username,_ and _Password_ for the RDS database instance.\
&#x20;   Click create.

![](<../../.gitbook/assets/image (1476).png>)

4\. Once created it will appear as below:

![](<../../.gitbook/assets/image (1442).png>)

5\. Click the _DB Identifier_ just created.

{% hint style="info" %}
Make a note of the following:

* _Endpoint_ - In this example: _aero-sql.cug4m2yk6h94.ap-south-1.rds.amazonaws.com_
* User - as specified earlier
* Password - as specified earlier
{% endhint %}

![](<../../.gitbook/assets/image (144).png>)

6\. The security group will need to be modified to allow inbound traffic this is done as follows:

6.1. Click the _VPC security groups_.

![](<../../.gitbook/assets/image (1513).png>)

6.2. Select the _Default_ security group, click _Inbound_ then click _Edit_.

![](<../../.gitbook/assets/image (1049).png>)

6.3. Add a new rule called **MS SQL**, with _Protocol_ as **TCP** and _Port Range_ as **1433**; and click Save.

![](<../../.gitbook/assets/image (689).png>)

## Parameter Store Identity and Access

1. Click IAM under Security, Identity & Compliance

![](<../../.gitbook/assets/image (193).png>)

2\. In IAM click policies click Create policy&#x20;

![](<../../.gitbook/assets/image (1353).png>)

3\. Select Import managed policy

![](<../../.gitbook/assets/image (281).png>)

4\. Search and select AmazonSSMManagedInstanceCore then click Import

![](<../../.gitbook/assets/image (347).png>)

5\. Click Add additional permission

![](<../../.gitbook/assets/image (620).png>)

6\. Choose service Systems Manager

![](<../../.gitbook/assets/image (1241).png>)

7\. Select Read and click Review Policy

![](<../../.gitbook/assets/image (1425).png>)

8\. Expand resources and resolve all the warnings by clicking All Resources.

![](<../../.gitbook/assets/image (1817).png>)

9\. Enter a Name and Description for the policy and click Create Policy

![](<../../.gitbook/assets/image (693).png>)

10\. Search for the Newly created policy, select it, and click Policy Actions

![](<../../.gitbook/assets/image (298).png>)

11\. Select Attach from Policy actions

![](<../../.gitbook/assets/image (1072).png>)

12\. Attach this new policy to the role aws-elasticbeanstalk-service-role and click Attach Policy

![](<../../.gitbook/assets/image (1039).png>)

####

## Create Elastic Beanstalk Application

The first step in using AWS Elastic Beanstalk is to create an application, which represents your web application in AWS. In Elastic Beanstalk an application serves as a container for the environments that run your web app and for versions of your web app's source code, saved configurations, logs, and other artifacts that you create while using Elastic Beanstalk.

1. Open the **Elastic Beanstalk** console, and then, in the _regions_ drop-down list, select your region.

![](<../../.gitbook/assets/image (798).png>)

2\. In the navigation pane, choose **Applications**, and then click _Create Application_.

![](<../../.gitbook/assets/image (92).png>)

3\. Use the on-screen form to provide an _application name_.

![](<../../.gitbook/assets/image (1788).png>)

4\. Click Create.

![](<../../.gitbook/assets/image (75).png>)

{% hint style="info" %}
You have successfully created the application. Next, we'll create the application's environments for each product: Subscription Manager, Data Stream Designer, and App Designer.
{% endhint %}

## Subscription Manager

### Create Environment

1. Select the Application, click on Actions then click Create environment

![](<../../.gitbook/assets/image (1321).png>)

2\. Click Select

![](<../../.gitbook/assets/image (1467).png>)

3\. Provide the _Environment name_ for Subscription Manager.

![](<../../.gitbook/assets/image (108).png>)

4\. Select the Platform information.&#x20;

5\. Select Sample Application and click Configure more options

![](<../../.gitbook/assets/image (301).png>)

6\. Click Edit under the Capacity section.

![](<../../.gitbook/assets/image (657).png>)

7\. Select **Load Balanced** under Environment Type and set the required Instance Min and Max to **1**. (More information can be found [here](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html))

![](<../../.gitbook/assets/image (43).png>)

8\. Change the Instance type to the required instance type.

![](<../../.gitbook/assets/image (635).png>)

9\. Click _Save._

![](<../../.gitbook/assets/image (1370).png>)

10\. Click _Edit_ under the **Network** section.

![](<../../.gitbook/assets/image (1703).png>)

11\. Under the _VPC_ section select the VPC this environment should run in, set the _visibility_ according to your requirements and select the load balancer availability zones.&#x20;

12\. Scroll down and click _Save._

![](<../../.gitbook/assets/image (942).png>)

13\. Click _Edit_ under the **Load balancer** section.

![](<../../.gitbook/assets/image (446).png>)

14\. Select _Application Load Balancer_ and scroll down.

15\. Click _Add listener._

![](<../../.gitbook/assets/image (349).png>)

16\. Enter _**443**_ in _Port_

17\. Select _Protocol_ _**HTTPS**_.

18\. Select the SSL certificate you added in the Certificate Manager earlier on and click _Add_.

19\. Scroll down.

![](<../../.gitbook/assets/image (145).png>)

20\. Select the _**default**_ Process and under Actions click _Edit._

![](<../../.gitbook/assets/image (1483).png>)

21\. Change the _Port_ to _**443**_ and the _Protocol_ to _**HTTPS**_, then scroll down.

![](<../../.gitbook/assets/image (1628).png>)

22\. Tick the _Stickiness policy enabled_ option and click _Save._

![](<../../.gitbook/assets/image (1627).png>)

23\. Click _Save._

![](<../../.gitbook/assets/image (675).png>)

24\. Click _Create environment_ to have the defined environment created.

![](<../../.gitbook/assets/image (1224).png>)

### Create S3 Bucket

1. In the AWS Management Console, choose **S3** under _**Storage**_ in the _**Services**_ drop-down.

![](<../../.gitbook/assets/image (857).png>)

4. In S3 click _Create Bucket_ to create a new bucket.
5. Enter a name for the bucket name and click _Create bucket_.
6. Select the Region for your bucket
7. Remove the checkmark for Block Public Access

![](<../../.gitbook/assets/image (793).png>)

8. Acknowledge the warning for a public bucket

![](<../../.gitbook/assets/image (1322).png>)

9. Click Create Bucket

![](<../../.gitbook/assets/image (978).png>)

![](<../../.gitbook/assets/image (1637).png>)

10. Copy the _sign.pfx_ and _sign.password.txt_ files (the signing certificate referenced in the [1. Preparation](../install.md#signing-certificate) guide) into the bucket and ensure the files are publicly accessible.
11. Copy the _ssl.pfx_ and _ssl.password.txt_ files (the SSL certificate referenced in the [1. Preparation](../install.md#https-ssl-certificate) guide) into the bucket and ensure the files are publicly accessible.

{% hint style="info" %}
The signing certificate is between the end user and the load balancer. The instance SSL certificate is used between the instances and the load balancer.
{% endhint %}

### Install Subscription Manager

1\. Run the installation wizard for Subscription Manager

![](<../../.gitbook/assets/image (512).png>)

2\. Run Subscription manager as Administrator

![](<../../.gitbook/assets/image (479).png>)

3\. Follow the instruction in the installation wizard: click Next.

![](<../../.gitbook/assets/image (1304).png>)

4\. Select the Install option (1) and click Next (2).

![](<../../.gitbook/assets/image (410).png>)

5\. Tick Database (1), Web Application (2), select AWS Package (3), and click Next (4).

![](<../../.gitbook/assets/image (1382).png>)

6\. Enter the secret store prefix (1), the S3 Bucket name from earlier (2), and click Next (3).

![](<../../.gitbook/assets/image (1260).png>)

7\. Select the installation path (1), the DNS name for the site (2), and click Next (3).

![](<../../.gitbook/assets/image (1642).png>)

8. Enter the SMTP details referenced in the [1. Preparation](../install.md#smtp-account) guide and click Test SMTP settings (1), If successful, click Next (2).

![](<../../.gitbook/assets/image (1374).png>)

9\. Enter the Signing Certificate details:&#x20;

![](<../../.gitbook/assets/image (1387).png>)

9.1. Browse to the certificate created earlier\
9.2. Enter the certificate password\
9.3. Select the subject name\
9.4. Select Local Machine\
9.5. Click Next

10\. Click Next once the installation has completed.

![](<../../.gitbook/assets/image (578).png>)

11\. Make a note of the Username and password, and click Finish.

![](<../../.gitbook/assets/image (1846).png>)

####

#### AWS Systems Manager – Parameter Store

1. Navigate to Parameter Store in AWS Systems Manager.

![](<../../.gitbook/assets/image (684).png>)

![](<../../.gitbook/assets/image (819).png>)

2\. Click **Create parameter**.

![](<../../.gitbook/assets/image (951).png>)

3\. Create a SecureString parameter.

![](<../../.gitbook/assets/image (778).png>)

![](<../../.gitbook/assets/image (866).png>)

4\. Browse to the folder where SM was installed

![](<../../.gitbook/assets/image (319).png>)

5\. Edit the file called App Secrets.xml: create the parameters as per the line items in the file:

![](<../../.gitbook/assets/image (204).png>)

6\. Locate the S3 folder in the deployment folder. Copy the contents to the S3 Bucket you created.

![](<../../.gitbook/assets/image (79).png>)

### Deploy the Subscription Manager

1. Click Environments in Elastic Beanstalk service
2. Click the SM Environment you created earlier

![](<../../.gitbook/assets/image (1417).png>)

3\. Use the on-screen form to upload the zip file.

![](<../../.gitbook/assets/image (393).png>)

4\. Select the zip file to deploy from the folder where SM was installed. Click Deploy.

![](<../../.gitbook/assets/image (544).png>)

5\. Navigate to the URL and log in using the following credentials:

* admin@xmpro․onxmpro․com&#x20;
* Pass@word1

![](<../../.gitbook/assets/image (1505).png>)

6\. Reset the administrator password and store it securely in a password vault.

7\. Click SM

![](<../../.gitbook/assets/image (1804).png>)

8\. Click Products

![](<../../.gitbook/assets/image (1414).png>)

9\. Click Installation Profile

![](<../../.gitbook/assets/image (362).png>)

## Data Stream Designer

### Create Environment

1. In the AWS Management Console choose **Elastic Beanstalk** under _Compute_ in the _**Services**_ drop-down.
2. In the navigation pane, choose _Environments_
3. On the application overview page, choose _Create a new environment_.
4. Follow the same instructions on environment creation as done for the Subscription Manager.

![](<../../.gitbook/assets/image (1664).png>)

5\. Run the Data Stream Designer installer as Administrator. Click Next.

![](<../../.gitbook/assets/image (74).png>)

6\. Select Install (1) and click Next (2).

![](<../../.gitbook/assets/image (314).png>)

7\. Select the items as shown below and click Next.

![](<../../.gitbook/assets/image (925).png>)

8\. Provide a Prefix and the S3 Bucket name

![](<../../.gitbook/assets/image (1286).png>)

9\. Provide the Database Details:

* Provide the SQL endpoint
* Change the SQL user
* Select a new DB and provide a name for the DB

![](<../../.gitbook/assets/image (846).png>)

10\. Provide the DNS name for the Environment

![](<../../.gitbook/assets/image (1446).png>)

11\. Browse to the downloaded installation profile and select it

![](<../../.gitbook/assets/image (1210).png>)

12\. Login using the credentials for SM

![](<../../.gitbook/assets/image (1200).png>)

13\. Click Next

![](<../../.gitbook/assets/image (852).png>)

14\. Once the installation completes, click Next

![](<../../.gitbook/assets/image (140).png>)

15\. Click Finish

![](<../../.gitbook/assets/image (696).png>)

### Install & Deploy Data Stream Designer

1. Browse to the installation folder, as outlined in [Subscription Manager](aws.md#install-subscription-manager).
2. Edit the App Secrets.xml file and create the Parameters in System Manager.
3. Upload and deploy the package.zip file to the newly created environment using upload and deploy as per SM deployment.

## App Designer

### Create Environment

1. In the AWS Management Console, choose **Elastic Beanstalk** under _Compute_ in the _**Services**_ drop-down.
2. In the navigation pane, choose _Environments_
3. On the application overview page, choose _Create a new environment_.
4. Follow the same instructions on environment creation as done for the Subscription Manager.

![](<../../.gitbook/assets/image (1664).png>)

5\. After installing Application Designer, run the setup as Administrator and click Next.

![](<../../.gitbook/assets/image (1694).png>)

6\. Select Install and click Next.

![](<../../.gitbook/assets/image (1844).png>)

7\. Select the items as below and click Next.

![](<../../.gitbook/assets/image (1700).png>)

8\. Provide the SQL endpoint and click Next.

![](<../../.gitbook/assets/image (8).png>)

9\. Provide the DNS name for the environment and click Next.

![](<../../.gitbook/assets/image (1749).png>)

10\. Provide the URL for the Data Stream Designer installed earlier, and click Next.

![](<../../.gitbook/assets/image (320).png>)

11. Enter the SMTP details referenced in the [1. Preparation](../install.md#smtp-account) guide and click Next.&#x20;

![](<../../.gitbook/assets/image (374).png>)

12. Enter the Twilio details referenced in the [1. Preparation](../install.md#twilio-optional) guide and click Next. If you don't want SMS notifications you can select "None" from the "Select Provider" dropdown.

![](<../../.gitbook/assets/image (1532).png>)

13\. Browse to the downloaded installation profile and select it. Click Next.

![](<../../.gitbook/assets/image (406).png>)

14\. Login with SM credentials to authenticate.

![](<../../.gitbook/assets/image (1835).png>)

15\. Click Next.

![](<../../.gitbook/assets/image (962).png>)

16\. Click Next after the installation is complete.

![](<../../.gitbook/assets/image (385).png>)



17\. Click Finish.

![](<../../.gitbook/assets/image (210).png>)

### Install & Deploy App Designer

1. Browse to the installation folder, as outlined in [Subscription Manager](aws.md#install-subscription-manager)
2. Edit the App Secrets.xml file and create the Parameters in System Manager.
3. Upload and deploy the package.zip file to the newly created environment using upload and deploy as per SM deployment.

![](<../../.gitbook/assets/image (1664).png>)

## Appendix

### SSL certificate in Certificate Manager

In the AWS console go to the Certificate Manager

* Select the region the SSL Certificate is required in
* The certificate can be either imported or a new certificate can be requested.

#### To request a new certificate

![](<../../.gitbook/assets/64 (1).png>)

1. Click _**Get started**_ under Provision Certificate

![](<../../.gitbook/assets/65 (1).png>)

2\. Click _**Request a certificate**_

![](../../.gitbook/assets/66.png)

3\. Enter the certificate domain name and click _**Next**_

![](../../.gitbook/assets/67.png)

4\. Select the DNS validation method and click _**Next**_

![](<../../.gitbook/assets/68 (1).png>)

5\. Review your settings and click _**Confirm and request**_ if correct

![](<../../.gitbook/assets/69 (1).png>)

6\. Once the DNS configuration file becomes available, click _**Continue**_

![](<../../.gitbook/assets/70 (1).png>)

7\. Contact your IT administrator to complete the DNS verification by adding the CNAME record to your website DNS

![](../../.gitbook/assets/71.png)

8\. Once the DNS verification is complete the SSL certificate is added to your certificate manager for the specified region

#### To import a certificate

![](<../../.gitbook/assets/72 (1).png>)

1. Click _**Get started**_ under Provision Certificate

![](<../../.gitbook/assets/73 (1).png>)

2\. Click _**Import a certificate**_

![](../../.gitbook/assets/74.png)

3\. Complete the certificate detail and click _**Next**_ to import the certificate

### Create the EB Application URLs

1. Search for **ElastiCache** in the _**Services**_ dropdown and select it.

![](../../.gitbook/assets/75.png)

2\. In the left-hand panel, click _Hosted Zones._

![](../../.gitbook/assets/76.png)

3\. Click _Create Hosted Zone._

![](<../../.gitbook/assets/77 (1).png>)

1. In the right-hand panel complete the _Domain Name_ using the domain name you created the SSL certificate for and click _Create_.

![](<../../.gitbook/assets/78 (1).png>)

5\. Click _Create Record Set._

![](../../.gitbook/assets/79.png)

6\. Change _Alias_ to _**Yes**_, then go to EC2 in AWS services and scroll down to Load Balancing and click Load Balancers.

![](../../.gitbook/assets/80.png)

7\. Select a Load Balancer and click _Tags_ to identify what Application is serviced by the selected Load Balancer.

![](../../.gitbook/assets/81.png)

8\. When the correct Load Balancer for the Application is identified, click the _Description_ Tab.

![](<../../.gitbook/assets/82 (1).png>)

9\. Copy the _DNS Name_ for the Load Balancer. Go back to the Record Set you created in Route 53.

![](<../../.gitbook/assets/83 (1).png>)

10\. Paste the Load Balancer DNS address in the Alias Target field and click Create.

This needs to be completed for each ELB Application.

![](<../../.gitbook/assets/84 (1).png>)

11\. The NS values must be provided to you by the DNS Administrator to create the NS records in the Domain DNS records. This needs to be completed for each ELB Application.

### Configure the security groups

1. In the AWS Management Console, choose **EC2** under _Compute_ in the _**Services**_ drop-down.
2. Click _Security Groups_ under the NETWORK & SECURITY option.

![](<../../.gitbook/assets/85 (1).png>)

3\. Click _Create security group._

![](<../../.gitbook/assets/86 (1).png>)

4\. Create the _**RDS\_security\_group**_ and select the _VPC_.

![](<../../.gitbook/assets/87 (1).png>)

5\. Add the following rules and replace the source with the security groups assigned to the environments you created earlier.

6\. Create an additional security group called _**REDIS\_Cache\_security\_group.**_

![](<../../.gitbook/assets/88 (1).png>)

7\. Add these rules again using the security groups for the environments created earlier as the source.

![](<../../.gitbook/assets/89 (1).png>)

8\. In Elastic Beanstalk, select the environment you want to change.

![](<../../.gitbook/assets/90 (1).png>)

9\. Click Configuration in the left pane

![](../../.gitbook/assets/91.png)

10\. Remove the _default_ security group and click _Apply._ Do this for all the environments.

![](../../.gitbook/assets/92.png)

11\. In Services, selects _**RDS**_ and click _Databases._

![](<../../.gitbook/assets/93 (1).png>)

12\. Select your RDS database and click _Modify._

![](../../.gitbook/assets/94.png)

13\. Scroll down to _Network and Security_. Select the RDS security group you created earlier and remove the _default_ security group.

![](../../.gitbook/assets/95.png)

14\. Scroll down and click _Continue._

![](<../../.gitbook/assets/96 (1).png>)

15\. Select _**Apply Immediately**_ and click _Modify DB Instance._

![](<../../.gitbook/assets/97 (1).png>)

16\. Select _**ElastCache**_ from _Services_ and click **Redis.**

![](../../.gitbook/assets/98.png)

17\. Select the Redis Cache you created earlier and from _Actions_ click _**Modify.**_

![](../../.gitbook/assets/99.png)

18\. Edit the Security Groups

![](<../../.gitbook/assets/100 (1).png>)

19\. Remove the default security groups and add the Redis Cache security group created earlier. Click save and modify.

## Next Step: Complete Installation

The installation of the XMPro Platform is now complete, but there are some environment setup steps before you can use the platform. Please click the below link for further instructions:

{% content-ref url="../3.-complete-installation/" %}
[3.-complete-installation](../3.-complete-installation/)
{% endcontent-ref %}
