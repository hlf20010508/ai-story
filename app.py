import time
from flask import Flask, render_template, request, jsonify
from GPT2_Chinese.generate_texts import main as gen_story

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/getOutput')
def get_output():
    begin_text = request.args.get('beginText')
    start_time = time.time()
    output = gen_story(begin_text, 1)
    end_time = time.time()
    return jsonify({
        'success': True,
        'output': output,
        'time': '%.3f'%(end_time - start_time)
    })

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8080',
        debug=True
    )