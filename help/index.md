# xes_py文档
## xes_py 是什么

本软件是为了修复xes编程助手修改管版Python而出的补丁工具，建议用xes编程和管版Python (anaconda)进行编程的玩家制作的工具

## 怎么使用
1. 从官网下载`xes_py.exe`
2. 从xes编程官网下载编程助手
3. 安装xes编程助手
4. 编程助手安装完成后双击`xes_py.exe`
5. 工具开始搜索xes编程助手安装目录，可能加载时间会有点长
6. 提示寻找成功后会自动绿化，然后提示成功，关闭窗口即可

tip: 建议将本文件放在`启动`文件夹，每次开机替换pip.inf文件，完美解决xes编程助手重装的问题

## 原理
### 这个东西之前网上是`没有`的，我是原创
1. xes编程助手流氓的主要原因就是把Python包和官版Python包装在一起
2. 但是xes的Python安装的包和官网版本不一样，所以数据是不相同的
3. 但是我发现xes为了加速，将pip的包源设为了xes的包源
4. 本工具将会找到pip.inf，将其中的包源修改为[https://pypi.org/simple/](https://pypi.org/simple/)