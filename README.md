# Namecheap and Heroku FastAPI Integration

This project provides seamless integration between Namecheap and Heroku using FastAPI. It allows users to suggest, check availability, and purchase domains through Namecheap, as well as dynamically create Heroku subdomains and acquire CNAME records.

## Table of Contents

1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Usage](#usage)
4. [Expected Outcome](#expected-outcome)
5. [Integration Steps](#integration-steps)
    - [Local Setup](#local-setup)
    - [Heroku Deployment](#heroku-deployment)
6. [Testing](#testing)
7. [Configuration](#configuration)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project facilitates the seamless integration of domain purchase and CNAME assignment for storefront e-commerce using Namecheap and Heroku APIs through FastAPI.

## Objective

The main objective is to provide users with the ability to purchase domains with their online stores through Namecheap. Additionally, it enables the dynamic creation of Heroku subdomains and CNAME acquisition.

## Usage

1. **Suggest Domains:**
Provides domain suggestions based on the user's business name.

2. **Check Domain Availability:**
Checks the availability of a specific domain name.

3. **Purchase Domain:**
Displays the pricing and allows the user to purchase a domain.

4. **Create Heroku Subdomain:**
Creates a custom subdomain on Heroku.

5. **Acquire CNAME Record:**
Acquires the CNAME record for a specific subdomain.

## Expected Outcome

- Seamless domain purchase through Namecheap.
- Seamless CNAME creation and assignment through Heroku.

## Integration Steps

### Local Setup

1. **Clone Repository:**

2. **Install Dependencies:**

3. **Configuration:**
- Update API keys, usernames, and other configuration details in the relevant files.

4. **Run FastAPI Application:**

5. **Access Local Endpoints:**
- Open a web browser or use a tool like [curl](https://curl.haxx.se/) to access the defined endpoints.

### Heroku Deployment

6. **Heroku Setup:**
- Create an account on [Heroku](https://www.heroku.com/).
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

7. **Login to Heroku:**

8. **Create Heroku App:**

9. **Deploy to Heroku:**

10. **Access Heroku Endpoints:**
 - Open a web browser or use a tool like [curl](https://curl.haxx.se/) to access the defined endpoints on your Heroku app.

## Testing

Follow the provided instructions for testing the project. Include sample requests and expected responses. You simply need to get both Heroku and Namecheap API Keys.

## Configuration

Update API keys, usernames, and other configuration parameters in the relevant files.

## Contributing

Feel free to contribute by reporting issues or submitting pull requests.


