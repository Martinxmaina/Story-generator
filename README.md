# Story Generator Application Documentation


## Overview
The Story Generator application is a Streamlit-based web app that generates short stories based on user-provided topics using the Mistral AI model. This application leverages the capabilities of the Mistral AI to create engaging narratives, making it a useful tool for writers, educators, and anyone interested in creative storytelling.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7 or higher
- Streamlit
- Mistral AI library
- Langchain library

You can install the required libraries using pip
'''


## Usage
Once the application is running, you will see the following interface:

1. **Input Field**: Enter a topic in the text input box. This topic will be used as the basis for the story generated by the Mistral AI.
2. **Story Generation**: After entering a topic, the application will automatically generate a story based on the input. The story will be displayed below the input field.

### Example
- **Input**: "A brave knight"
- **Output**: The application will generate a short story about a brave knight based on the provided topic 
<img width="1272" alt="Screenshot 2025-02-19 at 15 44 34" src="https://github.com/user-attachments/assets/28f4598e-bea2-47e5-925a-9ec9b2999ab4" />


## Why Mistral AI?
Mistral AI was chosen for this application due to its advanced natural language processing capabilities, which allow it to generate coherent and contextually relevant stories. Here are some reasons for its selection:

1. **High-Quality Output**: Mistral AI is designed to produce high-quality text that is engaging and creative, making it ideal for storytelling applications.
2. **Flexibility**: The model can adapt to various topics and styles, allowing users to generate stories across different genres.
3. **Ease of Integration**: Mistral AI can be easily integrated into Python applications, making it a suitable choice for this Streamlit app.

## 📦 Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/story-generator.git
cd story-generator
pip install -r requirements.txt
