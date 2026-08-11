# Elisa SEO Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking. Do not create Git commits unless the owner explicitly requests them.

**Goal:** Build the approved self-hosted, open-source Elisa SEO Agent web application from the existing SEO skill package, with Docker Compose, multiple AI providers, multi-project vaults, baseline rank tracking, site mapping, resumable workers, safe WordPress drafts, reporting, and a public landing page.

**Architecture:** A Next.js web UI talks to a FastAPI control API. A Python worker executes durable SQLite-backed jobs and skill adapters. A scheduler creates recurring weekly jobs. Each project has an SQLite operational record plus an Obsidian-compatible Markdown vault. External services are connector adapters with clear capability flags; On-Page.ai is optional.

**Tech Stack:** Next.js App Router and TypeScript; FastAPI and Python 3.12; SQLAlchemy 2 and Alembic; SQLite in WAL mode; Pydantic v2; pytest; Vitest; Playwright; Docker Compose; Markdown vault templates; httpx; structured JSON logging.

## Global Constraints

- Product is self-hosted only; do not add SaaS accounts, hosted tenancy, billing, or cloud persistence.
- Do not add Gmail outreach or local SEO/GBP workflows.
- Do not add automatic content generation to v1.
- Optimize existing content and create CMS drafts; never publish by default.
- On-Page.ai is optional. Core workflows must run without it and must clearly mark unavailable capabilities.
- DataForSEO is the explicit rank-tracking adapter; GSC and GA4 have separate measurement responsibilities.
- Support multiple AI providers through adapters: OpenAI, Anthropic, Google Gemini, Ollama, and generic OpenAI-compatible endpoints.
- Use local plaintext configuration for credentials in config/local.env; never write secrets to SQLite, project vaults, reports, logs, or exports.
- Every long-running task must be checkpointed, resumable, idempotent, and visible in the UI.
- Every project must have an isolated project vault and project-scoped operational data.
- All pages must show current status, blockers, and a next action.
- Respect robots.txt, rate limits, user-configured crawl limits, and CMS approval rules.
- Preserve existing skill files; wrap or adapt them rather than rewriting the source recipes.
- Do not create Git commits. Leave changes in the working directory for owner review.
- Run the listed verification commands after every task and record failures in the task notes.

---

## Task 1: Bootstrap the repository and Docker Compose foundation

**Files:**
- Create: package.json
- Create: pnpm-workspace.yaml
- Create: tsconfig.base.json
- Create: apps/web/package.json
- Create: apps/web/tsconfig.json
- Create: apps/web/next.config.ts
- Create: services/api/pyproject.toml
- Create: services/worker/pyproject.toml
- Create: services/scheduler/pyproject.toml
- Create: docker-compose.yml
- Create: .env.example
- Create: .gitignore
- Create: Makefile
- Create: README.md
- Test: scripts/verify-foundation.sh

**Interfaces:**
- Docker services are named web, api, worker, and scheduler.
- Shared runtime data is mounted at /data inside Python containers.
- SQLite database path is /data/app.db.
- Project vault root is /data/projects.
- Local credentials are read from /app/config/local.env and never from project files.
- API listens on port 8000 inside the Compose network.
- Web listens on port 3000 inside the Compose network.

- [ ] **Step 1: Create the workspace manifests**

Configure pnpm workspaces for apps/web and shared TypeScript packages. Configure Python projects with FastAPI, SQLAlchemy, Alembic, Pydantic, httpx, structlog, pytest, and ruff. Pin Python to 3.12 and Node to the current LTS version used by the repository.

- [ ] **Step 2: Create the Compose services**

Create Dockerfiles for web, api, worker, and scheduler. Mount ./data to /data and ./config to /app/config. Add health checks for the API and web services. Do not add Redis or Postgres in v1; SQLite is the local operational database.

- [ ] **Step 3: Create local configuration examples**

Add .env.example with non-secret defaults:

~~~env
APP_ENV=development
API_BASE_URL=http://localhost:8000
WEB_PORT=3000
API_PORT=8000
DATA_ROOT=/data
PROJECTS_ROOT=/data/projects
SQLITE_PATH=/data/app.db
LOG_LEVEL=INFO
CRAWL_MAX_CONCURRENCY=4
CRAWL_REQUEST_DELAY_MS=250
~~~

Add config/local.env.example containing provider key names only. Add config/local.env to .gitignore.

- [ ] **Step 4: Add the foundation verification script**

scripts/verify-foundation.sh must check Docker Compose configuration, required directories, health endpoints, and the existence of /data/app.db after startup. It must exit non-zero with a clear message if any check fails.

- [ ] **Step 5: Verify the foundation**

Run:

~~~bash
docker compose config
docker compose build
docker compose up -d
bash scripts/verify-foundation.sh
docker compose down
~~~

Expected result: Compose validates, images build, health checks pass, and the script reports FOUNDATION_OK.

---

## Task 2: Create the shared domain types and database schema

**Files:**
- Create: services/api/app/db/base.py
- Create: services/api/app/db/session.py
- Create: services/api/app/db/models/project.py
- Create: services/api/app/db/models/integration.py
- Create: services/api/app/db/models/seo.py
- Create: services/api/app/db/models/jobs.py
- Create: services/api/app/db/models/reports.py
- Create: services/api/app/db/models/__init__.py
- Create: services/api/alembic.ini
- Create: services/api/alembic/env.py
- Create: services/api/alembic/versions/0001_initial_schema.py
- Create: packages/contracts/src/domain.ts
- Create: packages/contracts/src/job.ts
- Create: packages/contracts/src/integration.ts
- Create: tests/api/test_database_schema.py

**Interfaces:**
- Project: id, name, domain, sitemap_url, goal, status, created_at, updated_at.
- Keyword: id, project_id, phrase, intent, business_value, priority, target_url_id, status.
- Page: id, project_id, url, page_type, title, h1, word_count, canonical_url, http_status, sitemap_lastmod, tier, crawl_status.
- RankingSnapshot: id, project_id, keyword_id, rank, ranking_url, engine, region, locale, device, captured_at, source.
- Job: id, project_id, type, status, priority, payload_json, result_json, error_json, lease_until, created_at, updated_at.
- Checkpoint: id, job_id, cursor_json, completed_units, total_units, last_safe_at.
- Approval: id, project_id, job_id, action_type, status, requested_at, decided_at, decision_note.
- AuditEvent: id, project_id, job_id, event_type, message, metadata_json, created_at.

- [ ] **Step 1: Write schema tests**

In tests/api/test_database_schema.py, create a project, keyword, page, ranking snapshot, job, checkpoint, approval, and audit event. Assert foreign-key ownership, enum validation, UTC timestamps, and uniqueness of project/domain plus project/keyword phrase.

- [ ] **Step 2: Implement SQLAlchemy models**

Use SQLAlchemy 2 typed declarative mappings. Enable SQLite foreign keys and WAL mode on connection. Store JSON payloads as SQLite JSON-compatible text through a typed helper.

- [ ] **Step 3: Create the first Alembic migration**

