import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
# 학습된 모델 가져오기
def get_train_model(path):
    with open(f"{path}", 'rb') as f:
        model = pickle.load(f)

    return model


#  예측 함수
def predict_win_rate(model, match_datas):
    match_data_pd = pd.DataFrame([match_datas],
                                 columns=['blue_gold', 'blue_dragons', 'blue_towers_destroyed', 'blue_kills',
                                          'blue_total_level', 'red_gold', 'red_dragons', 'red_towers_destroyed',
                                          'red_kills', 'red_total_level', 'game_duration'])

    # 블루팀과 퍼플팀의 승리 확률 예측
    win_prob = model.predict_proba(match_data_pd)[0][1]

    # 결과 출력
    print(f"블루팀 승리 확률: {win_prob * 100:.2f}%")
    print(f"레드팀 승리 확률: {100 - win_prob * 100:.2f}%")


#  사용자 입력 받기
def get_team_stats():
    teams = ["블루", "레드"]
    datas = []

    for team in teams:
        datas.append(int(input(f"{team}팀 의 총 골드량을 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 드래곤 처치 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 타워 파괴 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 킬 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 총 레벨을 입력하세요: ")))
        print()

    minute = int(input("게임 진행 시간을 입력하세요 (분): "))
    second = int(input("(초): "))

    duration = minute * 60 + second
    datas.append(duration)

    return datas
