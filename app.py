import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

# 설정 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# static_folder를 빈 문자열로 설정하여 현재 폴더를 기준으로 잡습니다.
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# API 호출 경로
@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('prompt') 
    
    try:
        # 1단계: 프롬프트 엔지니어로서 '프롬프트 설계' (강력한 지침으로 수정)
        design_msg = """
        당신은 세계 최고의 '프롬프트 엔지니어'입니다. 
        사용자의 요청을 분석해, 다른 AI가 20년 경력 전문가 수준의 결과물을 내놓도록 완벽한 [고급 명령어]를 설계하세요.

        [명령어 필수 포함 요소]
        1. #역할: 해당 분야의 최고 전문가 페르소나 설정
        2. #작업: 사용자가 요청한 구체적인 작업 목표
        3. #지시사항: 선택된 [프레임워크]의 핵심 요소를 단계별로 녹여낸 구체적 가이드
        4. #제약사항: 전문적인 톤앤매너 및 정보의 정확성 유지
        5. #출력형식: 마크다운 등을 활용한 깔끔한 가독성

        [절대 규칙]
        - 절대 "프롬프트: ~" 또는 "다음은 설계된 프롬프트입니다" 같은 설명조를 넣지 마세요.
        - 결과창에는 오직 다른 AI에게 복사해서 바로 입력할 수 있는 [명령어 본문]만 출력하세요.
        """
        p_res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": design_msg}, {"role": "user", "content": user_input}]
        )
        optimized_prompt = p_res.choices[0].message.content

        # 2단계: 설계된 프롬프트를 실제로 실행해보기 (정답 생성)
        a_res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": optimized_prompt}]
        )
        final_answer = a_res.choices[0].message.content

        return jsonify({
            "optimized_prompt": optimized_prompt,
            "final_answer": final_answer
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)