Create all tables and indexes required by the interfaces. Add indexes for project_id, job status, ranking keyword/date, page URL, and audit event date.

- [ ] **Step 4: Add TypeScript contracts**

Define Zod schemas and inferred TypeScript types matching API response objects. The web application must validate API responses before rendering.

- [ ] **Step 5: Run schema verification**

Run:

~~~bash
cd services/api
pytest tests/api/test_database_schema.py -q
alembic upgrade head
~~~

Expected result: all schema tests pass and the migration completes on a fresh SQLite file.

---

## Task 3: Implement project isolation and vault management

**Files:**
- Create: services/api/app/projects/service.py
- Create: services/api/app/projects/router.py
- Create: services/api/app/vault/service.py
- Create: services/api/app/vault/templates/README.md
- Create: services/api/app/vault/templates/00-strategy/project-profile.md
- Create: services/api/app/vault/templates/00-strategy/onboarding-checklist.md
- Create: services/api/app/vault/templates/00-strategy/money-keywords.md
- Create: services/api/app/vault/templates/00-strategy/tool-access-map.md
- Create: services/api/app/vault/templates/00-strategy/approval-rules.md
- Create: services/api/app/vault/templates/08-tracking/baseline-rankings.csv
- Create: services/api/app/vault/templates/07-queue/setup-tasks.md
- Create: services/api/app/vault/templates/09-reports/README.md
- Create: tests/api/test_project_vaults.py

**Interfaces:**
- POST /api/projects creates a project and its vault.
- GET /api/projects returns project summaries.
- GET /api/projects/{project_id} returns the project profile and status.
- POST /api/projects/{project_id}/activate updates active-project state.
- GET /api/projects/{project_id}/vault/status returns expected files and missing files.
- ProjectVaultService.create(project_id, profile) -> Path.
- ProjectVaultService.write_markdown(project_id, relative_path, content) -> None.
- ProjectVaultService.read_markdown(project_id, relative_path) -> str.

- [ ] **Step 1: Write project isolation tests**

Assert that two projects create separate directories, separate Markdown files, and cannot read each other’s page or keyword data. Assert that project switching changes the active project record only.

- [ ] **Step 2: Implement vault creation**

Create the approved directory structure under PROJECTS_ROOT/project_id. Render profile values into templates. Reject relative paths containing .., absolute paths, or path separators that escape the project root.

- [ ] **Step 3: Implement project APIs**

Validate project name, absolute HTTPS website URL, and optional sitemap URL. Create a UUID project ID. Write the active-project marker to /data/active-project.json without storing credentials.

- [ ] **Step 4: Implement vault status**

Check expected directories/files and return missing, present, and malformed items. The UI will use this endpoint for onboarding progress.

- [ ] **Step 5: Verify project isolation**

Run:

~~~bash
cd services/api
pytest tests/api/test_project_vaults.py -q
~~~

Expected result: all project isolation and path safety tests pass.

---

## Task 4: Implement local configuration and connector capability registry

**Files:**
- Create: services/api/app/config/settings.py
- Create: services/api/app/config/redaction.py
- Create: services/api/app/integrations/models.py
- Create: services/api/app/integrations/registry.py
- Create: services/api/app/integrations/router.py
- Create: services/api/app/integrations/health.py
- Create: services/api/app/config/local.env.example
- Create: tests/api/test_config_redaction.py
- Create: tests/api/test_integration_capabilities.py

**Interfaces:**
- GET /api/integrations returns configured/available/unavailable capability cards.
- POST /api/integrations/{integration_id}/test runs a connection test.
- SecretRefReader.get(name) -> str | None.
- redact_secrets(value) -> value with known secrets removed.
- ConnectorRegistry.get(integration_id) -> connector metadata.

- [ ] **Step 1: Write redaction tests**

Verify that API keys, passwords, bearer tokens, client secrets, and refresh tokens are removed from strings, dictionaries, exception messages, and JSON logs.

- [ ] **Step 2: Implement local.env loading**

Load config/local.env once at process startup. Do not copy any values into the database. Expose only named boolean/status metadata to the rest of the application.

- [ ] **Step 3: Implement capability metadata**

Register core capabilities and optional capabilities. On-Page.ai must report unavailable when its API key is absent. The system must distinguish required-for-task from optional-not-configured.

- [ ] **Step 4: Implement health tests**

Return safe connection status, last test time, and user-facing guidance. Never include secret values or full provider error payloads.

- [ ] **Step 5: Verify configuration safety**

Run:

~~~bash
cd services/api
pytest tests/api/test_config_redaction.py tests/api/test_integration_capabilities.py -q
~~~

Expected result: secrets are redacted and optional connectors degrade gracefully.

---

## Task 5: Build the AI provider adapter layer

**Files:**
- Create: services/api/app/ai/contracts.py
- Create: services/api/app/ai/router.py
- Create: services/api/app/ai/budget.py
- Create: services/api/app/ai/providers/openai.py
- Create: services/api/app/ai/providers/anthropic.py
- Create: services/api/app/ai/providers/gemini.py
- Create: services/api/app/ai/providers/ollama.py
- Create: services/api/app/ai/providers/openai_compatible.py
- Create: services/api/app/ai/registry.py
- Create: tests/api/test_ai_provider_contract.py
- Create: tests/api/test_ai_routing.py

**Interfaces:**
- AIRequest(task_type, system_prompt, user_prompt, model, max_tokens, temperature, project_id).
- AIResponse(provider, model, text, usage, request_id, raw_metadata).
- AIProvider.complete(request: AIRequest) -> AIResponse.
- AIProvider.health() -> ProviderHealth.
- AIRouter.select(task_type, project_id, preferred_provider=None) -> AIProvider.
- BudgetService.reserve(project_id, provider, estimated_tokens) -> BudgetReservation.
- BudgetService.commit(reservation, actual_usage) -> None.

- [ ] **Step 1: Write contract tests**

Use fake providers to verify normalized responses, provider failure handling, fallback order, budget rejection, and privacy permissions.

- [ ] **Step 2: Implement the common provider protocol**

Define a provider-independent request/response format. Store provider configuration metadata in SQLite but read credentials only from local.env.

- [ ] **Step 3: Implement providers**

Implement HTTP clients for OpenAI, Anthropic, Gemini, Ollama, and generic OpenAI-compatible endpoints. Each provider must support timeout, retry with bounded backoff, request IDs, usage extraction, and safe error normalization.

- [ ] **Step 4: Implement task routing**

Allow project settings to select providers per task type. Support fallback providers when the primary provider fails. Block providers not permitted for a project.

- [ ] **Step 5: Verify routing**

Run:

~~~bash
cd services/api
pytest tests/api/test_ai_provider_contract.py tests/api/test_ai_routing.py -q
~~~

Expected result: fake-provider tests pass without making external calls.

---

## Task 6: Implement the DataForSEO, GSC, GA4, and optional On-Page.ai connectors

