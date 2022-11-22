import pandas as pd
path='./data/data_git.csv'
data=pd.read_csv(path,sep=",").values[:,1:]
version=0
print("this is version_"+str(version))
print(data[0:version])
print('xiugai')
print('study')
print('dev_branch_0_修改完成100')
