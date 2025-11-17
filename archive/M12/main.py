'''
Tokenizer - converts raw text into tokens 


'''


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

'''



    Tokenization:

        Converts the input text into tokens (numerical representations).

        Adds special tokens ([CLS], [SEP]) required by transformer models.

    Padding and Truncation:

        Ensures all inputs have the same length by adding padding or truncating longer texts.

    Return Tensors:

        Converts tokens into PyTorch tensors (return_tensors="pt"), which are multi-dimensional arrays used in deep learning.

'''



text = ' I might like Python'
tokens = tokenizer(text, padding= True, truncation = True, return_tensors="pt")


'''



    Inference Mode:

        torch.no_grad() disables gradient computation during inference to save memory and speed up processing.

    Logits:

        Raw predictions from the model before applying any transformation (e.g., [2.3, -1.5]).

    Softmax Function:

        Converts logits into probabilities that sum to 1 (e.g., [0.95, 0.05]).

'''

with torch.no_grad():
    outputs = model(**tokens)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)




label_ids = torch.argmax(probabilities, dim=1)
labels = ['Negative', 'Positive']
label = labels[label_ids]
print(f"The sentiment is: {label}")



