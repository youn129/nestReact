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

### Docker + Nginx 환경 연동

- 백엔드, 프론트엔드, DB를 각각 Docker 컨테이너로 분리했습니다.
- Nginx로 `/api` 요청은 백엔드로 프록시 설정했습니다.

---

## 테스트 코드 설명

| tests                  | description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| `test_search.py`       | React 기반 상품 검색 페이지에 대한 Selenium 자동화 테스트                  |
| Page Object Model      | 테스트 코드와 DOM 로케이터 분리 → `home_page.py` 모듈로 구성               |
| Pytest 기반 구조화     | `pytest`로 간결한 구조 및 fixture 기반 실행 관리                           |
| 예외 시 Assertion 처리 | `assert` 문 및 메시지 기반으로 실패 원인 명확화                            |
| Postman 테스트         | OAuth2 token 발급, API 흐름 검증                                           |
| Jest 단위 테스트       | ebay-token.service.ts의 accessToken 로직에 대한 mock 기반 단위 테스트 작성 |
| Jest E2E 테스트        | eBay API 실제 호출 기반 전체 흐름 테스트                                   |

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
# → 실행되고 있는 백엔드/프론트엔드의 브라우저에 진입하고 자동화 테스트 실행됩니다.

# 3. 단위 테스트 / E2E 테스트 실행

$ cd app/backend
$ npm run test          # → Jest 단위 테스트 실행
$ npm run test:e2e      # → E2E 테스트 실행
```
