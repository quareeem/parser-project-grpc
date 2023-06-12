from sqlalchemy import Inspector, create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///shopkz_products.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String)
    articul = Column(String)
    price = Column(String, default="Нет в наличии")
    description = Column(Text)



def insert_into_table(data, table_name):
    class ProductTable(BaseModel):
        __tablename__ = table_name
        __table_args__ = {'extend_existing': True}

    session = Session()
    inspector = Inspector.from_engine(engine)

    if table_name not in inspector.get_table_names():
        Base.metadata.create_all(engine)

    
    new_record = ProductTable(
        name=data['name'], 
        articul=data['articul'], 
        price=data['price'],
        description=data['description'],
        )

    session.add(new_record)
    session.commit()
    print("[ √ ]  Saved to database: ", data['name'])
