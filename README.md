# Unit Converter

This is a simple web application for converting units of measurement using Streamlit. The application allows users to convert between different units of length, weight, and time.

## Features

- Convert between different units of length (Kilometers to Miles, Miles to Kilometers)
- Convert between different units of weight (Kilograms to Pounds, Pounds to Kilograms)
- Convert between different units of time (Seconds to Minutes, Minutes to Seconds, Minutes to Hours, Hours to Minutes, Hours to Days, Days to Hours)
- User-friendly interface with attractive styling

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:

    ```sh
    uv venv
    ```

3. Activate the virtual environment:

    ```sh
    uv activate
    ```

4. Install the required packages:

    ```sh
    uv pip install streamlit
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run Unit_converter.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Code Overview

The main code for the application is in the `Unit_converter.py` file. It includes the following sections:

- Importing the necessary libraries
- Setting up the Streamlit interface
- Defining the unit conversion logic
- Displaying the conversion results

## Styling

The application uses custom CSS to style the input fields, buttons, and success messages. The styles are defined within a `<style>` tag in the Streamlit markdown.

## Author

Developed by Abdul Haseeb Shaikh

## License

This project is licensed under the MIT License.