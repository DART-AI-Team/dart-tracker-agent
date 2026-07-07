---
name: git-convention
description: Use this skill whenever the user asks to create commits, write commit messages, create branches, open pull requests, or merge branches. Enforces this project's branch strategy (main/develop with feat/fix/chore/exp working branches), Conventional Commits format, PR target rules, merge methods, and commit message standards.
---

# Git Convention

## Branches

```
main ← demo / stable
 ↑
dev  ← integration
 ↑
feat/* · fix/* · chore/* · exp/*
```

| Branch | Role |
| --- | --- |
| `main` | Stable. Never push directly. |
| `dev` | Integration. |
| `feat/*` | New features. Delete after merge. |
| `fix/*` | Bug fixes. Delete after merge. |
| `chore/*` | Build / config / deps. Delete after merge. |
| `exp/*` | PoC. May keep. |

Examples: `feat/user-login`, `fix/token-expiry`, `chore/upgrade-node-20`.

## Commits

Format: `<type>(<scope>): <subject> (<JIRA-KEY>)` — scope optional, Jira ticket required.

Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `ci`, `exp`.

Rules:
- Imperative (`add`, not `added`).
- Subject ≤ 50 chars, no trailing period.
- One commit = one purpose.
- Body: **what** and **why**, not how.
- No `Co-Authored-By`.
- Every commit includes a Jira ticket number (e.g. `DART-123`).

**Branch name ≠ commit message** — never reuse the branch name as the subject.

| Branch | Commit message |
| --- | --- |
| `feat/user-login` | `feat: 사용자 로그인 API 추가 (DART-101)` |
| `fix/token-expiry` | `fix: 토큰 만료 시 무한 루프 수정 (DART-102)` |
| `chore/upgrade-node-20` | `chore: pnpm 10.x로 업그레이드 (DART-103)` |
| `exp/vector-search` | `exp: 신규 기능 연구-자연어 수치 표현 번역 모델 개발 (DART-104)` |

## PRs

| From | To | Merge |
| --- | --- | --- |
| `feat/*`, `fix/*`, `chore/*`, `exp/*` | `dev` | Squash |
| `dev` | `main` | Merge commit |
| `fix/*` from `main` (hotfix) | `main`, back-port to `dev` | Squash |

## Claude behavior

**Jira ticket** — before every commit or push, ask the user for the Jira ticket number and include it in the commit message. Never commit without it.

**New branch** — from `dev` (hotfix: from `main`):

```shellscript
git checkout dev && git pull && git checkout -b feat/xxx
```

**Tests** — include with logic changes when feasible.

**After merge** — delete branch (except `exp/*`):

```shellscript
git branch -d feat/xxx && git push origin --delete feat/xxx
```

**Hotfix → main** — back-port to `dev`:

```shellscript
git checkout dev && git pull && git merge main && git push
```
