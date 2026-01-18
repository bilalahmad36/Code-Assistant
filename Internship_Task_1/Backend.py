from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()


class UserLogin(BaseModel):
    username: str
    password: str


@app.post("/process_log/")
async def process_log(entry: LogEntry):
    try:
        result = graph.invoke({"Log_entry": entry.log})
        label = result.get("label", "").lower()
        # if label == "critical":
        db = SessionLocal()
        db_log = LOG_ENTRIES(Log=entry.log, Label=label)
        db.add(db_log)
        db.commit()
        db.close()
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}