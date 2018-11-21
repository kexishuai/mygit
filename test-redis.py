import redis


# 连接redis数据库
r = redis.StrictRedis('localhost', 6379)

# 存
r.set('name', '张三')

# 取
res = r.get('name')
print(res.decode('utf-8'))


# r.rpush('cars', '比亚迪', '特斯拉', '兰博基尼')
res = r.lrange('cars', 0, -1)
# print(res)
for r in res:
    print(r.decode())



