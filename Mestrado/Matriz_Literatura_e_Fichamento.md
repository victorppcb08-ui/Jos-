# Matriz Preliminar de Literatura e Fichamento

**Programa:** Mestrado Profissional em Controle da Administração Pública — Processo Seletivo 1/2026
**Linha de atuação:** Linha 2 — Tecnologias para Inovação do Controle e da Gestão Pública
**Projeto:** *Framework de Auditoria Preventiva Baseado em Inteligência Artificial para Detecção de Assimetria de Informação em Anteprojetos de Grandes Obras Públicas: Especificação e Validação no Contexto das Contratações Integradas*
**Autor:** José de Castro Barreto Junior (CGU)

---

## Nota metodológica

As cinco fontes foram selecionadas para cobrir, de forma equilibrada, os quatro pilares teórico-metodológicos do projeto: (i) o fenômeno-problema — a **assimetria de informação e a seleção adversa** (Akerlof, 1970; Nóbrega e Jurubeba, 2020); (ii) a **ponte com o Direito das licitações** brasileiro (Nóbrega e Jurubeba, 2020); (iii) o **método de construção do artefato** — a *Design Science Research* (Hevner *et al.*, 2004); e (iv) o **domínio de aplicação da IA no setor público** e o estado da arte da detecção de irregularidades em contratações (Wirtz, Weyerer e Geyer, 2019; dos Santos *et al.*, 2025). Priorizaram-se obras seminais (fundamentação conceitual), uma fonte nacional que conecta a teoria ao objeto jurídico e uma revisão empírica recente (2025) que evidencia lacunas do estado da arte ocupadas pela pesquisa.

---

## Parte 1 — Matriz preliminar de literatura

### 1.1 Visão comparativa (matriz)

| # | Fonte | Pergunta/Objetivo | Base teórica/conceitos | Método | Achados principais | Limitações | Contribuição para o projeto |
|---|-------|-------------------|------------------------|--------|--------------------|------------|-----------------------------|
| 1 | **Akerlof (1970)** — *The Market for "Lemons"* | Como a incerteza sobre a qualidade afeta o funcionamento dos mercados? | Economia da informação; seleção adversa; qualidade e incerteza | Modelagem teórico-econômica (analítico-dedutiva) | A informação privada do vendedor faz o produto ruim expulsar o bom, reduzindo preço/volume e podendo colapsar o mercado | Modelo abstrato; trata seleção adversa (não risco moral); sem aplicação à contratação pública | Alicerce teórico do problema: o anteprojeto deficiente é o "limão"; justifica mecanismos de revelação de informação |
| 2 | **Nóbrega e Jurubeba (2020)** — Assimetrias de informação na nova lei de licitações | Como a assimetria/seleção adversa se manifesta na Lei 14.133/2021 e como *signaling*/*screening* podem mitigá-la? | Economia da informação (Akerlof, Spence, Stiglitz); *signaling* e *screening*; Análise Econômica do Direito | Ensaio teórico-jurídico/doutrinário (qualitativo); análise normativa | Critérios de habilitação são insuficientes para revelar a qualidade dos licitantes; a Nova Lei avançou timidamente em regras de revelação | Ensaio sem validação empírica; foco na habilitação, não no anteprojeto; não trata de IA | Traduz a teoria para o Direito brasileiro das licitações; oferece o vocabulário (*signaling*/*screening*/seleção adversa) e reforça a atuação *ex ante* |
| 3 | **Hevner *et al.* (2004)** — Design Science in IS Research | Como conduzir e avaliar pesquisa rigorosa e relevante orientada a artefatos? | *Design Science*; ciclos de rigor e relevância; tipos de artefato | Ensaio conceitual/metodológico; proposição de framework e 7 diretrizes | Sete diretrizes da DSR equilibrando rigor e relevância e exigindo avaliação sistemática do artefato | Diretrizes genéricas; origem em SI corporativos; avaliação nem sempre trivial | Alicerce metodológico: estrutura as 4 fases do projeto e o critério de avaliação (estudo de casos, triangulação, entrevistas) |
| 4 | **Wirtz, Weyerer e Geyer (2019)** — AI and the Public Sector | Quais as aplicações e os desafios da IA no setor público? | Governo digital; taxonomias de IA; governança tecnológica | Revisão integrativa/conceitual da literatura | 10 áreas de aplicação; desafios técnicos, jurídicos, éticos e sociais; lacuna entre potencial e adoção | Estudo conceitual, sem validação empírica; anterior aos LLMs; não setorizado para obras | Situa o framework na IA no setor público e fornece a moldura de desafios (ética, explicabilidade, robustez), convergente com a OCDE |
| 5 | **dos Santos *et al.* (2025)** — Fraud detection in public procurement | Como métodos *data-driven* vêm sendo aplicados à detecção de fraude em contratações? | Ciência de dados; *machine learning*; indicadores de risco (*red flags*); análise de redes; PLN | Mapeamento sistemático da literatura (6.000+ triados; 93 selecionados) | Predomínio de ML para conluio e estatística para favoritismo; baseados em *red flags*; poucos chegam a sistemas reais | Foco reativo (fraude *ex post*); PLN de documentos técnicos subexplorado; escassez de *datasets* públicos | Evidencia o estado da arte e as lacunas (prevenção, PLN de documentos de engenharia, aplicação real) que o projeto ocupa |

