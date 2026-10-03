# Concepção Integrada da Pesquisa e do PTT

**Mestrado Profissional em Controle da Administração Pública — Instituto Serzedello Corrêa (ISC/TCU)**
**Disciplina: Metodologia Científica**
**Discente:** José de Castro Barreto Junior — Controladoria-Geral da União (CGU)
**Linha de Atuação:** Linha 2 — Tecnologias para Inovação do Controle e da Gestão Pública

> Formulário preenchido em correlação direta com o Projeto de Pesquisa
> *"Framework de Auditoria Preventiva Baseado em Inteligência Artificial para Detecção de Assimetria
> de Informação em Anteprojetos de Grandes Obras Públicas: Especificação e Validação no Contexto das
> Contratações Integradas"* (Processo Seletivo 1/2026).

---

## PARTE I — PROPOSTA DE PESQUISA

### 1. Qual o tema (assunto) mais abrangente da pesquisa?

O uso de **tecnologias de Inteligência Artificial (IA) e Processamento de Linguagem Natural (PLN) no
controle preventivo de obras públicas**, mais especificamente a aplicação dessas tecnologias para
detectar e mitigar **assimetrias de informação** em documentos técnicos da fase pré-licitatória de
grandes obras contratadas pelo regime de contratação integrada. O tema situa-se na interseção entre
controle governamental, economia da informação aplicada aos contratos administrativos e inovação
tecnológica aplicada à auditoria.

### 2. A partir do tema, defina um problema a partir do qual será realizada a investigação científica

No regime de contratação integrada (Leis nº 13.303/2016 e 14.133/2021), o poder público define o
objeto por meio de **anteprojeto de engenharia**, transferindo ao vencedor do certame a elaboração
dos projetos básico e executivo. Essa estrutura cria uma **assimetria de informação estrutural**: o
contratado, detentor de conhecimento técnico especializado, pode explorar lacunas do anteprojeto
(ausência de sondagens, falhas de dimensionamento de insumos, especificações inadequadas,
inconformidade com tabelas referenciais) para viabilizar **pleitos oportunistas de reequilíbrio
econômico-financeiro**. O problema é que o controle predominante é **reativo, amostral e dependente
da expertise individual do auditor**, sendo frequentemente acionado quando a correção já é inviável —
como demonstrou o Acórdão nº 686/2026-Plenário (TCU), no qual a irregularidade foi reconhecida, mas o
certame já adjudicado não pôde ser suspenso (*periculum in mora* reverso). Falta aos órgãos de
controle um instrumento sistemático, objetivo e replicável capaz de identificar essas assimetrias
**antes da licitação**, quando a correção ainda produz efeito sem gerar dano superior à irregularidade.

### 3. Quais os possíveis beneficiários da sua pesquisa?

- **Órgãos de controle interno e externo** — auditores da CGU e do TCU (usuários finais diretos do
  artefato), que passam a dispor de instrumento objetivo para a auditoria preventiva pré-licitatória;
- **Órgãos e entidades contratantes** (gestores públicos federais, estaduais e municipais executores
  de grandes obras), que podem corrigir anteprojetos antes do certame e reduzir aditivos;
- **Equipes de TI dos órgãos de controle**, como parceiras de implementação/replicação da arquitetura;
- **Gestores de programas de integridade** (reforçados pelo Decreto nº 12.304/2024 para contratos de
  grande vulto), como usuários do painel de alertas e da matriz de riscos;
- **O erário e o cidadão** — destinatário final das políticas de infraestrutura —, beneficiados pela
  maior economicidade e pela prevenção de desequilíbrios contratuais;
- **A comunidade acadêmica e demais Tribunais de Contas**, pela replicabilidade do protocolo
  metodológico e do catálogo de indutores de assimetria.

### 4. Qual seria a proposta de título para a pesquisa?

