# PowerShell script to start the FastAPI server
Write-Host "Starting FastAPI Server..." -ForegroundColor Green
Write-Host ""

Set-Location $PSScriptRoot

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "Warning: .env file not found. Creating template..." -ForegroundColor Yellow
    "GITHUB_TOKEN=your_github_token_here" | Out-File -FilePath ".env" -Encoding utf8
    Write-Host "Please update the .env file with your actual GitHub token." -ForegroundColor Yellow
    Write-Host ""
}

# Start the server
Write-Host "Server will be available at:" -ForegroundColor Cyan
Write-Host "  - http://localhost:8000/" -ForegroundColor White
Write-Host "  - http://localhost:8000/docs (API Documentation)" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

