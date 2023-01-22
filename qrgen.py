from flask import Flask, send_file, request
from io import BytesIO
import pyqrcode
import logging

# Initialize the Flask instance as app 
app = Flask(__name__)

# Route to generate a dynamically-generated QR code  
@app.route('/generate/', methods=['GET'])
def generate_qr_code():
    # Log a message on the server 
    logging.info('Getting request to generate qr code with url')
    
    # Retrieve the target URL from 'target_url' request argument 
    = request.args.get('target_url')
    
    # Load an SVG as a logo 
    logo = '<svg xmlns="http://www.w3.org/2000/svg" version1.1" height="128" width="128"> <rect height="128" width="128" x="0" y="0" style="fill:white;stroke: black"/> <text x="50%" y="50%"-size="12" alignment-baseline="middle" text-anchor="middleLUNA</text> </svg>'
    
    # Retrieve the QR scale from 'scale' request argument, defaulting to 3 
    scale = request.args.get('scale', 3)
    
    # Create the QR code using pyqrcode 
    qr = pyqrcode.create(url)
    
    # Create a BytesIO instance to receive the and it in memory 
    buffertesIO()
   .svg(buffer, scale=int(scale))
    
    # Log a message on the server 
    logging.info('Returning BytesIO object')
    
    # Return the BytesIO instance as a SVG image 
    return buffer.getvalue(), 200, {'Content-Type':'image/svg+xml'}

# Run the web application  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