### 1.2 Detalhamento por fonte

#### Fonte 1 — AKERLOF, George A. (1970)

- **Pergunta/objetivo:** demonstrar como a incerteza quanto à qualidade dos bens — decorrente da assimetria de informação entre vendedor e comprador — afeta o funcionamento e a própria existência dos mercados.
- **Base teórica/conceitos:** economia da informação; seleção adversa (*adverse selection*); relação qualidade–incerteza; papel das instituições (garantias, marcas, certificações, licenciamento) como respostas à assimetria. Utiliza o mercado de carros usados (os *lemons*) como modelo, com extensões para seguros, crédito e mercados de trabalho.
- **Método:** modelagem teórico-econômica de caráter analítico-dedutivo; construção de modelo formal ilustrado por exemplos.
- **Achados principais:** quando o vendedor detém informação privada sobre a qualidade, os produtos de má qualidade tendem a expulsar os bons do mercado; a assimetria reduz o preço e o volume transacionados e pode inviabilizar o mercado; instituições e mecanismos de sinalização emergem para mitigar o problema.
- **Limitações:** modelo abstrato e estilizado; concentra-se na seleção adversa (não modela risco moral nem contratos incompletos de longo prazo); não trata de contratação pública nem de análise de documentos técnicos; sem validação empírica no próprio artigo.
- **Contribuição para o projeto:** fornece o fundamento conceitual do fenômeno que a pesquisa combate. Nas contratações integradas, o anteprojeto com lacunas técnicas equivale ao "limão": o Estado transaciona sob informação incompleta, e o particular, detentor do conhecimento de projeto, explora a assimetria. Justifica teoricamente a necessidade de mecanismos de revelação/verificação de informação na fase pré-licitatória — precisamente o que o framework de IA operacionaliza.

#### Fonte 2 — NÓBREGA, Marcos; JURUBEBA, Diego Franco de Araújo (2020)

- **Pergunta/objetivo:** analisar como a assimetria de informação e o problema da seleção adversa se manifestam na Nova Lei de Licitações (Lei 14.133/2021), examinando dispositivos de habilitação e a possibilidade de empregar mecanismos de *signaling* e *screening* para mitigar a assimetria entre a Administração e os licitantes.
- **Base teórica/conceitos:** economia da informação (Akerlof, Spence, Stiglitz/Rothschild); seleção adversa; sinalização (*signaling*) e filtragem (*screening*); a licitação como mecanismo de revelação de informação; conhecimento disperso (Hayek); Análise Econômica do Direito.
- **Método:** ensaio teórico-jurídico/doutrinário, de abordagem qualitativa; revisão de literatura combinada com análise normativa dos dispositivos legais sob a ótica da análise econômica do direito.
- **Achados principais:** os critérios tradicionais de habilitação (Lei 8.666/93 e legislação correlata) são insuficientes para revelar as verdadeiras qualidades dos licitantes, mantendo "anuviada" informação relevante (governança, capacidade administrativa, qualidade da execução); a Nova Lei "perdeu grande oportunidade" de avançar em regras de revelação de informação, embora contenha, de forma tímida, mecanismos de *signaling* e *rating* bem-vindos.
- **Limitações:** ensaio doutrinário sem validação empírica; foco na fase de habilitação, sem tratar especificamente do anteprojeto de engenharia nem do regime de contratação integrada; não considera soluções tecnológicas/IA; transposição simplificada dos modelos econômicos para o Direito.
- **Contribuição para o projeto:** constrói a ponte direta entre a teoria econômica da informação e o Direito brasileiro das licitações, oferecendo o arcabouço conceitual (*signaling*, *screening*, seleção adversa) que o projeto adota e **estende da habilitação para o anteprojeto**. Reforça a tese central de que a mitigação da assimetria deve ocorrer *ex ante*, no desenho do certame — exatamente o momento pré-licitatório em que o framework atua. *(Fonte selecionada para o fichamento — Parte 2.)*

