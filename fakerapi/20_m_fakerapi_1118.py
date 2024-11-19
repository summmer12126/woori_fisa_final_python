# ### 1. 연 중위값 소비 (1인가구)

# - 20대:  19,540,000  ( 중위값) 월: 1,628,333
# - 30대 : 27,800,000   ( 중위값) 월: 2,316,666
# - 40대  : 36,000,000  ( 중위값) 월: 3,000,000

# store list 20,30,40 대 모두 같음
# final_for_fakerapi_doc.xlsx 참고

import pandas as pd  # 데이터 처리를 위한 pandas 라이브러리
from faker import Faker  # 가짜 데이터 생성을 위한 Faker 라이브러리
import random  # 난수 생성을 위한 random 라이브러리
from datetime import datetime, timedelta  # 날짜/시간 처리를 위한 datetime 라이브러리
import numpy as np  # 수치 계산을 위한 numpy 라이브러리

# Faker 초기화 및 시드 설정
fake = Faker('ko_KR')  # 한국어 로케일로 Faker 객체 생성
Faker.seed(42)  # Faker의 시드값 설정으로 동일한 결과 보장
random.seed(42)  # random 모듈의 시드값 설정

# 기본 설정값 정의
yearrange = 5 # 생성할 데이터의 연도 범위
age=20

mf="m"
savepath = f"DATA/woori_fisa_final_python/csvfile/{age}_{mf}_fakerapi_{datetime.today().strftime('%Y-%m-%d')}.csv"  # 저장할 파일 경로

# 목표 비율 정의
target_ratios = {
    '편의점': 0.136,            # 13.6%
    '카페/디저트': 0.0393,      # 3.93%
    '외식': 0.095,             # 9.5%
    '주유': 0.0735,            # 7.35%
    '영화/문화': 0.0142,        # 1.42%
    '마트': 0.0773,            # 7.73%
    '쇼핑': 0.0695,            # 6.95%
    '병원/약국': 0.0912,        # 9.12%
    '교육/육아': 0.0264,        # 2.64%
    '통신': 0.0468,            # 4.68%
    '자동차/하이패스': 0.0624,   # 6.24%
    '여행/숙박': 0.022,         # 2.2%
    '교통(대중)': 0.0338,       # 3.38%
    '기타': 0.2126             # 21.26%
}



ls_target_values = list(target_ratios.values())
ls_target_values[0]