**Files:**
- Create: services/api/app/connectors/dataforseo.py
- Create: services/api/app/connectors/gsc.py
- Create: services/api/app/connectors/ga4.py
- Create: services/api/app/connectors/onpage.py
- Create: services/api/app/connectors/common.py
- Create: services/api/app/connectors/fixtures/dataforseo_serp.json
- Create: services/api/app/connectors/fixtures/gsc_rows.json
- Create: services/api/app/connectors/fixtures/ga4_rows.json
- Create: services/api/app/connectors/fixtures/onpage_scan.json
- Create: tests/api/test_dataforseo_connector.py
- Create: tests/api/test_gsc_connector.py
- Create: tests/api/test_ga4_connector.py
- Create: tests/api/test_onpage_optional.py

**Interfaces:**
- RankProvider.capture(keyword, region, locale, device, depth) -> RankResult.
- SearchPerformanceProvider.query(site_url, start_date, end_date) -> list[SearchPerformanceRow].
- AnalyticsProvider.query(property_id, start_date, end_date) -> list[AnalyticsRow].
- OnPageProvider.scan(url, keyword, scan_type, region, locale) -> OnPageJobHandle.
- OnPageProvider.wait(handle) -> OnPageResult.
- Connector errors use ConnectorError(code, user_message, retryable, blocked_capabilities).

- [ ] **Step 1: Write fixture-based tests**

Mock each provider and assert normalized outputs, retries, authentication failures, rate-limit handling, and no secret leakage.

- [ ] **Step 2: Implement DataForSEO**

Implement login/password authentication from local.env, Google organic SERP task creation/polling, result normalization, rank-not-found handling, location/device settings, and request cost metadata.

- [ ] **Step 3: Implement GSC and GA4**

Implement local OAuth callback support with refresh-token storage in local.env. Normalize GSC search analytics and GA4 traffic/conversion rows. If OAuth is not configured, report setup guidance without blocking unrelated work.

- [ ] **Step 4: Implement On-Page.ai REST adapter**

Use the asynchronous scan endpoints. Submit scan, store provider job ID in the job payload, poll status, fetch result, and expose capability flags for lite, standard, deep, and internal-link workflows. Do not emulate result fields when the connector is unavailable.

- [ ] **Step 5: Verify connectors**

Run:

~~~bash
cd services/api
pytest tests/api/test_dataforseo_connector.py tests/api/test_gsc_connector.py tests/api/test_ga4_connector.py tests/api/test_onpage_optional.py -q
~~~

Expected result: all tests pass using fixtures and no live credentials.

---

## Task 7: Implement the durable job queue and checkpoint engine

**Files:**
- Create: services/api/app/jobs/models.py
- Create: services/api/app/jobs/repository.py
- Create: services/api/app/jobs/leases.py
- Create: services/api/app/jobs/checkpoints.py
- Create: services/api/app/jobs/router.py
- Create: services/worker/app/runner.py
- Create: services/worker/app/handlers.py
- Create: tests/api/test_job_leases.py
- Create: tests/worker/test_resume.py
- Create: tests/worker/test_idempotency.py

**Interfaces:**
- JobRepository.enqueue(project_id, job_type, payload, priority) -> Job.
- JobRepository.claim_next(worker_id, lease_seconds) -> Job | None.
- JobRepository.complete(job_id, result) -> None.
- JobRepository.fail(job_id, error, retryable) -> None.
- CheckpointService.save(job_id, cursor, completed_units, total_units) -> Checkpoint.
- CheckpointService.load(job_id) -> Checkpoint | None.
- JobRunner.run_once(worker_id) -> bool.
- IdempotencyService.reserve(key) -> bool.

- [ ] **Step 1: Write queue tests**

Cover priority ordering, lease expiration, two workers racing for one job, retryable failures, non-retryable failures, pause requests, and idempotency conflicts.

- [ ] **Step 2: Implement SQLite leasing**

Use short SQLite transactions and an atomic claim operation. Store lease_until and worker_id. Reclaim expired leases only after marking the previous attempt interrupted.

- [ ] **Step 3: Implement checkpoints**

Store cursor JSON and safe progress counters after every unit. Provide resume-from-checkpoint behavior to handlers.

- [ ] **Step 4: Implement idempotency**

Use a unique idempotency key table. Duplicate reservations must return the original operation status and must not repeat a CMS edit, link insertion, or ranking snapshot.

- [ ] **Step 5: Verify resume behavior**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_resume.py tests/worker/test_idempotency.py -q
~~~

Expected result: interrupted jobs resume from the last checkpoint and do not duplicate completed work.

---

## Task 8: Import and adapt the existing SEO skill package

**Files:**
- Create: skills/source/
- Create: skills/registry.yaml
- Create: services/worker/app/skills/contracts.py
- Create: services/worker/app/skills/loader.py
- Create: services/worker/app/skills/adapters.py
- Create: tests/worker/test_skill_registry.py
- Copy: openclaw-skills/ and relevant templates into skills/source/ without modifying originals

**Interfaces:**
- SkillDefinition(id, name, category, requires, optional_requires, produces, approval_required, supports_resume).
- SkillContext(project_id, job_id, vault_root, connector_registry, ai_router).
- SkillHandler.run(context, payload, checkpoint) -> SkillResult.
- SkillRegistry.get(skill_id) -> SkillDefinition and handler.
- SkillRegistry.eligible(skill_id, project_state) -> EligibilityResult.

- [ ] **Step 1: Copy source skills**

Copy the existing 34 skill directories into skills/source/. Preserve each SKILL.md, references, templates, and agents metadata. Do not copy skill-local memory logs into project state.

- [ ] **Step 2: Create the registry**

Register discovery, ranking, audit, optimization, linking, CMS, reporting, and optional connector skills. Mark Gmail and local SEO/GBP skills out of scope and ineligible.

- [ ] **Step 3: Implement the loader**

Read SKILL.md and metadata, validate required sections, and associate each skill with a deterministic adapter. The loader must fail with a user-readable error if a skill is malformed.

- [ ] **Step 4: Implement eligibility**

A skill with missing optional connectors remains eligible with degraded output. A skill with a required missing connector becomes blocked with a specific setup action.

- [ ] **Step 5: Verify registry**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_skill_registry.py -q
~~~

Expected result: all in-scope skills load, excluded skills are not routable, and missing optional connectors are represented accurately.

---

## Task 9: Implement sitemap import, crawl controls, and site architecture mapping

**Files:**
- Create: services/worker/app/crawl/http_client.py
- Create: services/worker/app/crawl/robots.py
- Create: services/worker/app/crawl/sitemaps.py
- Create: services/worker/app/crawl/classifier.py
- Create: services/worker/app/architecture/mapper.py
- Create: services/worker/app/architecture/link_inventory.py
- Create: services/api/app/architecture/router.py
- Create: tests/worker/test_sitemap_parser.py
- Create: tests/worker/test_crawl_limits.py
- Create: tests/worker/test_architecture_mapper.py

