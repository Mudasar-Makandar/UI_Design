from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route("/OSPPre")
def index():
    api_variable = 'ManufacturerProductFamilyProductLine'
    url = 'http://Osppre-Test.eba-vi3z5hvq.us-east-2.elasticbeanstalk.com'
    caseid = '567896789'
    productType = 'Molecular Diagnostics'
    manufacturer = 'Johnson Medical'
    productNumber = 'Quantum 3300'
    return render_template('index.html', variable=api_variable,
                            api_url = url,
                            case_id=caseid,
                            product_type=productType,
                            Manufacturer=manufacturer,
                            product_number=productNumber)
