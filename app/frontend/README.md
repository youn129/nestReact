# Auction App Fullstack 프로젝트

이 프로젝트는 **NestJS(백엔드)** + **React(프론트엔드)** + **MongoDB** + **Docker/Nginx**를 활용한 **경매 플랫폼**입니다.  
eBay API 및 OpenAI, Instagram 자동화 기능까지 통합된 **풀스택 환경**을 구성합니다.

## 실행 방법

### 1. 개발 서버 실행(동시 실행)

```bash
npm install
npm run start
백엔드: http://localhost:4000
프론트엔드: http://localhost:3000

2. Docker로 전체 서비스 실행

cd app
docker-compose up --build
프론트엔드: http://localhost:3001
API 요청은 /api로 시작하는 경로로 백엔드에 프록시됩니다.

리버스 프록시 구조 (Nginx)
아래는 Nginx가 API 요청과 정적 파일 요청을 자동 라우팅하는 구조입니다:


[Browser]
    ↓
http://localhost:3001
    ↓
[Nginx - myconfig1.conf]
    ├── /api/*           → http://backend:4000 (NestJS)
    └── 기타 경로         → /usr/share/nginx/html (React 정적 파일)
Nginx 설정은 frontend/nginx/myconfig1.conf에 정의되어 있으며,
Dockerfile을 통해 production 컨테이너에 복사됩니다.

외부 서비스 연동
MongoDB Atlas / Local MongoDB

eBay API (Token 자동 갱신)

OpenAI GPT API

Instagram / Naver 자동화 (Python + Selenium)

모든 API 키와 비밀번호는 .env 파일에 포함되어 있습니다다.

주요 스크립트 (루트)

"scripts": {
  "start:backend": "npm run start --prefix app/backend",
  "start:frontend": "npm start --prefix app/frontend",
  "start": "concurrently \"npm run start:backend\" \"npm run start:frontend\""
}

```
