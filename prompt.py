

prompt1 = """  
### Task: API Structure and Relationship Visualization  

**Objective:**  
Extract, analyze, and visualize the API structure and relationships within the given codebase. The output should be written to `api_structure.md`, creating or updating it as needed. The visualization should be generated using **Mermaid.js**, representing API interactions, dependencies, and flows.  

---

### Steps to Follow:  

1. **Extract API Endpoints:**  
   - Identify all API routes, including:  
     - **Base paths** (e.g., `/api/v1`, `/auth`, `/users`)  
     - **HTTP methods** (GET, POST, PUT, DELETE, PATCH)  
     - **Request structure (parameters, headers, body, query params)**  
     - **Response structure (success and error cases)**  

2. **Identify API Relationships and Dependencies:**  
   - Map direct API-to-API calls within services.  
   - Capture **conditional flows** (e.g., success vs. error handling).  
   - Identify dependencies between endpoints (e.g., authentication, database access).  

3. **Generate a Mermaid.js Diagram:**  
   - **Use flowcharts** to represent API interactions.  
   - **Group related routes** for clarity.  
   - **Clearly label connections** between APIs to indicate dependencies.  

4. **Handle Large API Graphs Efficiently:**  
   - If the graph is too complex, split it into smaller subgraphs.  
   - Link related graphs for better navigation.  
   - Ensure a **main overview graph** connects all subgraphs.  

---

### Execution Structure  

1. **Scan Codebase for API Definitions**  
   - Parse **controller/service files** to extract endpoints and method mappings.  
   - Analyze **middleware, authentication, and data flows**.  

2. **Structure API Data**  
   - Convert extracted API information into a structured format (JSON or dictionary).  
   - Organize by **routes, HTTP methods, dependencies, and data flows**.  

3. **Generate API Documentation (`api_structure.md`)**  
   - If the file exists, **update it** with new insights.  
   - If it does not exist, **create a new file** and write structured API documentation.  
   - Append extracted API data in **a readable Markdown format**.  

4. **Generate Mermaid.js Graph**  
   - Construct flowchart representation using Mermaid.js syntax.  
   - Embed the diagram into `api_structure.md` for easy visualization.  

5. **Save & Verify Output**  
   - Ensure all API endpoints are documented correctly.  
   - Validate Mermaid.js syntax to avoid rendering errors.  

---

### File Handling: `api_structure.md`  

- **Check if `api_structure.md` exists**:  
  - If **yes**, update it with new API insights.  
  - If **no**, create it and write structured API documentation.  
- Append a **Mermaid.js diagram** with the extracted API relationships.  

---
This is the example of the flow diagram. make sure to generate the flow diagram for the implementation workflow.
map<node,vector<pair<node,node>>> graph
where one node is the source node and the other is the destination node. and the pair.second represent the label of the edge.
like their is a route /auth the level of the egde will be like this auth route will handle the all  things related to the authentication.

### Example Mermaid.js Output  

```mermaid
graph TD
    A[Client] -->|Requests| B[Auth Service]
    B -->|Valid Token| C[User Service]
    B -->|Invalid Token| D[Error Response]
    C -->|Fetch Data| E[Database]
    C -->|Update Profile| F[Update API]
    F -->|Logs Update| G[Logging Service]
    subgraph API Grouping
        B
        C
        F
    end

    Execution Instructions
Extract API details from the project files.
Structure the extracted data in a readable format.
Generate a Mermaid.js visualization representing API interactions.
Write or update api_structure.md with the extracted details and visual representation.
Validate and finalize the Markdown file for clarity and correctness.
Ensure the final output is clear, structured, and accurate to help developers understand API relationships easily.

Reply Terminated when you are done with the task.
do not execute the code.
"""
prompt2 = """ 
### **Task: API Grouping, Documentation, and Visualization**  

#### **Objective:**  
Extract, analyze, and document all API routes, ensuring:  
1. **Related APIs are stored in the same file** based on their base route (e.g., `users.md` for `/users`, `orders.md` for `/orders`).  
2. **Unrelated APIs are documented separately** for modularity.  
3. **Mermaid.js diagrams** are generated to visualize API interactions.  

---

### **Steps to Follow:**  

#### **1. Extract API Endpoints**  
- Identify all API routes, including:  
  - **Base paths** (e.g., `/users`, `/orders`, `/auth`)  
  - **HTTP methods** (GET, POST, PUT, DELETE, PATCH)  
  - **Request and response structures**  

#### **2. Group APIs by Base Route**  
- **Each group should be stored in a separate file.**  
  - All `/users` APIs → `users.md`  
  - All `/orders` APIs → `orders.md`  
  - All `/auth` APIs → `auth.md`  

#### **3. Document API Details in Each File**  
Each file should contain:  
- **Route descriptions**  
- **Request parameters, headers, and body format**  
- **Response structures with status codes**  
- **Dependencies and external services called**  
- **Mermaid.js diagram of relationships**  

---

### **File Handling Instructions:**  
1. **Check if the file exists:**  
   - If **yes**, update it with new API insights.  
   - If **no**, create it and write structured API documentation.  
2. **Use the appropriate tools:**  
   - `create_file` → To create the file if not available.  
   - `write_to_file` → To update an existing file with new API details.  

---

### **Example File Structure and Documentation Format**  



### Example Mermaid.js Output   for every file diagram should be first.
This is the example of the flow diagram. make sure to generate the flow diagram for the implementation workflow.
map<node,vector<pair<node,node>>> graph
where one node is the source node and the other is the destination node. and the pair.second represent the label of the edge.
ex - like their is a  /auth/{`check`} the level of the egde will be like this auth route will handle the all  things related to the checking things.
```mermaid
graph TD
    A[Client] -->|Requests| B[Auth Service]
    B -->|Valid Token| C[User Service]
    B -->|Invalid Token| D[Error Response]
    C -->|Fetch Data| E[Database]
    C -->|Update Profile| F[Update API]
    F -->|Logs Update| G[Logging Service]
    subgraph API Grouping
        B
        C
        F
    end

#### **File: `users.md`**  
```markdown
# User APIs  

## GET /users  
- Description: Fetch a list of users.  
- Parameters:  
  - `page` (optional) - Pagination page number.  
- Response:  
  - 200: List of users.  
  - 401: Unauthorized.  

## POST /users  
- Description: Create a new user.  
- Request Body:  
  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string"
  }
Response:
201: User created successfully.
400: Validation error.
Execution Workflow:
Extract API information.
Group them by base route.
Check if the corresponding file exists.
If the file exists, update it using write_to_file.
If the file does not exist, create it using create_file and then write the details.
Append a Mermaid.js diagram with extracted API relationships.

Reply Terminated when you are done with the task.
do not execute the code.
"""
# prompt3 = """  

