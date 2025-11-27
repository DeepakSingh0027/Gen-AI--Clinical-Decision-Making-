# Quick Test Guide

## How to Run Tests

### Option 1: Automated Test Runner (Recommended)

1. **Start the server** (if not already running):
   ```bash
   cd server
   python -m uvicorn app.main:app --reload
   ```

2. **Run the test script** (in a new terminal):
   ```bash
   cd server
   python test_runner.py
   ```

3. **View results**:
   - Results displayed in terminal
   - Detailed results saved to `test_results.json`

### Option 2: Manual Testing via Browser

1. **Open the chatbox**:
   - Navigate to http://localhost:8000/

2. **Test these scenarios**:
   - Type: "What are the symptoms of diabetes?"
   - Type: "What is hypertension?"
   - Type: "How can I prevent heart disease?"
   - Type: "What are the signs of a heart attack?"

3. **Verify**:
   - Messages appear correctly
   - Responses are received
   - Error handling works (try with server stopped)

### Option 3: API Testing with curl/Postman

**Using curl:**
```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the symptoms of diabetes?"}'
```

**Using Postman:**
- Method: POST
- URL: http://localhost:8000/chat/
- Headers: Content-Type: application/json
- Body (raw JSON):
  ```json
  {
    "message": "What are the symptoms of diabetes?"
  }
  ```

## Test Scenarios to Demonstrate

### 1. Basic Functionality
- ✅ Server starts and responds
- ✅ Chatbox loads in browser
- ✅ Messages can be sent
- ✅ Responses are received

### 2. Medical Questions
- ✅ Symptom queries
- ✅ Disease information
- ✅ Treatment options
- ✅ Preventive care

### 3. Error Handling
- ✅ Invalid requests handled
- ✅ Network errors handled
- ✅ Token errors handled
- ✅ User-friendly error messages

### 4. Performance
- ✅ Response time < 10 seconds
- ✅ Multiple requests handled
- ✅ Server stability

## Expected Test Results

When running `test_runner.py`, you should see:

```
================================================================================
CLINICAL DECISION MAKING APPLICATION - TEST EXECUTION
================================================================================
Start Time: 2024-XX-XX XX:XX:XX
Base URL: http://localhost:8000
================================================================================

✓ Server is running

Executing 9 test cases...
================================================================================

[1/9] Running test...

[TC-004] Diabetes Symptoms Query
Category: Medical Question
Input: What are the symptoms of diabetes?
✓ Status: PASS
  Response Time: 2.34s
  Keywords Found: 3/4
  Found: thirst, urination, blood sugar
  Response Preview: diabetes is a condition where blood sugar levels are high...

...

================================================================================
TEST EXECUTION SUMMARY
================================================================================
Total Tests: 9
✓ Passed: 8
⚠ Partial: 1
✗ Failed: 0
Success Rate: 88.9%

Performance Metrics:
  Average Response Time: 2.45s
  Maximum Response Time: 4.12s
  Minimum Response Time: 1.89s
================================================================================
```

## Key Test Cases to Show Your Teacher

1. **TC-004: Diabetes Symptoms** - Shows medical question handling
2. **TC-009: Heart Attack Signs** - Shows emergency guidance
3. **TC-016: Valid API Request** - Shows API integration
4. **TC-031: Medical Accuracy** - Shows response quality

## Tips for Presentation

1. **Start with the methodology.txt** - Explain the architecture
2. **Show the test cases** - Demonstrate comprehensive testing
3. **Run live tests** - Execute test_runner.py during presentation
4. **Show the chatbox** - Demonstrate user interface
5. **Explain the flow** - Walk through data flow from user to AI and back

## Troubleshooting Tests

**If tests fail:**
- Check server is running
- Verify GITHUB_TOKEN is set correctly
- Check network connection
- Review error messages in test output

**If response times are slow:**
- Normal: 2-5 seconds per request
- Check API rate limits
- Verify token is valid

