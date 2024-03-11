# Release Notes

### v1.97, 22 Jun 2023

* Include Materialized Views in the Table property dropdown

### v1.96, 08 Mar 2023

* Handle column names with allowed special characters

### v1.95, 27 Feb 2023

* Made Column To Return optional unless Timeseries Aggregation is selected

### v1.94, 14 Oct 2022

* Fixed live update issue

### v1.93, 26 Sep 2022

* Handle sub-queries within the ADX query

### v1.92, 30 Jun 2022

* When the app page does not supply query parameter values during runtime, the Connector will use the original values that were specified as query parameters in the ADX query&#x20;

### v1.91, 28 Jun 2022

* Disable default date filter parameters when using query parameters

### v1.90, 27 Jun 2022

* Implemented query parameters functionality

### v1.83, 22 Jun 2022

* Optimized aggregation query using shuffle strategy and materialize function

### v1.82, 22 Jun 2022

* All non-numeric columns are added by default to the group by clause when using aggregation
* Changed the kql operator from contains to has in filter module for better performance

### v1.81, 21 Jun 2022

* Added help text to the Aggregation Parameters section: at least one column must be numeric

### v1.80, 16 Jun 2022

* Added live update functionality

### v1.70, 14 Jun 2022

* Added Timeseries dynamic aggregation functionality

### v1.60, 30 Nov 2021

* Resolved minor issue to make Sort, Take, and Order work at the source i.e. ADX

### v1.50, 01 Sep 2021

* Added Insert and Update operations to the entity to support refresh on button click without actual insert/update functionality

### v1.40, 28 Jun 2021

* Fixed issue with GetCustomQueryColumns

### v1.30, 25 Jun 2021

* Name change

### v1.20, 24 Jun 2021

* Non-static with token caching and HttpClient

### v1.10, 23 Jun 2021

* Non-static without token caching

### v1.00, 23 Jun 2021

* Initial Release
