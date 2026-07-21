# 🚀 SAAF
# Simple AI Agent Framework

### Learn. Build. Understand AI Agents.

An open-source AI Agent Engineering framework designed to help developers understand, build, and extend intelligent agent systems.

---

# 🌟 Overview

SAAF (Simple AI Agent Framework) is a modular AI Agent framework built from scratch using Python.

The goal of SAAF is not only to create AI agents, but to make the internal architecture of AI agents understandable.

Unlike frameworks that hide complexity behind abstractions, SAAF exposes the fundamental building blocks:

- 🧠 Memory Systems
- 💾 Storage Layer
- 🤖 Language Models
- 🔌 Tools
- 🧩 Reasoning Engine
- 📋 Intent Management
- 📝 Planning
- ⚙️ Workflow Execution
- 🔄 Agent Runtime

Developers can learn how intelligent agents perceive, reason, plan, execute, and remember.

---

# 🎯 Vision

AI Agents are becoming a fundamental part of modern software engineering.

However, many frameworks hide the internal decision-making process.

SAAF focuses on transparency and education.

The mission:

> Make AI Agent Engineering simple, understandable, and accessible.

SAAF provides:

✅ Clear architecture  
✅ Modular components  
✅ Educational implementations  
✅ Practical engineering examples  

---

# 🏗️ Architecture Overview

SAAF follows a layered agent architecture:


```
                       User Application

                              |
                              ▼

                         SAAF Agent

                              |
        ------------------------------------------------

        |              |              |               |

        ▼              ▼              ▼               ▼

    Memory        Reasoning        Tools        Observer

        |              |              |               |

        ▼              ▼              ▼               ▼


   Storage       LLM Engine     Tool Registry    Monitoring


                              |

                              ▼


                    Intent Validation Layer


                              |

                              ▼


                         Planner


                              |

                              ▼


                    Workflow Execution Engine


                              |

                              ▼


                       Workflow Nodes

```

---

# ✨ Current Features

## 🧠 Memory System

SAAF provides a modular memory architecture:

- Conversation Memory
- Short-Term Memory
- Long-Term Memory
- Memory Manager
- Persistent Storage


Architecture:

```
                 Memory Manager

                       |

       --------------------------------

       |              |               |

       ▼              ▼               ▼

 Conversation     Short-Term     Long-Term

 Memory            Memory         Memory

                                      |

                                      ▼

                                  SQLite

```

---

## 🔌 Dynamic Tool Plugin System

SAAF supports modular tool plugins.

New tools can be added without modifying the core framework.

Example:

saaf/tools/plugins/

├── calculator
├── weather
└── sql

Each plugin implements BaseTool and is automatically discovered by PluginLoader.

# 💾 Storage Layer

Persistent memory storage.

Current:

✅ SQLite


Future:

- PostgreSQL
- Vector Databases
- Knowledge Graph Storage


---

# 🔌 Tool Framework

SAAF supports modular tools.

Current tools:

✅ Calculator Tool


Architecture:

```
Tool Manager

      |

      |

 -----------------

 |               |

Calculator     Future Tools

```

Future tools:

- SQL Agent
- Web Search
- PDF Analyzer
- Email Agent
- API Tools

---

# 🤖 LLM Integration

SAAF supports local Large Language Models.

Current support:

✅ Ollama

Tested models:

- Phi3
- Llama3
- DeepSeek-R1
- Gemma3


Architecture:

```
User Request

      |

      ▼

Reasoning Engine

      |

      ▼

LLM Manager

      |

      ▼

Ollama Model

      |

      ▼

Structured JSON Intent

```

---

# 🧩 Intent Validation Engine

SAAF converts LLM output into validated agent instructions.


Flow:

```
LLM Response

      |

      ▼

JSON Parser

      |

      ▼

Intent Validator

      |

      ▼

AgentIntent Object

```

Example:

```python
AgentIntent(
    action="tool",
    tool="calculator",
    input="99*99"
)
```

Benefits:

- Structured execution
- Safer agent decisions
- Easier debugging
- Type-safe architecture

---

# 📋 Planning System

SAAF includes a planning layer.

Example:

User:

```
Calculate 25*40 and save result
```


Generated plan:

```
Workflow:

1. Execute Calculator Tool

2. Save Result To Memory

```

---

# ⚙️ Workflow Engine

SAAF supports multi-step workflows.


Example:

```
User Request

      |

      ▼

Workflow

      |

 ------------------

 |                |

Execute Tool   Save Memory

      |

      ▼

Workflow State

```


Workflow State example:

```python
WorkflowState(
 user_id="default",
 status="completed",
 data={
    "last_result":1000
 }
)
```

---

# 🧱 Workflow Nodes

Current nodes:

```
workflow/
│
├── nodes/
│
├── calculator_node.py
│
├── memory_node.py
│
└── tool_node.py

```

Each node performs one specific action.

Future:

- SQL Node
- API Node
- Search Node
- Vision Node

---

# 🚀 Current Status

## Current Version

```
v0.7.0
```


Completed:

✅ Agent Core  
✅ Memory System  
✅ SQLite Storage  
✅ Tool Manager  
✅ Calculator Tool  
✅ Reasoning Engine  
✅ Planner  
✅ Workflow Engine  
✅ Execution Context  
✅ Workflow Nodes  
✅ Ollama LLM Integration  
✅ LLM Output Parser  
✅ Intent Schema  
✅ Intent Validation Engine  


---

# ⚡ Quick Start


## Clone Repository

```bash
git clone https://github.com/visstech/saaf.git

cd saaf
```


## Create Environment

```bash
python -m venv .venv
```


Activate:

Windows:

```bash
.venv\Scripts\activate
```


Install:

```bash
pip install -r requirements.txt
```

---

# 🧪 Example Usage


```python
from saaf import Agent


agent = Agent()


response = agent.run(
    "calculate 99*99 and save result"
)


print(response)

```


Output:

```
The result of 99*99 is 9801.
```

---

# 📚 Documentation

```
docs/

├── introduction/

├── architecture/

├── memory/

├── reasoning/

├── workflow/

└── examples/

```

Documentation will grow with each SAAF milestone.

---

# 🛣️ Roadmap


## v0.8.0

Dynamic Tool Registry

- Automatic tool discovery
- Plugin architecture
- Tool selection


## v0.9.0

Knowledge System

- Vector Memory
- Embeddings
- RAG


## v1.0.0

Production AI Agent Framework

- Multi-Agent System
- API Server
- Plugin Marketplace
- Enterprise Deployment


---

# 🤝 Contribution

SAAF welcomes contributions from developers interested in:

- AI Agents
- Machine Learning
- Framework Engineering
- LLM Systems
- Documentation


Contributions are welcome in:

- Core modules
- Examples
- Documentation
- Integrations

---

# 👨‍💻 Developed By

## Vi.S.Senthil Kumar

Founder & Lead Developer

Visstech


---

# 📜 License

License information will be added as the project matures.

---

# 💙 SAAF Philosophy


## Learn.

## Build.

## Understand AI Agents.


SAAF is not only a framework for building agents.

It is a framework for understanding how intelligent agents are engineered.

```
