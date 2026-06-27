# Planing Lab 共享文件夹

## 目前的使用共享文件的方法是重新创建一个新容器挂载到共享文件夹上，将原容器的数据迁移到新容器上。参考[原服务器到有挂载共享文件的迁移](https://github.com/PLANING-lab/server/blob/main/%E5%8E%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%88%B0%E6%9C%89%E6%8C%82%E8%BD%BD%E5%85%B1%E4%BA%AB%E6%96%87%E4%BB%B6%E7%9A%84%E8%BF%81%E7%A7%BB.md)

## 为了大家更好使用共享文件夹，建立以下规则：
1. 大家不要主动去删除共享文件里的文件
2. 大家可以自行在文件夹shared_planing/里添加可能需要重复使用的文件。在添加时，请尽量细粒度的标记并且遵从子文件夹中README的详细命名规则。同时请在下表中，标记姓名和文件内容。如果文件出现错误，或者版本过旧等问题，可以联系你修改或删除。
3. 如在使用过程中发现有问题，如无法运行，也可以在下表中添加问题。
PS: 如果有其他需要补充的，及时更新优化进行调整。

## 文件夹列表
- cuda/ # 用于配置cuda环境
- LLM_model/ # 存放各个大模型
- pyg/ # 用于配置pyg环境


## 添加列表
e.g.
- shared_planing/LLM_model/Ministral-8B-Instruct-2410/ # 虞健翔
- shared_planing/LLM_model/Mistral-7B-Instruct-v0.3/ # 虞健翔


## Error
e.g.
- shared_planing/LLM_model/Qwen2_5-7b-Instruct/ # 虞健翔 模型运行出错，llama3.1 需要hugging face 账户认证