#### Fonte 3 — HEVNER, Alan R.; MARCH, Salvatore T.; PARK, Jinsoo; RAM, Sudha (2004)

- **Pergunta/objetivo:** estabelecer um arcabouço conceitual e diretrizes para conduzir e avaliar pesquisa em Sistemas de Informação orientada à criação de artefatos, conciliando rigor científico e relevância prática.
- **Base teórica/conceitos:** ciências do artificial (Simon); contraste entre os paradigmas *behavioral science* e *design science*; ciclos de rigor e relevância; tipologia de artefatos (*constructs*, *models*, *methods*, *instantiations*).
- **Método:** ensaio conceitual/metodológico; proposição de um framework conceitual e de sete diretrizes para a *Design Science Research* (DSR).
- **Achados principais:** as sete diretrizes — (1) o design como artefato; (2) relevância do problema; (3) avaliação do design; (4) contribuições de pesquisa; (5) rigor da pesquisa; (6) design como processo de busca; e (7) comunicação da pesquisa — orientam a produção e a avaliação sistemática do artefato, equilibrando rigor e relevância.
- **Limitações:** diretrizes genéricas e não prescritivas quanto a técnicas específicas; concebidas para SI corporativos, exigindo adaptação ao setor público; a exigência de avaliação rigorosa nem sempre é facilmente satisfeita em contextos organizacionais reais.
- **Contribuição para o projeto:** é o alicerce metodológico da pesquisa, que se propõe a produzir um artefato (o framework). As sete diretrizes estruturam as quatro fases do projeto (identificação do problema → modelagem/especificação da arquitetura → desenvolvimento demonstrativo → avaliação) e fundamentam o critério de avaliação por estudo de casos com triangulação retrospectiva e entrevistas com especialistas, além de legitimar o mestrado profissional orientado à solução.

#### Fonte 4 — WIRTZ, Bernd W.; WEYERER, Jan C.; GEYER, Carolin (2019)

- **Pergunta/objetivo:** oferecer uma visão integrativa das principais aplicações da Inteligência Artificial no setor público e dos desafios a elas associados.
- **Base teórica/conceitos:** governo digital/*e-government*; taxonomias de aplicação de IA; governança de tecnologia; abordagem conceitual-integrativa da literatura.
- **Método:** revisão integrativa/conceitual da literatura científica, com síntese qualitativa; proposição de dez áreas de aplicação de IA no setor público e mapeamento dos desafios em dimensões (tecnologia/implementação, direito/regulação, ética e sociedade).
- **Achados principais:** a IA tem amplo potencial em funções públicas, inclusive de fiscalização e detecção; persiste uma lacuna entre potencial e adoção efetiva; os desafios não são apenas técnicos, mas também jurídicos, éticos (transparência, explicabilidade, viés) e sociais, exigindo governança responsável.
- **Limitações:** estudo conceitual, sem validação empírica; caráter genérico (não setorizado para auditoria de obras); baseia-se em literatura anterior a 2018, precedendo os avanços recentes de PLN (grandes modelos de linguagem); perspectiva internacional, não brasileira.
- **Contribuição para o projeto:** situa o framework no campo consolidado da IA no setor público e fornece a moldura de desafios (ética, explicabilidade, robustez) que dialoga diretamente com os princípios da OCDE citados no projeto. Reforça que a inovação tecnológica no controle exige o tratamento de aspectos de governança, e não apenas de viabilidade técnica, sustentando a aderência à Linha 2 do programa.

#### Fonte 5 — dos SANTOS, Everton Schneider; dos SANTOS, Matheus Machado; CASTRO, Márcio; CARVALHO, Jônata Tyska (2025)

- **Pergunta/objetivo:** mapear sistematicamente como métodos *data-driven* (aprendizado de máquina, estatística, análise de redes e PLN) vêm sendo aplicados à detecção de fraude e irregularidades em contratações públicas.
- **Base teórica/conceitos:** ciência de dados aplicada ao controle; aprendizado de máquina; indicadores de risco de corrupção (*Corruption Risk Indicators*)/*red flags*; análise de redes; processamento de linguagem natural.
- **Método:** mapeamento sistemático da literatura (*systematic mapping study*), com triagem de mais de 6.000 trabalhos e seleção final de 93, categorizados por tipo de fraude, técnica empregada e fonte de dados.
- **Achados principais:** a maioria dos trabalhos emprega *machine learning* para detectar conluio e análise estatística para favoritismo; predominam abordagens baseadas em *red flags*/indicadores de risco; o uso de PLN sobre dados textuais ainda é pouco explorado; poucas soluções são efetivamente implementadas em sistemas reais.
- **Limitações:** foco predominantemente reativo (detecção de fraude *ex post*); escassez de aplicação em sistemas reais para descobrir novos casos; falta de *datasets* públicos, o que dificulta a replicação e a disseminação das metodologias.
- **Contribuição para o projeto:** evidência empírica e atualizada que fundamenta e, ao mesmo tempo, diferencia a pesquisa. Confirma a viabilidade e a tendência do uso de métodos *data-driven* no controle das contratações; e, sobretudo, identifica lacunas — foco preventivo, análise textual (PLN) de documentos técnicos e aplicação em casos reais — que o framework proposto ocupa de forma original, ao atuar na fase pré-licitatória sobre anteprojetos de engenharia, com cruzamento das tabelas referenciais SINAPI/SICRO. Reforça, ainda, a exigência de validação em casos reais, alinhada ao DSR.

