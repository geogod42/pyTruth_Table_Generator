
# Truth Table Generator

This project is a simple web application for generating truth tables from logical expressions. It uses Flask for the backend and a minimal HTML front-end for user interaction.

## Features

- Supports logical operations: `¬` (NOT), `∧` (AND), `∨` (OR), `⊕` (XOR), and `→` (IMPLIES).
- Generates truth tables for any valid logical expression.
- Dynamically extracts variables and evaluates all possible truth value combinations.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/truth-table-generator.git
   cd truth-table-generator
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the web application at `http://127.0.0.1:5000`.

## File Structure

- `app.py`: Main Flask application for handling routes and logical operations.
- `templates/index.html`: Front-end HTML for user interaction.
- `static/`: Directory for static files like icons and styles.
- `requirements.txt`: List of required Python packages.

## Example Usage

Enter a logical expression like:

```
(¬p → q) ∨ (q ⊕ ¬p)
```

Click "Generate Truth Table" to see the truth table for the entered expression.

## Contributing

Feel free to fork this repository and submit pull requests. Ensure that any new features are well-documented and tested.

## License

This project is licensed under the MIT License.