**Framework de Auditoria Preventiva Baseado em Inteligência Artificial para Detecção de Assimetria de
Informação em Anteprojetos de Grandes Obras Públicas: Especificação e Validação no Contexto das
Contratações Integradas.**

*(Título alternativo/sintético: "Auditoria preventiva assistida por IA: detecção de assimetria de
informação em anteprojetos de contratação integrada".)*

---

## PARTE II — ESPECIFICAÇÃO DA PESQUISA

### 5. Qual seria a pergunta a ser respondida pela sua pesquisa?

Como um **framework baseado em Inteligência Artificial** pode identificar e mitigar sistematicamente as
**assimetrias de informação em anteprojetos de grandes obras públicas**, contribuindo para a prevenção
de desequilíbrios contratuais (pleitos de reequilíbrio econômico-financeiro) nas contratações
integradas?

### 6. Pretende testar hipóteses na sua pesquisa? Qual(is) seria(m)?

A pesquisa é de **natureza aplicada e abordagem qualitativa**, estruturada segundo o *Design Science
Research*; nesse paradigma, o foco é a **construção e avaliação de um artefato**, e não o teste
estatístico-confirmatório de hipóteses. Ainda assim, a investigação é orientada por **proposições (ou
hipóteses de trabalho)** que podem ser avaliadas na fase de validação:

- **H1** — Os indutores de assimetria de informação recorrentes nos anteprojetos de contratação
  integrada podem ser **codificados em um número finito de categorias objetivas e verificáveis**
  (lacunas em projetos/sondagens; falhas de dimensionamento de insumos; inadequação de especificações
  técnicas/metodologias construtivas; inconformidade com SINAPI/SICRO).
- **H2** — Esses indutores, uma vez operacionalizados como **regras algorítmicas apoiadas em PLN e
  cruzamento referencial**, permitem **sinalizar antecipadamente** (na fase pré-licitatória) riscos que,
  retrospectivamente, correspondem a achados reais de auditoria.
- **H3** — A aplicação do framework a editais reais **reproduz (triangula)**, de forma preventiva,
  achados que no mundo real só foram reconhecidos em fase reativa — demonstrando o ganho de tempestividade.

### 7. Qual o propósito/objetivo principal da sua pesquisa?

**Projetar e especificar um framework de auditoria preventiva baseado em Inteligência Artificial** para
análise de conformidade técnica e econômica de anteprojetos de engenharia de obras de grande vulto,
gerando **especificação técnica e protótipo demonstrativo** diretamente aplicáveis pelos órgãos de
controle interno e externo da Administração Pública brasileira.

### 8. Que objetivos específicos você pretende alcançar com a pesquisa?

a) **Mapear e sistematizar os indutores de assimetria de informação** em anteprojetos, a partir da
jurisprudência do TCU e dos relatórios de auditoria da CGU, com codificação temática em quatro
categorias: (i) lacunas em projetos (geotecnia, sondagem); (ii) falhas de dimensionamento de insumos;
(iii) inadequação de especificações técnicas e metodologias construtivas; (iv) inconformidade com as
tabelas referenciais SINAPI/SICRO.

b) **Operacionalizar os parâmetros técnicos de verificação por tipologia construtiva** — critérios de
conformidade por categoria de serviço, requisitos mínimos de caracterização de fontes de materiais
(jazidas, areais, pedreiras) e limiares de alerta para desvios frente às tabelas referenciais de preços.

c) **Projetar a arquitetura lógica do framework em três camadas funcionais**: (i) ingestão e
normalização documental; (ii) motor de conformidade baseado em PLN com cruzamento SINAPI/SICRO;
(iii) painel de alertas e relatório de riscos (demonstrativo).

d) **Validar o framework especificado** mediante estudo de casos aplicado a **três editais reais** de
obras de grande vulto (edificação, rodovia, ferrovia), com **triangulação retrospectiva** dos achados
de auditoria e **entrevistas semiestruturadas** com especialistas em auditoria de obras, engenharia e
controle governamental.

