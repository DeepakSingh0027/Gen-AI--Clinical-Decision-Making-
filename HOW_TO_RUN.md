# How to Run the Chatbox Application

## Quick Start Guide

### Step 1: Start the Backend Server

Open a terminal and navigate to the server directory:

```bash
cd server
```

Then start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Or use the provided startup scripts:**
- **Windows Batch:** Double-click `start_server.bat`
- **PowerShell:** Run `.\start_server.ps1`

### Step 2: Access the Chatbox

Once the server is running, open your web browser and go to:

**🌐 http://localhost:8000/**

or

**🌐 http://localhost:8000/chatbox**

You should see a beautiful chat interface where you can:
- Ask medical questions
- Get AI-powered clinical decision support
- Have a conversation with the assistant

### Step 3: Configure Your API Token (Important!)

Before the chatbox can work properly, you need to set up your GitHub token:

1. Open `server/.env` file
2. Replace `your_github_token_here` with your actual GitHub token
3. Save the file
4. Restart the server (if it's running)

## Complete Setup Instructions

### Prerequisites
- Python 3.8 or higher
- All dependencies installed (run `pip install -r server/requirements.txt`)

### Environment Setup

1. **Create/Update `.env` file** in the `server` directory:
   ```
   GITHUB_TOKEN=your_actual_github_token_here
   ```

2. **Install dependencies** (if not already done):
   ```bash
   cd server
   pip install -r requirements.txt
   ```

### Running the Application

#### Option 1: Manual Start
```bash
cd server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Option 2: Using Startup Scripts
- **Windows:** `server\start_server.bat`
- **PowerShell:** `server\start_server.ps1`

#### Option 3: Direct Python
```bash
cd server
python -m uvicorn app.main:app --reload
```

## Access Points

Once running, you can access:

- **Chatbox Interface:** http://localhost:8000/ or http://localhost:8000/chatbox
- **API Documentation:** http://localhost:8000/docs
- **API Endpoint:** http://localhost:8000/chat/ (POST)

## Features

✅ Beautiful, modern chat interface
✅ Real-time messaging
✅ Medical question answering
✅ Clinical decision support
✅ Responsive design
✅ Error handling

## Troubleshooting

### Server won't start
- Check if port 8000 is already in use
- Verify Python and dependencies are installed
- Check for syntax errors in the code

### Chatbox shows errors
- Make sure the server is running
- Verify your `GITHUB_TOKEN` is set correctly in `server/.env`
- Check browser console for errors (F12)

### API returns errors
- Verify the `.env` file exists in the `server` directory
- Ensure `GITHUB_TOKEN` has a valid value (not the placeholder)
- Check server logs for detailed error messages

## Testing the Chatbox

1. Start the server
2. Open http://localhost:8000/ in your browser
3. Type a medical question like:
   - "What are the symptoms of diabetes?"
   - "How do I treat a headache?"
   - "What should I know about hypertension?"
4. Press Enter or click Send
5. Wait for the AI response

Enjoy your Clinical Decision Making Assistant! 🏥

