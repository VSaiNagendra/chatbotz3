
import psycopg2

engine_tool_chatdb = psycopg2.connect('dbname=teamlease user=sayint host=bot.sayint.ai port=5433 password=smartinsights')
cursor=engine_tool_chatdb.cursor()
cursor.execute("select t.message from emails.analytics e,emails.tracker t where e.classes_tsv @@ to_tsquery('simple','itform') and e.msg_id=t.msg_id order by e.msg_id DESC limit 12")
result=cursor.fetchall()
count=0
f=open('itformtest','w+')
for row in result:
    count=count+1
    msg=str(row)
    msg=msg.replace("\\n"," ").replace("\\r"," ")
    msg = msg[2:-3]
    print(msg)
    if(msg=='---------- Forwarded message ---------'):
        continue
    f.write(msg+'\n')
f.close()
print(count)
"""result = connect_teamlease.execute("select  from test_train_data where classes @@ to_tsquery('simple','salaryrelease') order by id")
f=open("salaryrelease","w+")
for row in result:
    msg=str(row)
    msg=msg.replace("\\n"," ").replace("\\r"," ")
    msg = msg[2:-3]
    f.write(msg)
    f.write("\n")
f.close()

result = connect_teamlease.execute("select message from test_train_data where classes @@ to_tsquery('simple','salarybreakup') order by id")
f=open("Salarybreakup.txt","w+")
for row in result:
    msg=str(row)
    msg=msg.replace("\\n"," ").replace("\\r"," ")
    msg = msg[2:-3]
    f.write(msg)
    f.write("\n")
f.close()

result = connect_teamlease.execute("select message from test_train_data where classes @@ to_tsquery('simple','itform') order by id")
f=open("itform.txt","w+")
for row in result:
    msg = str(row)
    msg = msg.replace("\\n", " ").replace("\\r", " ")
    msg = msg[2:-3]
    f.write(msg)
    f.write("\n")
f.close()

result = connect_teamlease.execute("select message from test_train_data where classes @@ to_tsquery('simple','form16') order by id")
f=open("form16.txt","w+")
for row in result:
    msg=str(row)
    msg=msg.replace("\\n"," ").replace("\\r"," ")
    msg=msg[2:-3]
    f.write(msg)
    f.write("\n")
f.close()"""



