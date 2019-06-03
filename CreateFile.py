import pandas as pd
import numpy as np

file1= 'C:/Users/saumy/PycharmProjects/GeoLocation/DataSet/google-play-store-apps/googleplaystore.csv'
file2 = 'C:/Users/saumy/PycharmProjects/GeoLocation/DataSet/bids-dataset-2/bid_requests.csv'
file3 = 'C:/Users/saumy/PycharmProjects/GeoLocation/DataSet/us-500/us-500.csv'


app = pd.read_csv(file1)
bidReq = pd.read_csv(file2)
user = pd.read_csv(file3)

app_data = pd.DataFrame(app)
bid_data=pd.DataFrame(bidReq)
user_data=pd.DataFrame(user)

for i in range(len(bid_data.Price)):
    print(bid_data.Bid_Id.values[i])
    bid_ID=(bid_data.Bid_Id.values[i])
    df2 = app_data.loc[((app_data['Price']) * 1000 >= bid_data.Price.values[i]) &
                       ((app_data['Age_group'] == bid_data.Target_group.values[i]) | (
                                   app_data['Age_group'] == 'Everyone'))]

    col = []
    col = (df2.columns.values)
    # print(col)
    final = pd.DataFrame(columns=col)
    name = (bid_data.Target_Segment.values[i])
    # print("NAME",name)
    # print(df2['Category'])
    filter_genre = df2.loc[(df2['Genres'].str.contains(name, na=False, case=False)) | (
            df2['Category'].str.contains(name, na=False, case=False))]
    # print(f'col names in filter genre {filter_genre.shape}')
    final = final.append(filter_genre, ignore_index=True)
    # print("FINALLLLLLLL",final.shape)
    # print("FINAL FILE DATAFRAME",final)

    final.drop_duplicates(keep='first', inplace=True)


    '''
    for j in range(len(final.Age_group)):
        age = final.Age_group.values[j]
        age_filter = final.loc[(final['Age_group'].str.contains(age, case=False))]
        age_filter.to_csv('bid_id_apps'+str(i)+'.csv')
    '''

'''
For Each BidID we need targeted Customers

'''

for i in range(len(bid_data.id_Location)):
    location =bid_data.id_Location.values[i]
    Age_group=bid_data.Target_group.values[i]
    print(location)
    finduser=user_data.loc[(user_data['state'].str.contains(location, na=False, case=False))&
                           user_data['Age_group'].str.contains(Age_group, na=False, case=False)]
    if not(finduser.empty):
        finduser.to_csv('users_bidId'+str(i+1)+'.csv', index=False)
        print(finduser)




print("Reached end of file")