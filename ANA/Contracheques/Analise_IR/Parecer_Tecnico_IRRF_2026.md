# Parecer Técnico: Revisão do IRRF de janeiro a outubro de 2026

**Interessada:** Ana Rosa Pessoa Peixoto Barreto, Assistente Social, matrícula 01891359, SES/DF (órgão 552)
**Objeto:** saber se o Imposto de Renda Retido na Fonte (IRRF) cobrado nos contracheques principal e de TPD (Lei DF 6.137/2018) de jan. a out./2026 foi calculado corretamente.
**Documentos examinados:** 18 contracheques. São 10 da Folha Normal (jan. a out.) e 8 da Folha Suplementar do TPD (fev. a set.). As rubricas de cada um foram transcritas e conferidas com o total bruto e o total de descontos impressos.
**Memória de cálculo:** `Memoria_Calculo_IRRF_2026.xlsx`, com fórmulas abertas para auditoria.

---

## 1. Conclusão

**Não há IR cobrado a maior.** O IRRF foi recalculado mês a mês pelo método da lei. O resultado bate **ao centavo** com o que o GDF reteve em todos os meses:

| | Valor |
|---|---:|
| IR devido, jan. a out./2026 (cálculo legal) | **R$ 66.169,57** |
| IR retido pelo GDF (principal + TPD) | **R$ 66.169,57** |
| **Diferença** | **R$ 0,00** |

A hipótese de que o IR do TPD estava errado não se confirma. A unificação dos contracheques em outubro também não mudou o critério: o resultado é matematicamente o mesmo. Por isso **não recomendo pedir recomposição ao GDF**. O pedido não teria fundamento e seria indeferido. A explicação está nas seções 4 a 6.

---

## 2. Legislação aplicada

| Tema | Norma |
|---|---|
| Tabela progressiva mensal e deduções (previdência oficial, dependentes) | Lei 9.250/1995, art. 4º; tabela vigente desde 05/2025 (Lei 15.191/2025), mantida para 2026 |
| Redução mensal do imposto a partir de jan./2026 | Lei 9.250/1995, art. 3º-A, incluído pela **Lei 15.270/2025** |
| **Vários pagamentos da mesma fonte no mesmo mês: o imposto incide sobre a soma** | **Lei 8.134/1990, art. 3º, parágrafo único; RIR/2018 (Decreto 9.580/2018), art. 677, § 2º** |
| Regime de caixa (tributa-se no mês do pagamento) | Lei 7.713/1988, art. 2º; RIR/2018 |
| IR sobre o 1/3 de férias gozadas | STJ, Tema Repetitivo 881 |
| Férias tributadas em separado na fonte | RIR/1999, art. 625, § 1º, regra mantida no RIR/2018 e nas orientações da RFB |
| Ajuste anual (soma de todos os rendimentos do ano) | Lei 9.250/1995, arts. 8º a 12 |
| Titularidade do IRRF de servidores do DF / quem responde pela restituição | CF, art. 157, I; STJ, Súmula 447 |
| TPD: base de cálculo e adicional de 25% | Lei DF 6.137/2018, art. 2º, §§ 1º, 2º e 5º; Decreto DF 39.048/2018 |

**Tabela mensal 2026**

| Base de cálculo (R$) | Alíquota | Parcela a deduzir (R$) |
|---|---:|---:|
| até 2.428,80 | 0% | 0,00 |
| 2.428,81 a 2.826,65 | 7,5% | 182,16 |
| 2.826,66 a 3.751,05 | 15% | 394,16 |
| 3.751,06 a 4.664,68 | 22,5% | 675,49 |
| acima de 4.664,68 | 27,5% | 908,73 |

- **Dedução por dependente:** R$ 189,59.
- **Redução da Lei 15.270:** até R$ 312,89 para rendimentos tributáveis de até R$ 5.000,00. Entre R$ 5.000,01 e R$ 7.350,00, a redução é 978,62 − 0,133145 × rendimento. **Acima de R$ 7.350,00 não há redução.**

---

