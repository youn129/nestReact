# --- Builder Stage ---
    FROM node:20-slim AS builder

    # 작업 디렉토리 설정
    WORKDIR /usr/src/app
    
    # 의존성 파일 복사 및 설치
    COPY package*.json ./
    RUN npm install
    
    # 소스 코드 복사
    COPY . .
    
    # NestJS 빌드
    RUN npm run build
    
    # --- Production Stage ---
    FROM node:20-slim AS production
    
    # 작업 디렉토리 설정
    WORKDIR /usr/src/app
    
    # 의존성 설치 (생산 환경)
    COPY package*.json ./
    RUN npm install --only=production  # 프로덕션 의존성만 설치
    
    # 빌드된 파일 복사
    COPY --from=builder /usr/src/app/dist ./dist
    
    # 앱 실행 포트
    EXPOSE 4000
    
    USER node
    # 앱 실행
    CMD ["npm", "run", "start:prod"]
    