from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending') # pending, approved, rejected

    def __repr__(self):
        return f'<Event {self.title}>'

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) # Optional (could be anonymous login attempt)
    action = db.Column(db.String(100), nullable=False)
    target = db.Column(db.String(100)) # e.g. "Event ID 45" or "User Login"
    ip_address = db.Column(db.String(45)) # IPv6 supports up to 45 chars
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # We can automatically set the IP locally or from proxy headers when created:
    # Example logic using our new utility:
    def __init__(self, **kwargs):
        super(AuditLog, self).__init__(**kwargs)
        if 'ip_address' not in kwargs:
            from app.utils.ip_utils import extract_real_ip
            self.ip_address = extract_real_ip()

    def __repr__(self):
        return f'<AuditLog {self.action} by User {self.user_id} @ {self.ip_address}>'
