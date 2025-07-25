from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


def dummy_classifier(image_bytes):
    labels = ['Akash', 'Amulya', 'Prajwal', 'Prashanth']
    return random.choice(labels)


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    print(f"file recieved {file.filename}")
    prediction = dummy_classifier(contents)
    return {"filename": file.filename,
            "size_kb": len(contents)//1024,
            "prediction": prediction}