#  ### **Task: Feature Analysis, Documentation, and Flow Diagram Generation**  

# #### **Objective:**  
# Extract, analyze, and document key features of the codebase while visualizing relationships through **Mermaid.js flow diagrams**.  
# All details should be stored in a single file: **`system_documentation.md`**.  
# - **If `system_documentation.md` exists**, update it with new insights.  
# - **If `system_documentation.md` does not exist**, create it and store all relevant data.  

# ---

# ### **File to Handle:**  
# - `system_documentation.md` → Stores database configurations, architecture, tools, and frameworks.  

# ---

# ### **Steps to Follow:**  

# #### **1. Extract Feature Information**  
# - Identify and document:  
#   - **Databases**: Type, configuration, usage, and relevant files.  
#   - **Architecture**: Structure, patterns, and deployment strategies.  
#   - **Tools & Frameworks**: Development tools and their purpose.  

# #### **2. File Handling Logic**  
# - **Check if `system_documentation.md` exists**:  
#   - If **yes**, update it with newly extracted insights.  
#   - If **no**, create the file and add all relevant data.  

# #### **3. Generate Mermaid.js Flow Diagram for System Structure**  
# - **Use flowcharts** to represent service interactions.  
# - **Show dependencies** between different components.  
# - **Split large graphs into subgraphs** if required for clarity.  

