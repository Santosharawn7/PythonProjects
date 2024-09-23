# Importing necessary libraries
import numpy as np  # Used for handling arrays and mathematical operations
from lightfm.datasets import fetch_movielens  # Importing the MovieLens dataset
from lightfm import LightFM  # Importing the LightFM library, which implements collaborative filtering models

# Fetching the MovieLens dataset, filtering only movies with a rating of 4.0 or higher
data = fetch_movielens(min_rating=4.0)

# Printing a representation of the training and testing datasets
print(repr(data['train']))
print(repr(data['test']))

# Initializing the LightFM model with the 'warp' loss function
# WARP (Weighted Approximate-Rank Pairwise) is a ranking-based loss function suitable for implicit feedback
model = LightFM(loss='warp')

# Training the model on the training data for 30 epochs, using 2 threads for parallel computation
model.fit(data['train'], epochs=30, num_threads=2)

# Defining a function to generate recommendations for given user_ids
def sample_recommendation(model, data, user_ids):
    # Extracting the number of users and items from the training data
    n_users, n_items = data['train'].shape

    # Looping through each user_id provided in the user_ids list
    for user_id in user_ids:
        # Finding the items this user has positively interacted with (known positives)
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # Predicting scores for all items for this user (how likely they are to like each item)
        scores = model.predict(user_id, np.arange(n_items))

        # Sorting the items based on predicted scores, from highest to lowest
        top_items = data['item_labels'][np.argsort(-scores)]

        # Displaying the user ID
        print("User %s" % user_id)
        print("   Known positives:")

        # Displaying the first 3 known positive items for this user
        for x in known_positives[:3]:
            print("         %s" % x)

        # Displaying the top 3 recommended items for this user
        print("   Recommended:")

        for x in top_items[:3]:
            print("         %s" % x)

# If this script is run as the main program, call the sample_recommendation function
# with the model, data, and a list of specific user IDs [3, 25, 450]
if __name__ == '__main__':
    sample_recommendation(model, data, [3, 25, 450])