---

## PARTE III — REVISÃO DE LITERATURA

### 9. Que estudos anteriores poderiam estar relacionados ao seu tema/problema? (apresentar pelo menos 2 fontes/referências)

1. **AKERLOF, George A. (1970) — "The market for 'lemons': quality uncertainty and the market
   mechanism"** (*The Quarterly Journal of Economics*, v. 84, n. 3). Fundamento seminal da economia da
   informação: demonstra que mercados com assimetria informacional tendem à **seleção adversa**.
   Aplica-se diretamente às contratações integradas — o próprio TCU, no Voto do Acórdão 686/2026,
   nominou o fenômeno como "assimetria de informações entre os licitantes".

2. **HEVNER, Alan R. et al. (2004) — "Design science in information systems research"** (*MIS
   Quarterly*, v. 28, n. 1). Arcabouço metodológico (*Design Science Research*) que orienta a produção
   de conhecimento pela **criação e avaliação de artefatos** para resolver problemas organizacionais
   concretos — base metodológica do framework proposto e adequado ao mestrado profissional.

3. **WIRTZ, Bernd W. et al. (2019) — "Artificial intelligence in the public sector: a research
   agenda"** (*International Journal of Public Administration*, v. 42, n. 7). Documenta a crescente
   aplicação de IA/PLN em funções de fiscalização governamental e organiza a agenda de pesquisa que
   sustenta a dimensão tecnológica da proposta.

*(Referências complementares já levantadas: ARROW (1963) sobre risco moral; STIGLITZ (2002) sobre
intervenção estatal corretiva; WILLIAMSON (1985) sobre custos de transação e contratos incompletos;
GRIMSEY & LEWIS (2004) sobre PPPs e finanças de projeto; DEVLIN et al. (2019) sobre BERT/PLN; além da
jurisprudência do TCU — Acórdãos nº 686/2026 e nº 2.429/2024 — e dos marcos normativos: Leis nº
13.303/2016 e 14.133/2021, Decreto nº 12.304/2024, Manual de Auditoria de Obras Públicas do TCU e
Recommendation of the Council on AI da OCDE, 2019.)*

### 10. Até o momento, que conceitos, abordagens, autores ou possíveis referenciais parecem úteis para compreender seu problema de pesquisa? Explique brevemente por quê.

A revisão organiza-se em **quatro eixos**:

- **Economia da informação e dos contratos** — **Akerlof (seleção adversa)**, **Arrow (risco
  moral)**, **Stiglitz (intervenção corretiva às falhas de mercado)** e **Williamson (custos de
  transação e contratos incompletos)**, com **Grimsey & Lewis** para contratos de infraestrutura.
  *Por quê:* fornecem a lente teórica que explica **por que** o anteprojeto deficiente gera
  comportamento oportunista e desequilíbrio — exatamente o fenômeno que a jurisprudência do TCU descreve
  em linguagem econômica.

- **Controle governamental, accountability e auditoria preventiva** — relação **principal-agente**
  aplicada ao setor público; a distinção **controle reativo × preventivo**; o conceito de **momento
  pré-licitatório** como janela tempestiva de intervenção. *Por quê:* fundamenta a tese central de que
  a correção eficaz ocorre antes da adjudicação (evitando o *periculum in mora* reverso do Acórdão
  686/2026).

- **Contratação integrada e grandes obras públicas** — Leis nº 13.303/2016 e 14.133/2021; anteprojeto,
  precisão orçamentária, matriz de riscos e reequilíbrio; integridade (Decreto nº 12.304/2024).
  *Por quê:* delimita o objeto normativo e os pontos concretos onde a assimetria se materializa.

- **IA, PLN e Design Science Research aplicados ao controle** — **Wirtz et al. (IA no setor
  público)**, **Devlin et al. (BERT/PLN)** e **Hevner et al. (DSR)**. *Por quê:* oferecem,
  respectivamente, a justificativa de aplicabilidade da IA ao controle, a tecnologia de análise
  documental e o método de construção/validação do artefato.

