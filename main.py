from crewai import Crew
from tools import NumVerifyTool, IpStackTool, MarketStackTool
from agents import AgentFactory
from tasks import TaskFactory

print("🔧 Inicializando...")

# Instanciar ferramentas
tools = [NumVerifyTool(), IpStackTool(), MarketStackTool()]

# Criar agentes com suas respectivas ferramentas
phone_agent = AgentFactory.get_phone_agent(tools)
ip_agent = AgentFactory.get_ip_agent(tools)
stock_agent = AgentFactory.get_stock_agent(tools)

# Criar tarefas para cada agente
tasks = TaskFactory.get_tasks(phone_agent, ip_agent, stock_agent)

# Criar equipe e executar
crew = Crew(
    agents=[phone_agent, ip_agent, stock_agent],
    tasks=tasks,
    verbose=True,
    max_iterations=1
)

print("🚀 Executando tarefas...")
resultado = crew.kickoff()

print("\n✅ Resultados das tarefas em output/")
