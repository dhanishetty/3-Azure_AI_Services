import gradio as gr
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def ocr_image_file(image1, end_point, API_Key):
    
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

            # Extract text (OCR) from an image stream. This will be a synchronously (blocking) call.
            result = client.analyze(
                image_data=image_data,
                visual_features=[VisualFeatures.READ]
            )
            if result.read is not None:
                sentence = ''
                for line in result.read.blocks[0].lines:
                    sentence += f"    {line.text}" + "\n"  
                    print(f"   Line: '{line.text}'")
                    output = sentence
            
        except :
            output = "*** Please check EndPoint URL and API_KEY ***"

    return output

title = "Azure Cognitive Services"
description = """ 
 <img src = "https://nightingalehq.ai/knowledgebase/glossary/what-are-azure-cognitive-services/cognitive-services.jpg" width = 300px>

# Computer Vision : OCR or Optical Character Recognition for text recognition or text extraction.
 
"""
    
demo = gr.Interface( ocr_image_file,
                    [gr.UploadButton("Click to Upload an Image File", file_types=["image"]), gr.Textbox(label="Enter your Endpoint URL", placeholder="URL", lines=1),gr.Textbox(type = "password", label="Enter your API-Key", placeholder="API-Key", lines=1)],
                    [gr.Textbox(label = "Output")],
                    title=title,
                    description=description,

).launch()