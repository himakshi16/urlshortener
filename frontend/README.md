# Frontend (React + Vite)

Development:

1. Install deps (from `frontend/`):

```bash
npm install
```

2. Run dev server (Vite):

```bash
npm run dev
```

This runs the React dev server on port 3000 and proxies `/api` (see `vite.config.js`). The React app uses the existing Django endpoints (`/shorten/`, `/generate-qr/`, `/s/<code>/`, `/qr/<code>/`).

Production build:

```bash
npm run build
```

You can serve the built files with any static server or integrate the build output into Django's static files pipeline.
