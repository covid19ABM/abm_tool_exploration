# Take-aways

- It's nice to setup some benchmark scenarios for comparison, and they can be cases like no covid pandemic and do nothing.
- With environment topology defined as spatial grids (e.g. Covid-ABS), the lockdown policy can be modeled as follows:
	- forbiding travel (and walk) activities
	- eliminating parameters for controlling agents mobility
- With that defined as network (e.g. OpenABM-covid19), the lockdown policy can be:
	- enliminate interaction between nodes in occupation and ranom network
	- enliminate interaction within specific group of agents (e.g. elders)
	- social distance and masking modeled by reducing the posibility of being infected during interaction
	- contact tracing modeled by randomly dropping interactions between app users
- Ways of modeling interactions between agents without a environment topology like above (e.g. city-scale indian):
	- define/identify interaction spaces (e.g. households, school, workspace, train traveling, etc.) as attributes of agents and define contact rates of agents in those spaces - contact rates can be modified then based on different lockdown policies.

- Do we consider population changes (e.g. due to age increase, births, deaths, migration, etc.)?  
- Questions remain:
	- Do we want to simulate virus spreading and disease progression?
	- Any hypothesis on how lockdown policies affect the health outcome measures? 
		- Possible factors: economics, infection, neighbourhood, persona
