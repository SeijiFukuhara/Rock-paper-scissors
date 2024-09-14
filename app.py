from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['グー', 'チョキ', 'パー']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = '引き分けです！'
    elif (user_choice == 'グー' and computer_choice == 'チョキ') or \
         (user_choice == 'チョキ' and computer_choice == 'パー') or \
         (user_choice == 'パー' and computer_choice == 'グー'):
        result = 'あなたの勝ちです！'
    else:
        result = 'コンピュータの勝ちです！'
    
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == "__main__":
    app.run(debug=True)
