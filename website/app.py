from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sources import LazadaBot
from flask import send_file


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':
        
        keyword = request.form['keyword']

        n_data = int(request.form['n_data'])
        output_file = request.form['output_file']
        file_type = request.form['file_type']
        
        
        now_dir = os.path.dirname(__file__)
        output_dir = os.path.join(now_dir, 'static', 'files')
               
            
    
        full_output_path = os.path.join(output_dir, output_file)
        
        bot = LazadaBot()
        bot.scrap(keyword=keyword, n_data=n_data, output_file=full_output_path, file_type=file_type)
        
        
        filename = f"{full_output_path}.{file_type}"

        if os.path.exists(filename):
             return send_file(filename, as_attachment=True)
        

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