---

## PARTE IV — EVIDÊNCIAS E INFORMAÇÕES NECESSÁRIAS À PESQUISA

### 11. Que dados/informações você projetaria que seriam necessários(as) para sua pesquisa?

- **Jurisprudência do TCU** sobre contratação integrada e obras de grande vulto (acórdãos, votos,
  relatórios de fiscalização), 2017–2026;
- **Relatórios de auditoria da CGU** sobre grandes obras (achados, apontamentos técnicos);
- **Editais e documentos técnicos reais** de três contratações integradas (anteprojetos de engenharia,
  memoriais descritivos, planilhas orçamentárias, matrizes de riscos, especificações técnicas);
- **Tabelas referenciais de preços e produtividade** — SINAPI (Caixa) e SICRO (DNIT);
- **Normativos** (Leis nº 13.303/2016 e 14.133/2021, Decreto nº 12.304/2024, Manual de Auditoria de
  Obras Públicas do TCU);
- **Conhecimento especializado** — obtido em entrevistas semiestruturadas com auditores, engenheiros e
  gestores de integridade, para validar os parâmetros e o artefato;
- **Literatura científica** (Scopus, Web of Science, Google Scholar via Portal de Periódicos CAPES).

### 12. Características dos dados que você pretende trabalhar

Predominantemente **dados textuais não estruturados e semiestruturados** (anteprojetos, memoriais,
votos e relatórios de auditoria em PDF/texto), a serem tratados por **PLN**; **dados estruturados e
tabulares** (planilhas orçamentárias, tabelas referenciais SINAPI/SICRO — valores, códigos de serviço,
quantitativos); **dados contábeis/financeiros** (orçamentos, valores contratados, aditivos);
**transcrições de áudio** das entrevistas (convertidas em texto para análise de conteúdo); e, de forma
acessória, **documentos técnicos de engenharia** (sondagens, caracterização de jazidas). Em síntese:
uma combinação de **dados textuais + planilhas/dados financeiros + transcrições**.

### 13. Onde você imagina obter essas informações/evidências? Haveria dificuldade de acesso, disponibilidade, autorização, tempo ou outro obstáculo previsível?

- **Fontes públicas e abertas:** jurisprudência em `pesquisa.apps.tcu.gov.br`; tabelas SINAPI
  (Caixa) e SICRO (DNIT); legislação; literatura via Portal CAPES. **Baixa dificuldade de acesso.**
- **Fontes internas/institucionais:** relatórios de auditoria da CGU (Sistema **e-Aud**), acessíveis ao
  pesquisador na condição de servidor da CGU; editais e documentos técnicos dos órgãos contratantes.
- **Entrevistas:** dependem de **disponibilidade de agenda** dos especialistas e de **anuência**.

**Obstáculos previsíveis:** (i) **heterogeneidade e qualidade dos documentos** (PDFs digitalizados/
imagem exigindo OCR, formatos não padronizados), que afeta a ingestão por PLN; (ii) **disponibilidade
dos editais completos** com todos os anexos técnicos; (iii) **tempo e agenda** para as entrevistas e
sua transcrição; (iv) eventual necessidade de **autorização/anonimização** para uso de documentos de
auditoria ainda não públicos; (v) **curadoria** das tabelas referenciais (versões por data-base). Todos
são mitigáveis com seleção criteriosa de casos já encerrados/públicos e pré-processamento documental.

### 14. Os dados de interesse possuem algum tipo de sigilo ou são dados pessoais sensíveis?

