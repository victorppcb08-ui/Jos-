from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# Page margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.2)
    section.right_margin = Inches(1.2)

def add_heading(doc, text, level=1, color=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.bold = True
    if level == 1:
        run.font.size = Pt(16)
        if color:
            run.font.color.rgb = RGBColor(*color)
        else:
            run.font.color.rgb = RGBColor(0x1F, 0x45, 0x7A)
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    elif level == 3:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x1F, 0x45, 0x7A)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    return p

def add_body(doc, text, bold=False, italic=False, indent=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(11)
    if indent:
        p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = Pt(16)
    return p

def add_divider(doc):
    p = doc.add_paragraph()
    run = p.add_run("─" * 70)
    run.font.color.rgb = RGBColor(0xBD, 0xBD, 0xBD)
    run.font.size = Pt(9)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)

def add_box(doc, label, content):
    p = doc.add_paragraph()
    run_label = p.add_run(f"▶ {label}: ")
    run_label.bold = True
    run_label.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    run_label.font.size = Pt(11)
    run_content = p.add_run(content)
    run_content.font.size = Pt(11)
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_after = Pt(3)

# =========================================================
# CAPA
# =========================================================
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("ROTEIRO COMPLETO DE ENTREVISTA")
run.bold = True
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(0x1F, 0x45, 0x7A)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Mestrado Profissional em Controle da Administração Pública")
run.bold = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("ISC/TCU — Processo Seletivo 2026")
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Candidato: José de Castro Barreto Junior")
run.bold = True
run.font.size = Pt(13)

doc.add_paragraph()
add_divider(doc)
doc.add_paragraph()

# =========================================================
# SEÇÃO 0 — PROTOCOLO
# =========================================================
add_heading(doc, "SEÇÃO 0 — PROTOCOLO: ANTES DE COMEÇAR", level=1)

add_heading(doc, "Pronome de Tratamento", level=2)
add_body(doc, "O uso correto dos pronomes de tratamento é fundamental para causar boa impressão. Utilize as formas abaixo para cada membro da banca:")

items = [
    ("Ministros do TCU", "\"Vossa Excelência\" (V. Exa.) — em discurso direto: \"Excelência\""),
    ("Auditores Federais de Controle Externo (AFCE)", "\"Senhor\" / \"Senhora\" — ex: \"Senhor Auditor\", \"Senhora Auditora\""),
    ("Professores / Doutores", "\"Professor\" / \"Professora\" — ou \"Doutor\" / \"Doutora\""),
    ("Forma segura universal", "\"O senhor\" / \"A senhora\" — funciona para qualquer membro sem risco de erro"),
]
for label, content in items:
    add_box(doc, label, content)

doc.add_paragraph()
add_body(doc, "⚠ NUNCA use: \"você\", \"tu\", \"o/a doutor(a)\" para Ministros (título errado), ou \"Vossa Senhoria\" (reservado a autoridades militares/policiais).", italic=True)

add_heading(doc, "Postura e Chegada", level=2)
body_items = [
    "Chegue 15–20 minutos antes. Traje formal (terno ou equivalente).",
    "Ao entrar: aguarde ser convidado a sentar. Diga: \"Bom dia / Boa tarde, senhores. É uma honra estar diante desta banca.\"",
    "Mantenha contato visual com quem faz a pergunta; ao responder, distribua o olhar pelos demais membros.",
    "Fale com ritmo moderado. Pausa breve antes de responder demonstra maturidade.",
    "Não interrompa. Se não entender a pergunta, peça gentilmente: \"O senhor poderia reformular a questão?\"",
]
for item in body_items:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(item)
    run.font.size = Pt(11)

add_heading(doc, "Abertura (antes da 1ª pergunta)", level=2)
add_body(doc, "Bom dia / Boa tarde, Excelências, senhores professores e auditores. É uma honra e um privilégio poder apresentar minha proposta de pesquisa a esta banca de tão elevado gabarito. Estou à disposição para as perguntas.", italic=True, indent=True)

add_divider(doc)
doc.add_paragraph()

