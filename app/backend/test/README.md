테스트 디렉토리 구조 설명

NestJS 기반 백엔드의 단위 테스트 및 E2E 테스트 코드들을 목적에 따라 구분하여 구성했습니다.

## 구조

test/
├── unit/ # 단위 테스트(Unit Test)
│ └── ebay-token.service.spec.ts # 서비스 로직 단위 테스트
├── ebay-token.e2e-spec.ts # eBay API 연동 E2E 테스트
├── app.e2e-spec.ts # 애플리케이션 상태 확인용 E2E 테스트
└── jest-e2e.json # E2E 테스트 전용 Jest 설정 파일

## 테스트 목적 및 설명

### unit/

- 서비스(\*.service.ts)와 로직 단위 기능 검증

- 외부 의존성(Mock 처리) 후 내부 동작 검증

- 실행 명령어: npm run test

### \*.e2e-spec.ts

- 전체 앱을 실행한 뒤 API 요청 흐름을 테스트

- 예: /api/get-ebay-token 응답 확인, 실제 eBay API 통신 여부 검증

- 실행 명령어: npm run test:e2e

### jest-e2e.json

- E2E 전용 환경 구성 (루트 디렉토리, 테스트 매칭 패턴 등)

---
