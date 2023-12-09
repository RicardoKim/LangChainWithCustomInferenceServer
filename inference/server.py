import uvicorn
from fastapi import FastAPI
from model.QueryRequest import QueryRequest

app = FastAPI()


@app.get("/query")
def queryRequest(queryRequest: QueryRequest):
    if "Cypher" in queryRequest.query:
        return{"assistant" : "MATCH p=()-[r:ACTED_IN]->() RETURN p LIMIT 25"}
    return {"assistant": "Hello World" + queryRequest.query}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)