# ---

# ### **Example Content for `system_documentation.md`**  

# ```markdown
# ## 1. System Flow Diagram

# This is the example of the flow diagram. make sure to generate the flow diagram for the implementation workflow.
# it should contain the detail of the 
# **Databases**: Type, configuration, usage, and relevant files. 
# **Architecture**: Structure, patterns, and deployment strategies.
# **Tools & Frameworks**: Development tools and their purpose.

# ```mermaid
# graph TD
#     A[Client] -->|Requests| B[Auth Service]
#     B -->|Valid Token| C[User Service]
#     B -->|Invalid Token| D[Error Response]
#     C -->|Fetch Data| E[Database]
#     C -->|Update Profile| F[Update API]
#     F -->|Logs Update| G[Logging Service]

#     subgraph System Components
#         B
#         C
#         F
#     end
# # System Documentation

# ## 1. Databases Used

# ### MongoDB
# - NoSQL database for flexible data storage.
# - Used for storing user and session data.
# - Configuration: `config/database.js`
#     ```js
#     module.exports = {
#       mongoURI: "mongodb://localhost:27017/mydb"
#     }
#     ```

# ## 2. Architecture Overview

# ### Microservices Architecture
# - Services communicate via REST APIs.
# - Database layer managed separately.
# - Authentication handled centrally.

# ## 3. Tools & Frameworks

# - **Backend**: Node.js, Express  
# - **Frontend**: React.js  
# - **Database**: MongoDB, PostgreSQL  
# - **Authentication**: JWT, OAuth  
# - **DevOps**: Docker, Kubernetes  


# ---
# ### **Execution Flow:**  
# 1. **Extract** details of APIs, databases, tools, and architecture.  
# 2. **Check for existing file (`system_documentation.md`)**.  
# 3. **Update if the file exists**, otherwise **create it and store all relevant data**.  
# 4. **Generate Mermaid.js diagrams** to visualize relationships.  
# Reply Terminated when you are done with the task.
# do not execute the code.
# ---
# """  

prompt3 = """
 # System Documentation Generator Prompt

## OBJECTIVE
Generate comprehensive system_documentation.md documenting system architecture, databases, and frameworks while visualizing relationships through Mermaid.js diagrams.

## INPUT REQUIREMENTS
Analyze codebase for:
- Database configurations and usage
- System architecture and patterns
- Tools, frameworks, and their relationships
- Service interactions and dependencies
- API endpoints and flows

## OUTPUT FORMAT

```markdown
# System Documentation

## 1. System Architecture Overview

### System Flow Diagram
```mermaid
graph TD
    %% Main System Flow
    subgraph Client["Client Layer"]
        [Client components]
    end
    
    subgraph Services["Service Layer"]
        [Service components]
    end
    
    subgraph Data["Data Layer"]
        [Database components]
    end
    
    %% Define relationships
    [System interactions]
```

## 2. Database Infrastructure

### Database Overview
- Database Types: [List all databases]
- Primary Usage: [Usage patterns]
- Configurations: [Config details]

### Database Relationships
```mermaid
graph LR
    %% Database connections
    [Database interaction diagram]
```

### Configuration Examples
```javascript
[Database configuration code]
```

## 3. Architecture Details

### Design Patterns
[List architectural patterns]

### Service Architecture
```mermaid
graph TD
    %% Service structure
    [Service architecture diagram]
```

### Deployment Strategy
[Deployment details]

## 4. Tools & Frameworks

### Core Technologies
- Backend: [Backend stack]
- Frontend: [Frontend stack]
- Database: [Database technologies]
- DevOps: [DevOps tools]

### Framework Integration
```mermaid
graph TD
    %% Framework relationships
    [Framework integration diagram]
```

## 5. API Structure
### Endpoints
[List major API endpoints]

### API Flow
```mermaid
sequenceDiagram
    [API interaction flow]
```
```

## STYLING GUIDELINES

1. Mermaid Diagram Styles:
```
classDef client fill:#e1f5fe,stroke:#01579b
classDef service fill:#f3e5f5,stroke:#4a148c
classDef database fill:#fff3e0,stroke:#e65100
```

2. Markdown Formatting:
- Use H1 (#) for document title
- Use H2 (##) for main sections
- Use H3 (###) for subsections
- Use code blocks for configurations
- Use bullet points for lists

## EXECUTION STEPS

1. System Analysis:
   - Analyze database configurations
   - Map system architecture
   - Document tools and frameworks
   - Identify service relationships

2. File Management:
   - Check for system_documentation.md
   - Create new or update existing
   - Preserve existing structure if updating

3. Documentation Generation:
   - Create system flow diagrams
   - Document database details
   - Map architectural patterns
   - List tools and frameworks

4. Relationship Visualization:
   - Generate service interaction diagrams
   - Create database relationship diagrams
   - Map framework dependencies
   - Document API flows

## EXECUTION FLOW
1. **Extract** details of APIs, databases, tools, and architecture.
2. **Check for existing file (`system_documentation.md`)**.
3. **Update if the file exists**, otherwise **create it and store all relevant data**.
4. **Generate Mermaid.js diagrams** to visualize relationships.

Reply Terminated when you are done with the task.
Do not execute the code.

## NOTES
- Generate diagrams based on actual system analysis
- Split large diagrams into subgraphs for clarity
- Include only discovered components and relationships
- Maintain consistent formatting throughout
- Update incrementally if file exists
"""

