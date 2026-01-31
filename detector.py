import re

def detectar_cpf(texto: str) -> bool:
    padrao_cpf = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b'
    return bool(re.search(padrao_cpf, texto))

def detectar_email(texto: str) -> bool:
    padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.search(padrao_email, texto))

def detectar_telefone(texto: str) -> bool:
    padrao_telefone = r'(?<!\d)(\(?[1-9]{2}\)?\s?)(9?\d{4}-?\d{4})(?!\d)'
    return bool(re.search(padrao_telefone, texto))

def detectar_rg(texto: str) -> bool:
    padrao_rg = r'\b\d{1}\.\d{3}\.\d{3}\b|\b\d{7}\b'
    return bool(re.search(padrao_rg, texto))

def detectar_endereço(texto: str) -> bool:
    from rapidfuzz import process
    listaRAS = [
    "asa sul", 
    "asa norte",
    "plano piloto",
    "gama",
    "taguatinga",
    "brazlândia",
    "sobradinho",
    "planaltina",
    "paranoá",
    "núcleo bandeirante",
    "ceilândia",
    "guará",
    "cruzeiro",
    "samambaia",
    "santa maria",
    "são sebastião",
    "recanto das emas",
    "lago sul",
    "riacho fundo",
    "lago norte",
    "candangolândia",
    "águas claras",
    "riacho fundo ii",
    "sudoeste/octogonal",
    "varjão",
    "park way",
    "scia/estrutural",
    "sobradinho ii",
    "jardim botânico",
    "itapoã",
    "sia",
    "vicente pires",
    "fercal",
    "sol nascente e pôr do sol",
    "arniqueira",
    "arapoanga",
    "água quente"
]
    resultado = process.extractOne(texto, listaRAS)
    if resultado is None:
        return False
    match, score, _ = resultado
    print(match, score)
    listaCapitalUF = [
    "rio brancoac", "rio branco/ac", "rio branco-ac", "rio branco_ac", "rio branco ac",
    "maceióal", "maceió/al", "maceió-al", "maceió_al", "maceió al",
    "macapáap", "macapá/ap", "macapá-ap", "macapá_ap", "macapá ap",
    "manausam", "manaus/am", "manaus-am", "manaus_am", "manaus am",
    "salvadorba", "salvador/ba", "salvador-ba", "salvador_ba", "salvador ba",
    "fortalezace", "fortaleza/ce", "fortaleza-ce", "fortaleza_ce", "fortaleza ce",
    "brasíliadf", "brasília/df", "brasília-df", "brasília_df", "brasília df",
    "vitóriaes", "vitória/es", "vitória-es", "vitória_es", "vitória es",
    "goiâniago", "goiânia/go", "goiânia-go", "goiânia_go", "goiânia go",
    "são luísma", "são luís/ma", "são luís-ma", "são luís_ma", "são luís ma",
    "cuiabámt", "cuiabá/mt", "cuiabá-mt", "cuiabá_mt", "cuiabá mt",
    "campo grandems", "campo grande/ms", "campo grande-ms", "campo grande_ms", "campo grande ms",
    "belo horizontemg", "belo horizonte/mg", "belo horizonte-mg", "belo horizonte_mg", "belo horizonte mg",
    "belémpa", "belém/pa", "belém-pa", "belém_pa", "belém pa",
    "joão pessoapb", "joão pessoa/pb", "joão pessoa-pb", "joão pessoa_pb", "joão pessoa pb",
    "curitibapr", "curitiba/pr", "curitiba-pr", "curitiba_pr", "curitiba pr",
    "recifepe", "recife/pe", "recife-pe", "recife_pe", "recife pe",
    "teresinapi", "teresina/pi", "teresina-pi", "teresina_pi", "teresina pi",
    "rio de janeirorj", "rio de janeiro/rj", "rio de janeiro-rj", "rio de janeiro_rj", "rio de janeiro rj",
    "natalrn", "natal/rn", "natal-rn", "natal_rn", "natal rn",
    "porto alegrers", "porto alegre/rs", "porto alegre-rs", "porto alegre_rs", "porto alegre rs",
    "porto velhoro", "porto velho/ro", "porto velho-ro", "porto velho_ro", "porto velho ro",
    "boa vistarr", "boa vista/rr", "boa vista-rr", "boa vista_rr", "boa vista rr",
    "florianópolissc", "florianópolis/sc", "florianópolis-sc", "florianópolis_sc", "florianópolis sc",
    "são paulosp", "são paulo/sp", "são paulo-sp", "são paulo_sp", "são paulo sp",
    "aracajuse", "aracaju/se", "aracaju-se", "aracaju_se", "aracaju se",
    "palmasto", "palmas/to", "palmas-to", "palmas_to", "palmas to", "df", "/df", "-df", "_df"
    ]
    resultadoCapUF = process.extractOne(texto, listaCapitalUF)
    if resultadoCapUF is None:
        return False
    matchCapUF, scoreCapUF, _ = resultadoCapUF
    print(matchCapUF, scoreCapUF)

    if score >= 59 or scoreCapUF >= 59:
        return True
    else:
        return False

def analisar_texto(texto: str) -> dict:
    tipos_detectados = []

    if detectar_cpf(texto):
        tipos_detectados.append("CPF")

    if detectar_email(texto):
        tipos_detectados.append("Email")

    if detectar_telefone(texto):
        tipos_detectados.append("Telefone")

    if detectar_rg(texto):
        tipos_detectados.append("RG")

    if len(texto) >= 100:
        if detectar_endereço(texto):
            tipos_detectados.append("Endereço")

    return {
        "dados_pessoais": len(tipos_detectados) > 0,
        "tipos_detectados": tipos_detectados
    }
