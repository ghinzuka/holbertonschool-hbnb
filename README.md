# HBnB Evolution: Part 1 (Model + API)

Welcome to the HBnB Evolution: Part 1 (Model + API), a RESTful API for managing cities, countries, users, and amenities using Flask and Flask-Restx.

Here is the UML for the models
![HBNB-Pouquerou-Grauleau (1)](https://github.com/ghinzuka/holbertonschool-hbnb/assets/102736316/216fbb01-a86b-4c36-8864-90bc50ea5302)


## Features

**Users**: Create, read, update, delete users.

**Cities**: Manage cities including CRUD operations.

**Countries**: CRUD operations for managing countries.

**Amenities**: Create, read, update, delete amenities.

## Getting Started

To run the application, follow these steps:

### Prerequisites

Python 3
Flask
Flask-Restx

### Installation

Clone the repository:
   ```bash
   git clone https://github.com/ghinzuka/holbertonschool-hbnb.git
   cd holbertonschool-hbnb
   ```
Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Setting Up
Initialize the data files:
For cities: Create a `data/cities.json` file.
For countries: Create a `data/countries.json` file.
For amenities: Create an `amenity_data.json` file.
Run the Flask application:
   ```bash
   python3 app_combined.py
   ```
Access the API:
   Open your browser or use tools like Postman to interact with the following endpoints:
Users API: [http://localhost:5000/users](http://localhost:5000/users)
Cities API: [http://localhost:5000/cities](http://localhost:5000/cities)
Countries API: [http://localhost:5000/countries](http://localhost:5000/countries)
Amenities API: [http://localhost:5000/amenities](http://localhost:5000/amenities)
## API Endpoints 
### Users
**GET** `/users`: List all users.

**POST** `/users`: Create a new user.

**GET** `/users/<user_id>`: Fetch a specific user.

**PUT** `/users/<user_id>`: Update a user.

**DELETE** `/users/<user_id>`: Delete a user.
### Cities
**GET** `/cities`: List all cities.

**POST** `/cities`: Create a new city.

**GET** `/cities/<city_id>`: Fetch a specific city.

**PUT** `/cities/<city_id>`: Update a city.

**DELETE** `/cities/<city_id>`: Delete a city.
### Countries
**GET** `/countries`: List all countries.

**POST** `/countries`: Create a new country.

**GET** `/countries/<country_code>`: Fetch a specific country.

**PUT** `/countries/<country_code>`: Update a country.

**DELETE** `/countries/<country_code>`: Delete a country.
### Amenities
**GET** `/amenities`: List all amenities.

**POST** `/amenities`: Create a new amenity.

**GET** `/amenities/<amenity_id>`: Fetch a specific amenity.

**PUT** `/amenities/<amenity_id>`: Update an amenity.

**DELETE** `/amenities/<amenity_id>`: Delete an amenity.
## Error Handling
The API handles various errors such as invalid data, resource not found, and conflicts (e.g., duplicate entries) using appropriate HTTP status codes and error messages.
## Documentation
API documentation is available via Swagger UI at [http://localhost:5000/](http://localhost:5000/). This provides details on all available endpoints, request/response formats, and example usage.
## Testing
Unit tests for each endpoint can be found in the `tests/` directory. Run tests using pytest:
  ```bash
  python3 -m unittest ./tests/test_country.py 
  ```

## Authors
This project was made by :
* <[[@ghinzuka](https://github.com/ghinzuka)]> POUQUEROU BAPTISTE
* <[Matthieu Grauleau](https://github.com/MatthieuGrauleau)>

## License
MIT License Copyright (c) 2021 Othneil Drew Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