prompt4 = """
    

# Extract, analyze, and document the tools, libraries, and implementation details used in the project while visualizing relationships through **Mermaid.js flow diagrams**.  
All details should be stored in **a single file: `implementation_details.md`**.  

- **If `implementation_details.md` exists**, update it with new insights.  
- **If `implementation_details.md` does not exist**, create it and store all relevant data.  

## OUTPUT FORMAT
<userStyle>Normal</userStyle>
```markdown
# Implementation Details

## 1. Technology Stack Overview
### Tools & Libraries
- Core Libraries: [list of main libraries]
- Development Tools: [development tools]
- Testing Frameworks: [test frameworks]
- Build Tools: [build tools]

### Implementation Stack
- Language: [programming language]
- Framework: [main framework]
- Package Manager: [package manager]
- Version Control: [VCS]

## 2. System Architecture & Flow

### Architecture Diagram
```mermaid
graph TD
    %% Tool & Library Relationships
    subgraph Core["Core Libraries"]
        [Core dependencies]
    end
    
    subgraph Dev["Development Tools"]
        [Dev tools found]
    end
    
    subgraph Build["Build Process"]
        [Build tools]
    end
    
    %% Show relationships
    [Tool interactions]
```

## 3. Library Dependencies
### Primary Dependencies
[List main dependencies with versions]

### Development Dependencies
[List dev dependencies with versions]

### Dependency Flow
```mermaid
graph LR
    %% Dependency relationships
    [Dependency chain]
```

## 4. Implementation Structure
### Project Organization
[Project structure overview]

### Build Process
```mermaid
flowchart TD
    %% Build process flow
    [Build steps]
```

## 5. Tool Integration
### Development Tools
[List integrated development tools]

### Tool Interaction Flow
```mermaid
graph TD
    %% Tool integration flow
    [Tool interaction diagram]
```

## 6. Configuration & Setup
### Tool Configuration
[Important tool configurations]

### Environment Setup
[Setup requirements]
```

## STYLING GUIDELINES

1. Mermaid Diagram Styles:
```
classDef core fill:#e1f5fe,stroke:#01579b
classDef dev fill:#f3e5f5,stroke:#4a148c
classDef build fill:#fff3e0,stroke:#e65100
```

2. Markdown Formatting:
- Use H1 (#) for document title
- Use H2 (##) for main sections
- Use H3 (###) for subsections
- Use bullet points for lists
- Use code blocks for configuration examples

## EXECUTION STEPS

1. Document Analysis:
   - Check for implementation_details.md
   - Create new or update existing
   - Maintain existing structure if updating

2. Content Generation:
   - Document all tools and libraries
   - Create relationship diagrams
   - Document implementation details

3. Relationship Visualization:
   - Show tool dependencies
   - Map library relationships
   - Document tool interactions

4. Validation:
   - Verify all sections are complete
   - Check diagram syntax
   - Validate markdown formatting

## NOTES
- Generate diagrams based on actual project analysis
- Include only discovered tools and libraries
- Maintain consistent formatting
- Update incrementally if file exists
- Focus on implementation and tool relationships
"""

