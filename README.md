# pySrun4k
## 简介
pySrun4k是一个模仿Srun4k认证客户端协议，用Python3实现的认证客户端。

实现了登录，检查在线状态，登出当前终端，登出所有终端功能。

## 依赖

requests

```pip install requests```

## 用法（Login.py）

可以直接通过命令行调用

### 登录
```python Login.py login <username> <password>```

或交互式使用，避免暴露密码

```python Login.py login # 交互式用户名和密码输入```

### 检查在线状态
```python Login.py check_online```

### 登出当前终端
```python Login.py logout <username>```

### 登出所有终端
```python Login.py logout_all <username> <password>```

## API

### 登录

```srun4k.do_login(username,pwd,mbytes=0,minutes=0)```

### 检查在线状态

```srun4k.check_online()```

### 登出当前终端

```srun4k.do_logout(username)```

### 登出所有终端

```srun4k.force_logout(username,password)```


## Docker版-自动监控保持在线
```bash
cd docker/
. env.sh user password
build #only once
start
```
后续可以改main_login_regular.py 根据check_online返回的ip地址实现ip更新git

## 原版
首先打开`main_login_regular.py`修改用户名和密码
```python
python main_login_regular.py # 适用于长期自动登录
```
