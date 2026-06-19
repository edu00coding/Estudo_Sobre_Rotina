# Analisando a Rotina

Este projeto tem como objetivo a documentação e análise sistemática de hábitos diários para identificação de padrões comportamentais, gargalos de energia e oportunidades de melhoria pessoal e profissional. Iniciado em janeiro de 2026, o projeto evoluiu de anotações físicas em um bullet journal para um repositório estruturado de dados.

## Objetivos do Projeto

A aplicação busca responder a perguntas fundamentais sobre a gestão de tempo e energia:
* Identificar correlações entre níveis de estresse e a busca por mecanismos de recompensa imediata (ex: consumo de álcool).
* Analisar os fatores que influenciam a escolha entre momentos de lazer e dedicação aos estudos de tecnologia.
* Avaliar o impacto de longo prazo das rotinas estabelecidas (visão retrospectiva de 6 a 12 meses).
* Extrair insights sobre dias com maior produtividade ou estados emocionais específicos (alegria, tristeza).

## Metodologia de Coleta

Os dados são inicialmente registrados de forma autodidata, seguindo uma escala de avaliação diária:
* **1:** Ruim
* **2:** Abaixo da média
* **3:** Médio (Meta padrão)
* **4:** Acima da média
* **5:** Intenso
* *Nota 0:* Reservada para casos de não ocorrência ou restrições específicas.

## Arquitetura e Fluxo de Dados

O projeto utiliza uma abordagem de persistência de dados para garantir a integridade das análises:

1.  **Armazenamento Inicial:** Os registros são consolidados em arquivos no formato `.csv`.
2.  **Processamento:** Scripts em **Python** realizam a leitura e conversão dos arquivos.
3.  **Persistência:** Utilização do **MongoDB** como banco de dados NoSQL para armazenamento das informações.
4.  **Análise:** Execução de queries diretamente no banco para extração de métricas e padrões.

## Próximos Passos

* Integração para leitura de dados em formato `.txt` para expandir as fontes de entrada.
* Desenvolvimento de visualizações de dados para facilitar a percepção de tendências ao longo dos meses.
* Refinamento dos scripts de automação para transferência entre CSV e Banco de Dados.

###Projeto desenvolvido a partir de um caderno de anotações 
