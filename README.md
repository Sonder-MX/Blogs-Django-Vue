# 个人博客(Django4+Vue3)

👉[原教程传送](https://www.dusaiphoto.com/article/103/).

## 预览

![home](./images/home.jpg)

## 环境配置

1. [安装 Pyhton](https://www.python.org/) (version >= 3.10)

   - 安装依赖
   - `pip install -r requirements.txt`
   - 或者 `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

2. [安装 nodejs](https://nodejs.org/en/) (version >= 18.14.0)

   - npm install -g @vue/cli

## 快速开始

### 准备

1. 进入 [blog_dv](/blog_dv) 文件夹下，依次执行以下命令，完成数据库的迁移(使用 sqlite 数据库)：

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

2. 创建超级用户：

   ```shell
   python manage.py createsuperuser  # 按提示创建超级用户
   ```

3. 进入 [frontend](/frontend) 文件夹下，执行以下命令：

   ```shell
   npm install
   ```

### 启动

1. 进入 blog_dv 目录下，打开终端输入：`python manage.py runserver`
2. 进入 frontend 目录下，打开一个新的终端：`npm run dev`
3. 打开浏览器，输入地址：http://localhost:8000/admin/ 进入后台管理
4. http://localhost:9000 进入客户端
5. 完成！
