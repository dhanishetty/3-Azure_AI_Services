import gradio as gr
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def EntityRecognition(endpoint, key, statements):
       
    if (endpoint == '' or key == ''):
        output = "*** Please provide EndPoint URL and API_KEY ***"
    
    else:
        try:
            endpoint = endpoint
            key = key

            entity_recognition_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

            documents = tuple(statements.split("|"))

            result = entity_recognition_client.recognize_entities(documents)[0]
                    

            reviews = ()
            for entity in result.entities:
                reviews = reviews + (f"Text: {entity.text} \t | \t Category: {entity.category} \t | \t Confidence Score: {round(entity.confidence_score, 2)}",)
                            
            output = "\n".join(reviews)
        except:
            output = "*** Please check EndPoint URL and API_KEY ***"

    return output

title = "Azure Cognitive Services"
description = """ 
<img src = "https://nightingalehq.ai/knowledgebase/glossary/what-are-azure-cognitive-services/cognitive-services.jpg" width = 300px>

# Language Service : Named Entity Recognition (NER) to identify and categorize entities in unstructured text like people, places, organizations, and quantities. 
 
  
"""

demo = gr.Interface( fn = EntityRecognition, inputs= [ gr.Textbox(label="Enter your Endpoint URL", placeholder="URL", lines=1), gr.Textbox(type = "password", label="Enter your API-Key", placeholder="API-Key", lines=1), gr.Textbox()], outputs= gr.Textbox(), title = title, description = description).launch()
