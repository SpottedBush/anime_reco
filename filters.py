import pandas as pd

def filter_data(user_df, item_df, threshold):
    item_df.drop(columns=['Other name', 'Name', 'Synopsis', 'Source', 'Premiered', 'Status', 'Producers', 'Licensors', 'Duration'], inplace=True) # Drop unnecessary columns
    item_df.rename(columns={'English name': 'Name'}, inplace=True) # Rename 'English name' to 'Name'
    item_df = item_df.drop(item_df[item_df.eq('UNKNOWN').any(axis=1)].index) # Drop rows with 'UNKNOWN' values
    item_df = item_df[item_df['Type'].isin(['Movie', 'TV', 'TV Short'])] # Only keep Movies, TV and TV Short
    item_df = item_df[item_df['anime_id'].isin(user_df['anime_id'])] # Only keep items that are in user_df

    user_df = user_df[user_df['anime_id'].isin(item_df['anime_id'])] # Only keep users that are in item_df
    user_counts = user_df['user_id'].value_counts() # Count the number of reviews per user
    user_df = user_df[user_counts[user_df['user_id']] > threshold] # Only keep users with more than threshold reviews
    user_df = user_df[user_df['rating'] != 0] # Remove reviews with rating 0 because it is not a valid rating
    return user_df, item_df
    
    
def load_and_filter_data(user_path, item_path, threshold=1000, logging=False):
    """Load and filter data

    Args:
        user_path (String): Path to user csv
        item_path (String): Path to item csv
        threshold (int, optional): Allow to keep users that has more than threshold reviews. Defaults to 1000.

    Returns:
        Pandas.DataFrame: Tuple of filtered user_df and item_df
    """
    if logging:
        print('Loading user ratings...')
    user_df = pd.read_csv(user_path)
    if logging:
        print('User ratings loaded')
        print('Loading animes list...')
    item_df = pd.read_csv(item_path)
    if logging:
        print('Animes list loaded')
    return filter_data(user_df, item_df, threshold)