# 수정된 merchant 딕셔너리 (amounts 제거)
merchant = {
    '01': {
        'name': '편의점',
        'ratio': ls_target_values[0],
        'stores': ["GS25", "CU", "세븐일레븐", "이마트24", "미니스톱"]
    },
    # '02': {
    #     'name': '카페/디저트',              
    #     'ratio': ls_target_values[1],
    #     'stores': [''],
    #     'amounts': (15000, 150000)
    # },

    '03': {
        'name': '외식',
        'ratio': ls_target_values[2],
        'stores': ['배달의민족', '본죽', '이삭토스트', '김밥천국', '롤링파스타', '맥도날드', '투다리', 
                  '역전할머니맥주', 'VIPS', '채선당', '원할머니보쌈', '삼원가든', '명동칼국수']
    },

    '04': {
        'name': '주유',                
        'ratio': ls_target_values[3],
        'stores': ['SK엔크린', 'GS칼텍스', 'S-OIL', '현대오일뱅크', '타이어뱅크'],

    },

    '05': {
        'name': '영화/문화',           
        'ratio': ls_target_values[4],
        'stores': ['CGV', '메가박스', '롯데시네마', '넷플릭스', '멜론', '키즈카페','롯데월드','에버랜드','캐리비안베이','현대미술관','아쿠아리움', '예술의전당','뮤지컬/연극'],

    },
    '06': {
        'name': '마트',               
        'ratio': ls_target_values[5],
        'stores': ['마켓컬리','이마트', '홈플러스', 'GS마트', '롯데마트','트레이더스', '농협하나로마트'],

    },
    '07': {
        'name': '쇼핑',              
        'ratio': ls_target_values[6],
        'stores': ['유니클로', 'H&M', '자라', '무신사', 'ABC마트','에이블리', '지그재그','현대백화점','롯데백화점','신세계백화점'],

    },
    '08': {
        'name': '병원/약국',          
        'ratio': ls_target_values[7],
        'stores': ['세브란스병원', '성모병원', '고려대병원', '연세사랑병원', '약국','연세치과','정형외과', '내과', '이비인후과'],

    },
    '09': {
        'name': '교육/육아',          
        'ratio': ls_target_values[8],
        'stores': ['교보문고', '영풍문고', '알라딘', '메가스터디', '인프런', '클래스101','yes24','밀리의서재','리디북스','서점'],

    },
    # '10': {
    #     'name': '통신',              
    #     'ratio': ls_target_values[9],
    #     'stores': ['KT'],
    #     'amounts': (15000, 150000)
    # },

    '11': {
        'name': '자동차/하이패스',     
        'ratio': ls_target_values[10],
        'stores':['하이패스', '한국도로공사', '서울고속도로', '서울외곽순환도로', '인천국제공항고속도로', '경부고속도로', '영동고속도로', '서해안고속도로', '호남고속도로'],

    },
    '12': {
        'name': '여행/숙박',          
        'ratio': ls_target_values[11],
        'stores': ['아고다', '여기어때', '야놀자', '에어비앤비', '익스피디아','하나투어','모두투어','대한항공','아시아나항공','KTX','SRT'],

    },
    # '13': {
    #     'name': '교통(대중)',         
    #     'ratio': ls_target_values[12],
    #     'stores': ['버스','지하철','KTX','SRT','무궁화'],
    #     'amounts': (55000, 100000)
    # },

    '14': {
        'name': '기타',              
        'ratio': ls_target_values[13],
        'stores': ['다이소','올리브영','세탁소', '미용실', '철물점', '인테리어', '청소서비스','레저','레저스포츠','회원제클럽'],

    }



}

def calculate_target_amount(annual_target, ratio, num_transactions):
    """
    카테고리별 연간 목표 금액을 기반으로 거래당 평균 금액을 계산하는 함수
    """
    target_amount = (annual_target * ratio * yearrange) / num_transactions
    return target_amount



