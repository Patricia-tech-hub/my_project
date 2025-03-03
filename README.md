# My Project Asteroids

# My Project Asteroids

## Description
This project retrieves data about asteroids that have approached Earth using NASA's API. It provides a command-line interface (CLI) to fetch and display information about these asteroids.

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a conda environment:
    ```sh
    conda env create -f environment.yml
    conda activate project_asteroids
    ```

3. Install the package:
    ```sh
    pip install -e .
    ```

## Usage
To get a list of asteroids that have approached Earth around a given date, run the following command:
```sh
asteroids <YYYY-MM-DD>


