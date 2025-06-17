# Go + Python 后端工程师学习路线图

> 目标：掌握 Go + Python 双语言开发能力，能够独立构建微服务、AI 推理服务、接口网关等后端系统。

---

## 🎯 总目标
- 构建生产级后端能力
- 掌握 Python + Go 双语言服务协作
- 理解微服务、异步、AI服务接口网关等核心能力

---

## 🗺️ 学习路线（按阶段拆分）

### ✅ 阶段一：巩固 Python 后端核心（第 1～2 周）

| 目标 | 内容 | 工具/框架 |
|------|------|-----------|
| 熟练 Django + DRF 开发 | 注册登录、JWT认证、CRUD、分页、权限 | Django、Django REST Framework |
| 理解模型与数据库 | 自定义用户模型、一对多、多对多 | SQLite / PostgreSQL |
| 简单部署 | 用 gunicorn + nginx 启动服务 | gunicorn、nginx、supervisor |

🔧 实战建议：做一个“任务管理 + 权限控制”系统（带前端Swagger文档）

---

### ✅ 阶段二：掌握异步任务 + 文件服务（第 2～3 周）

| 目标 | 内容 | 工具 |
|------|------|------|
| 实现异步注册/邮件任务 | Celery + Redis |
| 大文件上传/图片处理 | Django 存储系统 + OSS or MinIO |
| 接口性能优化 | select_related、缓存分页器、Throttle限流 |

🔧 实战建议：增加“用户注册邮件 + 图片上传 + 日志导出”功能模块

---

### ✅ 阶段三：基础 Go 后端开发（第 4～6 周）

| 目标 | 内容 | 工具 |
|------|------|------|
| 学习 Go 语言基础 | goroutine、channel、interface | Go 标准库 |
| 构建 REST API 接口 | 使用 Gin 或 Fiber 框架 | Gin/Fiber |
| Go 中间件、日志、配置管理 | zap、viper、gin-cors |

🔧 实战建议：写一个“用户查询 + 统计接口 + JWT 登录”的 Go API 服务

---

### ✅ 阶段四：实现 Go + Python 服务对接（第 7～8 周）

| 模式 | 内容 | 技术 |
|------|------|------|
| HTTP 模式 | Go 发请求 → Python FastAPI 接口 | net/http、requests、axios |
| gRPC 模式 | Go 调用 Python gRPC 服务（推荐） | gRPC、protobuf、grpclib |
| 消息队列模式 | Go 推消息 → Python 消费（Celery/Redis） | Kafka 或 Redis Stream |

🔧 实战建议：用 Go 做网关，Python 做一个 AI “问答”服务（调用 OpenAI 或私有 LLM）

---

### ✅ 阶段五：服务部署 + 监控 + 网关优化（第 9～10 周）

| 内容 | 技术 |
|------|------|
| Docker 容器化 | Dockerfile、docker-compose |
| 微服务注册发现 | Consul / Nacos（可选） |
| 请求追踪 + 性能监控 | Prometheus + Grafana + OpenTelemetry |
| 接口限流与缓存 | Go：ratelimit、Python：Redis + Throttle |
| 统一网关管理 | Go 网关服务，路由不同 Python 模块服务 |

🔧 实战建议：用 docker-compose 跑多个服务，模拟生产部署环境

---

### ✅ 阶段六（可选）：对接大模型 / 企业AI接口（第 10～12 周）

| 内容 | 工具 |
|------|------|
| 私有部署模型 | Llama.cpp、Ollama、Huggingface Transformers |
| 向量搜索 | FAISS、Weaviate、Qdrant |
| 多轮对话/记忆系统 | LangChain / RAG系统 |
| WebSocket 推理接口 | Python FastAPI + WebSocket、Go gorilla/websocket |

---

## 📘 附加资源推荐

### Python
- 《Django for Professionals》
- Django REST Framework 官方文档
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)

### Go
- 《The Go Programming Language》（Go圣经）
- [Go by Example](https://gobyexample.com/)
- Gin 官方文档

---

## 🧠 总结

| 能力 | 说明 |
|------|------|
| ✅ Python 工程化 | Django + DRF + Celery |
| ✅ Go 现代开发 | Gin + JWT + gRPC |
| ✅ 双栈协作服务 | Go 做高并发入口，Python 提供 AI/复杂逻辑 |
| ✅ 云端部署能力 | Docker + Nginx + Redis + 多服务 |

---

> 想要继续推进学习或实现实战项目，我可以每周定制任务或一对一指导落地实践。

