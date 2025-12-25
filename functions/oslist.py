# framework example
# it retrieves the operating system names written in the database
import sqlite3
import os

def list(databasefile):
  oslist_db = sqlite3.connect("otherfiles/"+databasefile)
  crs = oslist_db.cursor()
  data = crs.execute("SELECT id, oslist FROM oslist")
  return data
