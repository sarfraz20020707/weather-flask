import json
import requests
from fpdf import FPDF
from flask import flask,request,render_template 
API_KEY = "YOUR API KEY"
API_HOST = "weatherapi-com.p.rapidapi.com"
API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

app = Flask(__name__)