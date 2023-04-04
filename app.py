from flask import Flask, request
import numpy as np # linear algebra
import pandas as pd
import openai
import pandasql as psql


# This dictionary stores the mapping between order IDs and customer genders
df=pd.read_csv("C:/Users/Rana Azeem/Downloads/sales_data_sample.csv",encoding='latin1')
df.tail()
df.groupby('PRODUCTCODE')['SALES'].sum().sort_values()
df.columns
SALES=df.copy()

openai.api_key = "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"

def create_table_definition(sales):
  prompt="""### sqlite SQL table, with its properties:
  #
  # SALES({})
  #
  """.format(",".join(str(col) for col in df.columns))
  return prompt

def combine_prompts(sales,query_prompt):
  definition=create_table_definition(SALES)
  query_init_string=f"### A query to answer: {query_prompt}\n SELECT"
  return definition+query_init_string

myfirst = Flask(__name__)
@myfirst.route('/query', methods=['GET'])

def query():
    # get input from query parameters
    nlp_text = request.args.get('nlp_text')

    response=openai.Completion.create(
        model='text-davinci-002',
        prompt=combine_prompts(SALES,format(nlp_text)),
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['#',';']
    )
    response.choices[0].text
    a=str(response.choices[0].text).upper()

    sdf =  psql.sqldf('SELECT'+a)
    # perform calculation
    html_table = sdf.to_html()

    # Return HTML table as part of the Flask response
    return f'<html><body>{html_table}</body></html>'
    # return result as response

if __name__ == '__main__':
    myfirst.run(debug=True)