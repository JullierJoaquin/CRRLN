import os
from fastapi import Request
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, auth

cred_path = os.getenv("FIREBASE_CREDENTIALS")
if not firebase_admin._apps and cred_path:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)


async def verify_token(request: Request):
    body = await request.json()
    id_token = body.get("idToken")

    try:
        decoded_token = auth.verify_id_token(id_token)
        request.session["user"] = {
            "uid": decoded_token["uid"],
            "email": decoded_token.get("email")
        }
        return JSONResponse(content={"message": "Token válido"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": "Token inválido", "details": str(e)}, status_code=401)
