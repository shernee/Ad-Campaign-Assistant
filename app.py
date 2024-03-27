import gradio as gr
from chatbot import get_llama_response
from pipeline import content_pipeline, ad_generation_pipeline
import constants as c

strategy_options = ['Festive Promotion', 'Event-specific advertisement', 'Educational-use highlight', 'Educational-use highlight','Tech versatility showcase','Seasonal refresh']
domain_options = ['Problem solution', 'Storytelling narrative']
context_options = ['Utilize information','Ensure accuracy','Refer to','Incorporate','Leverage']

marketing_prompt = gr.Interface(
    fn=content_pipeline,
    inputs=[
        gr.components.Textbox(lines=2, placeholder='Enter initial prompt here...'),
        gr.components.Dropdown(choices=c.strategy_options, label='Strategy'),
        gr.components.Dropdown(choices=c.domain_options, label='Domain'),
        gr.components.Dropdown(choices=c.context_options,label='context'),
    ],
    outputs=gr.components.Textbox(lines=10, placeholder='Generated text will appear here...'),
    title='Generate Marketing Content',
    description='Select options to generate marketing content.'
)

ad_display_creatives = gr.Interface(
    fn=ad_generation_pipeline,
    inputs=[gr.components.Textbox(lines=2, placeholder='Enter the prompt generated from previous step..')],
    outputs =[gr.components.Textbox(lines=10),gr.Gallery(label='generated Images', elem_id='gallery', columns=[2], rows=[4], object_fit='contain', height='auto')],
    title='Display ad and image banners',
    flagging_options=['I like it! 👍', 'Nah..! 👎']
    )

bot = gr.ChatInterface(fn=get_llama_response)

demo = gr.TabbedInterface(
    interface_list=[marketing_prompt, ad_display_creatives, bot],
    tab_names=['Generate marketing content','Display ad and image banners','LLama Powered Chatbot']
)
demo.launch()

