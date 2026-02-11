
import os
from flask import Flask, request, render_template_string
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Initialize conversation history
conversation_history = {}

html_template = '''
<html>
  <body>
    <h1>Flask AI Chatbot</h1>
    <form action='' method='post'>
      <input type='text' name='user_input' placeholder='Type your message here'>
      <input type='submit' value='Send'>
    </form>
    <div id='conversation'>
      {% for message in conversation %}
        <p>{{ message }}</p>
      {% endfor %}
    </div>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    user_input = request.form['user_input']
    conversation_history['user'] = user_input
    
    # Call OpenAI GPT-4 API
    response = openai.Completion.create(
      model='gpt-4',
      prompt=user_input,
      max_tokens=1024,
      temperature=0.7
    )
    
    conversation_history['ai'] = response.choices[0].text
    
    # Render conversation history
    conversation = [f'User: {user_input}', f'AI: {response.choices[0].text}']
    return render_template_string(html_template, conversation=conversation)
  else:
    return render_template_string(html_template, conversation=[])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