A **maior parte é pública** (jurisprudência, legislação, tabelas referenciais, editais homologados).
Podem existir, contudo, **restrições pontuais**: (i) **relatórios de auditoria em elaboração ou com
restrição de acesso** até a deliberação/publicação; (ii) **dados pessoais** de agentes (LGPD) presentes
em documentos e, sobretudo, nas **entrevistas** (identificação dos participantes). Não se trata, em
regra, de "dados pessoais sensíveis" na acepção do art. 5º, II, da LGPD. As cautelas adotadas serão:
uso preferencial de **casos já encerrados e públicos**, **anonimização/pseudonimização** de
informações pessoais, **termo de consentimento livre e esclarecido** para as entrevistas, e observância
das normas internas de sigilo da CGU/TCU. O artefato é especificado para operar sobre **documentos
técnicos**, não sobre dados pessoais sensíveis.

### 15. Como você pretende coletar os dados de interesse?

- **Pesquisa e download em bases públicas** (portal de jurisprudência do TCU; sítios da Caixa/SINAPI e
  DNIT/SICRO; Portal de Periódicos CAPES; portais de licitação dos órgãos);
- **Acesso a bases de dados institucionais** (Sistema e-Aud da CGU) na condição de servidor;
- **Revisão sistemática** da jurisprudência e bibliográfica (Scopus, Web of Science, Google Scholar);
- **Solicitação de informação**, se necessário, inclusive por meio da **LAI**, para documentos não
  disponíveis em portais;
- **Entrevistas semiestruturadas** com especialistas (roteiro próprio), com gravação, transcrição e
  **análise de conteúdo**;
- **Coleta documental direta** dos editais e anexos técnicos dos três casos selecionados.

---

## PARTE V — INTEGRAÇÃO DISSERTAÇÃO–PTT

### 16. Qual ou quais PTT(s) poderiam ser derivados da sua pesquisa?

**Modalidade principal:**

- **[X] PROCESSO/TECNOLOGIA OU PRODUTO** — o *framework* de auditoria preventiva: **especificação
  técnica completa + protótipo demonstrativo** (arquitetura lógica, regras de negócio algorítmicas,
  fluxos de verificação por PLN, parâmetros de cruzamento SINAPI/SICRO e painel de alertas em Power BI).
  *(Enquadra-se no item 1.9 "a" do edital — produto técnico-tecnológico na modalidade processo/tecnologia.)*

**Modalidades secundárias/derivadas:**

- **[X] BASE DE DADOS TÉCNICO/CIENTÍFICA** — o **catálogo sistemático e codificado dos indutores de
  assimetria de informação** em anteprojetos de obras de grande vulto (contribuição original replicável).
- **[X] RELATÓRIO TÉCNICO CONCLUSIVO** — o **protocolo metodológico de auditoria pré-licitatória baseada
  em IA**, com potencial de incorporação ao Manual de Auditoria de Obras Públicas da CGU e do TCU.
- **[ ] MATERIAL DIDÁTICO** *(derivação possível)* — material de capacitação de auditores no uso do
  protocolo/ferramenta.
- **[ ] NORMA OU MARCO REGULATÓRIO** *(derivação possível, a longo prazo)* — subsídios para orientação
  técnica/normativo interno sobre requisitos mínimos de anteprojetos em contratação integrada.

### 17. Discorra sobre a aderência do PTT ao problema e ao campo profissional em que poderá ser utilizado.

O PTT responde **diretamente** ao problema: ele converte **critérios qualitativos de engenharia**
(viabilidade volumétrica de jazidas/areais, produtividade de insumos, conformidade de especificações e
de preços referenciais) em **parâmetros algorítmicos verificáveis**, operacionalizando no plano técnico
exatamente os elementos cuja ausência o Acórdão nº 686/2026-Plenário identificou como geradora de
assimetria entre licitantes. O campo profissional de uso é o **controle governamental** (controle
interno — CGU — e externo — TCU e demais Tribunais de Contas), atuando na **fase pré-licitatória**, que
é o único momento em que a correção é viável sem configurar o *periculum in mora* reverso. Assim, o
artefato rompe com o paradigma de auditoria **reativa, amostral e dependente da expertise individual**,
inserindo-se de forma aderente à Linha 2 do Programa (Tecnologias para Inovação do Controle) e à
prioridade institucional de inovação (PET-TCU 2023–2028).

