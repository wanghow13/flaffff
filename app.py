from flask import Flask, render_template
import poplib
from email.parser import Parser
app = Flask(__name__)

def get_emails():

    pop_server = poplib.POP3('pop.qq.com', 110)
    pop_server.user('1726909232@qq.com')
    pop_server.pass_('asejjqtxnhxneefb')

    num_emails = len(pop_server.list()[1])

    emails = []

    for i in range(1, num_emails + 1):
        _, lines, _ = pop_server.retr(i)
        email_content = b'\r\n'.join(lines).decode('utf-8')
        email = Parser().parsestr(email_content)
        emails.append({
            'subject': email['subject'],
            'from': email['from'],
            'date': email['date']
        })

    pop_server.quit()

    return emails




@app.route('/')
def show_list():
    # return "全部主机列表"
    # thelist = [1,2,3,4,5]
    thelist = [{"id": 1, "name": "cloud1", "url": "/detail/1"},
               {"id": 2, "name": "cloud2", "url": "/detail/2"},
               {"id": 3, "name": "cloud3", "url": "/detail/3"},
               {"id": 4, "name": "cloud4", "url": "/detail/4"},
               {"id": 5, "name": "cloud5", "url": "/detail/5"},
               {"id": 6, "name": "cloud6", "url": "/detail/6"},
               {"id": 7, "name": "cloud7", "url": "/detail/7"},
               {"id": 8, "name": "cloud8", "url": "/detail/7"},
               {"id": 9, "name": "cloud9", "url": "/detail/7"},
               {"id": 10, "name": "cloud10", "url": "/detail/7"},
               {"id": 11, "name": "cloud11", "url": "/detail/7"},
               {"id": 12, "name": "cloud12", "url": "/detail/7"},

               ]

    return render_template('list.html', mylist=thelist)

@app.route('/email-list')
def index():
    emails = get_emails()
    return render_template('email-list.html', mylist=emails)
# def show_email_list():
#     thelist =[{"sender": "zhangsan@qq.com",
#                "receiver":"maxin5452@qq.com",
#                "subject":"this is a test mail 1"
#                },
#               {"sender": "zhangsan@qq.com",
#                "receiver":"maxin5452@qq.com",
#                "subject":"this is a test mail 2"
#                },
#               {"sender": "zhangsan@qq.com",
#                "receiver":"maxin5452@qq.com",
#                "subject":"this is a test mail3"
#                },
#         ]
    #return str(thelist)




if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port="5001", debug="True")
