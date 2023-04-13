from __future__ import annotations
from dotenv import load_dotenv
load_dotenv()

class Config(object):
	def __init__(self,data:str):
		self.data = data
	def __call__(self):
		raise "cannot instaniate directly,please using methode create..."