def generate_expense_data(num_records=20000):
    """
    가상의 거래 데이터를 생성하는 메인 함수
    
    Parameters:
    num_records (int): 생성할 전체 거래 기록 수
    """
    # 데이터 생성 기간 설정
    end_date = datetime(2024, 11, 11)  # 종료 날짜
    start_date = datetime(2019, 11, 11)  # 시작 날짜
    
    # 연간 목표 총액 설정
    annual_target = 19_540_000  # - 20대:  19,540,000  ( 중위값) 월: 1,628,333 *12
    
    # 정기 결제 항목 정의
    subscriptions = {
        'Cafe': {'amount': 64000, 'interval': 30, 'category': '02', 'category_name': '카페/디저트'},  # 4000원 * 4회 * 4주
        'Netflix': {'amount': 17000, 'interval': 180, 'category': '05', 'category_name': '영화/문화'},
        'Melon': {'amount': 7900, 'interval': 30, 'category': '05', 'category_name': '영화/문화'},
        'KT': {'amount': 55000, 'interval': 30, 'category': '10', 'category_name': '통신'},
        'Transportation': {'amount': 55000, 'interval': 30, 'category': '13', 'category_name': '교통(대중)'}  # 월 55000

    }
    
    data = []

    remaining_records = num_records
    for cat_id, cat_info in merchant.items():
        # 카테고리별 거래 건수 계산
        num_transactions = int(remaining_records * cat_info['ratio'])
        # 목표 거래 금액 계산
        target_amount = calculate_target_amount(annual_target, cat_info['ratio'], num_transactions)
        
        # 각 거래 데이터 생성
        for _ in range(num_transactions):
            # 랜덤 날짜 생성
            random_days = random.randint(0, (end_date - start_date).days)
            random_date = start_date + timedelta(days=random_days)
            
            # 요일별, 시간대별 가중치 설정
            if random_date.weekday() < 5:  # 평일
                weights = [0.5]*6 + [2]*3 + [3]*2 + [4]*3 + [3]*4 + [4]*3 + [2]*3
            else:  # 주말
                weights = [0.5]*6 + [2]*4 + [4]*4 + [4]*4 + [3]*3 + [2]*3
            
            # 가중치를 적용하여 시간대 선택
            hour = random.choices(range(24), weights=weights)[0]
            timestamp = random_date.replace(hour=hour, minute=random.randint(0, 59))
            
            # 수정된 거래 금액 설정
            amount = int(round(random.normalvariate(target_amount, target_amount * 0.2), -1))
            # 카테고리별 특성을 반영한 기본적인 최소/최대 제한
            if amount < target_amount * 0.5:  # 목표 금액의 50% 미만인 경우
                amount = int(target_amount * 0.5)
            elif amount > target_amount * 2:  # 목표 금액의 200% 초과인 경우
                amount = int(target_amount * 2)
            
            # 거래 데이터 추가
            data.append({
                'transaction_id': fake.uuid4(),
                'datetime': timestamp,
                'category_id': cat_id,
                'category_name': cat_info['name'],
                'merchant_name': random.choice(cat_info['stores']),
                'amount': amount,
                'payment_method': random.choices(
                    [ '우리카드 우리 K-패스 (COOKIE CHECK)',   #체크3
                    'KB국민 노리2 체크카드(KB Pay)',
                    '신한카드 Hey Young 체크',   #신용2
                    '우리카드 DA@카드의정석',
                    'IBK 일상의 기쁨카드(신용)'],
                        weights=[
                            0.15,    # 우리 체크 15% 
                            0.10,    # KB 체크 10%
                            0.10,    # 신한 체크 10%
                            0.50,    # 카드의정석 50% (주 사용)
                            0.15     # 일상의 기쁨 15%
                        ]
                        )[0],
                        'transaction_type': '일반결제'
            })
        remaining_records -= num_transactions


        # 정기결제 데이터 생성
    current_date = start_date
    while current_date <= end_date:
        for sub_name, sub_info in subscriptions.items():
            # 정기 결제 주기에 맞는 날짜인지 확인
            if (current_date - start_date).days % sub_info['interval'] == 0:
                # 랜덤한 시간대 설정 (새벽 1-5시 사이)
                hour = random.randint(1, 5)
                timestamp = current_date.replace(hour=hour, minute=random.randint(0, 59))
                
                # 정기 결제 데이터 추가
                data.append({
                    'transaction_id': fake.uuid4(),  # 고유 거래 ID 생성
                    'datetime': timestamp,
                    'category_id': sub_info['category'],
                    'category_name': sub_info['category_name'],
                    'merchant_name': sub_name,
                    'amount': sub_info['amount'],
                    'payment_method': '우리카드 DA@카드의정석',
                    'transaction_type': '정기결제'
                })
        current_date += timedelta(days=1)

    # DataFrame 생성 및 시간순 정렬
    df = pd.DataFrame(data)
    df = df.sort_values('datetime').reset_index(drop=True)
    
    return df

# 데이터 생성 및 CSV 파일로 저장
df = generate_expense_data()
df.to_csv(savepath)

# === 통계 분석 섹션 시작 === === === === === === === === === === === === === === === === === === === ===

# 5년치 전체 데이터 분석
print(f"\n=== {yearrange} 거래 데이터 분석 ===")
total_amount = df['amount'].sum()
annual_amount = total_amount / yearrange
daily_count = round(len(df)/yearrange/365,1)