# =========================================================
# PERGUNTAS
# =========================================================
perguntas = [
    {
        "n": 1,
        "titulo": "APRESENTAÇÃO PROFISSIONAL",
        "pergunta": "Fale um pouco sobre você — sua trajetória profissional.",
        "criterio": "Experiência profissional e acadêmica (50 pontos)",
        "objetivo": "Avaliar relevância da experiência para o mestrado e capacidade de síntese.",
        "resposta": """Sou engenheiro formado pelo Instituto Militar de Engenharia em 2001. Antes de ingressar na carreira federal, servi ao Exército Brasileiro por sete anos, o que me deu uma base sólida de disciplina, gestão de projetos e liderança em ambientes de alta complexidade.

Em 2009, ingressei na Controladoria-Geral da União como Auditor Federal de Finanças e Controle, onde atuo há mais de 15 anos. Ao longo dessa trajetória, ocupei posições de crescente responsabilidade: fui Diretor de Auditoria de Obras, Secretário-Executivo Substituto, e exerci funções equivalentes ao terceiro escalão ministerial.

No campo acadêmico e da docência, tenho me dedicado à área de controle de obras públicas: publiquei trabalhos sobre aplicação do SINAPI e SICRO em auditorias, ministrei capacitações sobre o tema, e participei de grupos técnicos que contribuíram para a padronização de metodologias de fiscalização.

Minha motivação para o mestrado é transformar essa experiência acumulada em conhecimento científico que possa ser replicado institucionalmente — e contribuir para que o controle público brasileiro se torne mais preditivo e menos reativo diante das falhas em grandes contratações.""",
        "alertas": [
            "Tempo ideal: 2 a 2,5 minutos. Não ultrapasse 3 minutos.",
            "Não liste cargos mecanicamente — conecte cada passo à evolução de competência.",
            "Termine sempre apontando para o futuro (motivação para o mestrado).",
        ]
    },
    {
        "n": 2,
        "titulo": "APRESENTAÇÃO DO PRÉ-PROJETO",
        "pergunta": "Apresente seu projeto de pesquisa.",
        "criterio": "Domínio do tema (30 pts) + Viabilidade da proposta (20 pts)",
        "objetivo": "Verificar se o candidato domina o próprio projeto e sabe explicá-lo com clareza.",
        "resposta": """Meu projeto propõe o desenvolvimento de um Framework de Auditoria Preventiva baseado em Inteligência Artificial para detectar assimetria de informação em anteprojetos de grandes obras públicas — com foco específico nas contratações integradas.

O problema central é que o modelo de contratação integrada, previsto na Lei 13.303/2016 e na Lei 14.133/2021, transfere ao contratado a responsabilidade pelo projeto executivo. Isso cria uma janela estrutural de assimetria de informação: o fornecedor conhece os custos reais e os riscos técnicos; o Estado não. O resultado são sobrepreços, aditivos não previstos e obras que se tornam elefantes brancos.

A proposta aplica técnicas de Processamento de Linguagem Natural para analisar automaticamente os documentos de contratação — anteprojetos, memoriais descritivos, planilhas orçamentárias — cruzando-os com as tabelas SINAPI e SICRO. O sistema identifica padrões linguísticos e orçamentários que, historicamente, precedem irregularidades.

A metodologia é o Design Science Research, que privilegia a produção de artefatos testáveis e com utilidade prática comprovada. O produto final será um artefato validado — um modelo de auditoria — aplicável a auditorias reais do TCU, CGU e demais órgãos de controle.

A urgência deste tema foi reafirmada pelo Acórdão TCU nº 686/2026-Plenário, da relatoria do Ministro Bruno Dantas, que identificou sobrepreço de R$ 506,5 milhões na Ferrovia de Integração Oeste-Leste. Esse caso exemplifica exatamente a falha que meu framework busca detectar de forma preventiva.""",
        "alertas": [
            "Tempo ideal: 3 minutos. Estruture em: Problema → Solução → Método → Produto → Urgência.",
            "Sempre mencione o Acórdão 686/2026 — demonstra atualidade e relevância.",
            "Não use jargão excessivo. A banca quer entender, não ser impressionada por siglas.",
        ]
    },
    {
        "n": 3,
        "titulo": "APLICAÇÃO PRÁTICA",
        "pergunta": "Qual a aplicação prática do seu projeto? Como ele seria utilizado no dia a dia do controle público?",
        "criterio": "Viabilidade da proposta (20 pts) + Domínio do tema (30 pts)",
        "objetivo": "Avaliar se o projeto tem utilidade real ou é apenas teórico.",
        "resposta": """O framework foi concebido para uso operacional direto — não como produto acadêmico que fica na prateleira.

Na prática, quando um órgão público lança uma licitação de grande obra em contratação integrada, o auditor alimenta o sistema com os documentos de contratação: o anteprojeto, o memorial descritivo e a planilha estimativa. O framework realiza três análises simultâneas:

Primeira: análise linguística do anteprojeto em busca de indefinições intencionais — termos vagos que abrem espaço para futuros aditivos. Segunda: análise orçamentária cruzando os quantitativos com SINAPI e SICRO para identificar desvios que podem indicar superfaturamento potencial. Terceira: identificação de padrões históricos — comparando o documento com uma base de contratos auditados anteriormente e que resultaram em irregularidades.

O resultado é um relatório de risco automatizado, que o auditor usa como ponto de partida para aprofundar a análise humana — não para substituí-la.

Um exemplo concreto: se o sistema fosse aplicado ao contrato da FIOL II antes da assinatura, os padrões de superfaturamento que geraram os R$ 506,5 milhões do Acórdão 686/2026 provavelmente teriam sido sinalizados como risco elevado, permitindo intervenção preventiva.

Portanto, a aplicação prática é direta: transformar auditoria reativa em auditoria preventiva, reduzindo o dano ao erário antes que ele ocorra.""",
        "alertas": [
            "Use o exemplo da FIOL II para concretizar — torna a resposta memorável.",
            "Enfatize que a IA auxilia o auditor, não o substitui — isso agrada bancas conservadoras.",
            "Se perguntarem sobre custos de implantação: mencione que as ferramentas de PLN são em grande parte open source (Python/spaCy/BERT), reduzindo custos.",
        ]
    },
    {
        "n": 4,
        "titulo": "FUNDAMENTOS TEÓRICOS",
        "pergunta": "Qual a base teórica do seu projeto? Por que a teoria da assimetria de informação?",
        "criterio": "Domínio do tema (30 pts)",
        "objetivo": "Verificar profundidade do conhecimento acadêmico e coerência entre teoria e objeto.",
        "resposta": """A Teoria da Assimetria de Informação tem raízes sólidas na Economia Institucional e foi premiada com o Nobel de Economia em 2001, concedido a George Akerlof, Michael Spence e Joseph Stiglitz.

Akerlof (1970) demonstrou no artigo "The Market for Lemons" que, quando uma parte tem mais informação que a outra, o mercado produz resultados ineficientes — e em casos extremos, colapsa. Arrow (1963) aplicou essa lógica ao setor público, identificando que relações entre Estado e fornecedores são particularmente vulneráveis à seleção adversa e ao risco moral. Williamson (1985) complementou com a Teoria dos Custos de Transação, mostrando como a especificidade dos ativos em contratos de infraestrutura amplifica esses problemas.

No contexto das contratações integradas, a assimetria é estrutural e intencional: a lei permite que o fornecedor elabore o projeto executivo — que é justamente o documento que define os custos reais. Isso inverte a posição informacional: quem deveria ser fiscalizado detém a informação que o fiscal precisaria para fiscalizar.

Meu framework usa IA para tentar equalizar essa assimetria — identificando automaticamente nos documentos os indícios de que o fornecedor está ocultando informação ou criando ambiguidades que serão exploradas em futuros aditivos.

A coerência entre a teoria e a proposta de solução é, portanto, direta: a teoria explica por que o problema existe; o artefato propõe como detectá-lo antecipadamente.""",
        "alertas": [
            "Cite os autores com segurança: Akerlof (1970), Arrow (1963), Williamson (1985).",
            "Não é necessário entrar em equações — a banca quer compreensão conceitual.",
            "Se perguntarem sobre outras teorias: pode mencionar Principal-Agent Theory (Jensen & Meckling, 1976).",
        ]
    },
    {
        "n": 5,
        "titulo": "METODOLOGIA",
        "pergunta": "Por que você escolheu o Design Science Research como metodologia?",
        "criterio": "Domínio do tema (30 pts) + Viabilidade da proposta (20 pts)",
        "objetivo": "Verificar maturidade metodológica e coerência entre método e objetivo.",
        "resposta": """O Design Science Research — DSR — é a metodologia mais adequada quando o objetivo da pesquisa é produzir um artefato com utilidade prática comprovada, não apenas descrever ou explicar um fenômeno.

Hevner et al. (2004), no artigo seminal publicado no MIS Quarterly, estabeleceram os sete princípios do DSR para sistemas de informação. O que diferencia o DSR de uma pesquisa aplicada comum é o ciclo rigoroso de design, avaliação e refinamento — o artefato é testado iterativamente até demonstrar que resolve o problema para o qual foi criado.

No meu projeto, o problema é detectar assimetria de informação em anteprojetos. O artefato é o framework de auditoria. A validação ocorre em dois estágios: primeiro em casos históricos — contratos já auditados, onde já sabemos o resultado — para calibrar o modelo; depois em casos reais, em ambiente controlado, para verificar a aderência operacional.

A alternativa seria uma pesquisa puramente descritiva ou experimental, mas elas não produziriam um produto utilizável ao final. Para o mestrado profissional, que tem compromisso com a transformação da prática institucional, o DSR é a escolha natural e mais coerente com o edital do ISC/TCU.

Além disso, o DSR tem precedentes consolidados em pesquisas de auditoria e controle: autores como Venable et al. (2016) e Gregor & Hevner (2013) validaram sua aplicação em contextos muito próximos ao meu objeto de pesquisa.""",
        "alertas": [
            "Demonstre que conhece Hevner et al. (2004) — é a referência central do DSR.",
            "Enfatize o compromisso do mestrado PROFISSIONAL com produtos aplicáveis — isso conecta sua escolha ao perfil do programa.",
            "Evite entrar em detalhes excessivos sobre os ciclos do DSR a menos que perguntado.",
        ]
    },
    {
        "n": 6,
        "titulo": "CONTRATAÇÃO INTEGRADA",
        "pergunta": "Por que seu projeto foca em contratação integrada especificamente? Quais os riscos particulares desse modelo?",
        "criterio": "Domínio do tema (30 pts)",
        "objetivo": "Verificar domínio do direito das contratações públicas e dos riscos específicos do objeto.",
        "resposta": """A contratação integrada é o regime mais complexo e de maior risco dentro das modalidades de contratação pública brasileira, justamente porque concentra a assimetria de informação em seu ponto mais crítico: o projeto.

No regime tradicional — regido pela Lei 8.666/1993 e mantido como opção pela Lei 14.133/2021 — o Estado elabora o projeto básico com alto grau de detalhamento antes de licitar. O fornecedor concorre com base em quantitativos precisos. O controle é mais simples porque a informação está disponível.

Na contratação integrada, prevista originalmente no Regime Diferenciado de Contratações — RDC — e incorporada à Lei 13.303/2016 e 14.133/2021, o Estado fornece apenas um anteprojeto. O fornecedor elabora o projeto básico e o executivo, e depois constrói. Isso significa que o licitante vencedor definirá os próprios quantitativos e especificações técnicas — criando um incentivo estrutural para subdimensionar custos na proposta e recuperá-los em aditivos posteriores.

Os riscos específicos são: sobrepreço embutido no anteprojeto vago; aditivos de escopo e prazo sistematicamente subestimados na fase de licitação; e a dificuldade do órgão contratante de contestar o projeto executivo que não elaborou.

O Acórdão 686/2026 e o Acórdão 2.429/2024, ambos do TCU, documentam casos concretos em que esses riscos se materializaram em bilhões de reais de prejuízo ao erário. Eles são a evidência empírica que sustenta a relevância do meu objeto de pesquisa.""",
        "alertas": [
            "Domine a diferença entre contratação integrada e semi-integrada — podem perguntar.",
            "Mencione a Lei 14.133/2021 (Nova Lei de Licitações) — demonstra atualização legislativa.",
            "Os dois acórdãos são seus âncoras de credibilidade — use-os sempre que relevante.",
        ]
    },
    {
        "n": 7,
        "titulo": "INTELIGÊNCIA ARTIFICIAL E PLN",
        "pergunta": "Como exatamente a Inteligência Artificial seria aplicada? Quais técnicas e por quê?",
        "criterio": "Domínio do tema (30 pts) + Viabilidade da proposta (20 pts)",
        "objetivo": "Verificar se o candidato domina tecnicamente a proposta ou apenas usa IA como palavra da moda.",
        "resposta": """A proposta utiliza técnicas de Processamento de Linguagem Natural — PLN — aplicadas a documentos textuais de contratação. Não é IA genérica: são técnicas específicas, escolhidas pela natureza do problema.

Para análise dos anteprojetos, utilizarei modelos de reconhecimento de entidades nomeadas e análise de sentimento negativo — identificando termos que denotam indefinição, como \"a critério do contratado\", \"conforme necessidade\", \"a ser definido no projeto executivo\" — expressões que historicamente antecedem conflitos de escopo.

Para análise orçamentária, utilizarei algoritmos de comparação semântica e extração de quantitativos, cruzando os dados extraídos dos documentos com as tabelas SINAPI — Sistema Nacional de Pesquisa de Custos e Índices da Construção Civil — e SICRO — Sistema de Custos Referenciais de Obras. Desvios estatisticamente significativos em relação às referências oficiais são sinalizados como risco.

Para a classificação de risco, utilizarei modelos de aprendizado supervisionado treinados em um corpus de contratos auditados pelo TCU e CGU, onde o resultado — irregular ou regular — é conhecido. O modelo aprende os padrões que precederam irregularidades e os aplica a novos documentos.

As ferramentas são majoritariamente open source: Python com bibliotecas spaCy e Hugging Face Transformers para PLN; scikit-learn para aprendizado de máquina; e modelos de linguagem pré-treinados em português, como o BERTimbau, ajustados para o domínio jurídico-técnico.

A vantagem desse conjunto é que reduz o custo de implantação e facilita a adoção por órgãos públicos com restrições orçamentárias.""",
        "alertas": [
            "Se a banca não for técnica em IA: enfatize o resultado (detecção de risco), não o processo.",
            "Se houver especialista técnico na banca: esteja pronto para falar de overfitting, viés de dados de treinamento, e métricas de avaliação (precisão, recall, F1).",
            "Mencione BERTimbau — modelo BERT em português — demonstra que você pesquisou soluções específicas para o contexto nacional.",
        ]
    },
    {
        "n": 8,
        "titulo": "DISPONIBILIDADE E COMPROMETIMENTO",
        "pergunta": "Você tem disponibilidade para o mestrado? Há impedimento do seu órgão?",
        "criterio": "Experiência profissional e acadêmica (50 pts) — subfator comprometimento",
        "objetivo": "Verificar se o candidato tem condições reais de concluir o curso.",
        "resposta": """Sim, tenho plena disponibilidade e o apoio formal do meu órgão.

Quanto à disponibilidade de tempo: ao longo dos meus 15 anos na CGU, conciliei funções de alta demanda com estudo, docência e produção técnica. Ministrei capacitações e publiquei trabalhos em paralelo às minhas responsabilidades de gestão. Tenho disciplina e método para gerir múltiplas demandas — e a experiência comprova isso.

Quanto ao apoio institucional: a CGU tem interesse direto nos temas de controle de obras e adoção de tecnologia na auditoria pública. O meu projeto está alinhado com prioridades estratégicas do órgão. Já conversei com minha chefia imediata e há receptividade à minha participação no programa.

Devo mencionar também que o próprio mestrado profissional do ISC/TCU foi desenhado para servidores em atividade — o formato das aulas e a natureza aplicada das pesquisas reconhecem essa realidade. Isso me dá confiança de que o programa e minha situação são compatíveis.

Estou ciente de que o mestrado exige comprometimento sério. Tenho maturidade profissional e motivação genuína para concluí-lo com qualidade.""",
        "alertas": [
            "Não mencione dificuldades de agenda sem apresentar imediatamente a solução.",
            "Se perguntarem sobre afastamento formal (licença para capacitação): informe que está avaliando as opções administrativas disponíveis conforme a Lei 8.112/1990.",
            "Seja genuíno — a banca percebe respostas ensaiadas demais. Use suas próprias palavras.",
        ]
    },
    {
        "n": 9,
        "titulo": "CONTRIBUIÇÃO AO CAMPO",
        "pergunta": "Qual a contribuição original do seu projeto para o campo do controle público?",
        "criterio": "Domínio do tema (30 pts) + Viabilidade da proposta (20 pts)",
        "objetivo": "Verificar se o projeto tem originalidade e potencial de impacto.",
        "resposta": """O projeto tem três contribuições originais que o diferenciam do que já existe na literatura.

A primeira é a integração inédita entre teoria econômica da assimetria de informação e técnicas de Processamento de Linguagem Natural aplicadas especificamente ao domínio das contratações integradas no direito brasileiro. Não há, até onde minha revisão de literatura identificou, framework similar desenvolvido para o contexto institucional e normativo do Brasil.

A segunda é a produção de um artefato validado — não apenas um modelo teórico. O framework será testado em casos reais, com métricas de desempenho mensuráveis. Isso significa que ao final do mestrado existirá um produto que pode ser adotado imediatamente por órgãos de controle.

A terceira é a democratização do conhecimento especializado em auditoria de obras. Hoje, identificar assimetria de informação em anteprojetos exige um auditor experiente com domínio técnico de engenharia e jurídico-contratual — um perfil escasso. O framework permite que auditores com menos experiência específica realizem uma triagem de risco de qualidade, ampliando a capacidade de controle sem necessidade proporcional de ampliação do quadro.

Em termos de impacto potencial: se o framework reduzir em apenas 10% o sobrepreço em obras que passam por contratação integrada, o retorno para o erário seria de bilhões de reais anuais — dado o volume de contratos nessa modalidade no Brasil.

É uma contribuição que conecta ciência e prática, teoria e utilidade — que é exatamente o propósito de um mestrado profissional.""",
        "alertas": [
            "Esta resposta é sua grande síntese. Entregue-a com convicção.",
            "A frase sobre democratização do conhecimento especializado costuma causar impacto positivo em bancas.",
            "Se perguntarem sobre lacunas ou limitações: admita honestamente — dependência de corpus de treinamento, necessidade de atualização contínua das tabelas SINAPI/SICRO.",
        ]
    },
]

