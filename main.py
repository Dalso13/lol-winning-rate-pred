# 5. 전체 실행
import os
# from dotenv import load_dotenv
from ML import ml_lol as ml
import sys


def main():
    # load_dotenv()
    # api_key = str(os.environ.get("APIKEY"))
    
    # pyinstaller 가 경로를 못찾아서 넣어줌
    try:
        os.chdir(sys._MEIPASS)
        print(sys._MEIPASS)
    except:
        os.chdir(os.getcwd())
    # 모델 학습 or 가져오기
    model_path = "./LOL_pred_model"

    if os.path.isfile(model_path):
        model = ml.get_train_model(model_path)
    else:
        print("학습된 모델이 없기에 학습합니다.")
        # 파일 경로

        file_path = './match_data.csv'

        # 데이터 불러오기 및 준비
        data = ml.load_and_prepare_data(file_path)

        ml.train_model(data)
        model = ml.get_train_model(model_path)
    try:
        # 블루팀과 퍼플팀의 통계 입력 (사용자 입력 받기)
        match_stats = ml.get_team_stats()
        # match_stats = [33000, 1, 5, 9, 59, 37600, 4, 6, 14, 59, 1312]
        # match_stats = [33000, 1, 5, 9, 59, 37600, 4, 6, 14, 59, 1989]

        # 승리 확률 예측
        ml.predict_win_rate(model, match_stats)

        # realtime_data(api_key)
    except KeyboardInterrupt:
        print("강제종료")
    finally:
        os.system("pause")


# 실시간으로 가져올 경우
# def realtime_data(api_key):
#     name = input("닉네임을 입력하시오 (태그 X) : ")
#     tag = input("태그를 입력하시오 (ex: KR1) : ")
#
#     puuid = get_rt_data.get_puuid(name=name,tagline=tag, api_key=api_key)
#
#     return get_rt_data.get_game_data(puuid=puuid, api_key=api_key)


if __name__ == "__main__":
    main()
