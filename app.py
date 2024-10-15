# 실행
# python3 app.py

# export GRADIO_SERVER_NAME=0.0.0.0 >> 192... IP설정
# gradio app.py >> Auto-Reloading 
    ## https://www.gradio.app/guides/developing-faster-with-reload-mode

import gradio as gr

def predict(audio):
    # 오디오 처리 로직을 여기에 작성합니다.
    # audio는 파일 객체입니다.
    return "처리된 결과"

app = gr.Interface(fn=predict, inputs=["audio","text"], outputs="text")
app.launch()
