# 도커 기반 경매 API 테스트 자동화 시스템

> **실시간 경매 데이터 수집 및 자동화 테스트 기반 통합 시스템**  
> eBay API 연동, Pytest + Selenium 기반 테스트 자동화, Docker/Nginx 통합 환경에서 전체 API 흐름을 검증한 프로젝트입니다.

---

## 프로젝트 소개

이 프로젝트는 실시간 경매 데이터를 가져와 프론트/백엔드 통합 환경에서 동작을 검증하고,  
**Pytest + Selenium 기반 자동화 테스트**로 사용자 시나리오 및 API 흐름을 검증한  
**신입 QA 엔지니어 취업을 위한 포트폴리오 프로젝트**입니다.

### 주요 학습 내용:

- eBay OAuth2 기반 인증 처리 및 상품 검색 API 연동
- Postman으로 API 통신 흐름 및 오류 상황 테스트
- NestJS + MongoDB + React로 전체 서비스 구성
- Pytest 기반 구조화된 테스트 코드 작성
- Jest + Supertest 기반 E2E 및 단위 테스트 작성 (NestJS)
- Docker 및 Nginx 환경 연동 실습
- 실제 채용 플랫폼(Saramin) 기반 로그인/이력서 자동화 시나리오 구현

---

## Tech

| sec             | tech                                                |
| --------------- | --------------------------------------------------- |
| **Frontend**    | React, TypeScript, Bootstrap                        |
| **Backend**     | NestJS, TypeScript, Axios                           |
| **Database**    | MongoDB Atlas                                       |
| **Test Tools**  | Jest, Supertest, Pytest, Selenium (Python), Postman |
| **Infra/CI/CD** | Docker, Docker Compose, Nginx                       |
| **etc.**        | REST API, OAuth2, 환경변수 분리                     |

---

## 주요 기능

### 실시간 eBay API 연동

- eBay에서 OAuth2 방식으로 access token을 받아 상품 데이터를 가져옵니다.
- 사용자가 입력한 키워드를 기반으로 경매 품목을 실시간으로 조회합니다.

### API 테스트 및 UI 테스트 자동화

- Postman을 활용하여 API 정상/예외 흐름 테스트를 검증했습니다.
- Selenium + Pytest로 **token 발급으로 가져온 eBay API UI를 토대로 사용자 검색 테스트 자동화 구현**을 했습니다.
- `Page Object Model`을 도입했습니다.
- **Pytest의 파라미터화 기능**을 활용해 입력값에 따른 테스트 케이스 분기 적용했습니다.
- **실제 채용 플랫폼(Saramin)**에 로그인하고 특정 이력서를 클릭하는 시나리오를 자동화 구현했습니다.

### Docker + Nginx 환경 연동

- 백엔드, 프론트엔드, DB를 각각 Docker 컨테이너로 분리했습니다.
- Nginx로 `/api` 요청은 백엔드로 프록시 설정했습니다.

---

## 테스트 코드 설명

| tests                     | description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| `test_search.py`          | React 기반 상품 검색 페이지에 대한 Selenium 자동화 테스트                   |
| Page Object Model         | 테스트 코드와 DOM 로케이터 분리 → `home_page.py` 모듈로 구성                |
| Pytest 기반 구조화        | 다양한 검색어(`a`, `laptop`, 빈 문자열 등)에 대한 테스트 자동화 적용        |
| 예외 시 Assertion 처리    | `assert` 문 및 메시지 기반으로 실패 원인 명확화                             |
| `test_login.py`           | 사람인(Saramin) 사이트에서 카카오 로그인 후 이력서 목록 접근 및 클릭 테스트 |
| `saramIn/` Page 모듈 분리 | `LoginPage`, `MainPage`, `ResumePage` 클래스로 분리해 유지보수 용이성 확보  |
| Jest 단위 테스트          | ebay-token.service.ts의 accessToken 로직에 대한 mock 기반 단위 테스트 작성  |
| Jest E2E 테스트           | eBay API 실제 호출 기반 전체 흐름 테스트                                    |

---

## 실행방법

```bash
# 1. 백엔드 및 프론트엔드 서버 실행

$ cd app
$ npm run start
# → NestJS 백엔드와 React 프론트엔드가 실행됩니다.

# 2. (별도 터미널에서) 가상환경 활성화 후 테스트 실행

# 루트에서 가상환경 활성화
$ .\.venv\Scripts\activate.bat

# app 디렉토리 진입
$ cd app

# pytest 테스트 실행
$ pytest tests/python/test_search.py
$ pytest tests/python/test_login.py
# → 백엔드/프론트엔드 실행 상태에서 자동화 브라우저 테스트 진행됩니다.

# 3. 단위 테스트 / E2E 테스트 실행

$ cd app/backend
$ npm run test          # → Jest 단위 테스트 실행
$ npm run test:e2e      # → E2E 테스트 실행
```