## 3. Como cada rubrica entra no cálculo

| Rubrica (código) | Tratamento no IR |
|---|---|
| Vencimento (10004), GIABS (10139), Grat. Mov. (10140/20140), ATS (10502), GTS (10576), GCET (10586), Insalubridade (10801) | Tributáveis |
| 1/3 de férias (10865), em jun. | Tributável |
| TPD diurno e FFP (11041/11043) e diferenças de TPD (21041/21043) | Tributáveis |
| Auxílio-alimentação em pecúnia (10926) | **Não tributável** (natureza indenizatória, tratamento correto do GDF) |
| Seguridade Social (40920) | **Dedução** da base. Corresponde a 14% de Vencimento + ATS + GTS (ex.: jan. 18.606,79 × 14% = 2.604,95) |
| Empréstimos BRB e AES-SES | Sem efeito no IR |
| Dependentes | **2 dependentes** (R$ 379,18/mês), deduzidos pelo GDF |

O número de dependentes foi obtido por engenharia reversa. Sem eles, o IR de janeiro seria R$ 104,27 maior. Vale confirmar se os 2 dependentes cadastrados estão corretos e se há outros a incluir.

---

## 4. Memória de cálculo mês a mês (método legal: soma das folhas)

Fórmula: **IR = (Base × 27,5%) − 908,73**, com centavos truncados, como faz o SIGRH. Base = rendimentos tributáveis (principal + TPD) − seguridade − dependentes.

| Mês | Tributável principal | TPD | Tributável total | (−) Seguridade | (−) Dependentes | **Base** | **IR devido** | IR retido principal | IR retido TPD | **Total retido** | **Dif.** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jan | 24.132,99 | 0,00 | 24.132,99 | 2.604,95 | 379,18 | 21.148,86 | **4.907,20** | 4.907,20 | 0,00 | 4.907,20 | 0,00 |
| Fev | 24.132,99 | 1.244,14 | 25.377,13 | 2.604,95 | 379,18 | 22.393,00 | **5.249,34** | 4.907,20 | 342,14 | 5.249,34 | 0,00 |
| Mar | 23.919,08 | 5.404,78 | 29.323,86 | 2.604,95 | 379,18 | 26.339,73 | **6.334,69** | 4.848,38 | 1.486,31 | 6.334,69 | 0,00 |
| Abr | 24.004,67 | 5.604,16 | 29.608,83 | 2.604,95 | 379,18 | 26.624,70 | **6.413,06** | 4.871,91 | 1.541,15 | 6.413,06 | 0,00 |
| Mai | 24.229,78 | 6.806,53 | 31.036,31 | 2.616,17 | 379,18 | 28.040,96 | **6.802,53** | 4.930,73 | 1.871,80 | 6.802,53 | 0,00 |
| Jun* | 31.379,14 | 7.143,14 | 38.522,28 | 2.689,17 | 379,18 | 35.453,93 | **8.841,10** | 6.876,73 | 1.964,37 | 8.841,10 | 0,00 |
| Jul | 26.183,78 | 5.756,72 | 31.940,50 | 2.689,17 | 379,18 | 28.872,15 | **7.031,11** | 5.448,01 | 1.583,10 | 7.031,11 | 0,00 |
| Ago | 24.859,07 | 7.237,12 | 32.096,19 | 2.689,17 | 379,18 | 29.027,84 | **7.073,92** | 5.083,71 | 1.990,21 | 7.073,92 | 0,00 |
| Set | 24.859,07 | 4.428,88 | 29.287,95 | 2.689,17 | 379,18 | 26.219,60 | **6.301,66** | 6.301,66 | 0,00 | 6.301,66 | 0,00 |
| Out | 24.991,54 | 7.636,08 | 32.627,62 | 2.707,72 | 379,18 | 29.540,72 | **7.214,96** | 7.214,96 (unificado) | – | 7.214,96 | 0,00 |
| **Total** | 252.692,11 | 51.261,55 | 303.953,66 | 26.500,37 | 3.791,80 | 273.661,49 | **66.169,57** | 55.390,49 | 10.779,08 | **66.169,57** | **0,00** |

