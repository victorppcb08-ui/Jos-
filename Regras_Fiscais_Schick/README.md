# Regras Fiscais no Orçamento — Tradução e Insight Analítico

Material produzido a partir do texto-base **Allen Schick, "The Role of Fiscal Rules in Budgeting"** (OECD Journal on Budgeting, v. 3, n. 3, 2003).

## Entregáveis

| Arquivo | Conteúdo |
|---|---|
| `01_Traducao_O_Papel_das_Regras_Fiscais.docx` | Tradução integral do artigo para o português (PT-BR), com termos técnicos consagrados preservados entre parênteses. |
| `02_Plano_Estruturado_do_Insight.docx` | Plano metodológico: leitura crítica do texto-base, recorte temático, tese, arquitetura argumentativa, fontes e pontos de concatenação. |
| `03_Insight_Analitico_Regras_Fiscais.docx` | Insight analítico (4–5 páginas) na estrutura obrigatória: Título, Exposição do ponto, Desenvolvimento da análise, Conclusão. |
| `04_Revisores_do_Insight.docx` | Dois pareceres de revisão: (I) coerência e coesão textual; (II) concatenação com o texto-base. |

## Formatação (aplicada a todos os documentos)

Margens 2,5 cm (todas); fonte Arial 12; espaçamento 1,5 (sem espaçamento antes/depois no corpo); recuo de primeira linha de 1,25 cm; texto justificado.

## Recorte do insight

Título: *"Regras que fortalecem, não substituem: o paradoxo da eficácia e a armadilha pró-cíclica das regras fiscais"*. Desenvolve a distinção de Schick entre **efeito** e **eficácia** das regras, o corolário de desenho **contracíclico** e a **vida útil limitada** das regras, projetados sobre a experiência brasileira (LRF, EC 95/2016, LC 200/2023, precatórios, papel do TCU).

## Reprodutibilidade

A pasta `fontes/` contém os textos-fonte editáveis (`.txt`) e o gerador `build_docx.js` (docx-js). Para regenerar um `.docx` após editar o `.txt`:

```bash
node build_docx.js fontes/insight.txt 03_Insight_Analitico_Regras_Fiscais.docx --font Arial
```

O parâmetro `--font` aceita `Arial` (padrão) ou `Times` (Times New Roman), ambos admitidos pela norma de formatação.