---

## Parte 2 — Fichamento

### 2.1 Referência completa da obra fichada

NÓBREGA, Marcos; JURUBEBA, Diego Franco de Araújo. **Assimetrias de informação na nova Lei de Licitações e o problema da seleção adversa.** *Revista Brasileira de Direito Público – RBDP*, Belo Horizonte, ano 18, n. 69, p. 9-32, abr./jun. 2020. (Versão atualizada em ago. 2021, disponível em: licitacaoecontrato.com.br.)

### 2.2 Síntese das principais ideias, argumentos e achados

O artigo aplica o instrumental da **Análise Econômica do Direito** ao regime das contratações públicas, tomando como marco a edição da Nova Lei de Licitações (Lei 14.133/2021). A tese central dos autores é que o estudo jurídico das licitações no Brasil, tradicionalmente confinado à análise descritiva das normas, precisa avançar para **explicar, prever e compreender o comportamento dos atores** envolvidos no certame — e que a economia da informação oferece as ferramentas para isso.

Os autores partem da noção de **assimetria de informação**: a distribuição desigual de conhecimento entre as partes de uma transação. Recuperam os fundamentos seminais da teoria — o problema dos "limões" de **Akerlof** (a má qualidade expulsa a boa quando o comprador não a distingue), a **sinalização** de **Spence** e a **filtragem** de **Stiglitz/Rothschild** — e o argumento de **Hayek** sobre o conhecimento disperso na sociedade. A partir daí, sustentam que a licitação deve ser entendida como um **mecanismo de revelação de informação**: seu desenho institucional determina quanta informação relevante sobre os licitantes se torna observável pela Administração.

O argumento aplicado é que os **critérios de habilitação** vigentes (herdados da Lei 8.666/93 e da legislação correlata) são **insuficientes** para revelar as verdadeiras qualidades dos licitantes. Requisitos como regularidade fiscal ou qualificação técnica capturam pouco; aspectos decisivos — governança corporativa, capacidade administrativa, qualidade e quantidade efetivas dos bens e serviços na execução — permanecem "anuviados pelo manto da assimetria informacional". Disso decorre risco de **seleção adversa**: na ausência de bons sinais, o licitante de pior qualidade pode prevalecer.

O principal **achado crítico-normativo** é que a Nova Lei de Licitações **perdeu uma oportunidade relevante** de avançar em regras de revelação de informação e de redução de assimetrias, ainda que contenha, de forma tímida, dispositivos de *signaling* e *rating* que representam avanços bem-vindos. A conclusão adverte contra a leitura do novo marco pelas lentes de um "retrovisor jurisprudencial" e da doutrina tradicional, defendendo a incorporação de mecanismos econômicos de desenho de incentivos.

### 2.3 Análise crítica (pontos fortes e limitações)

