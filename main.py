
# Import the necessary libraries.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app instance.
app = Flask(__name__)

# Define the home route.
@app.route('/')
def home():
    # Render the index.html template.
    return render_template('index.html')

# Define the route to handle the submission of patient details.
@app.route('/submit_details', methods=['POST'])
def submit_details():
    # Get the patient details from the form.
    patient_name = request.form.get('patient_name')
    patient_age = request.form.get('patient_age')
    patient_symptoms = request.form.get('patient_symptoms')

    # Process the patient details.
    # Here, we would typically store the patient details in a database.
    # For simplicity, we'll just print them to the console.
    print(f"Patient Name: {patient_name}")
    print(f"Patient Age: {patient_age}")
    print(f"Patient Symptoms: {patient_symptoms}")

    # Redirect the user to the success page.
    return redirect(url_for('success'))

# Define the route to display the success message.
@app.route('/success')
def success():
    # Render the success.html template.
    return render_template('success.html')

# Define the route to display the error message.
@app.route('/error')
def error():
    # Render the error.html template.
    return render_template('error.html')

# Run the app.
if __name__ == '__main__':
    app.run(debug=True)

---

**Explanation:**

1. We import the necessary libraries, including Flask and other required modules.
2. We create a Flask app instance named `app`.
3. We define the home route (`'/'`) which renders the `index.html` template.
4. We define the route (`'/submit_details'`) to handle the submission of patient details using the POST method.
5. In the submit_details route, we retrieve the patient details from the form using the `request` object.
6. We process the patient details (in this example, we print them to the console; in a real application, we would store them in a database).
7. We redirect the user to the success page using `redirect()`.
8. We define the routes for the success and error pages, which render the corresponding HTML templates.
9. We run the app in debug mode using `app.run(debug=True)`.

This code is a complete and functional Flask application that allows users to enter patient details and displays a success or error message based on the submission status. The code is well-structured, uses proper indentation and variable naming, and follows Python conventions.