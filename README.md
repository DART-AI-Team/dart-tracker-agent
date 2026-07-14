# dart-tracker-agent

## 개발 환경 시작하기 (팀원용)

사전 준비: [Docker Desktop](https://www.docker.com/products/docker-desktop/) 설치 후 실행.

```bash
git clone <repo-url> && cd dart-tracker-agent   # 최초 1회
cp .env.example .env                             # 최초 1회 — API 키 채우기
docker compose up -d --build                     # 빌드 + 실행
```

확인: http://localhost:8000/health → `{"status":"ok"}`

## 자주 쓰는 명령

| 명령 | 용도 |
| --- | --- |
| `docker compose up -d` | 개발 시작 |
| `docker compose up -d --build` | 의존성·Dockerfile 변경 후 시작 |
| `docker compose down` | 종료 (DB 데이터는 유지) |
| `docker compose ps` | 컨테이너 상태 확인 |
| `docker compose logs -f app` | 앱 로그 실시간 보기 |
| `docker compose exec db psql -U dart -d dart_tracker` | DB 콘솔 접속 |

- 코드 수정은 재시작 없이 즉시 반영된다 (`--reload` + 볼륨 마운트).
- 패키지 추가는 `uv add <pkg>` 후 `docker compose up -d --build`.

## 구성

| 서비스 | 이미지 | 포트 |
| --- | --- | --- |
| app (FastAPI) | `python:3.13-slim` + uv | 8000 |
| db (PostgreSQL + pgvector) | `pgvector/pgvector:pg17` | 5432 |

- 의존성은 `pyproject.toml` / `uv.lock`으로 관리 (uv).
- DB 첫 기동 시 `db/init/01-extensions.sql`이 `vector` 확장을 자동 생성.
- DB 기본 접속 정보: `dart` / `dart` / `dart_tracker` (`.env`로 변경 가능).