\* Junho inclui R$ 7.844,78 de 1/3 de férias no "tributável principal" (ver item 6.3). A redução da Lei 15.270 é zero em todos os meses, porque o tributável total sempre passa de R$ 7.350,00.

**Exemplo completo, março/2026**
1. Tributável principal: 12.832,27 + 1.283,22 + 1.283,22 + 1.924,84 + 3.849,68 + 1.676,54 + 1.069,31 = **23.919,08**. O auxílio-alimentação de 494,54 fica de fora.
2. Somando o TPD de 1.378,26 + 4.026,52 = 5.404,78, o tributável total é **29.323,86**.
3. Base: 29.323,86 − 2.604,95 − 379,18 = **26.339,73**.
4. IR: 26.339,73 × 27,5% = 7.243,42; 7.243,42 − 908,73 = **6.334,69**.
5. Retido: 4.848,38 (principal) + 1.486,31 (TPD) = **6.334,69**. Diferença: **R$ 0,00**.

---

## 5. Por que a cobrança de "27,5% cheio" no contracheque do TPD está certa

A impressão de erro vem de o contracheque do TPD aplicar 27,5% sobre o bruto sem subtrair a parcela de R$ 908,73. Essa impressão não se sustenta, por três razões.

1. **A mesma fonte paga as duas folhas.** É o GDF/SES-DF, mesmo órgão (552) e mesma matrícula. A lei manda calcular o imposto sobre a **soma** dos pagamentos do mês (Lei 8.134/1990, art. 3º, par. único; RIR/2018, art. 677, § 2º). Não existe "uma tabela por contracheque".
2. **A parcela a deduzir só pode ser usada uma vez por mês.** A folha normal já a usou. A base da folha normal (≈ R$ 21 mil) já está na faixa de 27,5%, então cada real a mais de TPD é tributado a 27,5%:
   `IR(principal + TPD) = IR(principal) + 27,5% × TPD`
3. **O sistema do GDF faz exatamente isso.** O IR do TPD é calculado como "IR sobre a soma do mês − IR já retido na folha normal". A prova está nos centavos. Em abril, 27,5% × 5.604,16 = 1.541,14, mas o GDF cobrou **1.541,15**, que é justamente 6.413,06 − 4.871,91. Junho repete o padrão (1.964,36 contra **1.964,37**). As linhas r a v da aba 3 detalham a conta.

**A hipótese de "uma tabela por contracheque"** (aba 4) reduziria a retenção em cerca de R$ 8.731,67 de fev. a out. Mas isso não é economia. Na Declaração Anual, a Receita soma todos os rendimentos do ano, e esse valor viraria **imposto a pagar** em 2027. O imposto total do ano seria o mesmo.

---

## 6. Pontos específicos

### 6.1 Setembro: TPD sem desconto de IR
Não houve isenção nem erro. O imposto do TPD de setembro (**R$ 1.217,95**) foi lançado **no contracheque principal**. Agosto e setembro têm a mesma remuneração principal (R$ 25.499,07 bruto), mas o IR principal passou de **R$ 5.083,71** para **R$ 6.301,66**. A diferença, 1.217,95, é exatamente o IR incremental de 4.428,88 de TPD (4.428,88 × 27,5% = 1.217,94, mais 1 centavo de truncamento). **Setembro está correto.**

### 6.2 Outubro: unificação das folhas
IR da folha normal isolada (base 21.904,64): **5.115,04**. IR incremental do TPD: 7.636,08 × 27,5% = **2.099,92**. Soma: **7.214,96**, exatamente o valor cobrado. **A unificação não alterou o critério nem trouxe vantagem tributária.** Ela só juntou num único documento o que antes saía em dois. A alíquota efetiva de outubro (22,1% do tributável) está na mesma faixa dos meses anteriores (21,5% a 23,0%).

