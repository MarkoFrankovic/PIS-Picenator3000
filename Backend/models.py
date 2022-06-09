from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String

Base = declarative_base()

class Bambus(Base):
    """Bambus pice"""

    __tablename__ = "bambus"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Jaeger(Base):
    """Jaeger pice"""

    __tablename__ = "jaeger"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Voda(Base):
    """Voda pice"""

    __tablename__ = "voda"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Gin(Base):
    """Gin pice"""

    __tablename__ = "gin"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Travarica(Base):
    """Travarica pice"""

    __tablename__ = "travarica"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Vodka(Base):
    """Vodka pice"""

    __tablename__ = "vodka"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Jack(Base):
    """Jack pice"""

    __tablename__ = "jack"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Merlot(Base):
    """Merlot pice"""

    __tablename__ = "merlot"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)

class Stock(Base):
    """Stock pice"""

    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ime = Column(String(255), unique=True, nullable=False)
    ocjena = Column(Integer, nullable=False)
    url = Column(Text)