for q in perguntas:
    add_heading(doc, f"PERGUNTA {q['n']} — {q['titulo']}", level=1)
    
    add_box(doc, "Critério avaliado", q['criterio'])
    add_box(doc, "Objetivo da banca", q['objetivo'])
    
    p = doc.add_paragraph()
    run = p.add_run(f"❓ \"{q['pergunta']}\"")
    run.bold = True
    run.italic = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x4A, 0x4A, 0x4A)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    
    add_heading(doc, "Resposta Ideal:", level=3)
    
    paragrafos = q['resposta'].strip().split('\n\n')
    for para in paragrafos:
        add_body(doc, para.strip(), indent=True)
    
    add_heading(doc, "Pontos de Atenção:", level=3)
    for alerta in q['alertas']:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(alerta)
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x66, 0x33, 0x00)
        p.paragraph_format.left_indent = Inches(0.4)
    
    add_divider(doc)
    doc.add_paragraph()

# =========================================================
# TABELA ESTRATÉGICA
# =========================================================
add_heading(doc, "TABELA ESTRATÉGICA — RESUMO", level=1)

add_body(doc, "Use esta tabela para revisão rápida na véspera da entrevista:")
doc.add_paragraph()

table = doc.add_table(rows=1, cols=4)
table.style = 'Table Grid'

