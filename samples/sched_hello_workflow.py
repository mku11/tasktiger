from tasktiger import TaskTiger
import tasks

tiger = TaskTiger()

# 1. simple workflow
# task1 = tiger.delay(tasks.hello, args=("group1", 5))
# task2 = tiger.delay(tasks.hello, args=("group2", 5), depends=[task1.id])


# 2. multilevel workflow
# LVL 1
group1 = []
tasks_num = 4
for i in range(tasks_num):
    group1.append(tiger.delay(tasks.hello, args=("group1:" + str(i), 20)))
group2 = []
# LVL 2
# single deps
group2.append(tiger.delay(tasks.hello, args=("group2:0", 5), depends=[group1[0].id]))
group2.append(tiger.delay(tasks.hello, args=("group2:1", 7), depends=[group1[1].id]))
# multiple deps
deps = list(map(lambda x: x.id, [group1[2], group1[3]]))
group2.append(tiger.delay(tasks.hello, args=("group2:2", 4), depends=deps))
# no deps
group2.append(tiger.delay(tasks.hello, args=("group2:3", 2)))
# LVL 3
deps3 = list(map(lambda x: x.id, group2))
tiger.delay(tasks.hello, args=("group3:0", 4), depends=deps3)


# 3. unknown dep (always waiting)
# tiger.delay(tasks.hello, args=("nodep",5), depends=["111"])
