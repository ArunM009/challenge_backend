from flask import Flask, request, jsonify

app = Flask(__name__)

def third_highest_frequency(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    third_highest = None
    count = 0
    for num, freq in sorted_frequency:
        count += 1
        if count == 3:
            third_highest = num
            break
    
    return third_highest

@app.route('/third_highest_frequency', methods=['POST'])
def find_third_highest_frequency():
    data = request.json
    numbers = data.get('numbers', [])
    if not numbers:
        return jsonify({'error': 'No numbers provided'}), 400
    
    result = third_highest_frequency(numbers)
    return jsonify({'third_highest_frequency': result})

if __name__ == '__main__':
    app.run(debug=True)