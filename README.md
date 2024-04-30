# Movie Recommendation System
This repository contains a movie recommendation system implemented in Python using collaborative filtering techniques. The system utilizes both user-based and item-based collaborative filtering algorithms to generate movie recommendations for users based on their historical preferences.

## Installation

To run the recommendation system, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/cechup/Recommender-System-implemented-with-collaborative-filtering.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd Recommender-System-implemented-with-collaborative-filtering
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
### 1. Data Preparation
Before running the recommendation system, make sure to have a dataset of movie ratings in CSV format. Each row in the CSV file should represent a rating given by a user to a movie, with columns for the user ID, movie title, and rating.

### 2. Running the Recommendation System
The recommendation system consists of three main components:

- `RecSys_UserBased.py`: User-based collaborative filtering algorithm implementation.
- `RecSys_ItemBased.py`: Item-based collaborative filtering algorithm implementation.
- `RecSys_Output.py`: Output script to generate movie recommendations for a specific user.

#### User-Based Recommendations
To generate movie recommendations using the user-based collaborative filtering algorithm, run the following command:

```bash
python RecSys_UserBased.py
```

#### Item-Based Recommendations
To generate movie recommendations using the item-based collaborative filtering algorithm, run the following command:

```bash
python RecSys_ItemBased.py
```

#### Output Recommendations for a User
To obtain movie recommendations for a specific user, run the following command:
```bash
python RecSys_Output.py
```

Follow the prompts to enter the user ID for whom you want to generate recommendations. The script will output a list of the top 30 recommended movies for the specified user.

## Data Format

Ensure that your dataset is in the following format:

- CSV file with columns: `userId`, `title`, `rating`.
- Each row represents a rating given by a user to a movie.
- The `userId` column contains unique identifiers for users.
- The `title` column contains the titles of movies.
- The `rating` column contains the ratings given by users to movies.

## Author

Cecilia Peccolo

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
