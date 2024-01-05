from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['medicine_reminder']
medicines_collection = db['medicines']  # Collection to store medicines

@app.route('/')
def index():
    success_message = request.args.get('success')
    return render_template('index.html', success_message=success_message)

@app.route('/add_medicines', methods=['GET', 'POST'])
def add_medicines():
    if request.method == 'POST':
        # Validate inputs
        medicine_name = request.form['medicineName']
        repetitiveness = request.form['repetitiveness']
        repetition_count = request.form['repetitionCount']

        if not repetition_count.isdigit():
            return render_template('add_medicines.html', error="Repetition count must be a number")

        repetition_count = int(repetition_count)

        # Insert medicine data into MongoDB
        medicine_data = {
            'medicine_name': medicine_name,
            'repetitiveness': repetitiveness,
            'repetition_count': repetition_count
        }

        result = medicines_collection.insert_one(medicine_data)

        if result.inserted_id:
            return redirect(url_for('index', success="Medicine added successfully"))

    # Render the add_medicines.html page for GET requests
    return render_template('add_medicines.html')

@app.route('/medicines_report')
def medicines_report():
    medicines = list(medicines_collection.find())
    return render_template('medicines_report.html', medicines=medicines)


