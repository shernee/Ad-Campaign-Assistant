from transformers import AutoTokenizer, pipeline
import constants as c

tokenizer = AutoTokenizer.from_pretrained(c.llama_model, use_auth_token=True)
llama_pipeline = pipeline(
    'text-generation',  
    model=c.llama_model,
)

def format_message(message, history, memory_limit):
    SYSTEM_PROMPT = '''<s>[INST] <<SYS>>
    You are a helpful bot. Your answers are clear and concise.
    <</SYS>>
    '''

    if len(history) > memory_limit:
        history = history[-memory_limit:]

    if len(history) == 0:
        return SYSTEM_PROMPT + f'{message} [/INST]'

    formatted_message = SYSTEM_PROMPT + f'{history[0][0]} [/INST] {history[0][1]} </s>'

    for user_msg, model_answer in history[1:]:
        formatted_message += f'<s>[INST] {user_msg} [/INST] {model_answer} </s>'
    formatted_message += f'<s>[INST] {message} [/INST]'

    return formatted_message


def get_llama_response(message, history):
    query = format_message(message, history)
    response = ''
    try:
        sequences = llama_pipeline(
            query,
            do_sample=False,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            max_length=256,
        )

        generated_text = sequences[0]['generated_text']
        response = generated_text[len(query):] 
        return response.strip()
    except Exception as e:
        return ''