**Interfaces:**
- SitemapImporter.import_url(sitemap_url) -> SitemapImportSummary.
- CrawlPolicy(max_pages, concurrency, delay_ms, respect_robots) -> CrawlPolicy.
- PageFetcher.fetch(url) -> FetchedPage.
- PageClassifier.classify(url, html, metadata) -> PageClassification.
- ArchitectureMapper.map(project_id, cursor) -> ArchitectureProgress.
- LinkInventory.extract(html, base_url) -> list[LinkRecord].

- [ ] **Step 1: Write sitemap parser tests**

Cover sitemap indexes, nested sitemaps, namespaces, missing lastmod, duplicate URLs, malformed XML, and URL normalization.

- [ ] **Step 2: Implement sitemap-first import**

Parse the supplied sitemap without fetching every page. Store URLs, lastmod, source sitemap, and eligibility. Exclude archive, tag, search, pagination, login, cart, checkout, privacy, terms, and utility patterns by configurable rules.

- [ ] **Step 3: Implement crawl policy**

Fetch only selected batches after the lightweight manifest exists. Respect robots.txt, limit concurrency, add delay, enforce max pages, and save progress after each page.

- [ ] **Step 4: Implement page classification and hierarchy**

Classify URLs into homepage, top-level service/product, secondary page, location, blog/article, category, utility, or unknown. Infer tier from path depth and configured project rules. Store title, H1, word count, canonical, status, headings, and links.

- [ ] **Step 5: Implement architecture summary**

Return counts, tier distribution, page-type distribution, orphan candidates, duplicate/canonical warnings, and link graph edges. Write a Markdown architecture report to the project vault.

- [ ] **Step 6: Verify architecture mapping**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_sitemap_parser.py tests/worker/test_crawl_limits.py tests/worker/test_architecture_mapper.py -q
~~~

Expected result: parser, crawl safety, classification, progress, and architecture counts pass fixture tests.

---

## Task 10: Implement keyword intake, page mapping, and opportunity discovery

**Files:**
- Create: services/api/app/keywords/router.py
- Create: services/worker/app/keywords/importer.py
- Create: services/worker/app/keywords/mapper.py
- Create: services/worker/app/keywords/opportunities.py
- Create: services/worker/app/keywords/prioritizer.py
- Create: services/worker/app/keywords/topic_recommender.py
- Create: tests/worker/test_keyword_import.py
- Create: tests/worker/test_keyword_mapping.py
- Create: tests/worker/test_opportunity_scoring.py

**Interfaces:**
- KeywordImporter.import_csv(project_id, csv_bytes) -> ImportSummary.
- KeywordMapper.map_pages(project_id) -> MappingSummary.
- OpportunityMiner.find(project_id, sources) -> list[Opportunity].
- OpportunityScorer.score(opportunity, project_state) -> float.
- KeywordPrioritizer.batch(project_id, batch_size=10) -> list[KeywordBatch].
- TopicRecommender.recommend(project_id) -> list[TopicRecommendation].

- [ ] **Step 1: Write CSV and mapping tests**

Cover CSV columns phrase, URL, type, value, location, and notes; duplicate phrases; invalid URLs; missing required fields; page matching by exact URL, slug, title, and content.

- [ ] **Step 2: Implement keyword import**

Support paste and CSV. Validate phrases, preserve user-provided money-keyword flags, and write money-keywords.md.

- [ ] **Step 3: Implement page mapping**

Map keywords to existing pages using explicit user mappings first, then URL/title/H1/content evidence. Flag ambiguous or unmapped keywords for review.

- [ ] **Step 4: Implement opportunity mining**

Use GSC rows, ranking snapshots, page inventory, and optional DataForSEO/On-Page.ai evidence. Detect positions 11–30, high-impression/low-CTR, declines, wrong-page signals, missing pages, and content gaps.

- [ ] **Step 5: Implement prioritization**

Score business value, position opportunity, traffic opportunity, trend, readiness, competition, effort, and dependencies. Default to top 10, then next 10. Write the queue to 07-queue and 05-opportunities.

- [ ] **Step 6: Verify keyword workflows**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_keyword_import.py tests/worker/test_keyword_mapping.py tests/worker/test_opportunity_scoring.py -q
~~~

Expected result: deterministic mapping, opportunity detection, and top-10 batching pass.

---

## Task 11: Implement baseline rankings and weekly measurement

**Files:**
- Create: services/worker/app/rankings/baseline.py
- Create: services/worker/app/rankings/snapshots.py
- Create: services/worker/app/rankings/trends.py
- Create: services/worker/app/analytics/gsc_import.py
- Create: services/worker/app/analytics/ga4_import.py
- Create: services/api/app/rankings/router.py
- Create: tests/worker/test_baseline.py
- Create: tests/worker/test_trends.py
- Create: tests/worker/test_measurement_import.py

**Interfaces:**
- BaselineService.capture(project_id, keyword_ids, policy) -> BaselineSummary.
- SnapshotService.capture(project_id, keyword_ids, policy) -> SnapshotSummary.
- TrendService.compare(project_id, baseline_id, current_snapshot_id) -> TrendReport.
- GSCImporter.import_rows(project_id, rows) -> ImportSummary.
- GA4Importer.import_rows(project_id, rows) -> ImportSummary.

- [ ] **Step 1: Write baseline tests**

Cover rank found, rank not found, URL changes, device/location policy, provider errors, partial completion, and rerun behavior.

- [ ] **Step 2: Implement baseline capture**

Create one ranking snapshot per keyword and policy. Save CSV and Markdown copies under 08-tracking. Mark baseline ready only when all keywords are complete or documented as unavailable.

- [ ] **Step 3: Implement weekly snapshots**

Capture current rankings, GSC, and optional GA4 data. Compare against baseline and previous snapshots.

- [ ] **Step 4: Implement trend classification**

Classify gains, losses, stable, new, dropped, insufficient data, and provider error. Identify pages needing review.

- [ ] **Step 5: Verify measurement**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_baseline.py tests/worker/test_trends.py tests/worker/test_measurement_import.py -q
~~~

Expected result: baselines and trend reports are reproducible and preserve source metadata.

---

## Task 12: Implement the orchestrator and loop controller

**Files:**
- Create: services/worker/app/orchestrator/state.py
- Create: services/worker/app/orchestrator/planner.py
- Create: services/worker/app/orchestrator/decision.py
- Create: services/worker/app/orchestrator/loop_controller.py
- Create: services/worker/app/orchestrator/guards.py
- Create: services/api/app/orchestrator/router.py
- Create: tests/worker/test_orchestrator.py
- Create: tests/worker/test_loop_controller.py
- Create: tests/worker/test_stop_conditions.py

**Interfaces:**
- ProjectStateLoader.load(project_id) -> ProjectState.
- NextActionPlanner.plan(state) -> NextAction | Blocker.
- LoopController.start(project_id, goal, success_criteria, stop_conditions) -> LoopState.
- LoopController.run_once(loop_id) -> LoopDecision.
- LoopController.pause(loop_id) -> None.
- LoopController.resume(loop_id) -> None.
- LoopController.stop(loop_id, reason) -> None.

- [ ] **Step 1: Write decision tests**

