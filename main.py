import datetime 


F = open(r'.\result\status.log', 'a')

F.write(f'{datetime.datetime.now()} - The script started running \n')


# try:
#     SOME_SECRET = os.environ["SOME_SECRET"]
#     logging.info(f"Token value: {SOME_SECRET}")
# except KeyError:
#     SOME_SECRET = "Token not available!"
  
