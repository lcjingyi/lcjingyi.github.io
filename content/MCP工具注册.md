Title: MCP工具注册
Date: 2025-11-06 18:00
Category: MCP
Tags: MCP

# MCP 工具注册完整指南

## 什么是工具注册？

在 MCP (Model Context Protocol) 中，**工具注册**是告诉 AI 模型（如 Claude）你这个服务器能提供什么功能的过程。就像餐厅的菜单一样，注册的工具列表就是 AI 可以使用的"功能菜单"。

## 工具注册的核心组件

### 1. 工具定义结构

每个工具都必须包含以下核心信息：

```json
{
    "name": "工具的唯一标识符",
    "description": "工具功能的中文描述",
    "inputSchema": {
        "type": "object",
        "properties": {
            "参数名": {
                "type": "数据类型",
                "description": "参数描述"
            }
        },
        "required": ["必需参数列表"]
    }
}
```

### 2. 代码中的注册实现

在 `mcp_client.py` 中，工具注册通过 `_register_tools()` 方法实现：

```python
def _register_tools(self):
    """注册可用工具"""
    self.tools = {
        "integer_addition": {
            "name": "integer_addition",
            "description": "计算两个整数的和",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "第一个整数"},
                    "b": {"type": "integer", "description": "第二个整数"}
                },
                "required": ["a", "b"]
            }
        },
        "integer_multiplication": {
            "name": "integer_multiplication",
            "description": "计算两个整数的积",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "第一个整数"},
                    "b": {"type": "integer", "description": "第二个整数"}
                },
                "required": ["a", "b"]
            }
        }
    }
```

## 详细解析工具注册的各个部分

### 1. 工具名称 (name)

```python
"name": "integer_addition"
```

**要求**：
- 必须是**唯一**的标识符
- 使用小写字母和下划线
- 简洁明了，能表达工具功能
- 在 `call_tool` 方法中用作路由标识

**最佳实践**：
```python
# ✅ 好的命名
"weather_forecast"
"file_reader"
"database_query"

# ❌ 避免的命名
"tool1"
"addNumbers"  # 使用驼峰命名
"integer-addition-tool"  # 过于冗长
```

### 2. 工具描述 (description)

```python
"description": "计算两个整数的和"
```

**作用**：
- AI 模型根据描述理解工具用途
- 决定何时调用这个工具
- 提供用户友好的功能说明

**写作技巧**：
- 使用简洁、准确的中文描述
- 说明输入和输出的关系
- 避免技术术语，用自然语言

### 3. 输入模式 (inputSchema)

这是最关键的部分，定义了工具接受的参数：

```python
"inputSchema": {
    "type": "object",
    "properties": {
        "a": {"type": "integer", "description": "第一个整数"},
        "b": {"type": "integer", "description": "第二个整数"}
    },
    "required": ["a", "b"]
}
```

#### 3.1 参数类型 (type)

支持的常见类型：
```python
# 基本类型
"string"   # 文本
"integer"  # 整数
"number"   # 数字（包括小数）
"boolean"  # 布尔值

# 复合类型
"array"    # 数组
"object"   # 对象
```

#### 3.2 参数定义 (properties)

每个参数都需要定义：
```python
"a": {
    "type": "integer",           # 参数类型
    "description": "第一个整数"   # 参数说明
}
```

#### 3.3 必需参数 (required)

```python
"required": ["a", "b"]  # 这两个参数是必需的
```

**可选参数**：
```python
"properties": {
    "a": {"type": "integer", "description": "第一个整数"},
    "b": {"type": "integer", "description": "第二个整数"},
    "round": {"type": "boolean", "description": "是否四舍五入"}
},
"required": ["a", "b"]  # round 是可选参数
```

## 注册流程的完整过程

### 1. 初始化阶段

```python
def __init__(self):
    self.base_url = "http://localhost:8000"
    self.tools = {}  # 空的工具字典
    self._register_tools()  # 注册工具
```

### 2. 注册阶段

```python
def _register_tools(self):
    # 将工具定义存储到 self.tools 字典中
    self.tools = {
        "工具名": 工具定义,
        ...
    }
```

### 3. 查询阶段 (tools/list)

当 AI 模型询问可用工具时：

