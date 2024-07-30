from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pricing_data import get_initial_quote, get_counter_offer

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        session['customer_id'] = customer_id
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index')
def index():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/loan_purpose', methods=['GET', 'POST'])
def loan_purpose():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        customer_info = request.form
        customer_info = dict(customer_info)  # Convert to regular dictionary
        customer_info['customer_id'] = session['customer_id']
        session['customer_info'] = customer_info
        return render_template('loan_purpose.html')
    
    return redirect(url_for('index'))

@app.route('/loan_amount', methods=['POST'])
def loan_amount():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    
    session['loan_purpose'] = request.form.get('purpose')
    return render_template('loan_amount.html')

@app.route('/personalized_quote', methods=['GET', 'POST'])
def personalized_quote():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        loan_amount = float(request.form.get('loanAmount'))
        customer_info = session.get('customer_info', {})
        loan_purpose = session.get('loan_purpose')
        
        initial_quote = get_initial_quote(customer_info, loan_purpose, loan_amount)
        session['initial_quote'] = initial_quote
        
        return render_template('personalized_quote.html', quote=initial_quote)
    
    return redirect(url_for('loan_amount'))

@app.route('/get_counter_offer')
def get_counter_offer_route():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    
    customer_info = session.get('customer_info', {})
    loan_purpose = session.get('loan_purpose')
    loan_amount = float(session.get('initial_quote', {}).get('loan_amount', 0))
    initial_quote = session.get('initial_quote', {})
    
    counter_offer = get_counter_offer(customer_info, loan_purpose, loan_amount, initial_quote)
    return jsonify(counter_offer)

@app.route('/application_successful')
def application_successful():
    if 'customer_id' not in session:
        return redirect(url_for('login'))
    return render_template('application_successful.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)