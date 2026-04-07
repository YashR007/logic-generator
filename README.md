# Logic Generator

## Project Overview
This project is a logic generator designed to create complex logical expressions and procedures based on user-defined parameters. It serves various applications in programming, artificial intelligence, and mathematical problem solving.

## Features
- Generate logical expressions from simple inputs.
- Support for multiple logical operations (AND, OR, NOT, etc.).
- Easy integration with existing applications and tools.
- Ability to customize and extend functionality.

## Tech Stack
- **Programming Language**: Python
- **Framework**: Flask (for API creation)
- **Database**: SQLite (for storing user-defined expressions)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YashR007/logic-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd logic-generator
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## Project Structure
- `app.py`: Main application file.
- `logic_generator/`: Directory containing the logic generation logic.
- `templates/`: Directory for HTML templates (if applicable).
- `static/`: Directory for static files (if applicable).

## Usage Guide
1. Start the application by running `python app.py`.
2. Access the web interface at `http://localhost:5000` (if web-based).
3. Enter the parameters for the logical expression and submit.
4. The generated logic will be displayed.

## Credits
Made with ♡ by Dee's group