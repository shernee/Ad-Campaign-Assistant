from product_info import create_ad_prompt, create_ad_prompt
from prompt_library import search_results
from ad_generation import generate_ad_and_banner

def content_pipeline(prompt, strategy, domain, context):
    search_results(prompt)

    product_query = prompt
    user_strategy = strategy
    user_structure = domain
    user_context = context

    _, final_prompt = create_ad_prompt(product_query, user_strategy, user_structure, user_context)

    return final_prompt

def ad_generation_pipeline(ad):
    ad, banners = generate_ad_and_banner(ad)
    return ad, banners

