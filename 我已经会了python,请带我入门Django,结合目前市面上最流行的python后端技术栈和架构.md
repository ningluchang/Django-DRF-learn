---

# 现代前后端分离架构下的 Django 学习路线（基于 REST API）

---
## 2. Django 入门与基础（针对API开发）

### 2.1 Django项目与应用结构

- 创建Django项目，理解项目与App划分
- 熟悉项目配置文件（`settings.py`），添加第三方库配置
- 理解`manage.py`命令

（对应Spring Boot：项目结构、`application.yml`配置、启动类）

### 2.2 Django模型设计（数据库与业务模型）

- 创建模型类（类似Spring Boot实体类）
- 迁移数据库和数据同步（`makemigrations`、`migrate`）
- ORM基础操作（增删改查）
- 使用Shell调试ORM（`python manage.py shell`）

### 2.3 编写REST API — Django REST Framework (DRF)

- 安装并配置 DRF（`djangorestframework`）
- 创建序列化器（Serializer）把模型转换为JSON（类似Spring Boot的DTO）
- 编写基于函数视图或类视图的API端点
- 使用URL路由配置API路径
- 结合ViewSet和Router实现自动路由

（对应Spring Boot的`@RestController`，Spring Data的DTO，Spring MVC路由）

### 2.4 请求验证和异常处理

- DRF序列化器字段验证
- 自定义验证规则
- 统一异常响应处理

（对应Spring Boot中Hibernate Validator，`@ControllerAdvice`异常处理）

### 2.5 认证和权限管理

- 简单基于Token认证（DRF Token Auth）
- JWT认证（第三方库`djangorestframework-simplejwt`）
- 权限控制和角色管理（DRF权限类）
- 实战：登录、注册、用户信息接口

（对应Spring Security配置）

---

## 3. 进阶与项目实践

### 3.1 API版本管理和文档

- 使用`drf-yasg`或`drf-spectacular`自动生成Swagger文档
- API版本控制思路（URL或请求头）

### 3.2 测试策略

- 使用Django测试工具编写单元测试和集成测试
- DRF API接口测试实践

### 3.3 性能优化和缓存

- 查询优化：select_related、prefetch_related
- 使用缓存（Redis，Django cache框架）
- 限流和防刷设计

### 3.4 部署与运维

- WSGI配置（Gunicorn + Nginx）
- 环境变量管理和配置分离
- 数据库迁移和备份

---

## 4. 拓展主题（可按需学习）

- 异步支持：Django Channels和异步视图
- WebSocket API设计
- 与前端React/Vue项目集成实战
- 定时任务（Celery + Redis）
- 多数据库和分布式架构

---

## 2. 安装Django与Django REST Framework

```bash
pip install django djangorestframework
```

这一步类似Spring Boot里引入`spring-boot-starter-web`和`spring-boot-starter-data-jpa`这些starter依赖。

---

## 3. 创建Django项目

```bash
django-admin startproject myproject
cd myproject
```

**目录结构：**

```
myproject/
  manage.py             # 启动脚本（同Spring Boot项目的启动Main类）
  myproject/            # 项目包，包含配置和启动
    __init__.py
    settings.py         # 项目配置（对应application.yml，@Configuration）
    urls.py             # 全局路由配置（对应Spring MVC全局RequestMapping）
    asgi.py             # ASGI入口（处理异步请求）
    wsgi.py             # WSGI入口（处理同步请求，类似内嵌Tomcat）
```

> **小结**：Django项目相当于Spring Boot的工程根，`manage.py`相当于启动程序入口，`settings.py`相当于配置类和配置文件。

---

## 4. 运行服务器验证

执行：

```bash
python manage.py runserver
```

默认启动开发服务器，访问 `http://127.0.0.1:8000/` 会看到欢迎页面。

对应Spring Boot运行`mvn spring-boot:run`后访问 http://localhost:8080/

---

## 5. 创建应用（App）

Django用“App”组织业务模块，类似Spring Boot里不同的包或模块。

```bash
python manage.py startapp api
```

目录示例：

```
myproject/
  api/
    __init__.py
    admin.py         # 后台管理模块（可暂时不管）
    apps.py          # App配置
    models.py        # 模型（对应Spring Boot的Entity）
    tests.py         # 测试代码
    views.py         # 视图函数或视图类（对应Spring Controller）
    migrations/      # 数据库迁移记录
```

---

## 2. 生成迁移脚本并同步数据库

Django需要两步命令完成数据库更新：

```bash
python manage.py makemigrations api
python manage.py migrate
```

- `makemigrations`：根据模型变化生成数据库迁移文件（相当于生成DDL脚本）
- `migrate`：执行迁移，实际在数据库创建/修改表（类似Hibernate自动更新数据库）
