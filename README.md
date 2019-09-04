# GeoLocationBasedAd

This project involves geo location tracking and disaplying advertisement depending upon the criteria provided by the advertiser.
We have used below libraries in this project
* pandas
* numPy
![alt text](https://github.com/saumya-saumya/GeoLocationBasedAd/edit/master/CAPTURE.png)

Understanding Data:
This process started with the Collection of data related to how much they spent on advertising and marketing. After understanding and reading various details we understood the advertising cost is location dependent. The dataset of the users is collected from the google link provided, the application dataset with its attribute was found on google store dataset. After which we contacted a company to give us the bidding data, hence they provided us with the sample data because of their policy.
We cleaned the dataset by removing all the unwanted or non-ASCII characters in the whole dataset. In the user dataset we encountered users with some location which were not recognizable, therefore had to delete such users to avoid wrong location input. Also based on the user’s age grouped them into categories such as adult kid etc. Further we analyzed our dataset on the Tableau to find where the users are located on the map to avoid biased location recommendation. 
After gathering the necessary dataset, we tried to understand the data such that it can be used more effectively.

Some necessary conditions to be satisfied.
Bid_price<=App_price: To check if the bidding price of an advertiser is within range of price of application on the store.
Bid_Target==App_Target || Everyone: To check if the targeted age group in both dataset matches to filter out other irrelevant user age groups.
Bid_TargetSegment == App_TargetSegment: To check if the genre or category matches to obtain the final list of applications.
User_Location==Bid_Location: To match mandatory location within a certain range for both dataset to make it relevant to the user.
Bid_TargetGroup== User_TargetGroup: To check if both have same targeted users.
