#coding:utf-8
from sqlalchemy import create_engine,MetaData,Table,select

engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/blogdb')
metadata = MetaData()
metadata.bind = engine
auth_permission = Table('auth_permission',metadata,autoload = True)

# 若codename存在，返回code,code不存在返回空值
def query_code(codename):
        info = {'name':'','codename':''}
        s = select([auth_permission.c.codename, auth_permission.c.name, ]).where(auth_permission.c.codename == codename)
        codename_query = engine.execute(s)
        for row in codename_query:
            info['codename'] = row[0]
            info['name'] = row[1]
        codename_query.close()
        return info

# 若name存在，返回name,name不存在返回空值
def query_name(name):
        info = {'name':''}
        s = select([auth_permission.c.name,]).where(auth_permission.c.name == name)
        codename_query = engine.execute(s)
        for row in codename_query:
            info['name'] = row[0]
        codename_query.close()
        return info
#修改权限  
def updata(codename,name):
    s = auth_permission.update().where(auth_permission.c.codename == codename).values(name=name,codename=codename)
    c = engine.execute(s)
    c.close()
# 添加权限
def add(codename,name,content_type_id):
    s = auth_permission.insert().values(name=name,codename=codename,content_type_id=content_type_id)
    c = engine.execute(s)
    c.close()

# 删除权限
def delete(codename):
    s = auth_permission.delete().where(auth_permission.c.codename == codename)
    c = engine.execute(s)
    c.close()

# 查询权限
def query():
    result = []    
    s = select([auth_permission.c.name,auth_permission.c.codename,auth_permission.c.content_type_id]).order_by('id')
    c = engine.execute(s)
    for row in c:
        info = {}
        info['name'] = row[0]
        info['codename'] = row[1]
        info['content_type_id'] = row[2]
        result.append(info)
    c.close()
    return result