# 기본 통계 출력
print(f"\n전체 거래 건수: {len(df):,}건")
print(f"하루 거래 건수: {daily_count:,.2f}건")
print(f"기간: {df['datetime'].min().strftime('%Y-%m-%d')} ~ {df['datetime'].max().strftime('%Y-%m-%d')}")
print(f"{yearrange}년 총액: {total_amount:,.0f}원")
print(f"연평균 금액: {annual_amount:,.0f}원")

# 카테고리별 통계 분석
category_stats = df.groupby('category_name').agg({
    'amount': ['count', 'sum']
}).round(0)

# 카테고리별 분석 결과 출력
print(f"\n==={yearrange}카테고리별 분석:===")
print(f"{'카테고리':^12} {'거래건수':>8} {'총액':>15} {'비율':>8}")
print("-" * 50)

for cat_name, stats in category_stats.iterrows():
    count = int(stats['amount']['count'])
    sum_amount = stats['amount']['sum'] 
    actual_ratio = (sum_amount / total_amount)
    target_ratio = target_ratios[cat_name]
    
    print(f"{cat_name:^12} {count:8,} {sum_amount:15,.0f} {actual_ratio:7.2%} (목표: {target_ratio:6.2%})")

# 정기결제 분석
print(f"\n{yearrange}정기결제 분석:")
sub_stats = df[df['transaction_type'] == '정기결제'].groupby(['merchant_name']).agg({
    'amount': ['count', 'sum', 'mean']
}).round(0)

# 정기결제 분석 결과 출력
for merchant, stats in sub_stats.iterrows():
    count = int(stats['amount']['count'])
    sum_amount = stats['amount']['sum'] 
    mean_amount = stats['amount']['mean']
    print(f"{merchant:15} - {count:3d}회 총 {sum_amount:,.2f}원 (회당 {mean_amount:,.2f}원)")

# === 월별 분석 섹션 시작 ===

# 통계 분석 월별 분석
print(f"\n===월별 거래 데이터 분석 ===")
total_amount = df['amount'].sum() /60 # 월별(5년*12개월)
annual_amount = total_amount / yearrange 
daily_count = round(len(df)/yearrange/365,1)

print(f"\n월별 전체 거래 건수: {len(df)/60:,}건")
print(f"하루 거래 건수: {daily_count:,}건")
print(f"기간: {df['datetime'].min().strftime('%Y-%m-%d')} ~ {df['datetime'].max().strftime('%Y-%m-%d')}")
print(f"월 총액: {total_amount:,.0f}원")

# 카테고리별 분석
category_stats = df.groupby('category_name').agg({
    'amount': ['count', 'sum']
}).round(0)

print(f"\n===월별 카테고리별 분석:===")
print(f"{'카테고리':^12} {'거래건수':>8} {'총액':>15} {'비율':>8}")
print("-" * 50)

for cat_name, stats in category_stats.iterrows():
    count = int(stats['amount']['count']) /60 # 월별(5년*12개월)
    sum_amount = stats['amount']['sum'] /60
    actual_ratio = (sum_amount / total_amount)
    target_ratio = target_ratios[cat_name]
    
    print(f"{cat_name:^12} {count:8,.2f} {sum_amount:15,.0f} {actual_ratio:7.2%} (목표: {target_ratio:6.2%})")

# 정기결제 분석
print(f"\n월별 정기결제 분석:")
sub_stats = df[df['transaction_type'] == '정기결제'].groupby(['merchant_name']).agg({
    'amount': ['count', 'sum', 'mean']
}).round(0)

for merchant, stats in sub_stats.iterrows():
    count = int(stats['amount']['count'])
    sum_amount = stats['amount']['sum'] /60 # 월별(5년*12개월)
    print(f"{merchant:15} - {count:3d}회 총 {sum_amount:,.2f}원 (넷플은 6개월에 1번)")