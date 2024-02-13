# App Design: Physician's Scribe

## HTML Files

- **index.html**: The main page that serves as the user interface. It includes a form to record patient details and a button to submit the information.
- **success.html**: Displays a success message upon successful submission of patient details.
- **error.html**: Displays an error message if there's any issue during the submission of patient details.

## Routes

- **"/"**: The home route renders the **index.html** file and displays the form.
- **/submit_details**: Handles the submission of patient details from the form in **index.html**. This route processes the submitted data, stores it in a database (assuming there's one), and then redirects the user to the **success.html** or **error.html** page depending on the outcome.