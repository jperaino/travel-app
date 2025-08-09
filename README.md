# Travel App

Full-stack web application built with React + TypeScript frontend and Python FastAPI backend.

## Tech Stack

- **Frontend**: React, TypeScript, React Query, shadcn/ui (using pnpm)
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Database**: PostgreSQL with Alembic migrations
- **Authentication**: JWT tokens
- **Development**: Docker Compose
- **Deployment**: Vercel (frontend), Railway/Render (backend + database)

## Project Structure

```
travel-app/
├── frontend/          # React TypeScript application
├── backend/           # FastAPI application
├── docker-compose.yml # Local development environment
└── README.md
```

## Getting Started

1. Clone the repository
2. Copy environment files and configure variables
3. Run with Docker Compose: `docker-compose up`

See `IMPLEMENTATION_CHECKLIST.md` for detailed setup progress.
