# Gen-AI Clinical Decision Making

A FastAPI-based application for clinical decision-making assistance using Azure AI Inference.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A GitHub token for Azure AI Inference API

## Setup Instructions

### 1. Install Dependencies

Navigate to the `server` directory and install the required packages:

```bash
cd server
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the `server` directory with your GitHub token:

```bash
# In the server directory
echo GITHUB_TOKEN=your_github_token_here > .env
```

Or manually create a `.env` file with:
```
GITHUB_TOKEN=your_github_token_here
```

**Note:** Replace `your_github_token_here` with your actual GitHub token for the Azure AI Inference API.

### 3. Run the Server

From the `server` directory, run:

```bash
uvicorn app.main:app --reload
```

Or if you're in the project root:

```bash
cd server
uvicorn app.main:app --reload
```

The server will start on `http://localhost:8000` by default.

### 4. Access the Application

- **API Base URL:** `http://localhost:8000`
- **API Documentation (Swagger UI):** `http://localhost:8000/docs`
- **Alternative API Docs (ReDoc):** `http://localhost:8000/redoc`
- **Home Endpoint:** `http://localhost:8000/` - Returns a status message

## API Endpoints

### POST `/chat/`
Send a chat message to the LLM for medical assistance.

**Request Body:**
```json
{
  "message": "What are the symptoms of diabetes?"
}
```

**Response:**
```json
{
  "response": "LLM response here..."
}
```

## Project Structure

```
.
├── server/
│   ├── app/
│   │   ├── main.py          # FastAPI application entry point
│   │   ├── routes/          # API routes
│   │   ├── services/        # Business logic (LLM service)
│   │   ├── schemas/         # Pydantic models
│   │   └── models/          # Data models
│   └── requirements.txt     # Python dependencies
└── frontend/
    └── front_end.py         # Frontend (currently empty)
```

## Development

To run with auto-reload (development mode):
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

1. **Module not found errors:** Make sure you've installed all dependencies from `requirements.txt`
2. **Token errors:** Verify your `.env` file exists and contains a valid `GITHUB_TOKEN`
3. **Port already in use:** Change the port using `--port 8001` (or any available port)

