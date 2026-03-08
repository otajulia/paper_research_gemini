# Autopilot Report (2026-03-08)

## 논문 확인 결과 (요약)
- 제목: Association between Comprehensive Physical Fitness Tiers and Annual Healthcare Expenditures ...
- 데이터: NFA100 + NHIS 링크, n=154,051, 2015-2022
- 핵심 결과: 체력 tier가 높을수록 연간 의료비가 낮은 inverse dose-response, 특히 고령층에서 효과 큼
- 현재 상태: 강한 연관성 논문이나, top-tier 수락에 필요한 인과 식별/강건성/정책시뮬레이션 완성도는 부족

## 1) 이 논문의 글로벌 탑티어 분야/저널 포지셔닝

### 분야 분류
- 1순위: Public Health Policy / Population Health
- 2순위: Health Services Research
- 3순위: Health Economics / HEOR
- 4순위: Aging & Functional Epidemiology

### "노벨티가 글로벌 넘버원"일 때 가능한 저널
- 최상위 도전군: The Lancet Public Health, JAMA Network Open, The BMJ
- 분야 최상위군(현실적 고확률): Journal of Health Economics, Health Services Research, Medical Care, Value in Health

### 왜 이 포지션인가
- 강점: 국가 단위 객관적 체력측정 + 청구자료 연계, 고령층 기능체력의 비용 연관성
- 약점: 현재는 association 중심. top-tier는 causal credibility + policy counterfactual + 강한 일반화 검증 요구

## 2020년까지 관련 저널/학회 탐색 반영

### 저널(핵심)
- JAMA Network Open: 일반의학/보건정책/글로벌헬스 포괄
- Journal of Health Economics: 건강/의료의 가치·생산·분배에 대한 경제분석 전문
- Value in Health: HEOR/보건정책 의사결정 중심 국제 저널
- (포지셔닝 참고) The Lancet Public Health: 공중보건/정책 영향력 최상위군

### 학회(2020 포함)
- AcademyHealth ARM 2020: HSR 프리미어 포럼 (virtual 개최)
- ISPOR 2020, ISPOR Europe 2020: HEOR 대표 국제학회
- iHEA Congress: 건강경제학 글로벌 포럼(격년)
- APHA Annual Meeting 2020: 대형 공중보건 연례 학회

## 2) 수락 가능성을 높이기 위한 개선 전략

### A. 원고 품질 즉시 보정 (Gate 0)
- placeholder/깨진 문자/미완성 참고문헌 전수 수정
- 코호트 정의 문장 일치화(후향 코호트 vs 횡단면 표현 충돌 제거)
- 비용지표 정의(0비용 처리, CPI 보정, 환율 변환) 재현 가능하게 명시

### B. 인과성 업그레이드 (Gate 1)
- 추정량 명시: Participation-only -> Tier3/2/1 이동의 12개월 비용 ATE
- 방법: GPS(ordinal tier)+AIPW/TMLE + two-part cost model
- 진단: 가중 후 SMD, positivity, trimming 민감도

### C. 강건성/반증 (Gate 2)
- 모델군 교차검증: gamma-log, tweedie, log-normal, quantile
- unmeasured confounding 민감도(E-value 등)
- negative control outcome/exposure
- linkage/inclusion selection IPW (660,604 -> 154,051)

### D. 정책번역/이론 노벨티 (Gate 3)
- FREG(Functional Reserve-Expenditure Gradient) 이론 제안
- mobility 저하 임계점 이하에서 비용곡선 볼록성(convexity) 검증
- 정책 시뮬레이션: tier 이동 시나리오별 연/5년 재정효과 제시

## 3) 물리적 실험 제외, 데이터/이론 기반 개선 전략
- 신규 신체개입 실험 없이, 기존 행정·체력 데이터 재분석으로 완성
- 분석 단위:
  - 인과추정
  - 분포 꼬리(고비용군) 분석
  - 이질성(CATE) 및 형평성(소득/지역)
  - 반사실적 정책 시뮬레이션
- 이론 단위:
  - FREG 가설(H1 비선형 임계효과, H2 고령층 mobility 매개효과)
  - DAG 기반 가정 명시와 반증 실험 연동

## 4) 수락 가능 수준의 목표와 실험 설계

### 수치/이론 목표 (acceptance-grade)
1. 인과 신뢰성
- 가중 후 핵심 공변량 SMD <= 0.10
- 주요 대비(Participation-only vs Tier1/2/3)의 효과 방향이 >=4개 모델군에서 일치
- 고령층 1차 대비는 모든 인과추정기에서 95% CI가 0 배제

2. 일반화/재현성
- 시계열 홀드아웃(예: 2015-2019 학습, 2020-2022 검증)
- 집단 총의료비 예측 상대오차 <=10%
- calibration slope 0.9-1.1

3. 정책 활용성
- 최소 1개 현실 시나리오에서 95% UI 기준 순절감 확인
- 평균 대비 >=1.5배 절감효과 하위집단 식별

### 실험 설계 (전부 계산/통계 실험)
- E1 코호트/결측/링키지 품질 감사 (STROBE 흐름도 포함)
- E2 GPS+AIPW/TMLE로 tier 이동 인과효과 추정
- E3 two-part + tweedie + quantile로 비용분포 강건성 검정
- E4 negative control + E-value + 중증질환 washout 민감도
- E5 spline/threshold로 FREG 비선형 가설 검정
- E6 mobility 변수 매개분해(특히 고령층)
- E7 소득/성별/연령/지역별 CATE 맵 작성
- E8 정책 마이크로시뮬레이션(연간/5년 KRW·USD 절감, 부트스트랩 UI)

## 투고 라우팅 제안
- Route A (최상위 도전): Lancet Public Health / JAMA Network Open
- Route B (현실적 최적): Journal of Health Economics 또는 Health Services Research
- Route C (정책 확산형): Value in Health / Medical Care

## 결론
현재 원고는 이미 대규모 연계자료 기반의 강한 잠재력이 있습니다. 다만 top-tier 수락에는 "연관성"에서 "인과+정책"으로 프레임 전환이 필수이며, 위 8개 계산 실험을 완료하면 물리적 실험 없이도 수락 가능성을 실질적으로 끌어올릴 수 있습니다.
