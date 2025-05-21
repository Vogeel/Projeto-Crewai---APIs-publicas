from crewai import Task

class TaskFactory:
    @staticmethod
    def get_tasks(phone_agent, ip_agent, stock_agent):
        return [
            Task(
                description=(
                    "Valide o número +5511987654321. Analise os dados como país, operadora e tipo de linha. "
                    "Com base nisso, faça uma suposição sobre a natureza do número: pode ser comercial? SPAM? Particular? "
                    "Sugira como isso pode ser útil para negócios, segurança ou marketing."
                ),
                expected_output="Análise detalhada do número de telefone, com possíveis aplicações ou alertas.",
                agent=phone_agent,
                output_file="output/telefone.txt"
            ),
            Task(
                description=(
                    "Analise o IP 187.75.194.108. Retorne a cidade, país, fuso horário e provedor. "
                    "Com base na localização, sugira comportamentos prováveis do usuário, como idioma, horário de atividade e tipo de rede. "
                    "Faça uma breve inferência útil sobre esse IP para segurança, marketing ou análise de risco."
                ),
                expected_output="Relatório interpretativo com insights úteis com base na geolocalização do IP.",
                agent=ip_agent,
                output_file="output/ip.txt"
            ),
            Task(
                description=(
                    "Pesquise os dados de mercado da AAPL. Com base nos preços recentes, volume e data, forneça uma breve análise da tendência. "
                    "Inclua possíveis suposições sobre o comportamento futuro da ação. "
                    "Considere fatores como flutuação, volatilidade e oportunidades para investidores."
                ),
                expected_output="Relatório de mercado com análise interpretativa e projeções da ação da Apple.",
                agent=stock_agent,
                output_file="output/acoes.txt"
            )
        ]
