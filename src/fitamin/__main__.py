import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Fitamin')


def main():
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)


if __name__ == '__main__':
    main()
