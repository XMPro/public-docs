# Sizing Guideline

This is a guideline for the compute resources needed for the different components in a deployment.

Small, medium, and large sizing estimates are provided. The small option starts with the minimum recommended resources and, generally, each subsequent size doubles the number of CPU cores and available RAM. Not all components experience the same increase in load, so the estimates may not increase at the same rate for all components.

Many factors influence the number of Apps and Data Streams a deployment can effectively run. These factors include:

* the number of data streams,
* how frequently the streams process data,
* the size of the data payload,
* the number of recommendations to be monitored,
* the number of apps and event boards being served,
* the complexity of apps and event boards (the number of elements and integration points),
* and the number of concurrent users accessing the apps and event boards.

As a rough guide, an example workload for a _Medium_-sized deployment would be:

* \~200 Data Streams running across
* \~15 Stream Hosts,
* serving data and triggering recommendations for \~10 Apps

## On-Premise

<table><thead><tr><th width="263">Component</th><th>Small</th><th>Medium</th><th>Large</th></tr></thead><tbody><tr><td>Subscription Manager (SM) <br><strong>1</strong><br></td><td><p>2 CPU</p><p>8GB RAM</p></td><td><p>2 CPU</p><p>8GB RAM</p></td><td>4 CPU<br>16GB RAM</td></tr><tr><td><p>Application Designer (AD)</p><p><br> </p></td><td><p>2 CPU</p><p>8GB RAM</p></td><td>4 CPU<br>16GB RAM</td><td><p>8 CPU</p><p>32GB RAM</p></td></tr><tr><td>Data Stream Designer (DS)<br><br></td><td><p>2 CPU</p><p>8GB RAM</p></td><td>4 CPU<br>16GB RAM</td><td><p>8 CPU</p><p>32GB RAM</p></td></tr><tr><td>Stream Host Server (SH) <br><strong>2,3</strong><br></td><td><p>2 CPU</p><p>8GB RAM</p></td><td>4 CPU<br>16GB RAM</td><td><p>8 CPU</p><p>32GB RAM</p></td></tr><tr><td><p>SQL Database Server </p><p>(Combined for SM, AD, DS) <br><strong>4</strong></p></td><td><p>2 CPU</p><p>8GB RAM</p></td><td><p>4 CPU</p><p>16GB RAM</p></td><td><p>8 CPU</p><p>32GB RAM</p></td></tr></tbody></table>

{% hint style="info" %}
#### **Footnotes**

**1** High volumes of concurrent users may require additional compute.

**2** Multiple Stream Hosts can be deployed to the Stream Host Server.

**3** If the Stream Host needs more resources, consider increasing the RAM before adding\
&#x20;  additional CPU cores as Stream Hosts perform in-memory processing of events.

**4** High volumes of recommendations may require additional compute and storage.
{% endhint %}

## Azure

Estimates for Azure target the Premium v3 service plan for applications, and Azure SQL Database for the databases.

Azure SQL database estimates are based on the General-Purpose service tier and use the DTU-based purchasing model (a blended measure of compute, storage, and IO resources).

<table><thead><tr><th width="257">Component</th><th>Small</th><th>Medium</th><th>Large</th></tr></thead><tbody><tr><td>Subscription Manager (SM) App Service Plan<br><strong>1</strong></td><td>P1v3</td><td>P1v3</td><td>P2v3</td></tr><tr><td>Application Designer (AD) App Service Plan<br></td><td>P1v3</td><td>P2v3</td><td>P3v3</td></tr><tr><td>Data Stream Designer (DS) App Service Plan<br></td><td>P1v3</td><td>P1v3</td><td>P2v3</td></tr><tr><td>Stream Host Server (SH) App Service Plan<br><strong>2,3</strong></td><td>P1v3</td><td>P2v3</td><td>P3v3</td></tr><tr><td><p>Azure SQL Database  </p><p>(For each of SM, AD, DS) <br><strong>4</strong></p></td><td>Standard – 20 DTUs</td><td>Standard – 50 DTUs</td><td>Standard – 100 DTUs</td></tr></tbody></table>

{% hint style="info" %}
**Footnotes**

**1** High volumes of concurrent users may require additional compute.

**2** Multiple Stream Hosts can be deployed to the Stream Host App Service Plan.

**3** If the Stream Host needs more resources, consider increasing the RAM before adding \
&#x20;  additional CPU cores as Stream Hosts perform in-memory processing of events.

**4** High volumes of recommendations may require additional compute and storage.
{% endhint %}

For additional details please see [Azure App Service Pricing](https://azure.microsoft.com/en-au/pricing/details/app-service/windows/) and [Azure SQL Database Pricing](https://azure.microsoft.com/en-au/pricing/details/azure-sql-database/single/#pricing).

## AWS

Estimates for AWS target Amazon EC2 T3 instances for applications, and an Amazon RDS T3 instance for the databases.

<table><thead><tr><th width="264">Component</th><th>Small</th><th>Medium</th><th>Large</th></tr></thead><tbody><tr><td>Subscription Manager (SM) EC2 Instance<br><strong>1</strong></td><td>t3.large</td><td>t3.large</td><td>t3.xlarge</td></tr><tr><td>Application Designer (AD) EC2 Instance<br></td><td>t3.large</td><td>t3.xlarge</td><td>t3.2xlarge</td></tr><tr><td>Data Stream Designer (DS) EC2 Instance<br></td><td>t3.large</td><td>t3.large</td><td>t3.xlarge</td></tr><tr><td>Stream Host Server (SH) EC2 Instance<br><strong>2,3</strong></td><td>t3.large</td><td>t3.xlarge</td><td>t3.2xlarge</td></tr><tr><td><p>Amazon RDS for SQL   </p><p>(Combined for SM, AD, DS) <br><strong>4</strong></p></td><td>t3.large</td><td>t3.xlarge</td><td>t3.2xlarge</td></tr></tbody></table>

{% hint style="info" %}
#### **Footnotes**

**1** High volumes of concurrent users may require additional compute.

**2** Multiple Stream Hosts can be deployed to the Stream Host Server.

**3** If the Stream Host needs more resources, consider increasing the RAM before adding \
&#x20;  additional CPU cores as Stream Hosts perform in-memory processing of events.

**4** High volumes of recommendations may require additional compute and storage.
{% endhint %}

For additional details please see [AWS EC2](https://aws.amazon.com/ec2/instance-types/) and [RDS instance types](https://aws.amazon.com/rds/instance-types/).

_Meta tags: XMPro Sizing; Sizing Guidelines; XMPro Guidelines._
