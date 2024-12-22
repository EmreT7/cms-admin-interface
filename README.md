# CMS Admin Interface

## Description

This project is a simple Content Management System (CMS) for managing words and phrases in a local SQLite database. It provides an admin interface that allows users to view, edit, and update content easily. The CMS is built using Flask and includes features such as pagination, search functionality, and in-place editing.

## Features

- View a paginated list of words and phrases
- Edit words and phrases in-place
- Search functionality to filter words and phrases
- SQLite database for local storage
- Initial data loading from a JSON file

## Requirements

- Python 3.7+
- Flask
- Flask-SQLAlchemy

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/EmreT7/cms-admin-interface.git
   cd cms-admin-interface
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Ensure you have the `initial_data.json` file in the project root directory.

## Running the CMS

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. You should now see the CMS admin interface with the list of words and phrases loaded from the initial data.

## Usage

- **Viewing Words and Phrases**: The main page displays a paginated list of words and phrases.
- **Editing**: Click the "Edit" button next to any entry to edit its content in-place.
- **Searching**: Use the search bar at the top of the page to filter words and phrases by keyword.
- **Pagination**: Navigate through pages using the pagination controls at the bottom of the page.

## Project Structure

```
cms_admin_interface/
├── app.py
├── database.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── styles.css
├── initial_data.json
└── README.md
```