### 6.3 Junho: 1/3 de férias (ponto controvertido, de pequeno valor)
Pela regra do RIR/1999, art. 625, § 1º (repetida no RIR/2018 e nas orientações da RFB), as férias e o 1/3 são tributados na fonte **em separado** dos demais rendimentos do mês. O GDF somou o 1/3 (R$ 7.844,78) à remuneração. Se o cálculo fosse separado, a retenção de junho seria **≈ R$ 908,74 menor** (aba 5): R$ 7.932,36 em vez de R$ 8.841,10.

Isso é só diferença de **caixa**. O ajuste anual aplica uma única tabela sobre a soma do ano, e esse valor seria cobrado na Declaração de 2027. O prejuízo real é apenas o custo de ter antecipado ≈ R$ 909 por uns 10 meses, **menos de ~R$ 115** mesmo com Selic de 15% a.a. Não justifica um pedido.

### 6.4 Valor-hora do TPD (fora do escopo do IR, para sua verificação)
A quantidade no contracheque está em **horas e minutos** (ex.: 1937 = 19h37min). O valor-hora ficou constante de março a outubro: **R$ 70,26** no diurno e **R$ 87,82** no FFP. O adicional de 25% está corretamente aplicado. Em março, o FFP saiu ≈ R$ 58 acima de horas × valor-hora, a seu favor.

Atenção: o texto da Lei 6.137/2018 (art. 2º, § 2º) manda calcular o TPD sobre o vencimento do **último padrão vigente do cargo** (topo da carreira), **não sobre o vencimento inicial** (R$ 8.382,37). O valor-hora pago (R$ 70,26 × 200 h ≈ R$ 14.051,94) já está acima do inicial e do seu padrão 16 (R$ 13.247,18), o que sugere que o GDF usa o último padrão, como diz a lei. Para conferir se está exato, compare com a tabela salarial oficial da carreira e a fórmula do Decreto 39.048/2018.

---

## 7. Recomendações

1. **Não protocolar pedido de recomposição de IR.** Não há valor retido a maior, e o pedido seria indeferido.
2. **Comprovante de Rendimentos 2026** (fornecido pelo GDF no início de 2027): confira se ele **consolida** a folha normal e o TPD. Com base em jan. a out., devem constar ao menos R$ 303.953,66 de rendimentos tributáveis, R$ 26.500,37 de previdência oficial e **R$ 66.169,57 de IRRF**. Faltam nov., dez. e 13º. Se o TPD ou o IR de setembro estiverem faltando, aí sim cabe pedir retificação ao GDF. Pela Súmula 447/STJ e pelo art. 157, I, da CF, o DF responde pelo IRRF dos seus servidores.
3. **Declaração de Ajuste Anual 2027 (ano-calendário 2026):** a eventual **restituição** vem das deduções que a folha não considera: despesas médicas e plano de saúde, educação, PGBL (até 12% da renda tributável) e pensão alimentícia judicial. Junte os comprovantes. Confirme também os 2 dependentes.
4. **13º salário:** tem tributação exclusiva e separada. Não interfere nas contas acima.

---

## Anexo: abas da planilha `Memoria_Calculo_IRRF_2026.xlsx`

| Aba | Conteúdo |
|---|---|
| 0_Resumo | Quadro mês a mês (devido × retido × diferença) e conclusões |
| 1_Parametros | Tabela 2026, dependentes, redução da Lei 15.270 (células editáveis em amarelo) |
| 2_Rubricas | Todas as rubricas dos 18 contracheques, com classificação para o IR e filtro |
| 3_Memoria_Mensal | Cálculo completo (linhas a até w) com fórmulas e a prova do método do GDF |
| 4_Hipotese_Separada | Simulação de "uma tabela por contracheque" e seu efeito no ajuste anual |
| 5_Ferias_Junho | Tese da tributação do 1/3 de férias em separado |
| 6_TPD_ValorHora | Horas, valor-hora diurno e FFP, conferência do adicional de 25% |

*Este parecer tem caráter técnico-orientativo e foi baseado exclusivamente nos contracheques fornecidos. Recomenda-se confirmar os dispositivos citados nos textos oficiais (Planalto/RFB).*