```python
elif request.get("method") == "tools/list":
    response = {
        "jsonrpc": "2.0",
        "id": request.get("id"),
        "result": {
            "tools": list(server.tools.values())  # 返回所有注册的工具
        }
    }
```

## 如何添加新工具

### 示例：添加一个除法工具

#### 步骤 1：在 `_register_tools()` 中添加工具定义

```python
def _register_tools(self):
    """注册可用工具"""
    self.tools = {
        # 现有工具...

        # 新增除法工具
        "integer_division": {
            "name": "integer_division",
            "description": "计算两个整数的商",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "被除数"},
                    "b": {"type": "integer", "description": "除数"}
                },
                "required": ["a", "b"]
            }
        }
    }
```

#### 步骤 2：实现计算逻辑

```python
async def divide_numbers(self, a: int, b: int) -> Dict[str, Any]:
    """整数除法计算"""
    try:
        if b == 0:
            return {"success": False, "error": "除数不能为零"}

        response = requests.post(
            f"{self.base_url}/api/divide",
            json={"a": a, "b": b},
            timeout=5
        )
        response.raise_for_status()
        return {"success": True, "result": response.json()["result"]}
    except requests.RequestException as e:
        return {"success": False, "error": f"除法计算失败: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"除法计算错误: {str(e)}"}
```

#### 步骤 3：在 `call_tool()` 中添加路由

```python
async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """调用指定工具"""
    if tool_name == "integer_addition":
        # 现有加法逻辑...

    elif tool_name == "integer_multiplication":
        # 现有乘法逻辑...

    elif tool_name == "integer_division":  # 新增除法逻辑
        result = await self.divide_numbers(arguments["a"], arguments["b"])
        if result["success"]:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"{arguments['a']} ÷ {arguments['b']} = {result['result']}"
                    }
                ]
            }
        else:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": result["error"]
                    }
                ]
            }

    # 其他现有逻辑...
```

## 高级工具注册技巧

### 1. 复杂参数类型

```python
"analyze_text": {
    "name": "analyze_text",
    "description": "分析文本的情感和主题",
    "inputSchema": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "要分析的文本内容"
            },
            "options": {
                "type": "object",
                "properties": {
                    "sentiment": {"type": "boolean", "description": "是否分析情感"},
                    "topics": {"type": "boolean", "description": "是否分析主题"},
                    "language": {"type": "string", "description": "文本语言"}
                },
                "description": "分析选项"
            }
        },
        "required": ["text"]
    }
}
```

### 2. 数组参数

```python
"calculate_average": {
    "name": "calculate_average",
    "description": "计算数字列表的平均值",
    "inputSchema": {
        "type": "object",
        "properties": {
            "numbers": {
                "type": "array",
                "items": {"type": "number"},
                "description": "数字列表"
            }
        },
        "required": ["numbers"]
    }
}
```

### 3. 枚举参数

```python
"format_date": {
    "name": "format_date",
    "description": "格式化日期",
    "inputSchema": {
        "type": "object",
        "properties": {
            "date": {"type": "string", "description": "日期字符串"},
            "format": {
                "type": "string",
                "enum": ["YYYY-MM-DD", "MM/DD/YYYY", "DD-MM-YYYY"],
                "description": "输出格式"
            }
        },
        "required": ["date", "format"]
    }
}
```

## 工具注册的最佳实践

### 1. 命名规范
- 使用动词开头的描述性名称
- 小写字母和下划线
- 避免缩写，使用完整单词

### 2. 描述写作
- 清晰说明输入输出关系
- 使用自然语言，避免技术术语
- 包含使用场景说明

### 3. 参数设计
- 提供合理的默认值
- 明确区分必需和可选参数
- 使用适当的数据类型

### 4. 错误处理
- 在工具定义中描述可能的错误情况
- 提供有意义的错误消息
- 考虑边界情况

## 总结

MCP 工具注册是一个**声明式**的过程：

1. **定义工具**：在 `_register_tools()` 中声明工具的元数据
2. **实现逻辑**：编写具体的处理函数
3. **路由调用**：在 `call_tool()` 中连接工具名和处理逻辑
4. **自动发现**：AI 模型通过 `tools/list` 自动发现可用工具

这种设计让工具注册变得**声明式**和**可扩展**，开发者只需要专注于工具的定义和实现，MCP 框架会处理所有的通信和路由逻辑。