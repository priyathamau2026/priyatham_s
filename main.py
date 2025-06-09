from fastapi import FastAPI
import root
import Books


app = FastAPI()

# Include routes from other files (modular structure)
app.include_router(root.router)
app.include_router(Books.router)