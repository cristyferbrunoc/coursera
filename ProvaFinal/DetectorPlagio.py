import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
    textos fornecidos """

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def quantidade_palavras(frase):
    """Recebe uma Frase e retorna a quantidade de palavras da Frase."""
    return len(separa_palavras(frase))


def tamanho_palavras(palavra):
    """Devolve o tamanho de uma Palavra"""
    return len(palavra)


def retirarSimbolos(texto):
    sentenca = separa_sentencas(texto)
    frase = []
    for i in sentenca:
        frase.append(separa_frases(i))
    return frase


def unicaLista(lista):
    unicaLista = []
    for i in lista:
        for j in i:
            unicaLista.append(j)
    return unicaLista


def tamanhoMedioPalavra(texto):
    """Retorna a Média de Palavras"""

    if texto == "":
        return 0
    setenca = separa_sentencas(texto)
    frase = []
    for i in setenca:
        frase.append(separa_frases(i))
    palavra = []
    for i in frase:
        for j in i:
            palavra.append(separa_palavras(j))

    somaPalavra = 0
    for i in palavra:
        for j in i:
            somaPalavra += tamanho_palavras(j)

    tamanhoLista = []
    for i in palavra:
        tamanhoLista.append(len(i))

    return somaPalavra / sum(tamanhoLista)


def type_token(texto):
    if texto == "":
        return 0
    textoSemSimbolos = retirarSimbolos(texto)
    palavras = []
    for i in textoSemSimbolos:
        for j in i:
            palavras.append(separa_palavras(j))

    totalPalavrasDiferentes = n_palavras_diferentes(unicaLista(palavras))

    totalPalavras = []
    for i in palavras:
        totalPalavras.append(len(i))

    return totalPalavrasDiferentes / sum(totalPalavras)


def hapax_legomana(texto):
    if texto == "":
        return 0
    textoSemSimbolos = retirarSimbolos(texto)
    palavras = []
    for i in textoSemSimbolos:
        for j in i:
            palavras.append(separa_palavras(j))

    unicaspalavras = n_palavras_unicas(unicaLista(palavras))

    totalPalavras = []
    for i in palavras:
        totalPalavras.append(len(i))

    return unicaspalavras / sum(totalPalavras)


def totalCaracteresTexto(texto):
    if texto == "":
        return 0
    setenca = separa_sentencas(texto)
    frase = []
    for i in setenca:
        frase.append(separa_frases(i))
    palavra = []
    for i in frase:
        for j in i:
            palavra.append(separa_palavras(j))

    caracteres = []
    for i in palavra:
        for j in i:
            caracteres.append(tamanho_palavras(j))
    return caracteres


def tamanhoMedioSenteca(texto):
    if texto == "":
        return 0
    """Retorna a Média da Sentença"""
    sentenca = separa_sentencas(texto)
    palavras = []
    for i in sentenca:
        palavras.append(len(i))
    palavras = sum(palavras)
    sentenca = len(sentenca)

    return palavras / sentenca


def complexadadeSetenca(texto):
    if texto == "":
        return 0
    frase = []
    for i in separa_sentencas(texto):
        frase.append(separa_frases(i))

    return len(unicaLista(frase)) / len(separa_sentencas(texto))


def tamanhoMedioFrase(texto):
    """Retorna a Média da Frase"""
    if texto == "":
        return 0
    setenca = separa_sentencas(texto)
    frase = []
    for i in setenca:
        frase.append(separa_frases(i))
    caracteres = 0

    frase = unicaLista(frase)

    for i in frase:
        caracteres += len(i)

    return caracteres / len(frase)


def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""
    return [tamanhoMedioPalavra(texto), type_token(texto), hapax_legomana(texto),
            tamanhoMedioSenteca(texto), complexadadeSetenca(texto), tamanhoMedioFrase(texto)]


def compara_assinatura(as_a, as_b):
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver
    o grau de similaridade nas assinaturas. """
    return sum(map(lambda i, j: abs(i - j), as_a, as_b)) / 6


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos
    e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior
    probabilidade de ter sido infectado por COH-PIAH. """
    verificacao = []

    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        verificacao.append(compara_assinatura(ass_texto, ass_cp))

    menor = verificacao[0]
    c = 1

    return verificacao.index(min(verificacao)) + 1

"""print("O autor do texto {} está infectado com COH-PIAH".format(
    avalia_textos([
        "Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, "
        "sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, "
        "foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. "
        "Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. "
        "Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, "
        "como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, "
        "pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. "
        "Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. "
        "Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. "
        "Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. "
        "Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.",

        "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, "
        "e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, "
        "mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, "
        "as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. "
        "Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, "
        "e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante "
        "e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",

        "Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. "
        "Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, "
        "e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. "
        "No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal "
        "que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. "
        "Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a "
        "figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma "
        "invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, "
        "que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.",
        ""], [4.51, 0.693, 0.55, 70.82, 1.82, 38.5])))"""


def iniciar():
    assinatura = le_assinatura()
    textoUsuario = le_textos()

    print("O autor do texto {} está infectado com COH-PIAH".format(avalia_textos(textoUsuario, assinatura)))


iniciar()
