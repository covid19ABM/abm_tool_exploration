# Review Tooling Options 

In this document, we would like to review and compare a number of tools for developing ABMs in Python, from the perspective of supported features and usability for both developers and end-users (criterion list can be extended). Review should be based on literature reading and actual experience (if applicable).  

### Mesa (https://github.com/projectmesa/mesa) 

- Contains all the necessary components for ABM simulation 
- Nice feature: agent schedular, plugins and extensions 
- Nice extendability that allows sharing components in larger community (high impact) 
- Actively maintained, latest release in Oct 2022. 

### AgentPy (https://github.com/JoelForamitti/agentpy) 

- Optimized for Jupyter Notebooks. 
- Nice feature: sampling, data analysis, various visualization, parallelized execution of models 
- SImpler syntax than its major competitors 
- Relatively new addition, but it seems a stable version 
- Extensive documentation 

Cons: it has a smaller community than other packages, meaning that there are fewer people (than mesa, for example) that have actually used it in their work and it requires some deeper exploration to see if it is equivalent to mesa 

### RepastPy (https://github.com/Repast/repast4py) 

- Python implementation of Repast HPC 
- Allow building large, distributed agent-based models 

### CppyAB90M (https://github.com/janursa/CppyABM) 

- Mixed development in C++ and Python, so models developed in one language can be conveniently transferred to another (can be an addition if we want to scale up the model in the future). 

### PyNetLogo (https://github.com/quaquel/pyNetLogo) 

- Python interface to interact with NetLogo, which is considered the standard platform for developing ABMs 
- Can hardly do any hard coding of the background modules 

### Pylogo (https://github.com/RussAbbott/PyLogo) 

- Python implementation of elements of NetLogo 
- GUIs available through PySImpleGUI 
- Hardly find any API docs, but code quality looks good (via a rush scan) 

### PyPandora (https://github.com/pandora-analysis/pypandora) 

- Python interface of accessing Pandora 
- Hard coding not available 