Cover onboarding incomplete, missing connector, pending approval, queue available, measurement window, budget cap, repeated failures, completion, and user pause.

- [ ] **Step 2: Implement project state loading**

Read database state and required vault files. Never infer durable progress from chat history. Return explicit missing-data and stale-data conditions.

- [ ] **Step 3: Implement next-action planning**

Select the next eligible skill based on dependencies, queue priority, project goal, available connectors, and approval rules. Return one primary next action plus blockers.

- [ ] **Step 4: Implement loop controller**

Persist goal, success criteria, stop conditions, iteration count, current job, last decision, and next wake-up in SQLite and 07-queue/loops plus 08-tracking/loops.

- [ ] **Step 5: Implement guards**

Enforce provider budgets, crawl limits, approval gates, no-publish rule, maximum retries, and no duplicate action keys.

- [ ] **Step 6: Verify loop behavior**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_orchestrator.py tests/worker/test_loop_controller.py tests/worker/test_stop_conditions.py -q
~~~

Expected result: every loop decision is explainable, persisted, and resumable.

---

## Task 13: Implement page audits and checklist management

**Files:**
- Create: services/worker/app/audits/local_onpage.py
- Create: services/worker/app/audits/page_audit.py
- Create: services/worker/app/audits/ai_visibility.py
- Create: services/worker/app/audits/checklists.py
- Create: services/api/app/audits/router.py
- Create: services/api/app/checklists/router.py
- Create: tests/worker/test_page_audit.py
- Create: tests/worker/test_checklists.py
- Create: tests/worker/test_ai_visibility_optional.py

**Interfaces:**
- PageAuditor.audit(project_id, page_id, keyword_id, mode) -> PageAuditResult.
- LocalOnPageAudit.run(page) -> LocalAuditFindings.
- AIVisibilityAuditor.run(project_id, page_id, keyword_id) -> VisibilityResult.
- ChecklistService.create_from_audit(audit_id) -> Checklist.
- ChecklistService.complete_item(item_id, evidence) -> None.

- [ ] **Step 1: Write audit tests**

Cover title/H1, headings, word count, canonical, robots, image alt text, internal links, keyword stuffing heuristics, thin content, crawl status, and optional connector degradation.

- [ ] **Step 2: Implement local audit**

Use fetched page data and project keyword mapping. Produce evidence-backed findings without claiming live competitor comparisons.

- [ ] **Step 3: Implement optional On-Page.ai audit**

When configured, invoke lite/standard/deep scans according to task type. Store provider job/result references and mark unavailable otherwise.

- [ ] **Step 4: Implement checklist persistence**

Create checklist items with status, priority, evidence, recommendation, approval requirement, and verification field. Write a Markdown checklist to 07-queue/page-checklists.

- [ ] **Step 5: Verify audit workflow**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_page_audit.py tests/worker/test_checklists.py tests/worker/test_ai_visibility_optional.py -q
~~~

Expected result: audits produce actionable checklists and never invent optional-provider evidence.

---

## Task 14: Implement internal-link planning and queue generation

**Files:**
- Create: services/worker/app/linking/graph.py
- Create: services/worker/app/linking/keyword_mentions.py
- Create: services/worker/app/linking/planner.py
- Create: services/worker/app/linking/deduplication.py
- Create: services/api/app/linking/router.py
- Create: tests/worker/test_link_graph.py
- Create: tests/worker/test_link_planner.py
- Create: tests/worker/test_link_deduplication.py

**Interfaces:**
- LinkGraph.build(project_id) -> LinkGraphSummary.
- KeywordMentionCatalog.build(project_id) -> list[KeywordMention].
- InternalLinkPlanner.plan(project_id, target_page_id) -> list[LinkProposal].
- InternalLinkPlanner.plan_sitewide(project_id, batch) -> list[LinkProposal].
- LinkDeduplicator.filter(proposals) -> list[LinkProposal].

- [ ] **Step 1: Write graph tests**

Cover source/target links, anchor extraction, canonicalized URLs, links in navigation versus main content, orphan detection, and duplicate URLs.

- [ ] **Step 2: Implement the existing-link graph**

Use fetched HTML and page records. Store link placement and main-content confidence.

- [ ] **Step 3: Implement keyword mention catalog**

Find existing keyword and semantic mentions in page text. Link money pages to supporting pages using explicit mappings first.

- [ ] **Step 4: Implement plan generation**

Produce contextual source/target proposals with anchor text, sentence evidence, target keyword, priority, and reason. Use optional On-Page.ai recommendations only when available.

- [ ] **Step 5: Implement deduplication**

Reject links already present, repeated source/target pairs, navigation-only links when main content is required, and proposals without a natural anchor context.

- [ ] **Step 6: Verify linking plan**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_link_graph.py tests/worker/test_link_planner.py tests/worker/test_link_deduplication.py -q
~~~

Expected result: sitewide plans are deterministic, auditable, and do not duplicate existing links.

---

## Task 15: Implement WordPress draft/revision integration

**Files:**
- Create: services/worker/app/cms/contracts.py
- Create: services/worker/app/cms/wordpress.py
- Create: services/worker/app/cms/drafts.py
- Create: services/worker/app/cms/verification.py
- Create: services/api/app/cms/router.py
- Create: tests/worker/test_wordpress_client.py
- Create: tests/worker/test_cms_draft_safety.py
- Create: tests/worker/test_cms_verification.py

**Interfaces:**
- CMSClient.get_page(url_or_id) -> CMSPage.
- CMSClient.create_revision(page_id, content, metadata) -> CMSDraft.
- CMSClient.update_alt_text(media_id, alt_text) -> CMSDraft.
- CMSClient.verify_draft(draft_id) -> DraftVerification.
- DraftService.create_from_proposal(proposal_id) -> Draft.
- DraftService.approve(draft_id) -> None.
- DraftService.publish(draft_id) -> blocked unless project policy allows.

- [ ] **Step 1: Write CMS safety tests**

Assert that no publish request can occur under default policy, that draft content includes before/after values, and that rejected approvals do not create changes.

- [ ] **Step 2: Implement WordPress REST client**

Use local credentials and application password. Support page retrieval, revision/draft creation, media alt-text updates, and response normalization. Add bounded retries and safe error messages.

- [ ] **Step 3: Implement draft service**

Convert approved link proposals and checklist actions into drafts. Store CMS IDs and source/target metadata.

- [ ] **Step 4: Implement verification**

Refetch the draft and verify intended changes, title/slug preservation, structure preservation, and target link existence.

- [ ] **Step 5: Verify CMS behavior**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_wordpress_client.py tests/worker/test_cms_draft_safety.py tests/worker/test_cms_verification.py -q
~~~

Expected result: all CMS operations remain draft-only and verification detects mismatches.

---

## Task 16: Implement reporting and audit trails

**Files:**
- Create: services/worker/app/reports/renderer.py
- Create: services/worker/app/reports/weekly.py
- Create: services/worker/app/reports/on_demand.py
- Create: services/worker/app/reports/audit_trail.py
- Create: services/api/app/reports/router.py
- Create: services/worker/app/reports/templates/weekly.html
- Create: services/worker/app/reports/templates/on-demand.html
- Create: tests/worker/test_report_rendering.py
- Create: tests/worker/test_audit_trail.py