### 18. Indique o(s) destinatário(s) ou usuário(s) potencial(ais) do PTT.

- **Auditores e analistas da CGU e do TCU** (usuários diretos do painel de alertas e do protocolo);
- **Demais Tribunais de Contas** (estaduais e municipais) e **órgãos de controle interno** das três
  esferas, pela replicabilidade sem custo de licenciamento;
- **Equipes de TI dos órgãos de controle** (implementação/replicação da arquitetura);
- **Gestores de programas de integridade** (Decreto nº 12.304/2024) e **áreas de engenharia e
  licitação dos órgãos contratantes**, como usuários indiretos para correção prévia de anteprojetos.

### 19. Como você descreveria preliminarmente a complexidade do produto e se é compatível com o problema, seus destinatários e as condições de desenvolvimento?

**Complexidade: alta, porém compatível e viável.** Alta porque exige **integração multidisciplinar**
(engenharia civil, direito administrativo, economia dos contratos e ciência da computação) e a
articulação de múltiplos atores (CGU/TCU como usuários; especialistas em engenharia como detentores do
conhecimento a sistematizar; equipes de TI; órgãos normativos Caixa/SINAPI e DNIT/SICRO como fontes
referenciais). **Compatível** porque: (i) o produto é entregue como **especificação técnica + protótipo
demonstrativo** (não um sistema em produção), dosando o escopo ao tempo de um mestrado; (ii) apoia-se em
**tecnologias open source e bases de dados públicas e gratuitas**, sem investimento adicional em
licenças; (iii) o painel é projetado para **Power BI**, já licenciado na CGU; e (iv) a arquitetura é
**documentada para replicação** por equipes de TI de qualquer órgão, independentemente de porte ou
esfera federativa. A validação por **três casos reais + entrevistas** calibra a complexidade ao que é
exequível e útil aos destinatários.

### 20. Quais impactos seriam esperados a partir da aplicação/implementação do produto e qual seria o horizonte provável para que eles comecem a ser alcançados?

**Impactos esperados:**

- **Institucional** — instrumento concreto de **auditoria preventiva pré-licitatória**, atuando no
  momento em que a correção é viável (evitando o *periculum in mora* reverso);
- **Operacional** — **padronização e objetivação** dos critérios de verificação, reduzindo a
  dependência da expertise individual e ampliando a capacidade analítica das equipes;
- **Fiscal/econômico** — **identificação precoce de assimetrias** antes da adjudicação, permitindo
  corrigir anteprojetos ou adotar cautelas contratuais que previnam pleitos de reequilíbrio, com
  impacto direto na **economicidade** do gasto público;
- **Científico e de difusão** — **catálogo codificado de indutores** e **protocolo metodológico**
  replicáveis, além de artigo (Qualis ≥ A4) e dissertação.

**Horizonte provável:**

- *Curto prazo (ao término do mestrado, ~24 meses)* — entrega da especificação, do protótipo
  demonstrativo validado nos três casos e do protocolo/catálogo; primeiros pilotos internos de uso.
- *Médio prazo (1–2 anos após)* — incorporação do protocolo às rotinas de auditoria e eventual
  integração ao Manual de Auditoria de Obras Públicas; replicação por outros órgãos de controle.
- *Longo prazo (3+ anos)* — efeito sistêmico na **redução de aditivos de reequilíbrio** e na melhoria
  da qualidade dos anteprojetos de contratação integrada.

---

*Documento de trabalho elaborado para preenchimento do formulário "Concepção Integrada da Pesquisa e do
PTT" (Metodologia Científica), em aderência ao Projeto de Pesquisa do Processo Seletivo 1/2026.*
