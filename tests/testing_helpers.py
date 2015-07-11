from flask import url_for

def login(self):
    self.client.post(
        url_for('users.login'),
        data=dict(username="admin", password="password"),
        follow_redirects=True
        )
