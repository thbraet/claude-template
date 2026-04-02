# MCP Servers Catalog for Data Science

Available MCP (Model Context Protocol) servers relevant to data science workflows.

## Included in Template

These servers are pre-configured in `.mcp.json`:

| Server | Package | Description |
|---|---|---|
| **GitLab** | `@modelcontextprotocol/server-gitlab` | GitLab API access (issues, MRs, pipelines) |
| **PostgreSQL** | `@modelcontextprotocol/server-postgres` | Read-only database access with schema inspection |
| **Notion** | `@notionhq/notion-mcp-server` | Search, read, and write Notion pages and databases |

## Additional Servers by Category

### Databases & Data Warehouses

| Server | Package | Type | Use Case |
|---|---|---|---|
| **DuckDB** | `mcp-server-duckdb` (PyPI) | Community | Analytical queries on local files (Parquet, CSV) |
| **SQLite** | `mcp-server-sqlite` (PyPI) | Community | Local database for analysis |
| **MySQL** | `mcp-server-mysql` (npm) | Community | MySQL database access |
| **Snowflake** | `Snowflake-Labs/mcp` | Official (Snowflake) | Cortex AI, SQL orchestration |
| **BigQuery** | `LucasHild/mcp-server-bigquery` | Community | Google BigQuery access |
| **Databricks** | `markov-kernel/databricks-mcp` | Community | Databricks data access |
| **ClickHouse** | `ClickHouse/mcp-clickhouse` | Official (ClickHouse) | OLAP analytics |

### Cloud & Infrastructure

| Server | Package | Type | Use Case |
|---|---|---|---|
| **AWS Suite** | `awslabs/mcp` | Official (AWS) | S3, Redshift, SageMaker, and 65+ more |

### ML & Experiment Tracking

| Server | Package | Type | Use Case |
|---|---|---|---|
| **Weights & Biases** | `wandb/wandb-mcp-server` | Official (W&B) | Experiment tracking data |

### Data Tools

| Server | Package | Type | Use Case |
|---|---|---|---|
| **Filesystem** | `@modelcontextprotocol/server-filesystem` | Official (MCP) | Secure file access for data/reports/models directories |
| **Fetch** | `mcp-server-fetch` (PyPI) | Official (MCP) | Fetch web content (APIs, documentation) |
| **Jupyter** | `ihrpr/mcp-server-jupyter` | Community | Notebook interaction |
| **DataHub** | `acryldata/mcp-server-datahub` | Official (DataHub) | Data catalog, lineage |
| **Chroma** | `chroma-core/chroma-mcp` | Official (Chroma) | Vector search, embeddings |

## Adding a Server

Add to `.mcp.json`:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "package-name"],
      "env": {
        "API_KEY": "${YOUR_API_KEY}"
      }
    }
  }
}
```

For Python-based servers, use `uvx` instead of `npx`:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "uvx",
      "args": ["package-name", "--option", "value"]
    }
  }
}
```

## Environment Variables

MCP servers use `${VAR_NAME}` syntax to reference environment variables. Set these in your shell or `.env` file (never commit `.env`).

Required variables for template servers:
| Variable | Server | Description |
|---|---|---|
| `GITLAB_TOKEN` | GitLab | Personal access token |
| `DATABASE_URL` | PostgreSQL | Connection string |
| `NOTION_TOKEN` | Notion | Notion integration token |
