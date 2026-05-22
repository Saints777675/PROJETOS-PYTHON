"""
SISTEMA DE AVALIAÇÃO - UVVON
Atividade Online Pontuada 2

Lê as notas de alunos de um curso EAD e calcula:
  - Média do Módulo (MM) = AOP1 + AOP2 + AOP3 + PROVA REGULAR
  - Status: Aprovado, Prova de Recuperação ou Reprovado
  - Percentual de aprovados e reprovados

OBSERVAÇÃO: Variável TOTAL_ALUNOS está definida como 5 para testes.
            Para a versão final com 100 alunos, altere para 100.
"""

# ─────────────────────────────────────────────
# Configuração: altere para 100 na entrega final
# ─────────────────────────────────────────────
TOTAL_ALUNOS = 100  # Usar 100 na versão final


def ler_nota(mensagem: str, minimo: float, maximo: float) -> float:
    """Lê e valida uma nota dentro do intervalo [minimo, maximo]."""
    while True:
        try:
            nota = float(input(mensagem))
            if minimo <= nota <= maximo:
                return nota
            print(f"  ⚠  Nota fora do intervalo permitido [{minimo}, {maximo}]. Tente novamente.")
        except ValueError:
            print("  ⚠  Digite um número válido.")


def calcular_status(mm: float, nota_rec: float) -> str:
    """
    Determina o status final do aluno:
      - MM >= 7.0                          → Aprovado (direto)
      - MM < 3.0                           → Reprovado (sem recuperação)
      - 3.0 <= MM < 7.0 e MG >= 5.0       → Aprovado (pela recuperação)
      - 3.0 <= MM < 7.0 e MG < 5.0        → Reprovado
    """
    if mm >= 7.0:
        return "Aprovado"
    if mm < 3.0:
        return "Reprovado"
    # Tem direito à recuperação: 3.0 <= MM < 7.0
    mg = (mm + nota_rec) / 2
    return "Aprovado" if mg >= 5.0 else "Reprovado"


# ─────────────────────────────────────────────
# Processamento dos alunos
# ─────────────────────────────────────────────
resultados = []

print("=" * 55)
print("   SISTEMA DE AVALIAÇÃO - UVVON")
print(f"   Total de alunos: {TOTAL_ALUNOS}")
print("=" * 55)

for i in range(1, TOTAL_ALUNOS + 1):
    print(f"\n── Aluno {i}/{TOTAL_ALUNOS} " + "─" * 30)

    aop1 = ler_nota("  AOP1 [0 a 1]: ", 0, 1)
    aop2 = ler_nota("  AOP2 [0 a 2]: ", 0, 2)
    aop3 = ler_nota("  AOP3 [0 a 1]: ", 0, 1)
    prova = ler_nota("  Prova Regular [0 a 6]: ", 0, 6)

    mm = aop1 + aop2 + aop3 + prova

    nota_rec = 0.0
    fez_recuperacao = False

    if mm < 3.0:
        status = "Reprovado"
        print(f"  → Média do Módulo: {mm:.2f} — Reprovação direta (MM < 3,0). Sem direito à recuperação.")
    elif mm < 7.0:
        print(f"  → Média do Módulo: {mm:.2f} — Aluno convocado para Prova de Recuperação.")
        nota_rec = ler_nota("  Prova de Recuperação [0 a 10]: ", 0, 10)
        fez_recuperacao = True
        mg = (mm + nota_rec) / 2
        status = "Aprovado" if mg >= 5.0 else "Reprovado"
        print(f"  → Média Geral (com recuperação): {mg:.2f}")
    else:
        status = "Aprovado"
        print(f"  → Média do Módulo: {mm:.2f} — Dispensado da recuperação.")

    print(f"  ★ Status: {status}")

    resultados.append({
        "aluno": i,
        "aop1": aop1,
        "aop2": aop2,
        "aop3": aop3,
        "prova": prova,
        "mm": mm,
        "nota_rec": nota_rec,
        "fez_recuperacao": fez_recuperacao,
        "status": status,
    })

# ─────────────────────────────────────────────
# Relatório final
# ─────────────────────────────────────────────
total = len(resultados)
aprovados = sum(1 for r in resultados if r["status"] == "Aprovado")
reprovados = total - aprovados

pct_aprovados = (aprovados / total) * 100
pct_reprovados = (reprovados / total) * 100

print("\n" + "=" * 55)
print("   RELATÓRIO FINAL DA TURMA")
print("=" * 55)
print(f"{'Aluno':<8} {'MM':>6} {'Rec?':>5} {'N.Rec':>6}  Status")
print("-" * 55)

for r in resultados:
    rec_str = "Sim" if r["fez_recuperacao"] else "Não"
    nota_rec_str = f"{r['nota_rec']:.1f}" if r["fez_recuperacao"] else "  —  "
    print(f"  {r['aluno']:<6} {r['mm']:>6.2f} {rec_str:>5} {nota_rec_str:>6}  {r['status']}")

print("-" * 55)
print(f"\n  Total de alunos : {total}")
print(f"  Aprovados       : {aprovados:>3}  ({pct_aprovados:.1f}%)")
print(f"  Reprovados      : {reprovados:>3}  ({pct_reprovados:.1f}%)")
print("=" * 55)
