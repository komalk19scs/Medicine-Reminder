

---

# Medicine Reminder App
This project is a simple Medicine Reminder system built using Python (Flask), MongoDB, HTML, CSS, and JavaScript. This Flask web application serves as a Medicine Reminder, allowing users to input their name and medical history. Users can create a form to add one or more medicines, specifying schedules based on repetitiveness and repetition count.

## Table of Contents

- [Features](#features)
- [Technologies Used](#Technologies-Used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [How to Run Locally](#How-to-Run-Locally)
   - [Deployment (Example using Render) ](#Deployment(Example-using-Render))


## Features

- Capture user's name and medical history.
- Create a form for adding medicines with schedules.
- Specify medicine schedules based on:
  - Repetitiveness: Daily, Weekly, Monthly.
  - Repetition count: Indicates how many times a medicine needs to be taken per day, week, or month.
- View on-screen reports of all added medicines and their schedules.

## Technologies Used

- **Python (Flask):** Backend server and routing.
- **MongoDB:** NoSQL database for storing medicine data.
- **HTML, CSS, JavaScript:** Frontend and user interface.
- **Bootstrap:** Frontend framework for styling and layout.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB Atlas account

## How to Run Locally

1. Install required Python packages:

   ```bash
   pip install Flask pymongo
   ```

2. Set up MongoDB:

   - Create a MongoDB Atlas account.
   - Create a cluster and obtain the connection string.
   - Update the `MONGO_URI` in the `app.py` file with your MongoDB connection string.

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).

## Deployment (Example using Render)

1. Set up an account on [Render](https://render.com/).

2. Create a new web service on Render:

   - Repository: Link to your GitHub repository.
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -b 0.0.0.0:$PORT app:app`

3. Add environment variables on Render:

   - Key: `MONGO_URI`, Value: Your MongoDB Atlas connection string.

4. Deploy your app.

5. Open the provided URL to access your deployed Medicine Reminder.

1. Open your web browser and go to `http://localhost:5000/`.
2. Provide your name and medical history.
3. Create a form to add medicines with schedules based on repetitiveness and repetition count.
4. View on-screen reports of all added medicines and their schedules.


---

