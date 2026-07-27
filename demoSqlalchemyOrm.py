from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#引擎/会话/模型

#引擎：连接数据库
engine = create_engine("mysql+pymysql://root:yinmh900213@localhost:3306/ai_chat_app?charset=utf8mb4", echo=False)

#会话工厂【增删改查的上下文环境】
sessionLocal = sessionmaker(bind=engine)

#模型基类 其他模型继承该基类
base = declarative_base()



from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(base):
    __tablename__ = "users_1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    ps = Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # 建立对话记录的关系（方便后续通过 user.conversations直接获取）
    conversations = relationship("Conversation", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

class Conversation(base):
    __tablename__ = "conversations_1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users_1.id", ondelete="CASCADE"), nullable=False)
    role = Column(Enum("users", "assistant"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="conversations")

    def __repr__(self):
        return f"<Conversation(id={self.id}, role={self.role})>"

# 创建所有表：只需执行一次
base.metadata.create_all(engine)


