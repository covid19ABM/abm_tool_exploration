# Take-aways

- Most research are about evaluating different intervension policies on virus pandemic (e.g. infection rates).
- Maybe worth to spend time and check the bibliometric analysis survey to find the starting point.
	- Our work seems to fall in the conceptual and policy-based modeling cluster.
	- Nearly all the research in this field use SIR models or extended versions to model the pandemic and disease progression (see table 1 in the biblometric review paper).
- It's nice to setup some benchmark scenarios for comparison, and they can be cases like "no covid pandemic" and "do nothing".
- Different timeframes are applicable at once (to update variables on different pace).
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
	- way to abstract movement: as either long-distanced or local
- Ways of quantitatively modeling "mental health":
	- Search volumn of "mental health" and relevant terms on Google
	- evaluation of life quality, psychological distress, anxiety index, etc.
	- Mental health is not an independent variable, there are other impact factors like , e.g., gender and trust in the government.
	- There are quite some research (regression studies) about the association of policy sprintengy with mental health level, but not ABMs.

# Questions
- Do we consider population changes (e.g. due to age increase, births, deaths, migration, etc.)?  
- Do we want to simulate virus spreading and disease progression?
- Any hypothesis on how lockdown policies affect the health outcome measures? 
	- Possible factors: economics, infection, neighbourhood, persona
- Is it possible to have the infection data of individuals so that we don't have to model it ourselves?
