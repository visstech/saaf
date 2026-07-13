# 🤖 SAAF

# Simple AI Agent Framework

## Learn. Build. Understand AI Agents.

An open-source AI Agent Engineering framework designed to help developers understand, build, and extend intelligent agent systems.

---

# 🌟 Overview

SAAF (Simple AI Agent Framework) is a modular framework for learning and engineering AI agents.

The goal of SAAF is not only to build AI agents, but to make the internal architecture of AI agents understandable.

SAAF exposes the core building blocks behind intelligent agents:

* Memory
* Storage
* Language Models
* Tools
* Reasoning
* Planning
* Knowledge Systems

Developers can learn how these components work together to create intelligent applications.

---

# 🎯 Vision

AI agents are becoming a fundamental part of modern software systems.

However, many frameworks hide the internal working mechanisms behind abstractions.

SAAF focuses on transparency and education by providing:

* Clear architecture
* Modular components
* Simple implementations
* Practical examples

The mission:

> Make AI Agent Engineering simple, understandable, and accessible.

---

# 🏗️ Architecture Overview

SAAF follows a modular layered architecture:

```
                    User Application

                           |

                           ▼

                       SAAF Core

                           |

       -----------------------------------------

       |                 |                     |

       ▼                 ▼                     ▼

    Memory          Intelligence            Tools

       |                 |                     |

       ▼                 ▼                     ▼

  Storage Layer       LLM Layer          External Systems

```

---

# ✨ Features

## 🧠 Memory System

SAAF provides a flexible memory architecture:

* Conversation Memory
* Short-Term Memory
* Long-Term Memory
* Memory Manager

Current implementation:

```
Memory Manager

      |
      |
 --------------------
 |        |         |
 ▼        ▼         ▼

Conversation Short   Long
Memory     Term     Term

              |
              ▼

            SQLite
```

---

## 💾 Storage Layer

Persistent memory storage.

Current support:

* SQLite

Future support:

* PostgreSQL
* Vector Databases

---

## 🔌 Modular Architecture

SAAF components are designed independently.

Future extensions:

* Different LLM providers
* Custom memory systems
* New tools
* New reasoning engines

---

# 🚀 Current Status

Current version:

```
v0.2.0
Memory Foundation
```

Completed:

✅ Memory Model
✅ SQLite Storage
✅ Conversation Memory
✅ Short-Term Memory
✅ Long-Term Memory
✅ Memory Manager
✅ SAAF Core

---

# ⚡ Quick Start

## Installation

Clone the repository:

```bash
git clone https://github.com/visstech/saaf.git

cd saaf
```

Create environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧪 Example Usage

```python
from saaf.core import SAAF
from models.memory import Memory


agent = SAAF()


memory = Memory(
    user_id="senthil",
    memory_key="skills",
    memory_value={
        "languages": [
            "Python",
            "SQL",
            "PyTorch"
        ]
    },
    memory_type="skill",
    importance=10
)


agent.memory.remember(memory)


result = agent.memory.recall(
    "senthil",
    "skills"
)

print(result)
```

---

# 📚 Documentation

SAAF documentation:

```
docs/

├── 01_introduction/

│   ├── vision.md

│   ├── architecture.md

│   └── roadmap.md


└── 02_core/

    └── (coming soon)
```

---

# 🛣️ Roadmap

Future SAAF versions:

```
v0.3.0
Developer Experience

v0.4.0
LLM Integration

v0.5.0
Tool Framework

v0.6.0
Reasoning Engine

v0.7.0
RAG Knowledge System

v0.8.0
Multi-Agent System

v1.0.0
Production AI Agent Framework
```

---

# 🤝 Contribution

SAAF welcomes contributions from developers interested in:

* AI agents
* Machine learning systems
* Framework engineering
* Documentation
* Education

Future contributors can help improve:

* Core modules
* Examples
* Documentation
* Integrations

---

# 👨‍💻 Developed By

**Vi.S.Senthil Kumar**

Founder & Lead Developer

Visstech

---

# 📜 License

License information will be added as the project matures.

---

# 💙 SAAF Philosophy

```
Learn.
Build.
Understand AI Agents.
```

SAAF is not only a framework for building agents.

It is a framework for understanding how agents are engineered.
