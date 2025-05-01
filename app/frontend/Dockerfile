# --- Builder Stage ---
    FROM node:20-slim AS builder
    WORKDIR /usr/src/app
    COPY package*.json ./
    RUN npm ci
    COPY . .
    RUN npm run build  # React 빌드 -> build 디렉토리 생성
    
    # --- Production Stage ---
    FROM nginx:alpine AS production
    WORKDIR /usr/share/nginx/html
    COPY --from=builder /usr/src/app/build .
    COPY nginx/myconfig1.conf /etc/nginx/conf.d/default.conf
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    