# Header
hdr = table.rows[0].cells
hdr[0].text = "Pergunta"
hdr[1].text = "Critério (peso)"
hdr[2].text = "Palavras-chave obrigatórias"
hdr[3].text = "Tempo"

for cell in hdr:
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell._tc.get_or_add_tcPr()
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), '1F457A')
    shading.set(qn('w:color'), 'auto')
    shading.set(qn('w:val'), 'clear')
    cell._tc.get_or_add_tcPr().append(shading)

rows_data = [
    ["1. Trajetória", "Experiência (50%)", "IME, Exército, CGU, gestão, docência, SINAPI", "2–2,5 min"],
    ["2. Pré-projeto", "Domínio (30%) + Viab. (20%)", "Assimetria, PLN, SINAPI, SICRO, DSR, Acórdão 686/2026", "3 min"],
    ["3. Aplicação prática", "Viabilidade (20%)", "Relatório de risco, FIOL II, preventivo vs. reativo", "2 min"],
    ["4. Base teórica", "Domínio (30%)", "Akerlof, Arrow, Williamson, seleção adversa", "1,5 min"],
    ["5. Metodologia", "Domínio (30%) + Viab. (20%)", "DSR, Hevner, artefato, validação, mestrado profissional", "2 min"],
    ["6. Contratação integrada", "Domínio (30%)", "Lei 13.303, Lei 14.133, anteprojeto, aditivos", "2 min"],
    ["7. IA/PLN", "Domínio (30%) + Viab. (20%)", "PLN, NER, BERT, BERTimbau, SINAPI cruzamento", "2 min"],
    ["8. Disponibilidade", "Experiência (50%)", "Apoio CGU, disciplina, conciliação, maturidade", "1 min"],
    ["9. Contribuição original", "Domínio (30%) + Viab. (20%)", "Inédito, artefato validado, democratização, impacto", "2 min"],
]