**Pontos fortes.** (i) **Rigor teórico e interdisciplinaridade:** o texto mobiliza com precisão autores centrais da economia da informação (todos laureados com o Nobel) e os articula ao Direito das licitações, o que é raro na doutrina nacional. (ii) **Relevância e atualidade:** trata do marco legal em vigor (Lei 14.133/2021), com implicações diretas para a prática do controle. (iii) **Poder explicativo:** ao enquadrar a licitação como mecanismo de revelação, os autores deslocam o foco da mera legalidade formal para os **incentivos** e o comportamento estratégico dos atores — perspectiva fértil para o controle. (iv) **Clareza conceitual:** distingue com didatismo seleção adversa, *signaling* e *screening*.

**Limitações.** (i) **Ausência de validação empírica:** trata-se de ensaio doutrinário; não há dados, casos ou testes que dimensionem a magnitude do problema no Brasil. (ii) **Recorte na habilitação:** a análise concentra-se na fase de qualificação dos licitantes, **não abordando o anteprojeto de engenharia** nem, especificamente, o regime de **contratação integrada** — em que a assimetria é ainda mais aguda, pois o particular elabora os projetos básico e executivo. (iii) **Silêncio quanto a soluções tecnológicas:** o artigo diagnostica o problema e sugere mecanismos jurídico-econômicos, mas não explora instrumentos de **IA/PLN** para operacionalizar a revelação de informação. (iv) **Transposição simplificada:** a aplicação dos modelos econômicos ao Direito é, por vezes, mais ilustrativa do que formal.

### 2.4 Conexão com o projeto de pesquisa

O artigo é **base conceitual direta** do projeto e, ao mesmo tempo, delimita com clareza o **espaço de contribuição original** da dissertação. A conexão se dá em quatro planos:

1. **Fundamentação do problema.** Nóbrega e Jurubeba confirmam, no plano jurídico-econômico nacional, a hipótese que sustenta a pesquisa: a licitação brasileira convive com assimetria de informação estrutural e risco de seleção adversa. O projeto **transpõe** esse diagnóstico da fase de habilitação para o **anteprojeto de engenharia**, onde a assimetria — reconhecida pelo próprio TCU no Acórdão 686/2026-Plenário — se materializa em lacunas técnicas (ausência de sondagens, falhas de dimensionamento, inconformidade com SINAPI/SICRO).

2. **Vocabulário e moldura teórica.** O projeto adota os conceitos de *signaling*, *screening* e seleção adversa aqui sistematizados, integrando-os à teoria da agência e dos custos de transação (Williamson) que compõem seu referencial.

3. **Ocupação da lacuna.** As três principais limitações do artigo — ausência de validação empírica, silêncio sobre o anteprojeto/contratação integrada e sobre soluções tecnológicas — correspondem, justamente, ao **objeto do projeto**: um framework de IA (PLN + cruzamento referencial) que **operacionaliza a revelação de informação** *ex ante*, validado em editais reais de contratação integrada.

4. **Deslocamento do momento de intervenção.** O artigo defende a mitigação da assimetria no **desenho do certame**; o projeto concretiza essa intervenção na etapa **pré-licitatória**, único momento em que a correção é viável sem configurar o *periculum in mora* reverso documentado pelo TCU. Assim, a pesquisa avança do plano **normativo** (o que a lei deveria prever) para o plano **instrumental** (como o controle pode detectar e mitigar a assimetria na prática).

---

## Referências

AKERLOF, George A. The market for "lemons": quality uncertainty and the market mechanism. **The Quarterly Journal of Economics**, Cambridge, v. 84, n. 3, p. 488-500, 1970.

DOS SANTOS, Everton Schneider; DOS SANTOS, Matheus Machado; CASTRO, Márcio; CARVALHO, Jônata Tyska. Detection of fraud in public procurement using data-driven methods: a systematic mapping study. **EPJ Data Science**, [s. l.], v. 14, art. 52, 2025. DOI: 10.1140/epjds/s13688-025-00569-3.

HEVNER, Alan R.; MARCH, Salvatore T.; PARK, Jinsoo; RAM, Sudha. Design science in information systems research. **MIS Quarterly**, Minneapolis, v. 28, n. 1, p. 75-105, 2004.

NÓBREGA, Marcos; JURUBEBA, Diego Franco de Araújo. Assimetrias de informação na nova Lei de Licitações e o problema da seleção adversa. **Revista Brasileira de Direito Público – RBDP**, Belo Horizonte, ano 18, n. 69, p. 9-32, abr./jun. 2020.

WIRTZ, Bernd W.; WEYERER, Jan C.; GEYER, Carolin. Artificial intelligence and the public sector—applications and challenges. **International Journal of Public Administration**, New York, v. 42, n. 7, p. 596-615, 2019. DOI: 10.1080/01900692.2018.1498103.
