import gradio as gr
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def objects_image_file(image1, end_point, API_Key):
    
    if (end_point == '' or API_Key == ''):
        output = "*** Please provide EndPoint URL and API_KEY ***"
    else:
        try:
            endpoint = end_point
            key = API_Key
            # Create an Image Analysis client
            client = ImageAnalysisClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(key)
            )
            # [START read]
            # Load image to analyze into a 'bytes' object
            with open(image1, "rb") as f:
                image_data = f.read()

            # Extract objects list from an image
            result = client.analyze(
                image_data=image_data,
                visual_features=[VisualFeatures.OBJECTS]
            )
            if result.objects is not None:
                objectsList = ''
                for object in result.objects.list:
                    objectsList += f"   '{object.tags[0].name}', {object.bounding_box}, Confidence: {object.tags[0].confidence:.4f}" + "\n"  
                    output = objectsList
            
        except :
            output = "*** Please check EndPoint URL and API_KEY ***"

    return output

title = "Azure Cognitive Services"
description = """ 

<img src = "https://nightingalehq.ai/knowledgebase/glossary/what-are-azure-cognitive-services/cognitive-services.jpg" width = 300px>

# Computer Vision : Image Analysis, Detect physical objects in an image file and return their location, using a synchronous client.
  
"""
    
demo = gr.Interface( objects_image_file,
                    [gr.UploadButton("Click to Upload an Image File", file_types=["image"]), gr.Textbox(label="Enter your Endpoint URL", placeholder="URL", lines=1),gr.Textbox(type = "password", label="Enter your API-Key", placeholder="API-Key", lines=1)],
                    [gr.Textbox(label = "Output")],
                    title = title,
                    description = description

).launch()