for row_data in rows_data:
    row = table.add_row()
    for i, text in enumerate(row_data):
        row.cells[i].text = text
        for para in row.cells[i].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)

doc.add_paragraph()
add_divider(doc)
doc.add_paragraph()

# =========================================================
# ENCERRAMENTO
# =========================================================
add_heading(doc, "ENCERRAMENTO DA ENTREVISTA", level=1)

add_heading(doc, "Frase de Encerramento:", level=2)
add_body(doc, 
    "Senhores, quero agradecer imensamente a oportunidade e a atenção dispensada. "
    "Esta entrevista reforçou minha convicção de que o ISC/TCU é o ambiente ideal para "
    "transformar minha experiência acumulada em conhecimento científico de utilidade pública. "
    "Fico à disposição para qualquer esclarecimento adicional. Muito obrigado.", 
    italic=True, indent=True)

add_heading(doc, "Lembrete Final:", level=2)
lembretes = [
    "Ao sair: cumprimente individualmente se houver oportunidade. \"Muito obrigado, senhor / senhora.\"",
    "Não demonstre ansiedade após a saída — corredores e áreas comuns ainda são visíveis.",
    "Você foi aprovado nas 3 fases anteriores por mérito. A entrevista é sua oportunidade de confirmar o que o papel já mostrou.",
]
for l in lembretes:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(l)
    run.font.size = Pt(11)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Boa sorte, José. O preparo é a melhor forma de controlar o que pode ser controlado.")
run.bold = True
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x1F, 0x45, 0x7A)
run.italic = True

output_path = "/home/user/Jos-/Roteiro_Entrevista_Mestrado_ISC_TCU.docx"
doc.save(output_path)
print(f"Arquivo salvo: {output_path}")
