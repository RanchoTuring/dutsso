import sys
sys.path.append('.')
##################### 以上两行只是为了方便开发，实际不需要 #######################

import dutsso

# 查询招聘信息
date = "2018-09-10"
u = dutsso.User()
jobs = u.get_job(search_date=date)      # 如不填默认获取当天的
print("———— %s招聘信息获取如下 ————" % date)
for job in jobs:
    print(job)
