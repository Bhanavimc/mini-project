from flask import render_template, request, redirect, url_for, flash
from . import main
from .models import Opportunity  # Assuming you have a model for opportunities

# Simulate some opportunities for the dashboard page
@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Handle profile creation here (store in database, etc.)
        name = request.form['name']
        email = request.form['email']
        skills = request.form['skills']
        interests = request.form['interests']
        
        # Save the profile data in the database (assuming you have a model for profiles)
        # For now, we can just print or flash a message
        flash(f'Profile created for {name}', 'success')
        
        return redirect(url_for('main.dashboard'))

    # Fetch opportunities from the database (assuming you have a model)
    opportunities = Opportunity.query.all()  # Assuming you have a model named 'Opportunity'
    
    return render_template('dashboard.html', opportunities=opportunities)

# Handle Login Route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data and check credentials
        email = request.form['email']
        password = request.form['password']
        
        # For now, just check if the email is correct (you can replace with real validation)
        if email == 'test@example.com' and password == 'password':  # Replace with real validation
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    
    return render_template('login.html')
