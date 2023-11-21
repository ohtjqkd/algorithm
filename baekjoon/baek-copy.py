import shutil
import time
import requests
import os
from pydantic import BaseModel
from bs4 import BeautifulSoup

class Title(BaseModel):
    language: str
    languageDisplayName: str
    title: str
    isOriginal: bool

class Problem(BaseModel):
    problemId: int
    titleKo: str
    titles: list[Title]
    isSolvable: bool
    isPartial: bool
    acceptedUserCount: int
    level: int
    votedUserCount: int
    sprout: bool
    givesNoRating: bool
    isLevelLocked: bool
    averageTries: float
    official: bool

class JsonData(BaseModel):
    data: list[Problem]

def convert_level(level: int) -> str:
  if 0 < level <= 5:
    return 'bronze'
  elif 5 < level <= 10:
    return 'silver'
  elif 10 < level <= 15:
    return 'gold'
  elif 15 < level <= 20:
    return 'platinum'
  elif 20 < level <= 25:
    return 'diamond'
  elif 25 < level <= 30:
    return 'ruby'
  else:
    return 'unknown'

def copy_file(fn: str, ext: str, tier: str):
  try:
    if str(fn) not in os.listdir(f'./{tier}'):
      os.mkdir(f'./{tier}/{fn}')
    shutil.move(f'{fn}.{ext}', f'./{tier}/{fn}/{fn}.{ext}')
  except Exception as e:
    print(e)

def get_problem_info(fn: str):
  url = f'https://solved.ac/api/v3/problem/lookup?problemIds={fn}'
  res = requests.get(url)
  problems = res.json()
  parsed_problems = [Problem(**problem) for problem in problems]
  if problems == []:
    raise Exception('No problem found')
  return convert_level(parsed_problems[0].level)

file_list = os.listdir('.')
target_list = []
for f in file_list:
  if os.path.isfile(f):
    file_name, ext = f.split('.')
    try:
      int(file_name)
      copy_file(file_name, ext, get_problem_info(file_name))
    except Exception as e:
      continue
    time.sleep(1)
