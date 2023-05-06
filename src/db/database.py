from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, DateTime,func, relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), unique=True, nullable=False)
    last_name = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    public_key = Column(LargeBinary, unique=False, nullable=True)
    signer_key = Column(LargeBinary, unique=False, nullable=True)
    private_key = Column(LargeBinary, unique=False, nullable=True)
    password_hash = Column(String(128), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    files = relationship('File', backref='owner', lazy=True)

class Database:
    def __init__(self, db_file):
        self.engine = create_engine(f'sqlite:///{db_file}')
        self.session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)

    def create_user(self, username, password, full_name, email):
        user = User(username=username, password=password, full_name=full_name, email=email)
        self.session.add(user)
        self.session.commit()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def authenticate_user(self, username, password):
        user = self.get_user_by_username(username)
        if user is None:
            return False
        return user.password == password

    def close(self):
        self.session.close()
