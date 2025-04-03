# 🛍️ TinySecondhandPlatform

Django 기반으로 개발된 **중고 거래 웹 플랫폼**입니다.  
사용자는 회원가입 및 로그인을 통해 상품을 등록하고, 본인이 등록한 상품을 확인하거나 삭제할 수 있습니다.  
간단한 UI와 기능을 제공하여 학습 및 확장 목적에 적합한 구조로 설계되었습니다.

---

## 🚀 주요 기능

- ✅ 사용자 회원가입 / 로그인 / 로그아웃
- ✅ 로그인 사용자만 상품 등록 가능
- ✅ 상품 등록 시 이미지, 설명, 가격 입력
- ✅ 자신이 등록한 상품만 확인 가능 (`내 상품`)
- ✅ 상품 삭제 기능 (본인만 삭제 가능)
- ✅ Bootstrap 기반 반응형 UI
- ✅ 뒤로가기 / 네비게이션바 등 기본 UX 반영

---

## 🧱 기술 스택

| 구성 요소  | 기술                                 |
| ------ | ---------------------------------- |
| 백엔드    | Python 3.12 + Django 4.2.7         |
| 프론트엔드  | HTML, Bootstrap 5                  |
| 데이터베이스 | SQLite3                            |
| 기타     | Django Auth, CSRF 보호, Media 파일 업로드 |

---

## ⚙️ 설치 및 실행 방법 (macOS 기준)

\`\`\`bash
# 1. 프로젝트 다운로드 후 폴더로 이동
cd TinySecondhandPlatform\_Final\_WithDeleteAndMyProducts

# 2. 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 3. pip 최신화 및 패키지 설치
pip install --upgrade pip
pip install -r requirements.txt

# 4. 마이그레이션 수행
python manage.py makemigrations
python manage.py migrate

# 5. 개발 서버 실행
python manage.py runserver


테스트 계정 (선택), 예시
ID: testuser
PW: test1234
※ 직접 createsuperuser 명령어로 관리자 계정 생성 가능
접근주소
http://127.0.0.1:8000/admin/



TinySecondhandPlatform/
├── products/                # 상품 앱 (모델, 뷰, 폼)
├── templates/               # HTML 템플릿 (base, product\_list 등)
├── static/                  # Bootstrap, CSS 등 정적 파일
├── media/                   # 업로드된 이미지 저장 위치
├── TinyPlatform/            # 프로젝트 설정
├── manage.py
├── requirements.txt
└── README.md


보안 고려 사항
모든 상품 조작은 로그인된 사용자만 가능
상품 삭제는 작성자만 가능
모든 POST 요청은 CSRF 보호 적용
.gitignore에 venv/, db.sqlite3, media/ 등 중요 파일 제외

개발자
이름: 류재광 (Ryu JaeKwang)
학습 목적: Django 기초 프로젝트 + 보안 구조 이해 + 확장 기반 마련
