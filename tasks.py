from crewai import Task

class TaskFactory:
    @staticmethod
    def get_tasks(agent):
        return [
            Task(
                description="""
Use suas ferramentas para buscar:
1. Informações sobre o número de telefone +5511987654321
2. Localização e dados do IP 187.75.194.108
3. Dados da empresa AAPL (Apple Inc.) no mercado financeiro

Analise esses dados e gere um relatório completo, estruturado com título, subtítulos e conclusões.
""",
                expected_output="Relatório técnico estruturado com os dados extraídos e análise interpretativa.",
                agent=agent,
                output_file="output/resultado_final.txt"
            )
        ]
