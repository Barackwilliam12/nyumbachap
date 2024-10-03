
# NyumbaChap

NyumbaChap is a web application developed using Django for finding houses in Tanzania. The platform allows users to search for houses by location, price, status (for rent or sale), and more. It also provides a secure chat system between property owners and potential customers, along with customizable user profiles and dashboards.

## Features

- **Search for Properties**: Search by region, district, ward, price range, number of rooms, and house status (for rent/sale).
- **Private Chat**: Secure private messaging between property owners and customers.
- **User Profiles**: Customizable profiles with bio, role, address, and profile images.
- **User Dashboard**: Property owners can manage their listings and messages in a personal dashboard.
- **Blog Section**: A blog where users can post articles related to the real estate market.
- **Billing Plans**:
  - **Silver Plan**: Free listing option for users.
  - **Gold Plan**: Premium listing for 3999 Tsh.
  - **Platinum Plan**: Featured listing for 5999 Tsh.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Features](#features)
- [Billing Plans](#billing-plans)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these steps to set up NyumbaChap locally.

## Prerequisites

- Python 3.12.7
- Django==5.1.1
- PostgreSQL (or any other DB engine of your choice)

### Installation

1. **Clone the repository**

   ### bash
   git clone https://github.com/Barackwilliam12/nyumbachap.git
   cd Django_project
## Create a virtual environment

### bash

python3 -m venv venv
source venv3/bin/activate  
On Windows use `venv3\Scripts\activate`

## Install the required dependencies

### bash

pip install -r requirements.txt
Set up environment variables

## Rename the .env.example file to .env and fill in your database credentials and secret key.

## Apply migrations

### bash

python manage.py migrate

## Create a superuser

### bash

python manage.py createsuperuser

## Run the server

### bash

python manage.py runserver
Visit http://127.0.0.1:8000/ to access NyumbaChap.

# Project Structure

NyumbaChap/

├── Django_project/  
├── accounts/         
├── properties/          
├── chat/                
├── blog/                
├── templates/          
├── static/              
├── media/             
├── manage.py           
└── requirements.txt    



# Billing Plans
## Silver Plan: 
### Free listing with basic features.
## Gold Plan: 
### Enhanced listing with better visibility for 3999 Tsh.
## Platinum Plan: 
### Featured listing with top visibility and extra features for 5999 Tsh.

# Contributing

### We welcome contributions to NyumbaChap! If you want to contribute:

# Fork the repository

## Create a new feature branch:
git checkout -b feature/my-feature
## Commit your changes:
git commit -m 'Add some feature'
## Push to the branch: 
git push origin feature/my-feature

Open a pull request
# License
This project is licensed under the MIT License - see the LICENSE file for details.