**Interfaces:**
- ReportRenderer.render(report_type, project_id, data) -> RenderedReport.
- WeeklyReportService.generate(project_id, period) -> Report.
- OnDemandReportService.generate(project_id, request) -> Report.
- AuditTrailService.record(project_id, event) -> AuditEvent.
- GET /api/projects/{project_id}/reports returns report summaries.
- GET /api/reports/{report_id} returns report metadata and content.

- [ ] **Step 1: Write report tests**

Cover baseline/current ranking comparisons, task reason/evidence/expected goal/result, blockers, next verification date, and secret redaction.

- [ ] **Step 2: Implement audit events**

Record every job transition, approval, connector result, draft creation, verification, pause/resume, and loop decision in SQLite and Markdown.

- [ ] **Step 3: Implement weekly reports**

Render rankings, GSC/GA4 measurements, gains/losses, completed work, expected outcomes, measured outcomes, blockers, and next actions.

- [ ] **Step 4: Implement on-demand reports**

Accept a project and report scope, then generate a report of tasks completed, reasons, evidence, expected goal, current result, and next verification date.

- [ ] **Step 5: Verify reports**

Run:

~~~bash
cd services/worker
pytest tests/worker/test_report_rendering.py tests/worker/test_audit_trail.py -q
~~~

Expected result: reports render in HTML/Markdown and contain no credentials.

---

## Task 17: Build the web application shell and navigation

**Files:**
- Create: apps/web/app/layout.tsx
- Create: apps/web/app/page.tsx
- Create: apps/web/app/projects/page.tsx
- Create: apps/web/app/projects/[projectId]/layout.tsx
- Create: apps/web/app/projects/[projectId]/page.tsx
- Create: apps/web/app/projects/[projectId]/overview/page.tsx
- Create: apps/web/components/navigation/Sidebar.tsx
- Create: apps/web/components/navigation/ProjectSwitcher.tsx
- Create: apps/web/components/status/StatusBadge.tsx
- Create: apps/web/lib/api-client.ts
- Create: apps/web/lib/query-client.ts
- Create: apps/web/styles/globals.css
- Create: apps/web/tests/navigation.test.tsx

**Interfaces:**
- Routes: /, /projects, /projects/:id/overview, /projects/:id/architecture, /projects/:id/keywords, /projects/:id/rankings, /projects/:id/queue, /projects/:id/pages, /projects/:id/approvals, /projects/:id/reports, /settings/integrations, /settings/ai.
- API client reads API_BASE_URL and includes project ID headers where required.
- Navigation renders current project and next-action status.

- [ ] **Step 1: Write navigation tests**

Assert routes, active project switching, unavailable integration badges, and redirect to onboarding when no project exists.

- [ ] **Step 2: Implement application shell**

Create responsive desktop-first layout with sidebar, project switcher, status header, primary next action card, blocker count, pending approvals, and job activity.

- [ ] **Step 3: Implement API client**

Use typed fetch wrappers with timeout, error normalization, retry for GET requests, and safe error messages.

- [ ] **Step 4: Implement empty and loading states**

Every route must show an explanatory empty state and direct setup action when data is missing. Add skeletons for long-running queries.

- [ ] **Step 5: Verify web shell**

Run:

~~~bash
cd apps/web
pnpm test -- --run
pnpm build
~~~

Expected result: route tests pass and the production build succeeds.

---

## Task 18: Build onboarding, integrations, and project setup UI

**Files:**
- Create: apps/web/app/onboarding/page.tsx
- Create: apps/web/components/onboarding/OnboardingWizard.tsx
- Create: apps/web/components/onboarding/Checklist.tsx
- Create: apps/web/components/integrations/IntegrationCard.tsx
- Create: apps/web/components/ai/ProviderForm.tsx
- Create: apps/web/components/projects/ProjectForm.tsx
- Create: apps/web/tests/onboarding.test.tsx
- Create: apps/web/tests/integrations.test.tsx

**Interfaces:**
- Wizard step IDs: project, keywords, ranking-policy, ai, integrations, approval, review.
- Checklist statuses: unknown, provided, optional-not-provided, blocked, complete.
- Forms submit to project/integration APIs and never display raw saved credentials.

- [ ] **Step 1: Write onboarding tests**

Cover required fields, optional connector handling, CSV keyword import, provider setup, validation errors, back navigation, and resume after browser reload.

- [ ] **Step 2: Implement project form**

Collect website, sitemap, business model, services/products, geography, goal, competitors, and approval rules.

- [ ] **Step 3: Implement AI provider setup**

Allow multiple providers, model names, allowed tasks, fallback order, privacy permission, and budget. Display masked API-key state.

- [ ] **Step 4: Implement connector cards**

Show configured, connected, unavailable, blocked, last tested, and feature impact. Add connection-test buttons and setup guidance.

- [ ] **Step 5: Implement onboarding checklist**

Derive checklist status from the API. Show exact next action and allow the user to continue in reduced mode when only optional setup is missing.

- [ ] **Step 6: Verify onboarding**

Run:

~~~bash
cd apps/web
pnpm test -- --run tests/onboarding.test.tsx tests/integrations.test.tsx
~~~

Expected result: onboarding is resumable, understandable, and does not leak secrets.

---

## Task 19: Build architecture, keywords, rankings, queue, and page workspaces

**Files:**
- Create: apps/web/app/projects/[projectId]/architecture/page.tsx
- Create: apps/web/app/projects/[projectId]/keywords/page.tsx
- Create: apps/web/app/projects/[projectId]/rankings/page.tsx
- Create: apps/web/app/projects/[projectId]/queue/page.tsx
- Create: apps/web/app/projects/[projectId]/pages/page.tsx
- Create: apps/web/app/projects/[projectId]/pages/[pageId]/page.tsx
- Create: apps/web/components/architecture/ArchitectureSummary.tsx
- Create: apps/web/components/keywords/KeywordTable.tsx
- Create: apps/web/components/rankings/RankingTrend.tsx
- Create: apps/web/components/queue/JobQueue.tsx
- Create: apps/web/components/pages/PageAuditPanel.tsx
- Create: apps/web/tests/workspaces.test.tsx

**Interfaces:**
- Architecture screen shows total URLs, eligible URLs, page types, tiers, orphan candidates, and link graph summary.
- Keywords screen supports import, filters, priority, target page, and mapping warnings.
- Rankings screen shows baseline/current/trend by keyword and policy.
- Queue screen shows task reason, evidence, expected outcome, status, blocker, approval, and resume action.
- Page workspace shows audit checklist, keyword mapping, rankings, internal-link proposals, drafts, and audit history.

- [ ] **Step 1: Write workspace tests**

Assert that each screen renders intermediate progress, empty states, blocker states, and next actions using fixture API responses.

- [ ] **Step 2: Implement architecture screen**

