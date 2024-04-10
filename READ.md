# Deploy instructions
1. Install python 3.9.6^
2. Install pip or pip3 (package manager for python)
3. fill '.env'
4. run 'make build'
5. run 'make start'

### .env example
```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=
OPENAI_API_KEY=
MONGO_DB_URL=DemoChat?retryWrites=true"
PROJECT_DB_NAME="DemoChat"
SERVER_PORT="8000"
SERVER_HOST="127.0.0.1"
```
