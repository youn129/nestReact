# 도커 기반 경매 API 테스트 자동화 시스템

> **실시간 경매 데이터 수집 및 자동화 테스트 기반 통합 시스템**  
> eBay API 연동, Selenium 기반 UI 자동화 테스트, Docker/Nginx 통합 환경에서 전체 API 흐름을 검증한 프로젝트입니다.

---

## 프로젝트 소개

**이 프로젝트는 실시간 경매 데이터를 가져와 프론트/백엔드 통합 환경에서 동작을 검증하고,  
**Selenium 기반 자동화 테스트**를 통해 주요 외부 웹사이트(Naver, Instagram)의 UI 시나리오도 검증한  
**테스트 엔지니어 취업 준비용 포트폴리오 프로젝트**입니다.

이 프로젝트를 통해 다음을 실습했습니다:

- eBay OAuth2 기반 인증 처리 및 상품 검색 API 사용
- Postman으로 API 통신 흐름 및 오류 상황 테스트
- NestJS + MongoDB + React로 전체 서비스 구성
- Selenium으로 실제 사용자 행위 자동화 (SNS 로그인 및 이미지 저장)
- Docker 및 Nginx 환경 연동 실습

---

## 기술 스택

| 영역            | 기술 스택                                       |
|-----------------|--------------------------------------------------|
| **Frontend**    | React, TypeScript, Bootstrap                     |
| **Backend**     | NestJS, TypeScript, Axios, ConfigModule          |
| **Database**    | MongoDB Atlas                                    |
| **Test Tools**  | Postman, Selenium (Python), Pyperclip            |
| **Infra/CI/CD** | Docker, Docker Compose, Nginx (Reverse Proxy)    |
| **기타**        | REST API, OAuth2, Environment Variable (.env)    |

---

##  주요 기능

### 실시간 eBay API 연동
- eBay에서 OAuth2 방식으로 access token을 받아 상품 데이터를 가져올 수 있습니다.
- 사용자가 입력한 키워드를 기반으로 경매 품목을 실시간으로 조회합니다.

### API 테스트 및 오류 핸들링
- Postman을 활용하여 API 정상/비정상 흐름을 검증했습니다.
- 토큰 오류, 포트 충돌(socket hang up), 네트워크 실패 등 다양한 예외 상황을 테스트했습니다.

### 자동화 테스트 (Selenium)
- Instagram 자동 로그인 후 게시물 이미지 탐색 및 저장
- Naver 블로그 자동 로그인 후 블로그 제목/내용 입력 후 게시

> 위의 자동화 테스트를 통해 사용자 시나리오 기반의 UI 테스트 시나리오를 구현해봤습니다.

### Docker + Nginx 환경 연동
- 백엔드와 프론트엔드를 각각 Docker 컨테이너로 분리
- Nginx로 프록시 라우팅하여 `/api` 요청은 백엔드로 연결

---

## 테스트 사례 요약

| 테스트 케이스 | 설명 |

| eBay API Token Test | Postman으로 토큰 유효성 확인 및 API 응답 구조 검증 |
| Port Conflict Simulation | 4000번 포트 점유 상황에서 `socket hang up` 재현 및 해결 |
| Selenium Automation | 인스타그램 검색 → 게시물 진입 → 이미지 저장 자동화 |
| Selenium Blog Posting | Naver 자동 로그인 후 게시글 작성 테스트 |
| API Error Handling | 잘못된 인증, 잘못된 쿼리, 서버 미응답 상황 테스트 |

---

## 향후 개선 방향

- Jest 기반 단위 테스트 및 E2E 테스트 도입
- Swagger(OpenAPI) 문서화
- GitHub Actions 기반 CI/CD 자동화
- MSW를 통한 eBay API Mock Server 구성