Show counts and table views first. Add a graph visualization only after counts and relationships are correct.

- [ ] **Step 3: Implement keyword and ranking screens**

Provide CSV import controls, filters, target-page links, baseline/current comparison, and trend explanations.

- [ ] **Step 4: Implement queue and page workspace**

Show the work queue selected by the orchestrator and page-level evidence/checklists. Add pause/resume/retry controls.

- [ ] **Step 5: Verify workspaces**

Run:

~~~bash
cd apps/web
pnpm test -- --run tests/workspaces.test.tsx
~~~

Expected result: all core project workspaces render correct data and clear next actions.

---

## Task 20: Build approvals, blockers, progress, and live job feedback

**Files:**
- Create: apps/web/app/projects/[projectId]/approvals/page.tsx
- Create: apps/web/app/projects/[projectId]/jobs/[jobId]/page.tsx
- Create: apps/web/components/jobs/ProgressTimeline.tsx
- Create: apps/web/components/jobs/BlockerPanel.tsx
- Create: apps/web/components/jobs/LiveLog.tsx
- Create: apps/web/components/approvals/ApprovalCard.tsx
- Create: apps/web/tests/job_feedback.test.tsx
- Create: apps/web/tests/approvals.test.tsx

**Interfaces:**
- GET /api/jobs/{job_id} returns status, step, progress, checkpoint, blocker, and next action.
- POST /api/jobs/{job_id}/pause pauses after the current safe operation.
- POST /api/jobs/{job_id}/resume resumes from checkpoint.
- POST /api/jobs/{job_id}/retry retries only retryable failures.
- GET /api/jobs/{job_id}/events streams or polls audit events.
- POST /api/approvals/{approval_id}/approve and /reject record decisions.

- [ ] **Step 1: Write feedback tests**

Cover queued/running/checking/paused/blocked/completed/failed states, safe pause, resume after restart, retry guidance, and human-readable connector errors.

- [ ] **Step 2: Implement progress timeline**

Display current step, processed/total, batch, last checkpoint, elapsed time, pause, cancel, and live events.

- [ ] **Step 3: Implement blocker panel**

Classify blocking/warning/informational issues and show exact remediation actions.

- [ ] **Step 4: Implement approvals**

Show change summary, reason, evidence, expected outcome, before/after, and publish policy. Approve/reject actions update the job state.

- [ ] **Step 5: Verify feedback UI**

Run:

~~~bash
cd apps/web
pnpm test -- --run tests/job_feedback.test.tsx tests/approvals.test.tsx
~~~

Expected result: users always know what is happening and what they should do next.

---

## Task 21: Implement scheduler and weekly monitoring

**Files:**
- Create: services/scheduler/app/main.py
- Create: services/scheduler/app/schedules.py
- Create: services/scheduler/app/reconciliation.py
- Create: services/api/app/schedules/router.py
- Create: tests/scheduler/test_schedules.py
- Create: tests/scheduler/test_reconciliation.py

**Interfaces:**
- ScheduleService.create(project_id, cadence, timezone, task_types) -> Schedule.
- ScheduleService.pause(schedule_id) -> None.
- ScheduleService.run_due(now) -> list[Job].
- ReconciliationService.reconcile_stale_jobs() -> list[ReconciliationEvent].

- [ ] **Step 1: Write scheduler tests**

Cover weekly cadence, manual run-now, timezone handling, disabled schedules, duplicate prevention, and stale-job reconciliation.

- [ ] **Step 2: Implement schedule persistence**

Store cadence, timezone, enabled state, task types, last run, and next run in SQLite.

- [ ] **Step 3: Implement weekly workflow**

Create ranking snapshot, GSC/GA4 imports when configured, trend report, opportunity detection, and next-action planning jobs.

- [ ] **Step 4: Implement restart reconciliation**

Detect expired leases, mark interrupted jobs, preserve checkpoints, and enqueue safe continuation only once.

- [ ] **Step 5: Verify scheduler**

Run:

~~~bash
cd services/scheduler
pytest tests/scheduler/test_schedules.py tests/scheduler/test_reconciliation.py -q
~~~

Expected result: weekly jobs are created once, can be paused, and resume safely after restart.

---

## Task 22: Implement backups, restore, and export

**Files:**
- Create: services/api/app/backups/service.py
- Create: services/api/app/backups/router.py
- Create: services/api/app/exports/service.py
- Create: tests/api/test_backup_restore.py
- Create: tests/api/test_export_redaction.py
- Create: apps/web/app/projects/[projectId]/settings/backups/page.tsx
- Create: apps/web/tests/backups.test.tsx

**Interfaces:**
- POST /api/projects/{project_id}/backups creates a backup archive without credentials.
- POST /api/projects/{project_id}/restore validates and restores a backup.
- GET /api/projects/{project_id}/exports/{kind} returns vault, database, rankings, or reports export.
- BackupService.create(project_id) -> BackupArtifact.
- BackupService.restore(path) -> RestoreSummary.

- [ ] **Step 1: Write backup tests**

Assert that vault files, project database rows, reports, and ranking history are included and config/local.env is excluded.

- [ ] **Step 2: Implement safe archive creation**

Use a temporary directory, checksum the archive, exclude credentials, and write a manifest with project ID, schema version, and creation time.

- [ ] **Step 3: Implement restore validation**

Validate project ID, schema version, path safety, and archive checksum before replacing or merging data.

- [ ] **Step 4: Implement export UI**

Provide backup, restore, and individual export actions with warnings and progress.

- [ ] **Step 5: Verify backup flows**

Run:

~~~bash
cd services/api
pytest tests/api/test_backup_restore.py tests/api/test_export_redaction.py -q
cd ../../apps/web
pnpm test -- --run tests/backups.test.tsx
~~~

Expected result: backups restore complete local project state without credentials.

---

## Task 23: Build the static landing page and public documentation

**Files:**
- Create: landing-page/index.html
- Create: landing-page/styles.css
- Create: landing-page/assets/
- Create: docs/installation.md
- Create: docs/provider-setup.md
- Create: docs/project-workflow.md
- Create: docs/backup-restore.md
- Create: docs/troubleshooting.md
- Create: docs/security.md
- Create: docs/contributing.md
- Modify: README.md
- Create: landing-page/tests/landing-page.spec.ts

**Interfaces:**
- Landing page is static and deployable to GitHub Pages.
- All referral links are configured in one documented settings block and visibly disclosed.
- Documentation uses the product name Elisa SEO Agent and describes self-hosted operation.

- [ ] **Step 1: Write landing-page acceptance tests**

Assert presence of hero, workflow, feature sections, self-hosting explanation, optional integration distinction, installation command, GitHub CTA, referral disclosure, FAQ, and community links.

- [ ] **Step 2: Implement landing page**

Use semantic HTML, responsive CSS, accessible headings, keyboard navigation, reduced-motion support, and no runtime API dependency.

- [ ] **Step 3: Implement documentation**

Document Docker startup, local.env, multi-AI setup, optional On-Page.ai, DataForSEO, GSC, GA4, WordPress drafts, backups, pause/resume, and troubleshooting.