# prompt4 = """  
# ### **Task: Implementation Details Documentation and Flow Diagram Generation**  

# #### **Objective:**  
# Extract, analyze, and document the tools, libraries, and implementation details used in the project while visualizing relationships through **Mermaid.js flow diagrams**.  
# All details should be stored in **a single file: `implementation_details.md`**.  

# - **If `implementation_details.md` exists**, update it with new insights.  
# - **If `implementation_details.md` does not exist**, create it and store all relevant data.  

# ---

# ### **Steps to Follow:**  

# #### **1. Extract Implementation and Tool Details**  
# - Identify and document:  
#   - **Programming Language**: JavaScript (Node.js) or Python.  
#   - **Static Analysis Tools**: AST parsers (`esprima` for JS, `ast` for Python).  
#   - **Visualization Tools**: Mermaid.js for flow diagrams.  
#   - **Version Control**: GitHub/GitLab integration.  

# #### **2. File Handling Logic**  
# - **Check if `implementation_details.md` exists**:  
#   - If **yes**, update it with newly extracted insights.  
#   - If **no**, create the file and add all relevant data.  

# #### **3. Generate Mermaid.js Flow Diagram for Implementation Workflow**  
# - **Use flowcharts** to represent the relationship between tools.  
# - **Show dependencies** between different components.  
# - **Split large graphs into subgraphs** if required for clarity.  

# ---

# ### **File to Handle:**  
# - **`implementation_details.md`** → Contains programming language, tools, libraries, and version control details.  

# ---

# ### **Expected Content for `implementation_details.md`**  

# ```markdown
# # Implementation Details


# ## 1. Implementation Workflow Diagram  
# This is the example of the flow diagram. make sure to generate the flow diagram for the implementation workflow.
# it should contain the detail of the
# **Programming Language**: JavaScript (Node.js) or Python or like this.
# **Static Analysis Tools**: AST parsers (`esprima` for JS, `ast` for Python).
# **Version Control**: GitHub/GitLab integration and versioning
# **version control

# create a mermaid diagram for the implementation workflow. fof the above details



# ## 1. Programming Language  
# - The project is implemented in **JavaScript (Node.js)** or **Python**, depending on the service.

# ## 2. Tools & Libraries  

# ### Static Analysis  
# - **JavaScript**: `esprima` - Parses JavaScript code for structure analysis.  
# - **Python**: `ast` - Built-in library for parsing Python code.  

# ### Visualization  
# - **Mermaid.js**: Used to generate API and system flow diagrams.  

# ## 3. Version Control  
# - **GitHub/GitLab Integration**:  
#   - Tracks and updates markdown documentation.  
#   - Supports versioning of `implementation_details.md`.  


# ---

# ### **Execution Flow:**  
# 1. **Extract** details about implementation, tools, and version control.  
# 2. **Check for existing file (`implementation_details.md`)**.  
# 3. **Update if the file exists**, otherwise **create it and store all relevant data**.  
# 4. **Generate Mermaid.js diagrams** to visualize relationships.  

# Reply Terminated when you are done with the task.
# do not execute the code.
# ---
# """  

prompts = [prompt1, prompt2, prompt3, prompt4]