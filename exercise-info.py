import json
from flask import Flask, request, Response

app = Flask(__name__)

print('server listening on port 5003...')

@app.route('/exercise-info', methods=['GET'])
def get_suggested_exercise():
    """
    Provides information for a particular exercise
    """
    exercise_info_request = request.args.get('name')
    if not exercise_info_request:
        return Response(json.dumps('invalid query parameter'), mimetype='application/json', status=400)
    
    try:
        with open('exercise-info.json', 'r') as infile:
            exercise = json.load(infile)
    except FileNotFoundError:
        return Response(json.dumps('File not found.', mimetype='application/json', status=500))
    
    exercise_data = exercise.get(exercise_info_request)    
    if exercise_data:
        print('found some exercises')
        response_data = exercise_data
    
    print("sending over!")
    return Response(json.dumps(response_data), mimetype='application/json', status=200)

if __name__ == '__main__':
    # check to make sure the file path exsists before execution
    # note this is running on port 5002
    app.run(host='127.0.0.1', port=5003, debug=True)