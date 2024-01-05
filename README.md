

---

# Medicine Reminder App

This Flask web application serves as a Medicine Reminder, allowing users to input their name and medical history. Users can create a form to add one or more medicines, specifying schedules based on repetitiveness and repetition count.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Capture user's name and medical history.
- Create a form for adding medicines with schedules.
- Specify medicine schedules based on:
  - Repetitiveness: Daily, Weekly, Monthly.
  - Repetition count: Indicates how many times a medicine needs to be taken per day, week, or month.
- View on-screen reports of all added medicines and their schedules.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB Atlas account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/komalk19scs/Medicine-Reminder.git
   ```

2. Install dependencies:

   ```bash
   cd Medicine-Reminder
   pip install -r requirements.txt
   ```

3. Set up MongoDB Atlas:
   - Create a MongoDB Atlas account.
   - Create a cluster and configure network access.
   - Get the connection string.

4. Set environment variables:

   ```bash
   export MONGO_URI='your-mongodb-atlas-connection-string'
   ```

   (Replace `'your-mongodb-atlas-connection-string'` with your actual connection string.)

5. Run the application:

   ```bash
   python app.py
   ```

   The app should be running at `http://localhost:5000/`.

## Usage

1. Open your web browser and go to `http://localhost:5000/`.
2. Provide your name and medical history.
3. Create a form to add medicines with schedules based on repetitiveness and repetition count.
4. View on-screen reports of all added medicines and their schedules.


---

