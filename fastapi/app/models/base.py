from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, Integer, DateTime, text


class MixinModel(object):
    id = Column(Integer(unsigned=True), primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
