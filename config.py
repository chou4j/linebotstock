from __init__ import app

app.update_config({
  'HOST': '127.0.0.1',
  'PORT': 5000,
  'DEBUG': True,
  'WORKERS': 4,
  'DATABASE_CONFIG': '{"host":"localhost","port":5000,"user":"postgres","password":"50770329","dbname":"Test-Linebot"}',
  'PROJECT_PATH': 'D:\\users_env\\peanut\\taipei-heo-linebot',
  'SECRET_KEY': '50770329'
})