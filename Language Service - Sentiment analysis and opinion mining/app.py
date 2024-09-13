import gradio as gr
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def AnalyzeSentiment(endpoint, key, statements):
    
    
    if (endpoint == '' or key == ''):
        output = "*** Please provide EndPoint URL and API_KEY ***"
    
    else:
        try:
            endpoint = endpoint
            key = key

            text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

            documents = tuple(statements.split("\n"))

            result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
            docs = [doc for doc in result if not doc.is_error]

            reviews = ()
            for idx, doc in enumerate(docs):
                reviews = reviews + (f"Document text: {documents[idx]}",)
                reviews = reviews + (f"Overall sentiment: {doc.sentiment} {doc.confidence_scores}",)
            
            output = "\n\n".join(reviews)
    
        except:
            output = "*** Please check EndPoint URL and API_KEY ***"
    return output

title = "Azure Cognitive Services"
description = """ 

<img src = "https://nightingalehq.ai/knowledgebase/glossary/what-are-azure-cognitive-services/cognitive-services.jpg" width = 300px>

#  Language Service : Use Natural Language Understanding (NLU) for Sentiment analysis and opinion mining.
 
  
"""

demo = gr.Interface( fn = AnalyzeSentiment, inputs= [ gr.Textbox(label="Enter your Endpoint URL", placeholder="URL", lines=1), gr.Textbox(type = "password", label="Enter your API-Key", placeholder="API-Key", lines=1), gr.Textbox()], outputs= gr.Textbox(), title = title, description = description).launch()