import pandas as pd 
import CompaniesMod as cm

# function that concatenates multiple instances of a company (different periods)
def multi_period_table(*in_objs):
    # initialze data frame
    df_multi_period = pd.DataFrame()
    # for every provided object append it 
    for in_obj in in_objs:
        # Concatenate the DataFrame generated from each instance using create_df method
        df_multi_period = pd.concat([df_multi_period, in_obj.create_df()], ignore_index=False)
    return df_multi_period