- [ ] **Step 4: Add demo project documentation**

Describe synthetic demo data and the first-run path without requiring external credentials.

- [ ] **Step 5: Verify public assets**

Run:

~~~bash
python3 -m http.server 4173 --directory landing-page
npx playwright test landing-page/tests/landing-page.spec.ts
~~~

Expected result: landing page acceptance tests pass at desktop and mobile viewport sizes.

---

## Task 24: Add end-to-end testing and failure-path coverage

**Files:**
- Create: tests/e2e/onboarding.spec.ts
- Create: tests/e2e/site-map.spec.ts
- Create: tests/e2e/baseline.spec.ts
- Create: tests/e2e/pause-resume.spec.ts
- Create: tests/e2e/approval-draft.spec.ts
- Create: tests/e2e/project-switching.spec.ts
- Create: tests/e2e/backup-restore.spec.ts
- Create: tests/fixtures/demo-project.json
- Create: tests/fixtures/mock-connectors.ts
- Create: playwright.config.ts

**Interfaces:**
- E2E tests run against Docker Compose with mock external connectors.
- External credentials are never required for CI.
- Each test starts with a fresh temporary DATA_ROOT.

- [ ] **Step 1: Create mock connector fixtures**

Provide deterministic DataForSEO, GSC, GA4, On-Page.ai, AI, and WordPress responses. Include success, timeout, authentication error, rate limit, and partial-result fixtures.

- [ ] **Step 2: Write onboarding E2E test**

Create a project, configure two fake AI providers, import keywords, set ranking policy, and verify checklist progression.

- [ ] **Step 3: Write discovery/baseline E2E tests**

Import a fixture sitemap, display page counts, map hierarchy, capture baseline rankings, and verify the dashboard shows baseline data.

- [ ] **Step 4: Write pause/resume E2E test**

Start a multi-batch architecture job, pause after a checkpoint, restart the worker, resume, and assert no duplicate page records.

- [ ] **Step 5: Write approval/draft E2E test**

Generate an internal-link proposal, approve it, create a WordPress draft through the mock connector, verify the draft, and assert no publish request occurred.

- [ ] **Step 6: Write switching/backup E2E tests**

Create two projects, switch between them, verify isolation, back up one project, restore it into a clean data root, and verify reports and vault files.

- [ ] **Step 7: Verify E2E suite**

Run:

~~~bash
docker compose up -d
npx playwright test
docker compose down
~~~

Expected result: all E2E tests pass without live external credentials.

---

## Task 25: Add security, accessibility, and operational verification

**Files:**
- Create: tests/security/test_secret_scan.py
- Create: tests/security/test_path_safety.py
- Create: tests/security/test_project_isolation.py
- Create: apps/web/tests/accessibility.spec.ts
- Create: scripts/check-secrets.sh
- Create: scripts/healthcheck.sh
- Create: docs/security.md
- Modify: docker-compose.yml

**Interfaces:**
- No credential value may appear in tracked files, reports, logs, or HTTP responses.
- Project paths cannot escape DATA_ROOT.
- Every API route requiring project scope validates project ownership/existence.
- Core UI routes must pass automated accessibility checks.

- [ ] **Step 1: Implement secret scan**

Search tracked files and generated reports for known credential patterns and fail on detected values.

- [ ] **Step 2: Implement path and project isolation tests**

Attempt traversal paths, cross-project IDs, malformed archive paths, and invalid project headers. Assert safe rejection.

- [ ] **Step 3: Add accessibility tests**

Use Playwright accessibility checks for onboarding, dashboard, queue, blocker panel, approvals, and page workspace.

- [ ] **Step 4: Add health checks**

Health endpoints must report service status, database connectivity, worker heartbeat, scheduler heartbeat, and optional connector status without revealing secrets.

- [ ] **Step 5: Verify operational safety**

Run:

~~~bash
bash scripts/check-secrets.sh
bash scripts/healthcheck.sh
pytest tests/security -q
npx playwright test apps/web/tests/accessibility.spec.ts
~~~

Expected result: no secret findings, no isolation failures, and accessibility checks pass.

---

## Task 26: Package, document, and hand off the full system

**Files:**
- Modify: README.md
- Modify: docs/installation.md
- Modify: docs/project-workflow.md
- Create: docs/release-checklist.md
- Create: docs/operator-runbook.md
- Create: scripts/verify-release.sh
- Create: examples/demo-config/local.env.example
- Create: examples/demo-project/README.md

**Interfaces:**
- A new operator can install from a clean checkout with Docker Compose.
- The system can run a demo project without external credentials.
- The operator can connect real services by editing local.env and using the UI.
- No Git commit is created by the implementation agent.

- [ ] **Step 1: Write the clean-install checklist**

Document exact prerequisites, Docker startup, browser URL, first-run checks, project creation, and shutdown commands.

- [ ] **Step 2: Write the operator runbook**

Document pause/resume, logs, failed jobs, stale workers, database backup, vault backup, connector testing, and safe reset of demo data.

- [ ] **Step 3: Create the release verification script**

scripts/verify-release.sh must run Compose config validation, unit tests, integration tests, E2E tests, secret scanning, landing-page tests, and backup/restore checks.

- [ ] **Step 4: Run the full verification**

Run:

~~~bash
bash scripts/verify-release.sh
~~~

Expected result: the script prints RELEASE_VERIFIED only after every required check passes.

- [ ] **Step 5: Leave the working tree uncommitted**

Do not run git commit, git push, or repository publication commands. Provide the owner with the local file changes and verification output.

---

## Final acceptance checklist

The implementing agent must not claim completion until all of these are true:

- Docker Compose starts web, API, worker, and scheduler services.
- A user can create multiple isolated projects.
- Each project receives the approved vault structure.
- Credentials are read from local configuration and are absent from database, vault, reports, logs, and exports.
- At least two AI providers can be configured and routed by task.
- Missing optional providers degrade gracefully.
- Sitemap import reports intermediate counts and preserves checkpoints.
- Site architecture identifies page types, tiers, links, and orphan candidates.
- Keywords can be pasted and imported by CSV.
- Money keywords and pages are mapped and persisted.
- Baseline rankings are captured per keyword and policy.
- Weekly snapshots compare against baseline and prior snapshots.
- GSC and optional GA4 data are normalized and reported.
- DataForSEO rank tracking is implemented behind a connector interface.
- On-Page.ai is optional and its absence is accurately shown.
- Page audits create evidence-backed checklists.
- Internal-link proposals are deduplicated and auditable.
- WordPress changes are draft-only by default.
- Approval gates work.
- Jobs can pause and resume after process restart.
- Job retries do not duplicate completed work.
- Loop-controller decisions are persisted in SQLite and the project vault.
- Dashboard shows status, blockers, and next action.
- Reports include task, reason, evidence, expected outcome, measured result, and next verification date.
- Backups exclude credentials and restore project state.
- Landing page and setup documentation are present.
- Unit, integration, E2E, security, accessibility, and release verification tests pass.
- No Git commit is created.

