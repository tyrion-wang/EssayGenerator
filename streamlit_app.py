import openai
import streamlit as st
import os
import io

# 在这里输入您的OpenAI API访问密钥
openai.api_key = st.secrets["OPEN_AI_Key"]



def main():
	# 设置Streamlit页面标题和页面布局
	st.set_page_config(page_title="Essay Generator", page_layout="wide")

	# 添加Streamlit页面标题和说明
	st.title("Essay Generator")
	st.write("Enter your essay prompt and generate an essay with GPT-3.5 Turbo.")

    # 创建Streamlit表单，允许用户输入他们的作文题目、语言和所需字数
    with st.form(key='essay_generator'):
        prompt = st.text_input(label='Essay prompt', help="Enter your essay prompt.")
        length = st.slider(label='Essay length', min_value=50, max_value=500, value=100, step=50, help="Select the desired length of your essay.")
        language = st.selectbox(label='Language', options=['English', 'Chinese', 'Japanese', 'Korean'], help="Select the language in which you want your essay to be generated.")
        submit_button = st.form_submit_button(label='Generate essay')

        # 处理用户提交表单的情况
        if submit_button:
            # 设置OpenAI API生成作文的参数
            if language == 'English':
                model_engine = 'text-davinci-002'
            elif language == 'Chinese':
                model_engine = 'text-davinci-002'
            elif language == 'Japanese':
                model_engine = 'text-davinci-002'
            elif language == 'Korean':
                model_engine = 'text-davinci-002'
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=length,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # 处理OpenAI API生成错误的情况
            try:
                essay = response.choices[0].text.strip()
            except:
                st.error("Sorry, we were unable to generate an essay. Please try again with a different prompt.")

            # 在Streamlit应用程序中显示生成的作文
            st.subheader('Generated essay')
            st.write(essay)

            # 允许用户将生成的作文保存到他们的设备中
            save_button = st.button('Save essay to file')
            if save_button:
                with io.open('essay.txt', mode='w', encoding='utf-8') as file:
                    file.write(essay)
                st.success('Essay saved to file.')

if __name__ == '__main__':
    main()
