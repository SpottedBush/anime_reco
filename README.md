# Anime Recommendation System

Welcome to the Anime Recommendation System project! This repository contains a machine learning-based recommendation system designed to suggest anime titles based on user preferences. Whether you are a fan looking for your next favorite series or a developer wanting to explore recommendation algorithms, this project provides a comprehensive solution.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Source](#dataset)

## Introduction

The Anime Recommendation System utilizes collaborative filtering and content-based filtering techniques to provide personalized anime recommendations. The system is built using Python and various machine learning libraries, offering both command-line interface (CLI) and web-based interface options.

## Features

- **User-Based Collaborative Filtering**: Recommends anime based on similar user preferences.
- **Item-Based Collaborative Filtering**: Suggests anime similar to those a user has liked.
- **Content-Based Filtering**: Recommends anime based on the content features of previously liked titles.
- **Hybrid Approach**: Combines multiple recommendation techniques for improved accuracy.
- **Web Interface**: Interactive web application for user-friendly recommendations.
- **CLI Tool**: Command-line interface for quick recommendations and data manipulation.

## Installation

To get started with the Anime Recommendation System, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SpottedBush/anime_reco.git
    cd anime_reco
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python setup_database.py
    ```

## Usage

### Command-Line Interface (CLI)

To get recommendations via the CLI, run:

```bash
python recommend.py --user-id <user_id> --method <method>
```

- `--user-id`: The ID of the user for whom to generate recommendations.
- `--method`: The recommendation method to use (user_based, item_based, content_based, or hybrid).

## Dataset

The dataset used for this project includes anime titles, user ratings, and metadata. You can download the dataset [here](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?select=users-score-2023.csv).

Ensure that the dataset files are placed in the `datasets/` directory at the root of the project.