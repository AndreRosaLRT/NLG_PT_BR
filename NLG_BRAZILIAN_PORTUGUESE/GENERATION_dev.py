
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:50:31 2019

@author: andre
"""


# ######PRELIMINARES


import re

######
###

###############################################################################
#####################
###########ORDEM DA PALAVRA

###ADVÉRBIO    INÍCIO####

###########ORDEM DA PALAVRA
from nltk import unify


def adverbio_modo(indice=None):
	opcoes = ['bem','mal','assim','adrede',
			  'melhor','pior','depressa','devagar',
			  'acinte','debalde','cuidadosamente','calmamente',
			  'tristemente']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio
# adverbio_modo(1)

def adverbio_intensidade(indice=None):
	opcoes = ['muito','demais','todo','pouco',
		'tão','quão','demasiado','bastante','imenso','demais',
		'mais','menos','quanto','quase','tanto',
		'assaz','tudo','nada']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio
# adverbio_intensidade(1)
def adverbio_lugar(indice=None):
	opcoes = ['aí','aqui','acolá','cá',
		'lá','ali','adiante','abaixo','embaixo',
		'acima','adentro','dentro']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio
# adverbio_lugar(1)

def adverbio_tempo(indice=None):
	opcoes = ['ainda', 'agora',
			  'amanhã', 'à noite', 'anteontem',
			  'antes', 'à tarde', 'às vezes', 'atualmente',
			  'breve', 'cedo', 'depois','de manhã','de repente',
			  'de vez em quando','hoje','hoje em dia',
			  'já', 'logo', 'nunca','ontem','ora',
			  'outrora','quando','sempre','tarde','jamais']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

# adverbio_tempo(1)
def adverbio_negacao(indice=None):
	opcoes = ['não', 'nem', 'tampouco', 'nunca', 'jamais' ]
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

# adverbio_negacao(4)

def adverbio_relativo(indice=None):
	opcoes = ['de onde', 'quando', 'onde',
	                     'de quando', 'que', 'por onde']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

# adverbio_relativo(4)


def adverbio_afirmacao(indice=None):
	opcoes = ['sim','deveras',
	            'indubitavelmente','decididamente',
	              'certamente', 'realmente',
	              'decerto', 'certo',
	               'efetivamente']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

adverbio_afirmacao(4)

def adverbio_duvida(indice=None):
	opcoes = ['possivelmente','provavelmente',
	          'acaso','porventura',
	           'quiçá','será','talvez',
	           'casualmente']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

# adverbio_duvida(4)

def adverbio(tipo_de_adverbio, indice):
	"""
    HHHH
    """
	#    modo_insercao = choice.Menu(['insercao_manual','insercao_menu']).ask()

	if tipo_de_adverbio == 'Modo':

		adverbio = adverbio_modo(indice)

	elif tipo_de_adverbio == 'Intensidade':

		adverbio = adverbio_intensidade(indice)

	elif tipo_de_adverbio == 'Lugar':

		adverbio = adverbio_lugar(indice)

	elif tipo_de_adverbio == 'Tempo':

		adverbio = adverbio_tempo(indice)

	elif tipo_de_adverbio == 'Negacao':

		adverbio = adverbio_negacao(indice)

	elif tipo_de_adverbio == 'Afirmacao':
		adverbio = adverbio_afirmacao(indice)

	elif tipo_de_adverbio == 'Duvida':

		adverbio = adverbio_duvida(indice)

	elif tipo_de_adverbio == 'Adv_relativo':

		adverbio = adverbio_relativo(indice)

	return adverbio


# adverbio( "Modo", 2)

###ADVÉRBIO    FIM####

####################################################################
##### VERBO INÍCIO####

def def_classe_de_verbo(funcao_no_grupo_verbal):
	'''
    (str)-> str

    Retorna um str com classe de verbo dado um verbm em str.

    >>>def_classe_de_verbo ('andar')
    lexical
    >>> def_classe_de_verbo ('ir')
    auxiliar
    >>>def_classe_de_verbo ('poder')
    'modal'
    '''

	# print("Qual é a função do verbo no grupo verbal?")
	# funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
	#                                       'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()

	if funcao_no_grupo_verbal == 'Evento' or funcao_no_grupo_verbal == 'Evento+Núcleo':
		classe_verbo = 'lexical'
	elif funcao_no_grupo_verbal == 'Auxiliar' or funcao_no_grupo_verbal == 'Auxiliar+Núcleo':
		classe_verbo = 'auxiliar'
	elif funcao_no_grupo_verbal == 'Modal' or funcao_no_grupo_verbal == 'Modal+Núcleo':
		classe_verbo = 'modal'
	else:
		classe_verbo = None

	return classe_verbo


# EXEMPLOS
# def_classe_de_verbo("Modal")
# def_classe_de_verbo("Evento+Núcleo")
# def_classe_de_verbo("Auxiliar")
# def_classe_de_verbo("Auxiliar+Núcleo")


#######################################

##A próximo função precisa ir sendo atualizada e melhorada à medida que subo na escala de ordens:
# Resolver a questão de como vou fazer para dar entrada no 'verbo'-talvez alguma
#        subfunção que pergunta ao usuário qual é a o tipo_pessoa de experiência
#        ele pretende gerar. Provavelmente vai puxar do inventário de tipos de configuração
#        que vou introduzir a partir da anotação do texto na GUM- um inventário de
#        realizações de determinados significados semânticos específicos (de lá vamos puxar
#            as informações necessárias para a geração)


####ESTA FUNÇÃO DEPENDE DE FORNECIMENTO DO PARÂMETO 'VERBO'

#        A primeira função o verbo não precisa estar lematizado, ou seja, podemos entrar qualquer verbo, mesmo conjugado e
#        a função retorna o ME. Essa opção me paree um pouco redundante pois se sabemos de antemão qual é o verbo, já sabemos
##        qual é o ME. A segunda função depende de um verbo lematizado que dependerá por sua vez de escolhas dentro de opções de
#        tipos de experiências que são realizadas por verbos lematizados (esses verbos então serão realizações de opções dentro de
#            de uma estrutura em cascata de opções que ainda preciso descobrir como fazer)

# COMENTADA POR ENQUANTO POIS ELA ESTÁ FUNCIONANDO COMO UM PARSER.
# Não vou precisar ainda desta função, pois a entrada vai ser com o verbo no infinitivo
# def experiencia_do_verbo(verbo):
#
#     '''(str)-> str
#
#     Retorna um str com o morfema experiencial (ME) que realiza
#     a experiência do verbo, dado um verbo lematizado.
#     '''
#     # verbo = input ("Qual o verbo?")
#
#     MI = realizacao_transitoriedade_do_verbo()
#     ME =  (verbo[slice(-len(MI))])
#
#     return ME
# verbo = 'ando'
# experiencia_do_verbo ('ando')


def experiencia_do_verbo(verbo):
	'''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado

    >>>experiencia_do_verbo()
    'lev'
    >>>experiencia_do_verbo('')
    'diz'
    >>>experiencia_do_verbo('')
    't'
    '''

	# verbo = input ('Qual é o verbo lematizado?')
	ME = (verbo[slice(-2)])
	return (ME)


# experiencia_do_verbo("correr")

##############TRANSITORIEDADE######################################################

#
#
# def deteccao_transitoriedade_do_verbo_dev(verbo,tipo_de_orientacao,tipo_de_orientacao,)
#
#
def deteccao_transitoriedade_do_verbo(verbo):
	'''
    (str) -> str

    Retorna o morfema interpessoal que realiza a orientação interpessoal
    dados o verbo, seu padrão de morfologia, seu tipo_pessoa de orientação
    e o tipo_pessoa de pessoa.

    >>>deteccao_transitoriedade_do_verbo('expus')
    'us'
    >>>deteccao_transitoriedade_do_verbo('li')
    'i'
    >>>deteccao_transitoriedade_do_verbo('bebi')
    'i'

    '''
	# verbo = input ("Qual o verbo?")
	ME = experiencia_do_verbo(verbo)
	MI = (verbo[len(ME):])
	return MI


# deteccao_transitoriedade_do_verbo("ando")
#
#
# ###################opções para tipos de orientação interpessoal
#
# tipo_nao_finito = choice.Menu(['não_finito_subjuntivo_conjuntivo', 'não_finito_subjuntivo_condicional',
#                                     'não_finito_subjuntivo_optativo','não_finito_imperativo_I','não_finito_imperativo_II',
#                                    'não_finito_concretizado']).ask()
#
# tipo_finito = choice.Menu(['finito_presente','finito_pretérito_perfectivo_I','finito_pretérito_perfectivo_II',
#                       'finito_pretérito_imperfectivo','finito_passado_volitivo','finito_futuro']).ask()
#
# tipo_nao_orientado = choice.Menu(['não_orientado_infinitivo',
#                                 'não_orientado_gerúndio',
#                                 'não_orientado_particípio'
#                                     ]).ask()


def OI_tipo_de_orientacao(tipo_de_orientacao):
	return tipo_de_orientacao


# OI_tipo_de_orientacao("não_orientado_infinitivo")


#######
# opções de padrão de morfologia('-AR', '-ER', '-IR', '-OR')

def realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero=None,
                                          OI_tipo_de_pessoa=None, padrao_pessoa_morfologia=None):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo()
    'ar'
    '''
	if (padrao_de_morfologia == '-AR'):
		MI = 'ar'
	elif (padrao_de_morfologia == '-ER'):
		MI = 'er'
	elif (padrao_de_morfologia == '-IR'):
		MI = 'ir'
	elif (padrao_de_morfologia == '-OR'):
		MI = 'or'
	return MI
# realizacao_transitoriedade_infinitivo('-AR')


def detecta_padrao_morfologia(verbo):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo()
    'ar'
    '''
	if verbo == None:
		padraoMorfologia=None
	else:
		ME = experiencia_do_verbo(verbo)
		MI = (verbo[len(ME):])
		if MI == 'ar':
			padraoMorfologia='-AR'
		elif MI == 'er':
			padraoMorfologia='-ER'
		elif MI == 'ir':
			padraoMorfologia='-IR'
		elif MI == 'or':
			padraoMorfologia='-OR'
		else:
			padraoMorfologia=None

	return padraoMorfologia

teste = detecta_padrao_morfologia(None)


######
# opções
# padrao_de_morfologia = ['-AR', '-ER', '-IR', '-OR']
# OI_tipo_de_pessoa =['1pessoa','2pessoa','3pessoa'])
# OI_numero = ['singular', 'plural']
# padrao_pessoa_morfologia = ['3pessoa_do_singular', 'Morfologia_padrão']


def realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str,str,str,str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    a o padrão de morfologia, tipo_pessoa de orientação, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_presente()
    'o'
    :param genero:
    '''

	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"
	):
		MI = 'o'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão":
		MI = 'onho'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'as'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'es'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'):
		MI = 'õe'
	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ões'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
		MI = 'a'
	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'e'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'õe'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'omos'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ais'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eis'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'is'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ondes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'am'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'em'


	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'


	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'õem'

	return MI


# realizacao_transitoriedade_presente('-AR','singular','1pessoa')

# pretérito_perfectivo_I

# padrao_de_morfologia = choice.Menu(['-AR', '-ER', '-IR', '-OR']).ask()
# OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
# OI_numero = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"
                                                      ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão":
		MI = 'ei'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
		MI = 'i'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
		MI = 'us'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'aste'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'este'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iste'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'useste'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ou'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eu'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iu'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ôs'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'usemos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'astes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'estes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'istes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'usestes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'aram'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eram'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iram'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'useram'
	return MI


X=['-AR','-ER','-IR','-OR']
Y=['plural','singular']
Z=['1pessoa','2pessoa','3pessoa']
for i in X:
	for j in Y:
		for p in Z:
			transito = realizacao_transitoriedade_preterito_perfectivo_I(i,j,p)
			print(transito)
#
# realizacao_transitoriedade_preterito_perfectivo_I('-IR', 'singular', '1pessoa')


###pretérito imperfectivo
# padrao_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
# OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
# OI_numero = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e numero.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ava'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ia'
	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
		padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ía'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'unha'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'avas'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'):
		MI = 'ia'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ias'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ias'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'unhas'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ávamos'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'íamos'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ia'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ia'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'íamos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morforlogia_padrão':
		MI = 'únhamos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'áveis'
	#
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'íeis'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ía'
		else:
			MI = 'íeis'
	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'únheis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ava'
		else:
			MI = 'avam'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'iam'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ía'
		else:
			MI = 'íam'
	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'unham'
	return MI


# realizacao_transitoriedade_preterito_imperfectivo('-ER', 'plural', '1pessoa')


def realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.


    'ei'
    '''
	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ara'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'era'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'ira'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'usera'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'aras'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'eras'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'iras'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'useras'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'áramos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'êramos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'íramos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'úseramos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'áreis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'êreis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'íreis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'uséreis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'aram'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'eram'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'iram'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'useram'
	return MI

#
# X=['-AR','-ER','-IR','-OR']
# Y=['plural','singular']
# Z=['1pessoa','2pessoa','3pessoa']
# for i in X:
# 	for j in Y:
# 		for p in Z:
# 			transito = realizacao_transitoriedade_preterito_perfectivo_II(i,j,p)
# 			print(transito)

def realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.


    'ei'
    '''

	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'aria'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'eria'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'iria'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'oria'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'arias'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'erias'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'irias'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'orias'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríamos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríamos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríamos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríamos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríeis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríeis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríeis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríeis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'ariam'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eriam'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iriam'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oriam'

	return MI


# realizacao_transitoriedade_passado_volitivo('-AR', 'singular','1pessoa')


def realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no futuro, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'arei'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'erei'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'irei'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'orei'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ará'
		else:
			MI = 'arás'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'erá'
		else:
			MI = 'erás'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'irá'
		else:
			MI = 'irás'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'orá'
		else:
			MI = 'orás'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'ará'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'erá'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'irá'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'orá'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'aremos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'eremos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'iremos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'oremos'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'areis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'ereis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'ireis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'oreis'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'arão'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'erão'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'irão'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'orão'

	return MI


# realizacao_transitoriedade_futuro('-AR','plural','2pessoa')

def realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                     padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'onha'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'es'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'
	):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'as'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhas'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'emos'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'amos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhamos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'eis'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'ais'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhais'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'em'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'
	):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'am'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onham'
	return MI


# realizacao_transitoriedade_subjuntivo_conjuntivo('-ER','plural','2pessoa')
#######subjuntivo_condicional


def realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo condicional, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I('-AR','1pessoa','singular')
    >>>'asse'

    '''

	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'asse'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'esse'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'isse'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'usesse'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'asses'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'esses'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'isses'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usesses'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ássemos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êssemos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssemos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'uséssemos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ásseis'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êsseis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'ísseis'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usésseis'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'assem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'essem'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssem'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usessem'
	return MI


# realizacao_transitoriedade_subjuntivo_condicional('-AR','plural','2pessoa','3pessoa_do_singular')

###subjuntivo_optativo
def realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo_optativo ,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'user'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'useres'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'usermos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userdes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userem'

	return MI


# realizacao_transitoriedade_subjuntivo_optativo('-AR','plural','2pessoa')

############não_finito_concretizado

def realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                       padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo  não_finito_concretizado,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'or'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ores'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ormos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ordes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'orem'
	return MI


# realizacao_transitoriedade_nao_finito_concretizado('-AR','plural','2pessoa')

#######imperativo_I (afirmativo)

def realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                            padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_I,
    dados  o padrão de morfologia, tipo_pessoa de pessoa,número, padrão de pessoa da morfologia.

    >>>
    ''
    '''

	if OI_numero == 'singular':
		if OI_tipo_de_pessoa == '1pessoa':
			if (padrao_de_morfologia == '-AR' or
					padrao_de_morfologia == '-ER' or
					padrao_de_morfologia == '-IR' or
					padrao_de_morfologia == '-OR'):
				MI = 'Não há transitoriedade para imperativo_I na 1pessoa singular'

		elif OI_tipo_de_pessoa == '2pessoa':
			if padrao_de_morfologia == '-AR':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'a'
			elif (padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR'):
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'e'
			elif  padrao_de_morfologia == '-OR':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'onha'
				else:
					MI = 'õe'
####
		elif OI_tipo_de_pessoa == '3pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'e'
			elif (padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR') :
				MI = 'a'
			elif  padrao_de_morfologia == '-OR':
				MI = 'onha'
####
	elif OI_numero == 'plural':
		if OI_tipo_de_pessoa == '1pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'emos'
			elif padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR':
				MI = 'amos'
			elif padrao_de_morfologia == '-OR':
				MI = 'onhamos'

		elif OI_tipo_de_pessoa == '2pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'ai'
			elif padrao_de_morfologia == '-ER':
				MI = 'ei'
			elif padrao_de_morfologia == '-IR':
				MI='i'
			elif padrao_de_morfologia == '-OR':
				MI = 'onde'

		elif OI_tipo_de_pessoa == '3pessoa':
			if padrao_de_morfologia == '-AR':
				MI='em'
			elif (padrao_de_morfologia == '-ER' or
			    padrao_de_morfologia == '-IR'):
				MI = 'am'
			elif padrao_de_morfologia == '-OR':
				MI= 'onham'
	return MI


# realizacao_transitoriedade_imperativo_I('-AR', 'plural', 'pessoa')
# realizacao_transitoriedade_imperativo_I('-OR', 'singular', '2pessoa')


#######imperativo_II (negativo)


def realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_II,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>

    '''

	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'es'

	elif (
			(padrao_de_morfologia == '-ER' or '-IR')
			and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'
	):
		MI = 'as'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'singular'
	):
		MI = 'onhas'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'e'

	elif (
			(
					padrao_de_morfologia == '-ER' or '-IR'
			)
			and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'onha'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '1pessoa'
			and OI_numero == 'plural'
	):
		MI = 'emos'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'
	):
		MI = 'amos'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'onhamos'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'plural'
	):
		MI = 'eis'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'
	):
		MI = 'ais'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'plural'
	):
		MI = 'onhais'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'plural'
	):
		MI = 'em'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'
	):
		MI = 'am'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'onham'

	elif (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'
	):
		MI = 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida'

	return MI


# realizacao_transitoriedade_imperativo_II('-AR', '2pessoa','plural')
###gerúndio
# realizacao_transitoriedade_gerundio('-OR')

def realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero=None, OI_numero=None,
                                        OI_tipo_de_pessoa=None, padrao_pessoa_morfologia="Morfologia_padrão"
                                        ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no gerúndio,
    dadoo padrão de morfologia.

    >>>
    '''
	if padrao_de_morfologia == '-AR':
		MI = 'ando'

	elif padrao_de_morfologia == '-ER':
		MI = 'endo'

	elif padrao_de_morfologia == '-IR':
		MI = 'indo'

	elif padrao_de_morfologia == '-OR':
		MI = 'ondo'

	return MI


realizacao_transitoriedade_gerundio('-IR')

######particípio


def realizacao_transitoriedade_participio(padrao_de_morfologia,OI_numero, genero, OI_tipo_de_pessoa=None,
                                          padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no particípio,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_particípio ()
    ''
    '''

	if padrao_de_morfologia == '-AR' and OI_numero == 'singular' and genero == 'feminino':
		MI = 'ada'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and genero == 'feminino':
		MI = 'adas'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'singular' and genero == 'masculino':
		MI = 'ado'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and genero == 'masculino':
		MI = 'ados'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'singular' and genero == 'masculino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'singular' and genero == 'masculino'
	):
		MI = 'ido'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'plural' and genero == 'masculino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'plural' and genero == 'masculino'
	):
		MI = 'idos'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'singular' and genero == 'feminino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'singular' and genero == 'feminino'
	):
		MI = 'ida'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'plural' and genero == 'feminino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'plural' and genero == 'feminino'
	):
		MI = 'idas'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'singular' and genero == 'feminino':
		MI = 'osta'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'singular' and genero == 'masculino':
		MI = 'osto'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'plural' and genero == 'feminino':
		MI = 'ostas'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'plural' and genero == 'masculino':
		MI = 'ostos'

	return MI


#
#

# 
# realizacao_transitoriedade_participio('-AR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-AR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-AR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-AR', 'singular', 'feminino')
# 
# 
# realizacao_transitoriedade_participio('-ER', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-ER', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-ER', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-ER', 'singular', 'feminino')
# 
# realizacao_transitoriedade_participio('-IR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-IR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-IR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-IR', 'singular', 'feminino')
# 
# 
# realizacao_transitoriedade_participio('-OR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-OR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-OR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-OR', 'singular', 'feminino')
# 



# realizacao_transitoriedade_preterito_imperfectivo('-IR','singular','1pessoa')

def realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão"):
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo()
    'o'

    '''

	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero=None,
		                                           OI_tipo_de_pessoa=None, padrao_pessoa_morfologia=None)

	elif tipo_de_orientacao == 'presente':
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                       	padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                      padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                    padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'imperativo_I':
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                             padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'imperativo_II':
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                              padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa=None,
		                                           padrao_pessoa_morfologia=None)
	return MI


#
# # realizacao_transitoriedade_gerundio('-AR')
# realizacao_transitoriedade_do_verbo('gerúndio','-AR',None,None,None)
# realizacao_transitoriedade_do_verbo('presente','-AR','singular',None,'1pessoa')
# for i in X:
# 	for j in Y:
# 		for k in Z:
#
# 			transito = realizacao_transitoriedade_do_verbo('pretérito_perfectivo_II',i,j,None,k)
# 			print(transito)
# realizacao_transitoriedade_do_verbo('pretérito_imperfectivo','-ER','plural',None,'2pessoa')
# realizacao_transitoriedade_do_verbo('imperativo_I','-AR','singular',None,'2pessoa')
# realizacao_transitoriedade_do_verbo('imperativo_II','-AR','singular',None,'2pessoa')
# realizacao_transitoriedade_imperativo_I('AR','singular','1pessoa')
# realizacao_transitoriedade_do_verbo('imperativo')
# FORMAÇÃO DO VERBO ###################

#
# def formação_da_estrutura_do_verbo1 (): #O tipo_de_experiência
# #aqui vai ter relação com o tipo_pessoa de configuração
#     '''
#     (str) -> str
#
#     Retorna um verbo flexionado dados OE_experiência_do_verbo,
#     OI_orientação_interpessoal_do_verbo.
#
#     >>> formação_da_estrutura_do_verbo ()
#     'levo'
#     >>>formação_da_estrutura_do_verbo ()
#     'levei'
#     '''
#     OE_experiência_do_verbo = experiencia_do_verbo()
#     OI_orientação_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo ()
#
#     return OE_experiência_do_verbo + OI_orientação_interpessoal_do_verbo
# experiencia_do_verbo('andar')



#################
### FORMAÇÃO DOS VERBOS IRREGULARES
###VERBOS TERMINADOS EM : 'cer'


def formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
												 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		if OI_tipo_de_pessoa=='1pessoa':
			ME = verbo[slice(-3)]+'ç'
		else:
			ME = verbo[slice(-2)]

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'ç'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if (OI_tipo_de_pessoa=='3pessoa' or
			OI_tipo_de_pessoa == '1pessoa'):
			ME = verbo[slice(-3)]+'ç'
		else:
			ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'ç'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# formacao_verbo_CER('enternecer','presente','-ER','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_CER('enternecer','subjuntivo_conjuntivo','-ER','singular',None,'1pessoa')
# formacao_verbo_CER('enternecer','imperativo_I','-ER','plural',None,'3pessoa')
# formacao_verbo_CER('enternecer','imperativo_II','-ER','singular',None,'2pessoa')

###VERBOS TERMINADOS EM : 'çar'

def formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'c'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'c'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa=='2pessoa':
			ME = verbo[slice(-2)]
		else:
			ME=verbo[slice(-3)]+'c'
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'c'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo

# formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
#


###VERBOS TERMINADOS EM : 'Car'

def formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'qu'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'qu'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if (OI_tipo_de_pessoa=='3pessoa' or
			OI_tipo_de_pessoa == '1pessoa'):
			ME = verbo[slice(-3)]+'qu'
		else:
			ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'qu'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo

# formacao_verbo_CAR('focar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_CAR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_CAR('focar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_CAR('focar','imperativo_II','-AR','singular',None,'2pessoa')



###VERBOS TERMINADOS EM : 'GAR'

def formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'gu'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'gu'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if (OI_tipo_de_pessoa=='3pessoa' or
			OI_tipo_de_pessoa == '1pessoa'):
			ME = verbo[slice(-3)]+'gu'
		else:
			ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'gu'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
# formacao_verbo_GAR('entregar','pretérito_perfectivo_I','-AR','singular',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_GAR('entregar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_GAR('entregar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_GAR('entregar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_GAR('entregar','imperativo_II','-AR','singular',None,'2pessoa')

###VERBOS TERMINADOS EM : 'RUIR'

def formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if verbo[-5:]=='truir' and tipo_de_orientacao == 'presente':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'o'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-3)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ói'
				else:
					MI = 'óis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-3)]
				MI = 'ói'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-3)]
					MI = 'ói'
				else:
					ME = verbo[slice(-2)]
					MI = 'ímos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ís'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-3)]
					MI = 'ói'
				else:
					ME = verbo[slice(-3)]+'o'
					MI = 'em'

	elif verbo[-4:]=='ruir' and tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'o'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'i'
				else:
					MI = 'is'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-2)]
					MI = 'i'
				else:
					ME = verbo[slice(-2)]
					MI = 'ímos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ís'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-2)]
					MI = 'i'
				else:
					ME = verbo[slice(-2)]
					MI = 'em'
	elif verbo[-5:]=='truir' and tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = 'ói'
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'í'
		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif verbo[-4:]=='ruir' and tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-1)]
			MI = ''
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'í'
		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif (verbo[-5:]=='truir' or
		verbo[-4:]=='ruir'):
		if tipo_de_orientacao == 'pretérito_imperfectivo':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'ía'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ías'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'ía'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íamos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'íeis'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íam'

		elif tipo_de_orientacao == 'pretérito_perfectivo_I':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'í'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'
					else:
						MI = 'íste'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'iu'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'

					else:
						MI = 'ímos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'ístes'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'
					else:
						MI = 'íram'

		elif tipo_de_orientacao == 'pretérito_perfectivo_II':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			MI ='í'+ MI[1:]

		elif tipo_de_orientacao == 'subjuntivo_condicional':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
																   OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			MI = 'í' + MI[1:]

		elif tipo_de_orientacao == 'subjuntivo_optativo':
			ME = verbo[slice(-2)]
			if (OI_tipo_de_pessoa=='2pessoa' and OI_numero=='singular' or
			OI_tipo_de_pessoa=='3pessoa' and OI_numero=='plural'):
				MI = 'í'+(realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)[1:])
			else:
				MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
																		   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'passado_volitivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
															 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'pretérito_imperfectivo':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'ía'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ías'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'ía'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ímos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'íeis'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íam'

		elif tipo_de_orientacao == 'não_finito_concretizado':
			ME = verbo[slice(-2)]
			if (OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
			 OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
				MI = 'í'+(realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)[1:])
			else:
				MI=realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'futuro':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
												   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
																  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'imperativo_II':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
														  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'gerúndio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
													 padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'particípio':
			ME = verbo[slice(-2)]
			MI = "í" + realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
													   padrao_pessoa_morfologia)[1:]

		elif tipo_de_orientacao == 'infinitivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
													   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# verbo=formacao_verbo_RUIR('construir', 'presente', '-IR','plural' ,None, '3pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'presente', '-IR','plural' ,None, '3pessoa')
#
# verbo=formacao_verbo_RUIR('construir', 'subjuntivo_optativo', '-IR','plural' ,None, '3pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'subjuntivo_condicional', '-IR','plural' ,None, '3pessoa')
#
# verbo=formacao_verbo_RUIR('construir', 'imperativo_I', '-IR','plural' ,None, '2pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'imperativo_I', '-IR','plural' ,None, '2pessoa')
#
#
# verbo=formacao_verbo_RUIR('construir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')
# verbo=formacao_verbo_RUIR('ruir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')


# #
# formacao_verbo_RUIR('construir','particípio','-IR','singular','masculino',None)
# formacao_verbo_RUIR('focar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_RUIR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_RUIR('focar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_RUIR('focar','imperativo_II','-AR','singular',None,'2pessoa')

# VERBO agredir

def formacao_verbo_agredir(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	
	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'o'
				verbo = ME + 'id' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)] + 'id'

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)] + 'id'
				MI = 'e'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)] + 'id'
					MI = 'e'
					verbo = ME + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'imos'
					verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)] + 'id'
					MI = 'e'
					verbo = ME + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'id'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "ir" + MI
				else:
					ME = verbo[slice(-4)]
					MI = 'e'
					verbo = ME + "id" + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "id" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'id' + MI
				else:
					MI = 'amos'
					verbo = ME + 'id' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'id' + MI

				else:
					MI = 'am'
					verbo = ME + 'id' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'id' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo
# 
# formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# formacao_verbo_agredir('agredir','particípio','singular','masculino',None)
# formacao_verbo_agredir('agredir','gerúndio',None,None,None)
# formacao_verbo_agredir('agredir', 'infinitivo', None, None, None)
# formacao_verbo_agredir('agredir', 'pretérito_perfectivo_II', 'singular', None, '1pessoa')
# formacao_verbo_agredir('agredir','pretérito_imperfectivo','singular',None,'1pessoa')

# VERBO aferir


def formacao_verbo_aferir(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'o'
				verbo = ME + 'ir' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'imos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'ir'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "ir" + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'e'
					verbo = ME + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "ir" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ir' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ir' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ir' + MI

				else:
					MI = 'am'
					verbo = ME + 'ir' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'ir' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	return verbo


#
# formacao_verbo_aferir('aferir', 'não_finito_concretizado',  'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'subjuntivo_optativo',  'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'particípio',  'singular', 'masculino', None)
# formacao_verbo_agredir('aferir','particípio','singular','feminino',None)


# VERBO MEDIR
def formacao_verbo_medir(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-3)]
				MI = 'o'
				verbo = ME + 'ç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'imos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	if tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'eç'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicionalsubjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "eç" + MI

				else:
					ME = verbo[slice(-2)]
					MI = 'e'
					verbo = ME + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "eç" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'eç' + MI
				else:
					MI = 'amos'
					verbo = ME + 'eç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'eç' + MI
			else:
				MI = 'am'
				verbo = ME + 'eç' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'eç' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	return verbo


#
# formacao_verbo_medir('medir','presente','singular',None,'2pessoa')
# formacao_verbo_medir('medir','presente','singular',None,'3pessoa')
# formacao_verbo_medir('medir','presente','singular',None,'1pessoa')
# formacao_verbo_medir('medir', 'infinitivo',  'singular', 'masculino', None)
# formacao_verbo_medir('medir','particípio','singular','feminino',None)
# formacao_verbo_medir('medir','gerúndio',None,None,None)


# VERBO SABER
def formacao_verbo_saber(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'infinitivo':
		verbo = verbo

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	#

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)

		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'ei'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-2)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'e'
				verbo = ME + MI

			else:
				MI = 'es'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-2)]
			MI = 'e'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

			else:
				ME = verbo[slice(-2)]
				MI = 'emos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'eis'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

			else:
				ME = verbo[slice(-2)]
				MI = 'em'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			MI = 'oube'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI

			else:
				MI = 'ste'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':

			MI = 'oube'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI
			else:
				MI = 'oubemos'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			MI = 'oubestes'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI

			else:
				MI = 'ouberam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)]
		if ((OI_tipo_de_pessoa == '1pessoa' or '3pessoa') and OI_numero == 'singular'):
			MI = 'oubera'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI
			else:
				MI = 'ouberas'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI
			else:
				MI = 'oubéramos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI

			else:
				MI = 'oubéreis'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI

			else:
				MI = 'ouberam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':

		ME = verbo[slice(-4)]
		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'
				or OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			MI = 'oubesse'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubesses'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubésssemos'
				verbo = ME + MI
		#
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubésseis'
				verbo = ME + MI
		#
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'aib' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)
		verbo = ME + 'oub' + MI
	#
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'oub' + MI

	elif tipo_de_orientacao == 'imperativo_I':

		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + "aib" + MI
			else:
				MI = 'e'
				verbo = ME + 'ab' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			MI = 'a'
			verbo = ME + 'aib' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'aib' + MI
			else:
				MI = 'amos'
				verbo = ME + 'aib' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			MI = 'ei'
			verbo = ME + 'ab' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'aib' + MI
			else:
				MI = 'am'
				verbo = ME + 'aib' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"
		else:
			MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
			                                              padrao_pessoa_morfologia)
		verbo = ME + 'aib' + MI

	return verbo


#
# formacao_verbo_saber('saber', 'pretérito_imperfectivo',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'presente',  'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'presente',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'particípio',  'singular', 'feminino', None)
# formacao_verbo_saber('saber', 'gerúndio',  None, None, None)
# formacao_verbo_saber('saber', 'não_finito_concretizado',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'futuro',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'passado_volitivo',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_I',  'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_II',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_condicional',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_conjuntivo',  'plural', None, '3pessoa')
# formacao_verbo_saber('saber', 'imperativo_II',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'imperativo_I',  'singular', None, '2pessoa')


# VERBO ESTAR

def formacao_verbo_estar(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	ME = verbo[slice(-2)]
	if tipo_de_orientacao == 'subjuntivo_condicional':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'esse'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
				verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
				verbo = ME + 'iv' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI


	elif tipo_de_orientacao == 'imperativo_I':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ej' + MI
				else:
					MI = 'á'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				MI = 'ai'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI

	elif tipo_de_orientacao == 'imperativo_II':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI
		if OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'er'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
				verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'
				verbo = ME + 'iv' + MI

			if OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo = ME + 'iv' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
				verbo = ME + 'iv' + MI
	elif tipo_de_orientacao == 'pretérito_imperfectivo':

		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'futuro':

		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':

		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ou'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa'):

				MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
				                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia)

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'ão'
			verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ive'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'eve'
				verbo = ME + MI
		if OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
				verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ivera'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'ivera'
				verbo = ME + MI
		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'

				verbo = ME + MI
	elif tipo_de_orientacao == 'não_finito_concretizado':

		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':

		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':

		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo
# formacao_verbo_estar('estar','presente','singular',None,'1pessoa')

# VERBO DIZER

def formacao_verbo_dizer(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-3)]
				MI = 'go'
				verbo = ME + MI


			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'es'
					verbo = ME + MI


			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = ''
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'emos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'eis'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'isse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI

				else:
					MI = 'isseste'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'isse'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa':
			ME = verbo[slice(-4)]
			if padrao_pessoa_morfologia == "3pessoa_do_singular":
				MI = 'isse'
				verbo = ME + MI

			else:
				MI = 'issemos'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI

				else:
					MI = 'issestes'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI
				else:
					MI = 'isseram'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ia'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'

				else:
					MI = 'ias'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'íamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'íeis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'iam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'issera'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isseras'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'issera'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isséramos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isséreis'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'


				else:
					MI = 'isseram'

				verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iria'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'irias'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríamos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríeis'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iriam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
												OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI[1:]
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'issesse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issesses'
				verbo = ME + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
					verbo = ME + MI

				else:
					MI = 'isséssemos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issésseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':

			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):

				MI = 'a'
				verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'as'
					verbo = ME + 'g' + MI
		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'amos'
					verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'ais'
					verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'am'
					verbo = ME + 'g' + MI


	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
																padrao_pessoa_morfologia)
		verbo = ME + MI


	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
					verbo = ME + MI
				else:
					MI = 'iz'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'iga'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'izei'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igam'
				verbo = ME + MI


	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igas'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'iga'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = 'er'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'eres'
					verbo = ME + 'iss' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'ermos'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'erem'
				verbo = ME + 'iss' + MI
	elif tipo_de_orientacao == 'infinitivo':
		ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if genero == 'masculino':
				MI = 'ito'
			else:
				MI = 'ita'
		else:
			if genero == 'masculino':
				MI = 'itos'
			else:
				MI = 'itas'

		verbo = ME + MI
	return verbo
#
formacao_verbo_dizer('maldizer','presente','-ER','singular',None,'3pessoa')
#
# ##TESTE dizer
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'presente',  numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_I',  numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_imperfectivo',  numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_II',  numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'passado_volitivo',  numero, None, tipo_pessoa))
#
# #futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'futuro',  numero, None, tipo_pessoa))
#
# #subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_conjuntivo',  numero, None, tipo_pessoa))
#
# #subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_condicional',  numero, None, tipo_pessoa))
#
#
# #subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_optativo',  numero, None, tipo_pessoa))
#
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_I',  numero, None, tipo_pessoa))
#
# # imperativo_II
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_II',  numero, None, tipo_pessoa))
#
# # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'não_finito_concretizado',  numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_dizer('dizer', 'infinitivo',  numero, 'feminino', None))
#
# # gerúndio
# print(formacao_verbo_dizer('dizer', 'gerúndio',  None, None, None))
#
# # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_dizer('dizer', 'particípio',  numero, genero, None))
#

#VERBO CONTER DETER
def formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
					   OI_numero, genero, OI_tipo_de_pessoa,
					   padrao_pessoa_morfologia='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo = ME + 'iv' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
																padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ende'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'inh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo = ME + 'inh' + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
														 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'em'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'eve'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ivera'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo


###VERBO TRAZER

def formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]+'g'
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
													 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		else:
			if OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
				ME = verbo[slice(-2)]
				MI = ''
			else:
				ME = verbo[slice(-2)]
				MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
												 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)] + 'oux'
		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			OI_tipo_de_pessoa == '3pessoa' and 	OI_numero == 'singular'):
				MI='e'
		else:
			MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-3)]+'r'
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]+'r'
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'g'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero =='singular':
			ME = verbo[slice(-2)]
			MI = ''
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero =='plural':
			ME = verbo[slice(-2)]
			MI = 'ei'
		else:
			ME = verbo[slice(-3)] + 'g'
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
													 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)] + 'g'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# formacao_verbo_trazer('trazer','gerúndio','-ER',None,None,None)
# formacao_verbo_trazer('trazer','particípio','-ER','singular','feminino',None)
# print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None)
#
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'3pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'3pessoa','Morfologia_padrão')





	










	



	verbo = ME + MI

	return verbo

# formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
#


# VERBO TER

def formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                       OI_numero,genero, OI_tipo_de_pessoa,
                       padrao_pessoa_morfologia='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo = ME + 'iv' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ende'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo = ME+MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa' :

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME+'inh'+MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo = ME + 'inh' + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'em'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'eve'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ivera'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	
	return verbo

# 
# ##TESTE ter
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# #presente
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
#
# # # gerúndio
# print(formacao_verbo_ter('ter', 'gerúndio', '-ER', None, None, None))
# #
# # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None))

# ####################################################################################

# VERBO SER

def formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		if OI_numero == 'singular':
			ME = 'er'
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'eis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'er'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia,OI_numero, genero,
		                                           OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'ou'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = ''
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'é'
				else:
					MI = 'és'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = ''
				MI = 'é'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo[slice(-2)]
					MI = 'omos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ois'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo[slice(-2)]
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':

		ME = 'f'
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ui'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'oi'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
					verbo = ME + MI
				else:
					MI = 'omos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ostes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ora'
				verbo = ME + MI


			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_condicional':

		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'osse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
					verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia="Morfologia_padrão")
		verbo = ME + 'ej' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'or'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo = ME + MI



		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ej' + MI
				else:
					MI = 'ê'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ede'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
				MI = 'ais'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI
	
	return verbo

# # ##TESTE ser
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # #presente
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# #
# # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_optativo
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # infinitivo
# print(formacao_verbo_ser('ser', 'infinitivo', '-ER', numero, 'feminino', None))
# #
# # # # gerúndio
# print(formacao_verbo_ser('ser', 'gerúndio', '-ER', None, None, None))
# # #
# # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_ser('ser', 'particípio', '-ER', numero, genero, None))

# ####################################################################################

# VERBO IR

def formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero,
		                                         OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero,
		                                           genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				MI = 'ou'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'ais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				MI = 'ai'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = 'i'
				MI = 'des'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'am'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = 'f'
				MI = 'ui'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'
				MI = 'oi'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'omos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'ostes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = 'f'
				MI = 'ora'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'osse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if  OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = 'v'
				MI = 'á'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia,
		                                                        OI_numero, OI_tipo_de_pessoa,     padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ai'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'i'
				MI = 'de'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = 'v'
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'or'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo = ME + MI

	return verbo
# #
# # #
# # # # ##TESTE ir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ir('ir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_ir('ir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # gerúndio
# # print(formacao_verbo_ir('ir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# # # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_ir('ir', 'particípio', '-IR', numero, genero, None))




# VERBOS VIR E INTERVIR


def formacao_verbo_vir_intervir(verbo, tipo_de_orientacao,padrao_de_morfologia,
                                OI_numero,genero, OI_tipo_de_pessoa,
                                padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	ME = verbo[slice(-2)]

	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero,
		                                           OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'inha'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inhas'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínheis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inham'
				verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero,
		                                         OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		if OI_numero == 'singular':
			if genero == 'masculino':
				MI = 'indo'
			else:
				MI = 'inda'
		else:
			if genero == 'masculino':
				MI = 'indos'
			else:
				MI = 'indas'
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'enho'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if verbo == 'vir':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'em'
					else:
						MI = 'ens'
					verbo = ME + MI
				else:
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ém'
					else:
						MI = 'éns'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if verbo == 'vir':
					MI = 'em'
				else:
					MI = 'ém'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'imos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'indes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'im'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'eio'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'iemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'iestes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieram'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iera'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieras'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieram'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iesse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iesses'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iéssemos'
				verbo = ME + '' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'iésseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhas'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enham'
				verbo = ME + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa' :
				if verbo =='vir':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
						verbo = ME + 'enh' + MI
					else:
						MI = 'em'
						verbo = ME + MI
				else:
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
						verbo = ME + 'enh' + MI
					else:
						MI = 'ém'
						verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'enhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'inde'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = verbo = ME + 'enh' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ier'
				verbo = ME + MI

			if OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ieres'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'iermos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierdes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierem'
				verbo = ME + MI
	return verbo

#
# # #
# # # # ##TESTE intervir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_vir_intervir('intervir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_vir_intervir('intervir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_vir_intervir('intervir', 'particípio', '-IR', numero, genero, None))
#
# ######################################
#
#
# # # # ##TESTE vir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_vir_intervir('vir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_vir_intervir('vir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_vir_intervir('vir', 'particípio', '-IR', numero, genero, None))


# VERBO HAVER
def formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         OI_numero,genero, OI_tipo_de_pessoa,
                         padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = 'ido'
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			ME = verbo[slice(-4)]
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'ei'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'á'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'á'
				else:
					ME = verbo[slice(-2)]
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'á'
				else:
					ME = verbo[slice(-2)]
					MI = 'eis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ão'
				
		verbo = ME + MI
	
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'e'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'este'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'e'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'estes'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'eram'

		verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				MI = 'era'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'eras'


			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'era'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'eram'
		verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
				verbo = ME + 'ouv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
					verbo = ME + 'ud' + MI
				else:
					MI = 'éssemos'
					verbo = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
				verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'  or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'aj' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ais'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'aj' + MI
				else:
					MI = 'á'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + 'aj' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				MI = 'ei'
				verbo = ME + 'av' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + 'aj' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + MI
				else:
					MI = 'amos'
					verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'  or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo = ME + 'ouv' + MI

	return verbo

# # # # # ##TESTE haver
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # infinitivo
# print(formacao_verbo_haver('haver', 'infinitivo', '-ER', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# print(formacao_verbo_haver('haver', 'gerúndio', '-ER', None, None, None))
# # # # # #
# # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_haver('haver', 'particípio', '-ER', numero, genero, None))

# VERBO PODER

def formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         OI_numero, genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero,
		                                         OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero,
		                                           genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
			                                         OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			verbo = ME +'ss'+ MI


		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
			                                         OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			verbo = ME + MI
	
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ude'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udeste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ôde'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'uderam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'udera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderas'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'udera'

		elif OI_numero =='plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):

				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
				verbo = ME + 'ud' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '3pessoa' :
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
				                                                       OI_tipo_de_pessoa,
				                                                       padrao_pessoa_morfologia)
				verbo = ME + 'ud' + MI

			elif OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo = ME + 'ud' + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'ud' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ossa'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ode'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'ossa'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'odei'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa':

				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ossa'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia,
		                                                    OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME +'ud'+MI

	return verbo


# # # # ##TESTE poder
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # # #presente
# # # print("A conjugação é:")
# 
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # subjuntivo_optativo
# # # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # # infinitivo
# print(formacao_verbo_poder('poder', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # gerúndio
# print(formacao_verbo_poder('poder', 'gerúndio', '-ER', None, None, None))
# # # # # # #
# # # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_poder('poder', 'particípio', '-ER', numero, genero, None))
# 





# VERBO FAZER


def formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'presente':
		if OI_numero  == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-3)]
				MI = 'ço'
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
				else:
					MI = 'es'
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'az'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-2)]
				MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				MI = 'azeis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'azem'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero=='singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'iz'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeste'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ez'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeram'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'izera'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izeras'

			elif OI_tipo_de_pessoa == '3pessoa' :
				ME = verbo[slice(-4)]
				MI = 'izera'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéramos'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'izeram'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)[slice(1,7)]
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'aria'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'aria'
				else:
					MI = 'arias'
			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'aria'


		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'aríamos'
			elif OI_tipo_de_pessoa == '2pessoa' :
				MI = 'aríeis'
			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'ariam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'izesse'

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izesses'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izéssemos'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izésseis'

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izessem'
		verbo = ME+MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'

			elif OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'amos'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
		verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'
			if OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo = ME + 'iz' + MI

	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular.'

			elif OI_tipo_de_pessoa == '2pessoa' :

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ç' + MI
				else:
					MI = 'z'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'a'
				verbo = ME + 'ç' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ç' + MI
				else:
					MI = 'ei'
					verbo = ME + 'z' + MI


			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if tipo_de_orientacao == 'imperativo_II':
			ME = verbo[slice(-3)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					verbo = 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:'
				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'as'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'a'
					verbo = ME + 'ç' + MI

			elif OI_numero == 'plural':

				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'amos'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'ais'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'am'
					verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI
	
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if genero == 'feminino':
				MI = 'eita'
			elif genero == 'masculino':
				MI = 'eito'
		elif OI_numero == 'plural':
			if genero == 'feminino':
				MI = 'eitas'
			elif genero == 'masculino':
				MI = 'eitos'
		verbo = ME + MI
	return verbo

# #
# #
# # # # # # ##TESTE fazer
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # # ###
# # # # # # #presente
# # # # print("A conjugação é:")
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # ###
# # # # print("A conjugação pretérito_perfectivo_I é:")
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # # #
# # # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # futuro
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # subjuntivo_optativo
# # # # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # infinitivo
# print(formacao_verbo_fazer('fazer', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # # gerúndio
# print(formacao_verbo_fazer('fazer', 'gerúndio', '-ER', None, None, None))
# # # # # # # #
# # # # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_fazer('fazer', 'particípio', '-ER', numero, genero, None))
#

#################################################################################

def formacao_da_estrutura_do_verbo_modal(TIPO_DE_EXPERIENCIA,verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if (TIPO_DE_EXPERIENCIA == 'Ser' or
			TIPO_DE_EXPERIENCIA == 'Fazer' or
			TIPO_DE_EXPERIENCIA == 'Sentir'):

		if verbo == 'dever':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
			                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão")
			verbo = ME + MI

		elif verbo == 'poder':
			verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                   OI_numero, genero, OI_tipo_de_pessoa,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'haver':
			verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                   OI_numero, genero, OI_tipo_de_pessoa,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'ter':

			verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                 OI_numero, genero, OI_tipo_de_pessoa,
			                                 padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
	# elif verbo == 'ter de':
	# 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
	# 	                           OI_numero, genero, OI_tipo_de_pessoa,
	# 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
	return verbo


# formacao_da_estrutura_do_verbo_modal('Sentir','poder','presente','-ER','singular',None,'1pessoa')

def formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	padrao_de_morfologia=detecta_padrao_morfologia(verbo)
	if verbo == 'estar':
		verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ter':
		verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'haver':
		verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ir':
		verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'vir':
		verbo = formacao_verbo_vir_invervir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ser':
		verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	return verbo
#
# formacao_da_estrutura_do_verbo_AUX('estar','presente','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo_AUX('ser','presente','singular',None,'1pessoa','Morfologia_padrão')

def formacao_verbo_participio(verbo, tipo_de_orientacao, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	ME = verbo[slice(-2)]
	padrao_de_morfologia=detecta_padrao_morfologia(verbo)
	MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa=None,padrao_pessoa_morfologia='Morfologia_padrão')
	verbo_participio = ME + MI

	return verbo_participio

# #
# formacao_verbo_participio("cortar",'particípio','singular','masculino',None)


def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
                                       genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	padrao_de_morfologia=detecta_padrao_morfologia(verbo)
	if verbo == 'estar':
		verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                     OI_numero,
		                                     genero, OI_tipo_de_pessoa,
		                                     padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ter':
		verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                   OI_numero,
		                                   genero, OI_tipo_de_pessoa,
		                                   padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'haver':
		verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                     OI_numero,
		                                     genero, OI_tipo_de_pessoa,
		                                     padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ir':
		verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                  OI_numero,
		                                  genero, OI_tipo_de_pessoa,
		                                  padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'vir':
		verbo_conj = formacao_verbo_vir_invervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                            OI_numero,
		                                            genero, OI_tipo_de_pessoa,
		                                            padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ser':
		verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                   OI_numero,
		                                   genero, OI_tipo_de_pessoa,
		                                   padrao_pessoa_morfologia='Morfologia_padrão')
	elif verbo[-5:] == 'fazer':
		verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
									 OI_numero, genero, OI_tipo_de_pessoa,
									 padrao_pessoa_morfologia)

	elif verbo == None:
		verbo_conj = ''
	else:

		OE_experiencia_do_verbo = experiencia_do_verbo(verbo)
		OI_orientacao_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao,
																				  padrao_de_morfologia,
																				  OI_numero,
																				  genero, OI_tipo_de_pessoa,
																				  padrao_pessoa_morfologia)
		verbo_conj = OE_experiencia_do_verbo + OI_orientacao_interpessoal_do_verbo
	return verbo_conj
# formacao_da_estrutura_do_verbo('ser','presente','singular',None,'1pessoa')
#
# X=['-AR','-ER','-IR','-OR']
# Y=['plural','singular']
# Z=['1pessoa','2pessoa','3pessoa']
#
# for j in Y:
# 	for p in Z:
# 		transito = formacao_da_estrutura_do_verbo('fazer','pretérito_perfectivo_I',j,None,p)
# 		print(transito)
# formacao_da_estrutura_do_verbo('fazer','pretérito_perfectivo_I','singular',None,'1pessoa')

# ###########################################################################
# #########################################################################

#
# formacao_da_estrutura_do_verbo('ser','presente','-AR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('andar','pretérito_perfectivo_I','-AR','singular',None,'3pessoa')
# formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','-ER','plural',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','presente','-OR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','gerúndio','-OR',None,None,None)
# formacao_da_estrutura_do_verbo('cortar', 'particípio', '-AR', 'singular', 'feminino', None)
#
# TIPO_DE_EXPERIENCIA = ['Ser','Fazer', 'Sentir']
#  funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
# 	                                      'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()
#
#
# formacao_da_estrutura_do_verbo('ser','presente','-AR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('andar','pretérito_perfectivo_I','-AR','singular',None,'3pessoa')
# formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','-ER','plural',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','presente','-OR','singular',None,'1pessoa')
# # formacao_da_estrutura_do_verbo('expor','gerúndio','-OR',None,None,None)
# formacao_da_estrutura_do_verbo('cortar', 'particípio', '-AR', 'singular', 'feminino', None)
#
# TIPO_DE_EXPERIENCIA = ['Ser','Fazer', 'Sentir']
#  funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
# 	                                      'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()
#


def verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
                tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa,
                padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna a estrutura que realiza os verbos no português.
    '''
	classe_do_verbo = def_classe_de_verbo(funcao_no_grupo_verbal)
	padrao_de_morfologia = detecta_padrao_morfologia(verbo)
	if classe_do_verbo == 'lexical':
		if (TIPO_DE_EXPERIENCIA == 'Ser' or
				TIPO_DE_EXPERIENCIA == 'Fazer' or
				TIPO_DE_EXPERIENCIA == 'Sentir'):
			if verbo == 'estar':
				verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
									 genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

			elif verbo == 'trazer':
				verbo = formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
								  genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'ter':
				verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
										   OI_numero, genero, OI_tipo_de_pessoa,
										   padrao_pessoa_morfologia)
			elif verbo == 'ser':
				verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
										   OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'ir':
				verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
										  genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'haver':
				verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif verbo == 'agredir':
				verbo = formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
			elif verbo == 'aferir':
				verbo = formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											  OI_numero, genero, OI_tipo_de_pessoa,
											  padrao_pessoa_morfologia)
			elif verbo == 'medir':
				verbo = formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif verbo == 'saber':
				verbo = formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif (verbo == 'vir' or verbo == 'intervir'):
				verbo = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
													OI_numero, genero, OI_tipo_de_pessoa,
													padrao_pessoa_morfologia)
			elif (verbo == 'conter' or verbo == 'deter'):
				verbo = formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
													OI_numero, genero, OI_tipo_de_pessoa,
													padrao_pessoa_morfologia)
			elif verbo == 'poder':
				verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)

			else:
				if verbo[-4:] == 'ruir':

					verbo = formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia,
												OI_numero, genero, OI_tipo_de_pessoa,
												padrao_pessoa_morfologia)

				elif verbo[-3:] == 'car':
					verbo = formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
				elif verbo[-5:] == 'fazer':
					verbo = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
												 OI_numero, genero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)
				elif verbo[-3:] == 'gar':
					verbo = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
				elif verbo[-3:] == 'çar':
					verbo = formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)

				elif verbo[-3:] == 'cer':
					verbo = formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)

				elif verbo[-5:] == 'dizer':
					verbo = formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
												 genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
				else:
					verbo = formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
														   genero, OI_tipo_de_pessoa,
														   padrao_pessoa_morfologia)
	elif classe_do_verbo == 'modal':
		if (TIPO_DE_EXPERIENCIA == 'Ser' or
				TIPO_DE_EXPERIENCIA == 'Fazer' or
				TIPO_DE_EXPERIENCIA == 'Sentir'):

			if verbo == 'dever':
				ME = verbo[slice(-2)]
				MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
														 OI_tipo_de_pessoa,
														 padrao_pessoa_morfologia="Morfologia_padrão")
				verbo = ME + MI

			elif verbo == 'poder':
				verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia='Morfologia_padrão')

			elif verbo == 'haver':
				verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia='Morfologia_padrão')

			elif verbo == 'ter':

				verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
										   OI_numero, genero, OI_tipo_de_pessoa,
										   padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
	# elif verbo == 'ter de':
	# 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
	# 	                           OI_numero, genero, OI_tipo_de_pessoa,
	# 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
	elif classe_do_verbo == 'auxiliar':
		verbo = formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
												   genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
	else:
		verbo = ''
	return verbo


#EXEMPLOS
# verbo_geral("Fazer",'Evento','trazer','pretérito_perfectivo_I','singular',None,'3pessoa')

#
# verbo=verbo_geral("Fazer",'Evento','usufruir','imperativo_I','singular',None,'2pessoa')
# # verbo_geral("Fazer",'Evento','espaçar','imperativo_I','plural',None,'3pessoa')
# # formacao_verbo_ÇAR('espaçar', 'imperativo_I', '-AR','plural',None,'3pessoa')

# verbo_geral("Fazer",'Evento','desfazer','pretérito_perfectivo_II','plural',None,'1pessoa')
# # # verbo_geral("Fazer",'Evento','ficar','pretérito_perfectivo_I','singular',None,'1pessoa')
# verbo_geral("Fazer",'Evento','abraçar','presente','singular',None,'1pessoa')
# verbo_geral('Ser','Auxiliar','ter','passado_volitivo','singular',None,'1pessoa')
# verbo_geral('Fazer','Evento','ir','passado_volitivo','singular',None,'1pessoa')
# verbo_geral('Fazer','Evento','cortar', 'particípio', 'singular', 'feminino',None)
# verbo_geral('Ser','Evento','ser', 'particípio', 'singular','masculino', '1pessoa')
# verbo_geral('Sentir','Evento','enternecer','presente','singular',None,'2pessoa')
# verbo_geral('Sentir','Evento','poder','presente','singular',None,'2pessoa')
# verbo_geral(None,None,None,None,None,None,None,None)

#####ORDEM DO GRUPO#####
#    grupo verbal

#
# print('Qual de Agência?')
# 	AGENCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não-agenciado']).ask()
#
# print('Qual o verbo auxiliar de AGÊNCIA passiva desejado?')
# 		auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()
#
# print('Qual o verbo auxiliar de AGENCIA passiva desejado?')
# 	auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()

def realizacao_de_AGENCIA_passiva(verbo_AUX, tipo_de_orientacao_AUX, OI_numero_AUX,
                                  genero_AUX, OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX,
                                  TIPO_DE_EXPERIENCIA_LEX,funcao_no_grupo_verbal_POS_FINAL,  verbo_LEX,
                                  tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX,
                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''
    '''
	verbo_auxiliar_passiva = formacao_da_estrutura_do_verbo_AUX(verbo_AUX,  tipo_de_orientacao_AUX,
	                                                            OI_numero_AUX,
	                                                            genero_AUX, OI_tipo_de_pessoa_AUX,
	                                                            padrao_pessoa_morfologia_AUX)

	verbo_lexical = verbo_geral( TIPO_DE_EXPERIENCIA_LEX,funcao_no_grupo_verbal_POS_FINAL, verbo_LEX,
                    tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                    padrao_pessoa_morfologia_LEX)

	grupo_verbal_AGENCIA_passiva = verbo_auxiliar_passiva + ' ' + verbo_lexical
	return grupo_verbal_AGENCIA_passiva
#
# # #
# formacao_da_estrutura_do_verbo_AUX('ser','particípio','singular','masculino',None,'Morfologia_padrão')
# verbo_geral("Fazer",'Evento','levar','particípio','singular','masculino',None,'Morfologia_padrão')
# # # #
# realizacao_de_AGENCIA_passiva('ser','particípio','singular','masculino',None,'Morfologia_padrão','Fazer','Evento','levar','particípio','singular','masculino',None,'Morfologia_padrão')

# #




# partindo do sistema

##para grupo verbal, fiz seleções nos sistemas de tempo secundário e agenciamento
# pq as outras seleções já são feitas na ordem da palavra verbal(ficaria redundante)

# print('Qual o tipo_pessoa de evento desejado para o grupo verbal?')
# 	TIPO_DE_EVENTO = choice.Menu(['Ser', 'Fazer', 'Sentir']).ask()
# print('Selecione um lema verbal que realize o tipo_pessoa de evento desejado:')
# 		print('Qual a agência do GV?')
# 		AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado_passiva',
# 		                       'não_agenciado']).ask()
# print('Há a seleção de  tempo secundário')
# 			TEMPO_SECUNDARIO = choice.Menu(['-', '1_reiteração', '2_reiterações',
# 			                                '3_reiterações', '4_reiterações']).ask()
# print('Dêixis modal = não_modalizada')
# 				print('Selecione a finitude')
# 				FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
#
# print('Qual a dêixis temporal?')
# 					DEIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
# print('Qual o aspecto verbal?')
# 					ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
#
# print('Selecione o tipo_pessoa de OI não-orientação desejada')
# 						não_orientado = choice.Menu(['infinitivo', 'gerúndio'])
					
					
					#############


# Observação importante sobre o desenvolvimento da função de grupo verbal: Como os sistemas de
# FINITUDE,DEIXIS_TEMPORAL, ASPECTO na ordem do grupo são 'síndromes' de significados que reverberam
#desde o morfema, resolvi não repetir por uma questão de custo de desenvolvimento().
#########################################


def grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
                 tipo_de_orientacao_1,  OI_numero_1, genero_1,
                 OI_tipo_de_pessoa_1,padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2,
                 verbo_2, tipo_de_orientacao_2,  OI_numero_2, genero_2, OI_tipo_de_pessoa_2,padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                 tipo_de_orientacao_3,  OI_numero_3, genero_3, OI_tipo_de_pessoa_3,padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                 tipo_de_orientacao_4, 
                 OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4,TIPO_DE_EXPERIENCIA_LEX,
                 funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, 
                 OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''()->str
	Retorna a estrutura que realiza o grupo verbal, dadas escolhas de
	tipo_pessoa DE EVENTO, AGÊNCIA, TEMPO SECUNDÁRIO, FINITUDE E ASPECTO.
	>>>grupo_verbal()
	 'ando'
	>>>grupo_verbal()
	 'estou andando'
	>>>grupo_verbal()
	 'andava'
	'''

	if TIPO_DE_EXPERIENCIA_GV == 'Ser' or TIPO_DE_EXPERIENCIA_GV == 'Fazer' or TIPO_DE_EXPERIENCIA_GV == 'Sentir':

		if AGENCIA == 'agenciado_ativa' or AGENCIA == 'não_agenciado':

			verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
                 tipo_de_orientacao_1,  OI_numero_1, genero_1,
                 OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
			verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
			                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, 
			                     OI_numero_2,
			                     genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
			verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
			                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, 
			                     OI_numero_3,
			                     genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)
			verbo4 = verbo_geral(TIPO_DE_EXPERIENCIA_4,
			                     funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4, 
			                     OI_numero_4,
			                     genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4)
			Evento = verbo_geral(TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
			                     verbo_LEX, tipo_de_orientacao_LEX, 
			                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX
			                     , padrao_pessoa_morfologia_LEX)

			grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento

		else:
			tipo_de_orientacao_LEX = 'particípio'
			verbo_4 = 'ser'
			verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1,
			                     funcao_no_grupo_verbal_1,
			                     verbo_1, tipo_de_orientacao_1,  OI_numero_1,
			                     genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
			verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
			                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, 
			                     OI_numero_2,
			                     genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
			verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
			                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, 
			                     OI_numero_3,
			                     genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)

			verbos_passiva = realizacao_de_AGENCIA_passiva(verbo_4,tipo_de_orientacao_4, 
			                                               OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
			                                               padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
			                                               funcao_no_grupo_verbal_POS_FINAL, verbo_LEX,
			                                               tipo_de_orientacao_LEX,
			                                               OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
			                                               padrao_pessoa_morfologia_LEX)


			grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva
	return (re.sub(' +', ' ', grupo_verbal).strip())

#####ex###
#
# #levo

# grupo_verbal('Fazer',"agenciado_ativa",None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,"Fazer","Evento",'trazer','presente','singular',None,'1pessoa')


# grupo_verbal('Fazer', 'agenciado_passiva', None, None, None,
#              None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None,
#              None, None, None, None, 'Ser', 'Auxiliar', 'ser', 'pretérito_perfectivo_I',
#              'singular', None, '1pessoa', 'Morfologia_padrão', 'Fazer', 'Evento',
#              'descartar', 'particípio', 'singular', 'masculino',None,'Morfologia_padrão')

# # #estava sendo levado
#
# grupo_verbal('Fazer', 'agenciado_passiva', 'Ser', 'Auxiliar', 'estar',
#                  'pretérito_imperfectivo', '-AR', 'singular', None,
#                  '1pessoa', 'Morfologia_padrão', None, None,
#                  None, None, None, None, None, None,
#                  None, None, None, None,
#                  None, None, None, None, None,
#                  None, 'Ser', 'Auxiliar', 'ser','gerúndio','-ER',
#              'singular',None,'1pessoa','Morfologia_padrão','Fazer','Evento',
#              'levar','particípio','-AR','singular','masculino',None,'Morfologia_padrão')
#
# #'deveria ter sido levado'
# grupo_verbal('Fazer', 'agenciado_passiva', "Fazer", 'Modal', 'dever', 'passado_volitivo', '-ER', 'singular', None,
#              '1pessoa', "Morfologia_padrão", 'Ser', 'Auxiliar', 'ter', 'infinitivo', '-ER', None, None, None, None,
#              None, None, None,None, None, None, None, None, None, 'Ser', 'Auxiliar', 'ser', 'particípio', '-ER', 'singular', 'masculino', None, 'Morfologia_padrão',  "Fazer", 'Evento', 'levar', 'particípio', '-AR', 'singular', 'masculino', None, 'Morfologia_padrão')


#
# #
# ####

###########################################
#
#
# def grupo_conjuntivo():
# 	'''
#     '''
#
# 	modo_insercao = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
#
# 	if modo_insercao == 'inserção_manual':
# 		conjuncao = input('Escreva a conjunção desejada:')
#
# 	elif modo_insercao == 'inserção_menu':
#
# 		print('Qual o tipo_pessoa de conjunção?')
# 		tipo_de_conjuncao = choice.Menu(['paratática(linker)', 'hipotática(binder)']).ask()
#
# 		if tipo_de_conjuncao == 'paratática(linker)':
# 			print('Qual o tipo_pessoa da conjunção paratática(linker)?')
# 			tipo_de_paratática = choice.Menu(['Aditiva', 'Adversativa', 'Conclusiva',
# 			                                  'Alternativa',
# 			                                  'Explicativa']).ask()
# 			if tipo_de_paratática == 'Aditiva':
# 				conjuncao = choice.Menu(['e', 'mas ainda', 'mas também', 'nem']).ask()
#
# 			elif tipo_de_paratática == 'Adversativa':
# 				conjuncao = choice.Menu(['contudo', 'entretanto', 'mas',
# 				                         'não obstante', 'no entanto',
# 				                         'porém', 'todavia']).ask()
#
# 			elif tipo_de_paratática == 'Alternativa':  # PRECISO VER COMO IMPLEMENTAR UM COMPLEXO COM ESTE TIPO
# 				conjuncao = choice.Menu(['já', 'ou', 'ora',
# 				                         'quer']).ask()
#
# 			elif tipo_de_paratática == 'Conclusiva':
# 				conjuncao = choice.Menu(['assim', 'então', 'logo',
# 				                         'por conseguinte', 'por isso',
# 				                         'portanto']).ask()
#
# 			elif tipo_de_paratática == 'Explicativa':
# 				conjuncao = choice.Menu(['pois', 'porquanto', 'porque',
# 				                         'que']).ask()
#
# 		elif tipo_de_conjuncao == 'hipotática(binder)':
# 			print('Qual o tipo_pessoa da conjunção hipotática(binder)?')
# 			tipo_de_hipotática = choice.Menu(['Causal', 'Concessiva', 'Condicional',
# 			                                  'Conformativa', 'Final', 'Proporcional',
# 			                                  'Temporal', 'Comparativa', 'Consecutiva',
# 			                                  'Integrante', 'Relativa']).ask()
#
# 			if tipo_de_hipotática == 'Causal':
# 				conjuncao = choice.Menu(['porque', 'pois', 'porquanto',
# 				                         'como', 'pois que', 'por isso que',
# 				                         'á que', 'uma vez que', 'visto que',
# 				                         'visto como', 'que']).ask()
#
#
# 			elif tipo_de_hipotática == 'Concessiva':
# 				conjuncao = choice.Menu(['embora', 'conquanto', 'ainda que',
# 				                         'mesmo que', 'posto que', 'bem que',
# 				                         'se bem que', 'apesar de que', 'nem que',
# 				                         'que']).ask()
#
#
# 			elif tipo_de_hipotática == 'Condicional':
# 				conjuncao = choice.Menu(['se', 'caso', 'quando',
# 				                         'conquanto que', 'salvo se', 'sem que',
# 				                         'dado que', 'desde que', 'a menos que',
# 				                         'a não ser que']).ask()
#
#
# 			elif tipo_de_hipotática == 'Conformativa':
# 				conjuncao = choice.Menu(['conforme', 'como', ''
# 				                                             'segundo', 'consoante']).ask()
#
# 			elif tipo_de_hipotática == 'Final':
# 				conjuncao = choice.Menu(['para que',
# 				                         'a fim de que', 'porque',
# 				                         'que']).ask()
#
#
# 			elif tipo_de_hipotática == 'Proporcional':
# 				conjuncao = choice.Menu(['à medida que', 'ao passo que', 'à proporção que',
# 				                         'enquanto', 'quanto mais',
# 				                         'quanto menos']).ask()
#
#
# 			elif tipo_de_hipotática == 'Temporal':
# 				conjuncao = choice.Menu(['quando', 'antes que',
# 				                         'depois que', 'até que', 'logo que',
# 				                         'sempre que', 'assim que', 'desde que',
# 				                         'todas as vezes que', 'cada vez que', 'apenas',
# 				                         'mal', 'desde que']).ask()
#
# 			elif tipo_de_hipotática == 'Comparativa':
# 				conjuncao = choice.Menu(['mais que', 'mais do que',
# 				                         'menos que', 'maior que', 'menor que',
# 				                         'melhor que', 'pior que',
# 				                         'menos do que', 'maior do que',
# 				                         'menor do que', 'melhor do que',
# 				                         'pior do que']).ask()
#
# 			elif tipo_de_hipotática == 'Consecutiva':
# 				conjuncao = choice.Menu(['De modo que', 'De maneira que']).ask()
#
# 			elif tipo_de_hipotática == 'Integrante':
# 				conjuncao = choice.Menu(['que', 'se']).ask()
#
# 			elif tipo_de_hipotática == 'Relativa':
# 				conjuncao = choice.Menu(['porque', 'pois', 'porquanto',
# 				                         'como', 'pois que', 'por isso que',
# 				                         'á que', 'uma vez que', 'visto que',
# 				                         'visto como', 'que']).ask()
#
# 	return conjuncao
#
#
# # def conjunção_continuativa():
# # 	'''
# #     '''
# # 	print('Qual o modo de inserção da conjunção?')
# # 	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
# #
# # 	if modo_inserção == 'inserção_manual':
# # 		conjunção_continuativa = input('Escreva o continuativo desejado:')
# #
# # 	elif modo_inserção == 'inserção_menu':
# # 		print('Escolha um continuativo:')
# # 		conjunção_continuativa = input("""
# #                                  1:e
# #                                  2:é
# #                                  3:ah
# #                                  4:mas
# #                                  5:sim
# #                                  6:bem
# #                                  7:não
# #                                  8:agora
# #                                  9:então
# #                                  10:pois é
# #                                  11:tipo_pessoa
# #                                  12:tipo_pessoa assim
# #                                  13:ó
# #                                  14:daí
# #                                  15:aí
# #                                  16:aí então
# #                                  17:quer
# #                                  18:dizer
# #                                  19:assim
# #                                  20:em
# #                                  21:seguida
# #                                  22:por fim
# #                                  23:porque
# #                                  24:porém
# #                                  25:também
# #                                  26:é que
# #                                  27:olha
# #
# #
# #
# #                                Escolha uma opção:""")
# #
# # 		if conjunção_continuativa == '1':
# # 			conjunção_continuativa = 'e'
# # 		elif conjunção_continuativa == '2':
# # 			conjunção_continuativa = 'é'
# # 		elif conjunção_continuativa == '3':
# # 			conjunção_continuativa = 'ah'
# # 		elif conjunção_continuativa == '4':
# # 			conjunção_continuativa = 'mas'
# # 		elif conjunção_continuativa == '5':
# # 			conjunção_continuativa = 'sim'
# # 		elif conjunção_continuativa == '6':
# # 			conjunção_continuativa = 'bem'
# # 		elif conjunção_continuativa == '7':
# # 			conjunção_continuativa = 'não'
# # 		elif conjunção_continuativa == '8':
# # 			conjunção_continuativa = 'agora'
# # 		elif conjunção_continuativa == '9':
# # 			conjunção_continuativa = 'então'
# # 		elif conjunção_continuativa == '10':
# # 			conjunção_continuativa = 'pois é'
# # 		elif conjunção_continuativa == '11':
# # 			conjunção_continuativa = 'tipo'
# # 		elif conjunção_continuativa == '12':
# # 			conjunção_continuativa = 'tipo_pessoa assim '
# # 		elif conjunção_continuativa == '13':
# # 			conjunção_continuativa = 'ó'
# # 		elif conjunção_continuativa == '14':
# # 			conjunção_continuativa = 'daí'
# # 		elif conjunção_continuativa == '15':
# # 			conjunção_continuativa = 'aí'
# # 		elif conjunção_continuativa == '16':
# # 			conjunção_continuativa = 'aí então '
# # 		elif conjunção_continuativa == '17':
# # 			conjunção_continuativa = 'quer'
# # 		elif conjunção_continuativa == '18':
# # 			conjunção_continuativa = 'dizer'
# # 		elif conjunção_continuativa == '19':
# # 			conjunção_continuativa = 'assim'
# # 		elif conjunção_continuativa == '20':
# # 			conjunção_continuativa = 'em'
# # 		elif conjunção_continuativa == '21':
# # 			conjunção_continuativa = 'seguida'
# # 		elif conjunção_continuativa == '22':
# # 			conjunção_continuativa = 'por fim'
# # 		elif conjunção_continuativa == '23':
# # 			conjunção_continuativa = 'porque'
# # 		elif conjunção_continuativa == '24':
# # 			conjunção_continuativa = 'porém'
# # 		elif conjunção_continuativa == '25':
# # 			conjunção_continuativa = 'também'
# #
# # 		elif conjunção_continuativa == '26':
# # 			conjunção_continuativa = 'é que'
# # 		elif conjunção_continuativa == '27':
# # 			conjunção_continuativa = 'olha'
# #
# # 	return conjunção_continuativa
# #
# #
# # ###ESSE TRECHO QUE SEGUE É PRA GUARDAR PRO CASO DE PRECISAR FICAR MAIS ESPECÍFICO NO GRUPO_VERBAL
# # #
# # # print ('Quais tempos secundários?')
# # #        TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro', 'tempo_secundário_não_orientado']).ask()
# # #        compilação_TEMPORAL = []
# # #
# # #
# # #        while  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'tempo_secundário_DT_presente' or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_passado'or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_futuro' or TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_não_orientado':
# # #            compilação_TEMPORAL= [TEMPO_PRIMÁRIO,TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL]
# # #            TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro']).ask()
# # #            if TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'NA':
# # #                break
# # #
# # #
# # #        if AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '+':
# # #            grupo_verbal = verbo_geral () + ' ' + verbo_geral ()
# # #
# # #    return  grupo_verbal
# # #
# #
# # # #####################################
# #
# #
# # ######PALAVRAS NOMINAIS- SUBSTANTIVO
# #
# #
# # # NUMERATIVOS
# #
# ###NUMERATIVOS  CARDINAIS ATÉ A 4 CASA(9 000) NÃOS SEI SE VOU IMPLEMENTAR ATÉ A 6 CASA.....
# #

def ordinal(cardinal,genero):
	'''
    '''
	num = str(cardinal)
	if genero == 'masculino':
		ordinal = num + 'º'
	else:
		ordinal = num + 'ª'

	return ordinal
# num_ordinal = ordinal(4,'masculino')
# #
def porcento(cardinal):
	'''
    '''
	porcento = str(cardinal) + '%'

	return porcento
# porcento(10)

##NÚMEROS CARDINAIS ATÉ A 4 CASA(9 000) NÃOS SEI SE VOU IMPLEMENTAR ATÉ A 6 CASA.....
def num_cardinal_1dig_extenso(unidadeExtenso,genero):
	if unidadeExtenso == "zero":
		numerativo = ''
	else:
		if unidadeExtenso == 'dois':
			if genero == 'feminino':
				numerativo = unidadeExtenso[slice(-3)] + 'uas'
			elif genero == 'masculino':
				numerativo = unidadeExtenso
		elif unidadeExtenso == 'um':
			if genero == 'feminino':
				numerativo = unidadeExtenso + 'a'
			elif genero == 'masculino':
				numerativo = unidadeExtenso
		else:
			numerativo = unidadeExtenso

	return numerativo
# num_cardinal_1dig_extenso('zero','feminino')

def num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero):
	if dezenaExtenso == "zero":
		numerativo = num_cardinal_1dig_extenso(unidadeExtenso,genero)
	elif dezenaExtenso == 'dez':
		if unidadeExtenso == 'zero':
			numerativo = dezenaExtenso
		elif unidadeExtenso == 'um':
			numerativo = 'onze'
		elif unidadeExtenso == 'dois':
			numerativo = 'doze'
		elif unidadeExtenso == 'três':
			numerativo = 'treze'
		elif unidadeExtenso == 'quatro':
			numerativo = 'quatorze'
		elif unidadeExtenso == 'cinco':
			numerativo = 'quinze'
		elif unidadeExtenso == 'seis':
			numerativo = 'dezesseis'
		elif unidadeExtenso == 'sete':
			numerativo = 'dezessete'
		elif unidadeExtenso == 'oito':
			numerativo = 'dezoito'
		elif unidadeExtenso == 'nove':
			numerativo = 'dezenove'
	else:
		digito1 = num_cardinal_1dig_extenso(unidadeExtenso, genero)
		if digito1 == "zero":
			digito1 = ''
		if digito1 == "":
			numerativo = dezenaExtenso +  digito1
		else:
			numerativo = dezenaExtenso + ' e ' +digito1

	return numerativo

# num_cardinal_2dig_extenso('zero','zero','feminino')

def num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero):
	if centenaExtenso == "zero":
		numerativo = num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero)
	else:
		digitos2= num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero)

		if digitos2 =='':
			if (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
					centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
					centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
					centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
				if genero == 'feminino':
					centena = centenaExtenso[slice(-2)] + 'as'
				elif genero == 'masculino':
					centena = centenaExtenso[slice(-2)] + 'os'
				numerativo = centena + digitos2
			else:
				numerativo = centenaExtenso
		else:
			if centenaExtenso == 'cem':
				centena = 'cento e '

			elif (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
					centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
					centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
					centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
				if genero == 'feminino':
					centena = centenaExtenso[slice(-2)] + 'as e '
				elif genero == 'masculino':
					centena = centenaExtenso[slice(-2)] + 'os e '

			numerativo = centena + digitos2

	return numerativo

# num_cardinal_3dig_extenso('duzentos','zero','zero', 'feminino')

def num_cardinal_4dig_extenso(milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,genero):  # Número com 4 dígitos
	if milharExtenso == "zero":
		numerativo = num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero)
	else:
		digito3 = num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero)
		if digito3 == '':
			if milharExtenso == 'dois mil':
				if genero == 'masculino':
					milhar = milharExtenso

				elif genero == 'feminino':
					milhar = milharExtenso[:1] + 'uas' + milharExtenso[4:]
			else:
				milhar = milharExtenso
		else:
			milhar = milharExtenso
			numerativo = milhar + " e " + digito3

	return numerativo

# num_cardinal_4dig_extenso('zero','trezentos', 'zero', 'três', 'feminino')

# tipoRealCard = choice.Menu(['extenso', 'numérico']).ask()

def num_cardinal(tipoRealCard, cardNumerico, milharExtenso,
				 centenaExtenso,dezenaExtenso,unidadeExtenso,genero):

	if tipoRealCard == 'numérico':
		numCardinal = cardNumerico

	elif tipoRealCard == 'extenso':
		numCardinal = num_cardinal_4dig_extenso(milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,genero)


	return numCardinal

# num_cardinal("extenso", None, 'zero','duzentos', 'zero', 'zero', 'feminino')
# 
# funcaoNumerativo = choice.Menu(['quant_precisa_absoluta(cardinais)',
# 		                                 'quant_precisa_div/multi(fração/multiplicativos)',
# 		                                 'quant_imprecisa_pron_indef_numer',
# 		                                 'quant_imprecisa_pron_indef_valor_alt_baixo',
# 		                                 'ordem_lugar_preciso(ordinal)',
# 		                                 'ordem_lugar_impreciso(posição_relativa'
# 		                                 ]).ask()
# print("""
#                     'algum'
#                     'nenhum'
#                     3: 'todo'
#                     4: 'muito'
#                     5: 'pouco'
#                     6: 'vário'
#                     7: 'tanto'
#                     8: 'outro'
#                     9: 'quanto'
#                     10: 'alguma'
#                     1'nenhuma'
#                     1'toda'
#                     13: 'muita'
#                     14: 'pouca'
#                     15: 'vária'
#                     1'tanta'
#                     17:'outra'
#                     18: 'quanta'
#                     19:'alguns'
#                     20:'nenhuns'
#                     21:'todos'
#                     22:'muitos'
#                     23:'poucos'
#                     24:'vários'
#                     25:'tantos'
#                     26:'outros'
#                     27:'quantos'
#                     28:'algumas'
#                     29:'nenhumas'
#                     30:'todas'
#                     31:'muitas'
#                     32:'poucas'
#                     33:'várias'
#                     34:'tantas'
#                     35:'outras'
#                     36:'quantas'
#
#                                Escolha uma opção:""")


def Numerativo(funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			   milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido):
	'''
    '''
	if funcaoNumerativo == 'ordem_lugar_preciso(ordinal)':
		Numerativo = ordinal(cardinal,genero)

	elif funcaoNumerativo == 'quant_precisa_div/multi(fração/multiplicativos)':
		if tipo_precisa == 'porcentagem':
			Numerativo = porcento(cardinal)

	elif funcaoNumerativo == 'quant_precisa_absoluta(cardinais)':
		Numerativo = num_cardinal(tipoRealCard, cardinal, milharExtenso,centenaExtenso,
								  dezenaExtenso,unidadeExtenso,genero)
	elif funcaoNumerativo == 'quant_imprecisa_pron_indef_numer':
		Numerativo = numIndefinido
	else:
		Numerativo=''
	return Numerativo
#
# # ordinal
# Numerativo('ordem_lugar_preciso(ordinal)','5','masculino',None,None,
# 			   None,None,None,None,None)
# #cardinal
# Numerativo('quant_precisa_absoluta(cardinais)',None,'feminino',None,"extenso",
# 			   "zero","duzentos","zero","zero",None)
#
# def NumerativoIndefinidoSwitcher():
# 	i = int(input())
#
# 	switcherNumInd = {
# 		'algum',
# 		'nenhum',
# 		3: 'todo', \
# 		4: 'muito',
# 		5: 'pouco',
# 		6: 'vário',
# 		7: 'tanto',
# 		8: 'outro',
# 		9: 'quanto',
# 		10: 'alguma',
# 		1'nenhuma',
# 		1'toda',
# 		13: 'muita',
# 		14: 'pouca',
# 		15: 'vária',
# 		16: 'tanta',
# 		17: 'outra',
# 		18: 'quanta',
# 		19: 'alguns',
# 		20: 'nenhuns',
# 		2'todos',
# 		2'muitos',
# 		23: 'poucos',
# 		24: 'vários',
# 		25: 'tantos',
# 		26: 'outros',
# 		27: 'quantos',
# 		28: 'algumas',
# 		29: 'nenhumas',
# 		30: 'todas',
# 		3'muitas',
# 		3'poucas',
# 		33: 'várias',
# 		34: 'tantas',
# 		35: 'outras',
# 		36: 'quantas',
# 	}
#
# 	return switcherNumInd.get(i, 'Seleção nao disponível')

# #
# # #
# #
# # ###A palavra nominal que realiza o Ente no GRUPO NOMINAL- Flexiona para nos eixos:
# # #     Gênero, Número, Grau. Por enquanto, vou trabalhar apenas com Gênero e número.(ORDEM DA PALAVRA AINDA)
# # # COMECEI APENAS COM SUBSTANTIVOS QUE SÃO REGULARES NAS SUAS FLEXÕES: gato:gatos:gatas:

def detectaExpSubstantivo(substantivo,genero,numero):  ##dado o substantivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um substantivo, dados
    o substantivo flexionado, o gênero e o numero.

    >>>detectaExpSubstantivo('','masculino','plural')
    'gat'
    '''


	if genero == 'masculino' and numero == 'singular':
		raizSubs = (substantivo[slice(-1)])

	elif genero == 'feminino' and numero == 'singular':
		raizSubs = (substantivo[slice(-1)])

	elif genero == 'masculino' and numero == 'plural':
		raizSubs = (substantivo[slice(-2)])

	elif genero == 'feminino' and numero == 'plural':
		raizSubs = (substantivo[slice(-2)])
	return raizSubs
# detectaExpSubstantivo('gatos','masculino','plural')
# #
# # # OS LEMAS QUE SERVIRÃO PARA  FUNÇÃO QUE SEGUE VIRÃO DA ANOTAÇÃO NA ONTOLOGIA:
# # #        o que na ontologia tiver anotado como Thing, vai servir como um
# # ##        banco lexical do qual o operador vai selecionar(não sei ainda se
# # #        vai ser importado automaticamente ou se vou ter de inserir manualmente
# # #        )
# #
# genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
# lemaSubs = input('Qual é o substantivo lematizado?')


def realizaExpSubstantivo(lemaSubs,genero):  ##dado o substantivo_lematizado- por enquanto, apenas para
	##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver
	#    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
	'''(str)-> str

    Retorna o morfema que realiza a experiência em um substantivo, dado
    o substantivo lematizado.

    >>>realizaExpSubstantivo()
    'gat'
    '''
	if genero == 'masculino' or genero =='feminino':
		morfExpSubs = lemaSubs[slice(-1)]

	elif genero == 'não-binário':
		morfExpSubs = lemaSubs

	return morfExpSubs

# realizaExpSubstantivo('gata','masculino')
# #

def realizacao_flexoes_substantivos(genero,numero):
	'''(str,str,str)->

    Retorna os morfemas que realizam as flexões de genero e numero dados
    a experiência do substantivo e os genero e numeros desejados.

	genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
    >>>realizacao_flexoes_substantivos()
    'os'
    '''

	if genero == 'masculino' and numero == 'singular':
		morfema_flexao_substantivo = 'o'
	elif genero == 'feminino' and numero == 'singular':
		morfema_flexao_substantivo = 'a'
	elif genero == 'masculino' and numero == 'plural':
		morfema_flexao_substantivo = 'os'
	elif genero == 'feminino' and numero == 'plural':
		morfema_flexao_substantivo = 'as'
	elif genero == 'não-binário' and numero == 'singular':
		morfema_flexao_substantivo = ''
	elif genero == 'não-binário' and numero == 'plural':
		morfema_flexao_substantivo = 's'

	return morfema_flexao_substantivo
# realizacao_flexoes_substantivos("masculino",'plural')
# #
# # ###Com relação aos substantivos comuns tenho que ver a abordagem que vou tomar
# # # com relação aos substantivos não binários, ou inerentemente masculinos ou femininos. Me parece
# # # que o sistema se organiza a realizar o gênero em alguns casos na ordem da palavra, e em
# # # outros casos na ordem do grupo (mesa: não parece ter uma contrapartida masculina)
# #
# print('Escolha o tipo_pessoa de feminino:')
# tipo_feminino_ÃO = choice.Menu(['oa', 'ona', 'ã', 'esa', 'casos_exceção']).ask()
#
# print('Escolha o tipo_pessoa de plural:')
# tipo_masc_ÃO = choice.Menu(['ãos', 'ões', 'ães']).ask()

# terminado em 's':;;;tonicidade = choice.Menu(['oxítona', 'paroxítona', 'proparoxítona']).ask()

def formacao_da_estrutura_do_substantivo_comum(substantivo_lematizado,numero,
											   genero, tipo_feminino_ÃO,
											   tipo_masc_ÃO,acentTonica):
	'''(str, str)-str

    Retorna a realizacao de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.

    >>>formacao_da_estrutura_do_substantivo_comum(,

    '''
	
	if substantivo_lematizado[-1:] == 'm':
		

		if numero == 'singular':

			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'ns'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'or':
		
		if genero == 'masculino' and numero == 'singular':

			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 's'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo
	elif substantivo_lematizado[-2:] == 'ão':
		
		if (genero == 'masculino' and numero == 'singular'
				or genero == 'não-binário' and numero == 'singular'):
			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO

		elif (genero == 'masculino' and numero == 'plural'
		      or genero == 'não-binário' and numero == 'plural'):

			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_masc_ÃO+'s'

		elif genero == 'feminino' and numero == 'plural':

			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO+ 's'

	elif substantivo_lematizado[-1:] == 'x':
		substantivo_comum = substantivo_lematizado

	elif substantivo_lematizado[-1:] == 's':
		if acentTonica == 'paroxítona':
			substantivo_comum = substantivo_lematizado
		elif acentTonica == 'oxítona':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_numero = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_numero

	elif (substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z'):
		
		if genero == 'masculino' and numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'al':
		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'ais'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'el':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'éis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'il':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'is'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'ol':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'óis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'ul':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'úis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	else:

		if genero == 'masculino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'o'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'os'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 's'

			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	return substantivo_comum

# formacao_da_estrutura_do_substantivo_comum("ancião",'plural',"masculino", None,
# 											   "ão",None)
# formacao_da_estrutura_do_substantivo_comum("artesão",'singular',"feminino", "ã",
# 											   None,None)

# formacao_da_estrutura_do_substantivo_comum("carro","plural",
# 											   "não-binário", None,
# 											   None,None)
# formacao_da_estrutura_do_substantivo_comum("varal","plural",
# 											   "não-binário", None,
# 											   None,None)
# # # ADJETIVOS

def deteccao_experiencia_do_adjetivo(adjetivo,genero,numero):  ##dado o adjetivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um adjetivo, dados
    o adjetivo flexionado, o gênero e o número.

    >>>deteccao_experiencia_do_adjetivo()
    'esportiv'
    '''

	if numero == 'singular':
		if genero == 'masculino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
			
		elif genero == 'feminino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
	elif numero == 'plural':
		if genero == 'masculino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
	
		elif genero == 'feminino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
	
	return raiz_experiencial_adjetivo
# deteccao_experiencia_do_adjetivo("esperto","masculino","singular")
# #


def realizacao_experiencia_do_adjetivo(adjetivo_lematizado,genero):
	'''(str)-> str
	genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
	adjetivo_lematizado = 
    
    Retorna o morfema que realiza a experiência em um adjetivo, dado
    o adjetivo lematizado.

    >>>realizacao_experiencia_do_adjetivo()
    'gat'
    '''

	if genero == 'masculino/feminino':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]

	elif genero == 'não-binário':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado

	return morfema_experiencial_do_adjetivo

# realizacao_experiencia_do_adjetivo("esperto","masculino/feminino")


def realizacao_flexoes_adjetivos(genero,numero):
	'''(str,str,str)->

    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do adjetivo e os gênero e números desejados.
	
	genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
    >>>realizacao_flexoes_adjetivos()
    'os'
    '''
	if numero == 'singular':
		if genero == 'masculino':
			morfema_flexao_adjetivo = 'o'
	
		elif genero == 'feminino':
			morfema_flexao_adjetivo = 'a'
		elif genero == 'não-binário':
			morfema_flexao_adjetivo = ''

	elif numero == 'plural':
		if genero == 'masculino' :
			morfema_flexao_adjetivo = 'os'

		elif genero == 'feminino' and numero == 'plural':
			morfema_flexao_adjetivo = 'as'
		
		elif genero == 'não-binário':
			morfema_flexao_adjetivo = 's'

	return morfema_flexao_adjetivo


def adjetivo_modificador(adjModificacao,adjetivo_lematizado,genero,numero):
	'''(str, str)-str

    Retorna a realizacao de um adjetivo comum dados a experiência_do_adjetivo
    e as flexões_desejadas.
    
    print('Há realizacao de adjetivo com funções de modificação (class, epítetos)?')
	real_modificadores = choice.Menu(['sim', 'NA']).ask()
	
	adjetivo_lematizado = input('Qual é o adjetivo lematizado?')
	genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()

    >>>estrutura_do_adjetivo ()

    '''

	if adjModificacao == None:
		modificador = ''

	else:
		if numero == 'singular':
			if genero == 'masculino':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
				morfema_flexao_adjetivo = 'o'
				genero

			elif genero == 'feminino':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
				morfema_flexao_adjetivo = 'a'
				genero

			elif genero == 'não-binário':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado
				morfema_flexao_adjetivo = ''
				genero
		elif numero == 'plural':
			if genero == 'masculino':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
				morfema_flexao_adjetivo = 'os'
				genero

			elif genero == 'feminino':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
				morfema_flexao_adjetivo = 'as'
				genero
			elif genero == 'não-binário':
				morfema_experiencial_do_adjetivo = adjetivo_lematizado
				morfema_flexao_adjetivo = 's'

		modificador = morfema_experiencial_do_adjetivo + morfema_flexao_adjetivo

	return modificador
# adjetivo_modificador("sim",'esperto','feminino','singular')
# #
# # # PRONOMES#
# #
# # # PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
# # # FICA UM POUCO SUBVERSIVA

def realizacao_pronominal_casoreto(pessoa_da_interlocucao,genero,numero,morfologia_do_pronome="de_terceira_pessoa"):
	'''(str)->str
    Retorna o pronome adequado dado uma pessoa da intelocução.
	pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
	morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()	
    >>>realizacao_pronominal_casoreto ('','')
    'eu'
    '''
	
	if pessoa_da_interlocucao == 'falante' and numero == 'singular':
		pronome_pessoal_reto = 'eu'
		

	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'singular':
		
		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'tu'
		else:
			pronome_pessoal_reto = 'você'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular':
		if genero == 'masculino':
			pronome_pessoal_reto = 'ele'
		else:
			pronome_pessoal_reto = 'ela'

	elif pessoa_da_interlocucao == 'falante' and numero == 'plural':
		pronome_pessoal_reto = 'nós'

	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'plural':
		
		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'vós'
		else:
			pronome_pessoal_reto = 'vocês'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural':
		
		if genero == 'masculino':
			pronome_pessoal_reto = 'eles'
		else:
			pronome_pessoal_reto = 'elas'

	return pronome_pessoal_reto


# realizacao_pronominal_casoreto("não_interlocutor", "feminino", "singular", morfologia_do_pronome="de_terceira_pessoa")


def realizacao_pronome_caso_obliquo(transitividade_verbo,tonicidade,pessoa_da_interlocucao,numero,genero,morfologia_do_pronome,reflexivo=False):
	'''(str)->str
    Retorna o pronome oblíquo adequado dado uma pessoa da intelocução.
	tonicidade = choice.Menu(['átono', 'tônico']).ask()
	pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
	morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()
	transitividade_verbo =choice.Menu(['direto','direto_preposicionado, 'indireto']).ask()
    >>>realizacao_pronominal_caso_oblíquo ()
    'me'
    '''

	if pessoa_da_interlocucao == 'falante' and numero == 'singular' and tonicidade == 'átono' and transitividade_verbo == "direto":
		pronome_pessoal_obliquo = 'me'

	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'singular' and tonicidade == 'átono':
		pronome_pessoal_obliquo = 'te'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular' and tonicidade == 'átono':

		if morfologia_do_pronome == 'padrão':
			if genero == 'masculino':
				pronome_pessoal_obliquo = 'o'

			elif genero == 'feminino':
				pronome_pessoal_obliquo = 'a'
		elif morfologia_do_pronome == 'não_padrão':
			if genero == 'masculino':
				pronome_pessoal_obliquo = 'ele'
			else:
				pronome_pessoal_obliquo = 'ela'
		else:
			if reflexivo==True:
				pronome_pessoal_obliquo = 'se'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular' and tonicidade == 'átono' and transitividade_verbo == "indireto":
		pronome_pessoal_obliquo = 'lhe'

	elif pessoa_da_interlocucao == 'falante' and numero == 'plural' and tonicidade == 'átono':
		pronome_pessoal_obliquo = 'nos'

	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'plural' and tonicidade == 'átono':
		pronome_pessoal_obliquo = 'vos'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural' and tonicidade == 'átono':
		if morfologia_do_pronome == 'padrão':

			if genero == 'masculino':
				pronome_pessoal_obliquo = 'os'

			elif genero == 'feminino':
				pronome_pessoal_obliquo = 'as'
		else:
			if reflexivo == True:
				pronome_pessoal_obliquo = 'se'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural' and tonicidade == 'átono' and transitividade_verbo == "indireto":
		pronome_pessoal_obliquo = 'lhes'

		if morfologia_do_pronome == 'não_padrão':

			if genero == 'masculino':
				pronome_pessoal_obliquo = 'eles'
			else:
				pronome_pessoal_obliquo = 'elas'
		if transitividade_verbo == 'indireto':
			if pessoa_da_interlocucao == 'falante' and numero == 'singular' and tonicidade == 'tônico':
				pronome_pessoal_obliquo = 'mim'

			elif pessoa_da_interlocucao == 'ouvinte' and numero == 'singular' and tonicidade == 'tônico':

				if morfologia_do_pronome == 'padrão':
					pronome_pessoal_obliquo = 'ti'
				else:
					pronome_pessoal_obliquo = 'você'

		elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular' and tonicidade == 'tônico':
			if morfologia_do_pronome == 'não_padrão':
				if genero == 'masculino':
					pronome_pessoal_obliquo = 'ele'

				elif genero == 'feminino':
					pronome_pessoal_obliquo = 'ela'
			else:
				pronome_pessoal_obliquo = 'si'

		elif pessoa_da_interlocucao == 'falante' and numero == 'plural' and tonicidade == 'tônico':
			pronome_pessoal_obliquo = 'nós'

		elif pessoa_da_interlocucao == 'ouvinte' and numero == 'plural' and tonicidade == 'tônico':

			if morfologia_do_pronome == 'padrão':
				pronome_pessoal_obliquo = 'vós'
			else:
				pronome_pessoal_obliquo = 'vocês'

		elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural' and tonicidade == 'tônico':

			if morfologia_do_pronome == 'não_padrão':
				if genero == 'masculino':
					pronome_pessoal_obliquo = 'eles'

				elif genero == 'feminino':
					pronome_pessoal_obliquo = 'elas'
			else:
				pronome_pessoal_obliquo = 'si'

	return pronome_pessoal_obliquo
# realizacao_pronome_caso_obliquo("indireto",'tônico',"não_interlocutor",'singular','feminino',"padrão")

##TENHO QUE VER SE FAZ SENTIDO MUDAR ESTA(inserir parâmetros??)
# def pronome_relativo():
# 	'''
#     '''
# 	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
#
# 	if modo_inserção == 'inserção_manual':
# 		pronome_relativo = input('Escreva o pronome desejado:')
#
# 	elif modo_inserção == 'inserção_menu':
#
# 		print('Qual tipo_pessoa de relativo?')
# 		tipo_pronome_relativo = choice.Menu(['variável', 'invariável']).ask()
# 		if tipo_pronome_relativo == 'variável':
#
# 			print('Qual o gênero?')
# 			gênero = choice.Menu(['masculino', 'feminino']).ask()
# 			print('Qual o número?')
# 			número = choice.Menu(['singular', 'plural']).ask()
#
# 			if gênero == 'masculino' and número == 'singular':
# 				pronome_relativo = choice.Menu(['o qual', 'cujo', 'quanto', 'pelo qual']).ask()
#
# 			elif gênero == 'masculino' and número == 'plural':
# 				pronome_relativo = choice.Menu(['os quais', 'cujos', 'quantos', 'pelos quais']).ask()
#
# 			elif gênero == 'feminino' and número == 'singular':
# 				pronome_relativo = choice.Menu(['a qual', 'cuja', 'quanta', 'pela qual']).ask()
#
# 			elif gênero == 'feminino' and número == 'plural':
# 				pronome_relativo = choice.Menu(['as quais', 'cujas', 'quantas', 'pelas quais']).ask()
#
# 		elif tipo_pronome_relativo == 'invariável':
# 			pronome_relativo = choice.Menu(['quem', 'que',
# 			                                'a quem', 'a que', 'porque', 'como']).ask()
#
# 	return pronome_relativo

# #
# # ##PRECISO IMPLEMENTAR LETRA MAIÚSCULA NO CASO DE INICIO DE FRASE.
# # # SUBSTANTIVOS PRÓPRIOS VIRÃO DA LISTA DE NOMES PRÓPRIOS ANOTADOS NA GUM
# # # Por enquanto, vou deixar um input
# #
# #
# # def nome_próprio():
# # 	'''(str)->str
# #     Retorna o nome próprio. #Futuramente parte das listas de léxicos
# #     advindas da anotação na GUM.
# #     '''
# # 	nome_próprio = input('Qual é o nome próprio?')
# # 	return nome_próprio.capitalize()
# #
# #
# # ####DÊIXIS DO GN
# #

def estrutura_logica_deixis():
	'''
    '''

	estrutura_lógica_det_dêixis = input("""

            α(Dêitico_ñ_seletivo_específico) # ex.: O,A
            α(Dêitico_ñ_seletivo_ñ_específico) #ex.: Um,uns
            3: α(Dêitico_prox) #Este
            4: α(Dêitico_pess) #Meu
            5: β(Dêitico_prox)^α(Dêitico_pess) # ex.: Este meu
            6: β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess) # ex.: O meu
            7: β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess) # ex.: Um meu





            Selecione uma opção:""")

	if estrutura_lógica_det_dêixis == '1':

		estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_específico)'

	elif estrutura_lógica_det_dêixis == '2':

		estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_ñ_específico)'

	elif estrutura_lógica_det_dêixis == '3':

		estrutura_lógica_det_dêixis = 'α(Dêitico_prox)'

	elif estrutura_lógica_det_dêixis == '4':

		estrutura_lógica_det_dêixis = 'α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '5':

		estrutura_lógica_det_dêixis = 'β(Dêitico_prox)^α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '6':

		estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '7':

		estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)'

	return estrutura_lógica_det_dêixis

# #
# # # a fazer: verificar as opções que coloquei para os diferentes tipos de dêixis:
# # # não preciso talvez colocar todas as opções de especificidade em cada um deles
# # # pra não ter a possibilidade de dar erro nas escolhas.
def Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,número, gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()
	                          print('Selecione número:')
	número = choice.Menu(['singular', 'plural']).ask()
	print('Selecione o gênero')
	gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

	if (DETERMINAÇÃO_espeficifidade == 'específico'  and ORIENTAÇÃO == 'NA'):

		if número == 'plural' and gênero == 'masculino':
			determinante = 'os'
		elif número == 'plural' and gênero == 'feminino':
			determinante = 'as'
		elif número == 'singular' and gênero == 'masculino':
			determinante = 'o'
		elif número == 'singular' and gênero == 'feminino':
			determinante = 'a'

	return determinante
# Dêitico_ñ_seletivo_específico('específico', 'NA','plural', 'feminino')
# #
def Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,número,gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	print('Selecione número:')
		número = choice.Menu(['singular', 'plural']).ask()
		print('Selecione o gênero')
		gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

	if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'NA':
		if número == 'singular' and gênero == 'masculino':
			determinante = 'um'
		elif número == 'plural' and gênero == 'masculino':
			determinante = 'uns'
		elif número == 'singular' and gênero == 'feminino':
			determinante = 'uma'
		elif número == 'plural' and gênero == 'feminino':
			determinante = 'umas'
	return determinante
# Dêitico_ñ_seletivo_ñ_específico('não_específico','NA','plural','masculino')
# # 	####
# #

def Dêitico_prox(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,pessoa_da_interlocução_proximidade,número,gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()
	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa',
	                          'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()
	print('Selecione a pessoa da interlocução:')
		pessoa_da_interlocução_proximidade = choice.Menu(
			['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
	print('Selecione número:')
			número = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero')
			gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''


	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade':

		if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'este'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'estes'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'esta'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'estas'

		elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'esse'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'esses'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'essa'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'essas'

		elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'aquele'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'aqueles'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'aquela'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'aquelas'

	return determinante
# Dêitico_prox('específico','orientação_específica_proximidade','próximo_ao_não_interlocutor','plural','masculino')

def Dêitico_pess(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,pessoa_da_interlocução_possuidor,
				 número_obj_possuído,gênero_obj_possuído,morfologia_do_pronome='morfologia_terceira_pessoa'):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask

	print('Selecione a pessoa da interlocução do possuidor')
		pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

	print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()
	print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'terceira_pessoa']).ask()
    '''

	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':

		if pessoa_da_interlocução_possuidor == '1s':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'meu'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'meus'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'minha'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'minhas'

		elif pessoa_da_interlocução_possuidor == '2s':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'teu'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'teus'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'tua'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'tuas'
				else:
					determinante = 'suas'

		elif (pessoa_da_interlocução_possuidor == '3s' or
		      pessoa_da_interlocução_possuidor == '3p'):

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'suas'

		elif pessoa_da_interlocução_possuidor == '1p':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'nosso'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'nossos'
			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'nossa'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'nossas'

		elif pessoa_da_interlocução_possuidor == '2p':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vosso'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossos'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossa'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossas'
				else:
					determinante = 'suas'

	return determinante
# Dêitico_pess('específico','orientação_específica_pessoa','2p','plural','feminino','padrão')


# ##talvez não use 
# def Dêitico_genérico(DETERMINAÇÃO_espeficifidade):
# 	
# 	'''
# 	
# 	DETERMINAÇÃO_espeficifidade = choice.Menu(['genérico(contável)', 'genérico(de_massa)']).ask()
# 	
# 	:return: 
# 	'''
# 	
# 
# 	if (DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' or
# 			DETERMINAÇÃO_espeficifidade == 'genérico(contável)'):
# 		determinante = ''  # Neste caso, o grupo nominal CONTÁVEL é realizado no plural e o DE MASSA no singular
# 
# 	return determinante
# #

def Dêixis_geral(DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
				 ORIENTAÇÃO_alpha,gênero_alpha,número_alpha,morfologia_do_pronome_alpha,
				 pessoa_da_interlocução_possuidor,número_obj_possuído,
				 gênero_obj_possuído,pessoa_da_interlocução_proximidade):
	'''
	estrutura_lógica_det_det = choice.Menu(["alpha", "beta^alpha]).ask()


    '''
	if DETERMINAÇÃO_espeficifidade_alpha == 'específico':
		if ORIENTAÇÃO_alpha == 'orientação_específica_proximidade':
			alpha = Dêitico_prox(DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
										pessoa_da_interlocução_proximidade, número_alpha, gênero_alpha)
		elif ORIENTAÇÃO_alpha == 'orientação_específica_pessoa':
			alpha = Dêitico_pess(DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,pessoa_da_interlocução_possuidor,
			 número_obj_possuído,gênero_obj_possuído,morfologia_do_pronome_alpha)
		else:
			alpha = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_alpha,
														 ORIENTAÇÃO_alpha,número_alpha, gênero_alpha)
	elif DETERMINAÇÃO_espeficifidade_alpha == 'não_específico':
		alpha = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_alpha,
													   ORIENTAÇÃO_alpha, número_alpha, gênero_alpha)

	else:

		alpha = ''

	if DETERMINAÇÃO_espeficifidade_beta =='específico':

		if ORIENTAÇÃO_beta == 'orientação_específica_proximidade':
			beta = Dêitico_prox(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
								pessoa_da_interlocução_proximidade,
								número_beta, gênero_beta)
		elif ORIENTAÇÃO_beta == 'orientação_específica_pessoa':
			beta = Dêitico_pess(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
										pessoa_da_interlocução_possuidor,
										número_obj_possuído, gênero_obj_possuído, morfologia_do_pronome_beta)
		else:
			beta = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, número_beta,
														 gênero_beta)
	elif DETERMINAÇÃO_espeficifidade_beta == 'não_específico':
		beta = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_beta,
													   ORIENTAÇÃO_beta, número_beta, gênero_beta)

	else:
		beta = ''

	if beta !='':
		return beta + ' ' + alpha
	else:
		return (re.sub(' +', '',( beta + ' ' + alpha) ))
	

#
# Dêixis_geral( None,None,
# 				 None,None,None,'específico','orientação_específica_proximidade',
# 			 'masculino','singular','morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
#
# Dêixis_geral(None,None,
# 				 None,None,None, 'específico',
# 				 'NA','masculino','singular','morfologia_terceira_pessoa',
# 				 None,None,
# 				 None,None)
#
# Dêixis_geral('específico','orientação_específica_proximidade','masculino','singular','morfologia_terceira_pessoa',
# 			 'específico','orientação_específica_pessoa',
# 			 'masculino','singular','morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
# #
#
# print('Qual o tipo_pessoa de Ente?')
# tipo_de_Ente = choice.Menu(['consciente', 'não_consciente', 'NA']).ask()
#
# print('Qual tipo_pessoa de não_consciente?')
# tipo_de_nao_consciente = choice.Menu(['material', 'semiótico']).ask()
#
# print('Qual tipo_pessoa de material?')
# tipo_de_nao_consciente_material = choice.Menu(
# 	['animal', 'objeto_material', 'substância_material', 'abstração_material']).ask()
#
# print('Qual a classe de palavra que realiza o Ente?')
# classe_palavra_Ente = choice.Menu(
# 	['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_oblíquo']).ask()
# print('Qual tipo_pessoa de semiótico?')
# tipo_de_nao_consciente_semiotico = choice.Menu(
# 	['instituição', 'objeto_semiótico', 'abstração_semiótica']).ask()


def Ente(tipo_de_Ente,tipo_de_nao_consciente,tipo_de_nao_consciente_material,
		 tipo_de_nao_consciente_semiotico,classe_palavra_Ente,substantivo_lematizado,numero,
		genero, tipo_feminino_ÃO, tipo_masc_ÃO,acentTonica,nomeProprio,pessoa_da_interlocucao,
		 transitividade_verbo,tonicidade,morfologia_do_pronome,reflexivo):
	'''


    '''

	if tipo_de_Ente == 'NA':
		Ente = ''


	elif tipo_de_Ente == 'não_consciente':
		
		if tipo_de_nao_consciente == 'material':
			if (tipo_de_nao_consciente_material == 'animal' or
					tipo_de_nao_consciente_material == 'objeto_material' or
					tipo_de_nao_consciente_material == 'substância_material' or \
					tipo_de_nao_consciente_material == 'abstração_material'):
				
				if classe_palavra_Ente == 'substantivo_comum':
					Ente = formacao_da_estrutura_do_substantivo_comum(substantivo_lematizado, numero, genero,
																	  tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica)

				elif classe_palavra_Ente == 'substantivo_próprio':
					Ente = nomeProprio
				elif classe_palavra_Ente == 'pronome_caso_reto':
					Ente = realizacao_pronominal_casoreto(pessoa_da_interlocucao,genero,
														  numero,morfologia_do_pronome)
				elif classe_palavra_Ente == 'pronome_caso_oblíquo':
					Ente = realizacao_pronome_caso_obliquo(transitividade_verbo,tonicidade,
														   pessoa_da_interlocucao,numero,genero,
														   morfologia_do_pronome,reflexivo)
		elif tipo_de_nao_consciente == 'semiótico':

			if (tipo_de_nao_consciente_semiotico == 'instituição' or
					tipo_de_nao_consciente_semiotico == 'objeto_semiótico' or
					tipo_de_nao_consciente_semiotico == 'abstração_semiótica'):

				if classe_palavra_Ente == 'substantivo_comum':
					Ente = formacao_da_estrutura_do_substantivo_comum(substantivo_lematizado, numero, genero,
																	  tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica)
				elif classe_palavra_Ente == 'substantivo_próprio':
					Ente = nomeProprio
				elif classe_palavra_Ente == 'pronome_caso_reto':
					Ente = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
														  numero, morfologia_do_pronome)
				elif classe_palavra_Ente == 'pronome_caso_oblíquo':
					Ente = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
														   pessoa_da_interlocucao, numero, genero,
														   morfologia_do_pronome, reflexivo)

	elif tipo_de_Ente == 'consciente':
		if classe_palavra_Ente == 'substantivo_comum':
			Ente = formacao_da_estrutura_do_substantivo_comum(substantivo_lematizado, numero, genero,
															  tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica)

		elif classe_palavra_Ente == 'substantivo_próprio':
			Ente = nomeProprio
		elif classe_palavra_Ente == 'pronome_caso_reto':
			Ente = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
												  numero, morfologia_do_pronome)
		elif classe_palavra_Ente == 'pronome_caso_oblíquo':
			Ente = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
												   pessoa_da_interlocucao, numero, genero,
												   morfologia_do_pronome, reflexivo)
	return Ente

#
# Ente('não_consciente','material','animal',
# 		 None,'substantivo_comum','gato','singular',
# 		'feminino', None, None,None,None,None,
# 		 None,None,None,None)
# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "plural",
#      "feminino",None, None,None,None,"não_interlocutor",
#      None,None,None,None)
# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "plural",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)

# #
# # ###No caso do Ente, ainda tenho que modelar as opções de Ente realizados por substantivos compostos (devido ao padrão de
# # # morfologia das flexões
# #

#####ESTRUTURA DO GRUPO NOMINAL:

##
# print('Há Qualificador no gn?')
# tem_qualificador = choice.Menu(['sim', 'NA']).ask()
# realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()


def qualificador(indicePreposicao=None,dissocEnteNucleo=None,DETERMINAÇÃO_espeficifidade_beta=None,ORIENTAÇÃO_beta=None,
				 gênero_beta=None,número_beta=None,morfologia_do_pronome_beta=None,
				 DETERMINAÇÃO_espeficifidade_alpha=None,ORIENTAÇÃO_alpha=None,gênero_alpha=None,
				 número_alpha=None,morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				 número_obj_possuído=None, gênero_obj_possuído=None,pessoa_da_interlocução_proximidade=None,#
				 funcaoNumerativo=None,cardinal=None,genero=None,tipo_precisa=None,tipoRealCard=None,
			  	 milharExtenso=None,centenaExtenso=None,dezenaExtenso=None,unidadeExtenso=None,numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
				 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
				 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,#
				 temQualificador=None,tipoQualificador=None,epitetoModificacao=None,adjetivo_epiteto=None,
				 classificadorModificacao=None,adjetivo_classificador=None,contracao=None):


	if temQualificador == 'sim':
		if tipoQualificador == 'frase-preposicional':
			Qualificador = frase_preposicional(indicePreposicao, dissocEnteNucleo, temQualificador, tipoQualificador,
						DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
						gênero_beta, número_beta, morfologia_do_pronome_beta,
						DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
						número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
						número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,  #
						funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
						milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
						numIndefinido,
						tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
						tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
						numero,
						tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
						pessoa_da_interlocucao,
						transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,  #
						epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
						adjetivo_classificador, contracao)
		# else:
		# 	Qualificador = "que" + oraçãoProjetada()
	else:
		Qualificador = ''
	return re.sub(' +',' ', Qualificador).strip()
#
# qualificador(indicePreposicao=10,dissocEnteNucleo=None,temQualificador='sim',tipoQualificador='frase-preposicional',
# 					DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,contracao='-contração')

def estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=None,DETERMINAÇÃO_espeficifidade_beta=None,ORIENTAÇÃO_beta=None,
				 gênero_beta=None,número_beta=None,morfologia_do_pronome_beta=None,
				 DETERMINAÇÃO_espeficifidade_alpha=None,ORIENTAÇÃO_alpha=None,gênero_alpha=None,
				 número_alpha=None,morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				 número_obj_possuído=None, gênero_obj_possuído=None,pessoa_da_interlocução_proximidade=None,#
				 funcaoNumerativo=None,cardinal=None,genero=None,tipo_precisa=None,tipoRealCard=None,
			  	 milharExtenso=None,centenaExtenso=None,dezenaExtenso=None,unidadeExtenso=None,numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
				 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
				 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,#
				 epitetoModificacao=None,adjetivo_epiteto=None,classificadorModificacao=None,adjetivo_classificador=None):
	GN_downranked = estrutura_GN(dissocEnteNucleo,temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador)

	return re.sub(' +',' ',GN_downranked).strip()
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None)
# #
# #parei aqui
# # ####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
# # ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# # # com função de Numerativo no GN DE PRIMEIRO NÍVEL)
# 	print('Há dissociação entre Ente e Núcleo do GN?')
# 	dissocEnteNucleo = choice.Menu(['sim', 'não']).ask()

def estrutura_GN(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=None,DETERMINAÇÃO_espeficifidade_beta=None,ORIENTAÇÃO_beta=None,
				 gênero_beta=None,número_beta=None,morfologia_do_pronome_beta=None,
				 DETERMINAÇÃO_espeficifidade_alpha=None,ORIENTAÇÃO_alpha=None,gênero_alpha=None,
				 número_alpha=None,morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				 número_obj_possuído=None, gênero_obj_possuído=None,pessoa_da_interlocução_proximidade=None,#
				 funcaoNumerativo=None,cardinal=None,genero=None,tipo_precisa=None,tipoRealCard=None,
			  	 milharExtenso=None,centenaExtenso=None,dezenaExtenso=None,unidadeExtenso=None,numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
				 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
				 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,#
				 epitetoModificacao=None,adjetivo_epiteto=None,classificadorModificacao=None,adjetivo_classificador=None):


	if dissocEnteNucleo == None:

		Determinante = Dêixis_geral(DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
				 ORIENTAÇÃO_alpha,gênero_alpha,número_alpha,morfologia_do_pronome_alpha,
				 pessoa_da_interlocução_possuidor,número_obj_possuído,
				 gênero_obj_possuído,pessoa_da_interlocução_proximidade)
		
		numerativo = Numerativo(funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			   milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido)
		
		ente = Ente(tipo_de_Ente,tipo_de_nao_consciente,tipo_de_nao_consciente_material,
		 tipo_de_nao_consciente_semiotico,classe_palavra_Ente,substantivo_lematizado,numero,
		genero, tipo_feminino_ÃO, tipo_masc_ÃO,acentTonica,nomeProprio,pessoa_da_interlocucao,
		 transitividade_verbo,tonicidade,morfologia_do_pronome,reflexivo)
		
		Classificador = adjetivo_modificador(classificadorModificacao,adjetivo_classificador,genero,numero)
		
		Epíteto = adjetivo_modificador(epitetoModificacao,adjetivo_epiteto,genero,numero)
		
		Qualificador = qualificador(temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador)

		GN = Determinante + ' ' + numerativo + ' ' + ente + ' ' + Classificador + ' ' + Epíteto + ' ' + Qualificador

	else:

		Núcleo_lógico = estrutura_GN_downraked(dissocEnteNucleo,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador)

		Qualificador = qualificador(temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador)
		GN = Núcleo_lógico + ' ' + Qualificador
	return  (re.sub(' +', ' ', GN).strip())
#
# estrutura_GN(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None)
# #
# # ########PREPOSIÇÃO
# preposicoes = ['a','ante','após','até','com','contra',
# 				   'de','desde','em','entre','para','por','perante','sem',
# 				   'sob','sobre','trás']



def preposicao(indice):
	opcoes = ['a', 'ante', 'após', 'até', 'com', 'contra',
				   'de', 'desde', 'em', 'entre', 'para', 'por', 'perante', 'sem',
				   'sob', 'sobre', 'trás']
	nums = [x for x in range(len(opcoes))]
	preposicoes = dict(zip(nums, opcoes))

	preposicao=preposicoes[indice]
	return preposicao
# preposicao(0)
# preposicao(11)


# print("Com ou sem contração")
# contracao = choice.Menu(['+contração', '-contração']).ask()

def frase_preposicional(indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None,
						DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
						gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
						DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
						número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
						número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,  #
						funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
						milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
						numIndefinido=None,
						tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
						tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
						numero=None,
						tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
						pessoa_da_interlocucao=None,
						transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
						epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
						adjetivo_classificador=None, contracao=None):
	'''
    '''
	prep = preposicao(indicePreposicao)
	grupo_nominal = (re.sub(' +', ' ',estrutura_GN_downraked(dissocEnteNucleo,temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador))).strip()

	if prep == 'por':
		if grupo_nominal[:2] == 'o ':
			frase_prep = 'pel' + grupo_nominal
		elif grupo_nominal[:2] == 'a ':
			frase_prep = 'pel' + grupo_nominal
		else:
			frase_prep = prep + ' ' + grupo_nominal
	elif prep == 'a':
		if grupo_nominal[:2] == 'a ':
			frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
		elif grupo_nominal[:2] == 'o ':
			frase_prep = prep + grupo_nominal
		elif grupo_nominal[:5] == 'aquel':
			frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
		else:
			frase_prep = prep + ' ' + grupo_nominal
	elif prep == 'de':
		if (grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a ' or
				grupo_nominal[:3] == 'est' or
				grupo_nominal[:3] == 'ist' or
				grupo_nominal[:3] == 'ess' or
				grupo_nominal[:3] == 'iss' or
				grupo_nominal[:5] == 'aquel' or
				grupo_nominal[:5] == 'aquil'):
			frase_prep = (prep[slice(-1)]) + grupo_nominal
		elif (grupo_nominal[:2] == 'um' or
		      grupo_nominal[:2] == 'un' or
		      grupo_nominal[:2] == 'el' or
		      grupo_nominal[:4] == 'outr'):
			
			if contracao == '+contração':
				frase_prep = (prep[slice(-1)]) + grupo_nominal
			else:
				frase_prep = prep + ' ' + grupo_nominal
		else:
			frase_prep = prep + ' ' + grupo_nominal
	elif prep == 'em':
		if (
				grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a ' or
				grupo_nominal[:2] == 'el' or
				grupo_nominal[:3] == 'est' or
				grupo_nominal[:3] == 'ist' or
				grupo_nominal[:3] == 'ess' or
				grupo_nominal[:3] == 'iss' or
				grupo_nominal[:5] == 'aquel' or
				grupo_nominal[:5] == 'aquil'
		):
			frase_prep = 'n' + grupo_nominal
		else:
			if (
					grupo_nominal[:2] == 'um' or
					grupo_nominal[:2] == 'un' or
					grupo_nominal[:4] == 'outr'
			):

				if contracao == '+contração':
					frase_prep = 'n' + grupo_nominal
				else:
					frase_prep = prep + ' ' + grupo_nominal

	elif prep == 'para':
		if (
				grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a '
		):
			if contracao == '+contração':
				frase_prep = 'pr' + grupo_nominal
			else:
				frase_prep = prep + ' ' + grupo_nominal
		else:
			frase_prep = prep + ' ' + grupo_nominal
	else:
		frase_prep = prep + ' ' + grupo_nominal
	return frase_prep

# for i in range(12):
# 	frase = frase_preposicional(indicePreposicao=i,dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,
# 					DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,contracao='-contração')
# 	print(frase)
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None)

# # ############ORDEM DA ORAÇÃO
# print('Há circunstância?')
# temCircunstancia = choice.Menu(['sim', 'não']).ask()
# print('Selecione o tipo_pessoa de grupo que realiza a circunstância:')
# realizacaoCircunstancia = choice.Menu(['grupo_nominal', 'frase_preposicional', 'grupo_adverbial']).ask()

def circunstancia(temCircunstancia=None,realizacaoCircunstancia=None,
				  indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None,
				  DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
				  gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
				  DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
				  número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				  número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,  #
				  funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
				  milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
				  numIndefinido=None,
				  tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				  tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
				  numero=None,
				  tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
				  pessoa_da_interlocucao=None,
				  transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
				  epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
				  adjetivo_classificador=None, contracao=None,tipo_de_adverbio=None, indice=None
				  ):
	'''
    '''

	if temCircunstancia == None:
		Circunstancia = ''
	else:
		if realizacaoCircunstancia == 'grupo_nominal':
			Circunstancia = estrutura_GN_downraked(dissocEnteNucleo,temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta,
				 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
				 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
				 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
				 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			  	 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
				 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
				 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
				 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador)
		elif realizacaoCircunstancia == 'frase_preposicional':
			Circunstancia = frase_preposicional(indicePreposicao, dissocEnteNucleo, temQualificador, tipoQualificador,
						DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
						gênero_beta, número_beta, morfologia_do_pronome_beta,
						DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
						número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
						número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,  #
						funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
						milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
						numIndefinido,tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
						tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
						numero,tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
						pessoa_da_interlocucao,transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,  #
						epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
						adjetivo_classificador, contracao)
		elif realizacaoCircunstancia == 'grupo_adverbial':
			Circunstancia = adverbio(tipo_de_adverbio, indice)

	return re.sub(' +',' ',Circunstancia).strip()
#
# circunstancia(temCircunstancia='sim',realizacaoCircunstancia='frase_preposicional',
# 			  indicePreposicao=9,dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,
# 				DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,contracao='-contração'
# 			,tipo_de_adverbio=None, indice=None)
# # ##SISTEMAS DA ORAÇÃO
# #
# #
# # def AGENCIAMENTO():
# # 	## no caso de materiais meteorológicas, o Meio conflui
# # 	# com o Processo (por isso :AG_processo_sem_alcance,AG_processo+alcance );
# # 	# pode haver escopo (Ex.: choveu uma chuva grossa)
# # 	print('Qual o tipo_pessoa de Agenciamento?')
# # 	AGENCIAMENTO = choice.Menu(['AG_médio_sem_alcance',
# #
# # 	                            'AG_médio_com_alcance',
# # 	                            'AG_efetivo_operativo',
# # 	                            'AG_efetivo_receptivo_agentivo',
# # 	                            'AG_efetivo_receptivo_não_agentivo',
# # 	                            'AG_processo_sem_alcance',
# # 	                            'AG_processo+alcance']).ask()
# #
# # 	return AGENCIAMENTO
# #
# #
# # ###tipos de processo oração
# # # Material
# # ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)
# #
# # # def PROCESSO_MATERIAL():
# # #    Processo_material = choice.Menu(['PR_material_transformativo_transitivo',
# # #                                     'PR_material_criativo_transitivo',
# # #                                     'PR_material_transformativo_intransitivo',
# # #                                     'PR_material_criativo_intransitivo']).ask()
# # #
# # #    return Processo_material
# #
# #
# # ###tipos de processo oração
# # # Material
# # ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)
# #
# # def PROCESSO_MATERIAL():
# # 	print('Qual o tipo_pessoa de ação realizada pelo processo?')
# # 	TIPO_DE_AÇÃO = choice.Menu(['transformativo', 'criativo']).ask()
# #
# # 	print('Qual o tipo_pessoa de impacto?')
# # 	IMPACTO = choice.Menu(['IMPA_transitivo', 'IMPA_intransitivo', 'IMPA_NA']).ask()
# # 	Processo_material = 'PR_material_' + TIPO_DE_AÇÃO + '_' + IMPACTO
# #
# # 	return Processo_material
# #
# #
# # #
# # #
# # #
# #
# # # relacional
# #
# # ##def atribuição_de_relação():
# # ##    '''
# # ##    '''
# # ##    atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
# # ##                                         'atribuição_proj_ment_desiderativa',
# # ##                                         'atribuição_proj_verbal',
# # ##                                         'atribuição_expan_elaboração',
# # ##                                         'atribuição_expan_intencificação',
# # ##                                         'sem_atribuição_de_relação']).ask()
# # ##    return atribuição_de_relação
# # ##
# # #
# # #
# # #
# # #
# # #
# # #
# # # def processo_relacional():
# # #    '''
# # #    '''
# # #    atribuição_relação = atribuição_de_relação()
# # #
# # #    tipo_de_relacional = choice.Menu (['PR_relacional_intensivo_atributivo',
# # #                                       'PR_relacional_intensivo_identificativo',
# # #                                       'PR_relacional_possessivo_atributivo',
# # #                                       'PR_relacional_possessivo_identificativo',
# # #                                       'PR_relacional_circunstancial_atributivo',
# # #                                       'PR_relacional_circunstancial_identificativo']).ask()
# # #
# # #    relacional =  tipo_de_relacional + '_' +  atribuição_relação
# # #
# # #    return relacional
# # #
# # #
# # #
# #
# #
# # #    if (atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_atributiva'or
# # #        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_identificativa' or
# # #
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_identificativa'or
# # #
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_identificativa'or
# # #
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_identificativa'or
# # #
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_identificativa'or
# # #
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_atributiva' or
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_identificativa' or
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_atributiva' or
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_identificativa' or
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_atributiva' or
# # #        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_identificativa'):
# # #
# # #        relacional = atribuição_relação + ' ' + tipo_de_relacional
# # #
# # #    return relacional
# # #
# # #
# #
# #
# # # TRANSITIVIDADE
# #
# #
# # ##subsistemas
# #
# # ##agenciamento oração
# #
# # ##MODO
# #
# # # subsistemas:
# #
# # # sujeitabilidade
# # # coloquei aqui apenas responsabilidade e pressuposição pois
# # # pessoa e número já é decidido na ordem da palavra 9tenho que ver o impacto teórico que
# # ##isso tem..não sei se preciso repetir as escolhas)
# #
# # def SUJEITABILIDADE():
# # 	'''
# #     '''
# # 	print('Qual o tipo_pessoa de Sujeito?')
# # 	RESPONSABILIDADE = choice.Menu(['SUJ_responsável',
# # 	                                'SUJ_distante_impessoal',
# # 	                                'SUJ_distante_não_responsável', 'SUJ_-sujeitabilidade']).ask()
# #
# # 	PRESSUPOSIÇÃO_DO_SUJEITO = choice.Menu(['recuperado_explícito', \
# # 	                                        'recuperado_implícito',
# # 	                                        'não_recuperável', 'recuperação_NA']).ask()
# #
# # 	SUJEITABILIDADE = RESPONSABILIDADE + '_' + PRESSUPOSIÇÃO_DO_SUJEITO
# #
# # 	return SUJEITABILIDADE
# #
# #
# # def TIPO_DE_MODO():
# # 	'''
# #     '''
# # 	print('Qual o tipo_pessoa de modo da oração?')
# # 	tipo_de_modo = choice.Menu(['MOD_declarativo_+perguntafinito',
# # 	                            'MOD_declarativo_-perguntafinito',
# # 	                            'MOD_interrogativo_elemental',
# # 	                            'MOD_interrogativo_polar',
# # 	                            'MOD_imperativo']).ask()
# #
# # 	return tipo_de_modo
# #
# #
# # ########
# #
# #
# # ######
# #
# # def AVALIAÇÃO_MODAL():
# # 	'''
# #     '''
# #
# # 	AVALIAÇÃO = choice.Menu(['+', '-']).ask()
# #
# # 	if AVALIAÇÃO == '-':
# # 		AVALIAÇÃO_MODAL = ''
# #
# # 	else:
# # 		POLARIDADE = choice.Menu(['positiva', 'negativa']).ask()
# # 		##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
# # 		# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
# #
# # 		if POLARIDADE == 'positiva':
# # 			Adjunto_polaridade = ''
# #
# # 		elif POLARIDADE == 'negativa':
# # 			Adjunto_polaridade = 'não'
# #
# # 	return Adjunto_polaridade
# #
# #
# # ###
# # def TIPO_POLARIDADE():
# # 	'''
# #     '''
# # 	print('Qual o tipo_pessoa de polaridade?')
# # 	tipo_polaridade = choice.Menu(['positiva', 'negativa']).ask()
# # 	##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
# # 	# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
# #
# # 	return tipo_polaridade
# #
# #
# # def POLARIDADE():
# # 	'''
# #     '''
# # 	print('Qual o tipo_pessoa de polaridade?')
# # 	tipo_polaridade = choice.Menu(['positiva', 'negativa']).ask()
# # 	##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada (em que estruturas?).
# # 	# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
# #
# # 	if tipo_polaridade == 'positiva':
# # 		Adjunto_polaridade = ''
# #
# # 	elif tipo_polaridade == 'negativa':
# # 		Adjunto_polaridade = 'não'
# #
# # 	return Adjunto_polaridade
# #
# #
# # ##############
# #
# # ## Preciso resolver como vou abordar a questão deste sistema: por enquanto vou mexer apenas com
# # # polaridade, e ir incrementando as combinações.
# # #
# # # def TIPO_AVALIAÇÃO_MODAL ():
# # #    '''
# # #    '''
# # #    AVALIAÇÃO = choice.Menu (['+', '-']).ask()
# # #
# # #    if AVALIAÇÃO == '-':
# # #        AVALIAÇÃO_MODAL = 'AvM_sem_avaliação_modal'
# # #
# # #    else:
# # #        POLARIDADE = choice.Menu (['positiva','negativa']).ask()
# # #        ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
# # #        #Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
# # #
# # #        if POLARIDADE == 'positiva':
# # #            Adjunto_polaridade == 'AvM_polaridade_positiva'
# # #
# # #        elif POLARIDADE == 'negativa':
# # #            Adjunto_polaridade == 'AvM_polaridade_negativa'
# # #
# #
# # ##para o sistema de modo, AINDA não considerei o subsistema de VALIDAÇÃO. (será implementado)
# #
# # def MODO():
# # 	'''
# #     '''
# #
# # 	print('Faça as escolhas de MODO da oração:')
# # 	MODO = SUJEITABILIDADE() + '_' + TIPO_DE_MODO()
# # 	return MODO
# #
# #
# # # A DÊIXIS: VER, POIS ELA É DECIDIDA DESDE A ORDEM DA PALAVRA...
# #
# #
# # # TEMA
# #
# #
# # def TEMA_TEXTUAL():
# # 	'''
# #     '''
# # 	print('Há TEMA TEXTUAL?')
# # 	Tema_textual = choice.Menu(['sim', 'não']).ask()
# # 	if Tema_textual == 'não':
# # 		TEMA_TEXTUAL = ''
# # 	else:
# # 		print('Há TEMA TEXTUAL continuativo?')
# # 		tem_continuativo = choice.Menu(['sim', 'não']).ask()
# # 		if tem_continuativo == 'não':
# # 			TEMA_CONTINUATIVO = ''
# # 		else:
# # 			TEMA_CONTINUATIVO = conjunção_continuativa() + ','
# # 		print('Há TEMA TEXTUAL conjuntivo?')
# # 		tem_conjuntivo = choice.Menu(['sim', 'não']).ask()
# # 		if tem_conjuntivo == 'não':
# # 			TEMA_CONJUNTIVO = ''
# # 		else:
# # 			TEMA_CONJUNTIVO = grupo_conjuntivo()
# # 		print('Há TEMA TEXTUAL relativo?')
# # 		tem_relativo = choice.Menu(['sim', 'não']).ask()
# # 		if tem_relativo == 'não':
# # 			TEMA_RELATIVO = ''
# # 		elif tem_relativo == 'sim':
# # 			print('Qual a tipo_pessoa de relativo?')
# # 			tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
# # 			if tipo_de_relativo == 'nominal':
# # 				TEMA_RELATIVO = pronome_relativo()
# # 			elif tipo_de_relativo == 'adverbial':
# # 				TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
# # 				                             'onde', 'de quando', 'que', 'por onde']).ask()
# #
# # 		TEMA_TEXTUAL = TEMA_CONTINUATIVO + TEMA_CONJUNTIVO + TEMA_RELATIVO
# #
# # 	return TEMA_TEXTUAL
# #
# #
# # def TEMA_INTERPESSOAL():
# # 	'''
# #     '''
# #
# # 	print('Há TEMA INTERPESSOAL?')
# #
# # 	Tema_interpessoal = choice.Menu(['sim', 'não']).ask()
# # 	if Tema_interpessoal == 'não':
# # 		TEMA_INTERPESSOAL = ''
# #
# # 	elif Tema_interpessoal == 'sim':  ###POR ENQUANTO, TRABALHANDO COM A realizacao DE APENAS 1 TEMA INTERPESSOAL
# #
# # 		TIPO_TEMA_INTERPESSOAL = choice.Menu(['TI_avaliação_modo', 'TI_avaliação_comentário',
# # 		                                      'TI_encenação_troca', 'TI_encenação_papel_falante', 'TI_polaridade',
# # 		                                      'TI_encenação_papel_ouvinte',
# # 		                                      'TI_NA']).ask()
# #
# # 		if (TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_modo' or TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_comentário' or
# # 				TIPO_TEMA_INTERPESSOAL == 'TI_polaridade'):
# #
# # 			tipo_realizacao = choice.Menu(['grupo_adverbial', 'frase_preposicional']).ask()
# # 			if tipo_realizacao == 'grupo_adverbial':
# # 				TEMA_INTERPESSOAL = advérbio() \
# # 			else:
# # 				TEMA_INTERPESSOAL = frase_preposicional()
# #
# # 		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_troca':
# # 			TEMA_INTERPESSOAL = elemento_qu()
# #
# # 		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_falante':
# # 			TEMA_INTERPESSOAL = partícula_modal()
# # 		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_ouvinte':
# # 			TEMA_INTERPESSOAL = nome_próprio()  ##talvez um pronome, mas por enquanto vou deixar so o nome
# #
# # 	return TEMA_INTERPESSOAL
# #
# #
# # def TEMA_IDEACIONAL():
# # 	'''
# #     ''' \
# #  \
# # 	print('Qual a ORIENTAÇÃO MODAL do tema?')
# # 	ORIENTAÇÃO_MODAL = choice.Menu(['orientado', 'não_orientado']).ask()
# #
# # 	print('Qual a ORIENTAÇÃO TRANSITIVA do tema?')
# # 	ORIENTAÇÃO_TRANSITIVA = choice.Menu(['direcional', 'não_direcional']).ask()
# #
# # 	print('Qual a SELEÇÃO TEMÁTICA do tema?')
# # 	SELEÇÃO_TEMÁTICA = choice.Menu(['default', 'proeminente']).ask()
# #
# # 	if ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'default':
# # 		print('Qual o tipo_pessoa de TEMA DEFAULT?')
# # 		TEMA_DEFAULT = choice.Menu(['imperativo',
# # 		                            'indicativo']).ask()
# #
# # 		if TEMA_DEFAULT == 'imperativo':
# # 			TEMA_IDEACIONAL = 'TID_default_imperativo'
# #
# # 		elif TEMA_DEFAULT == 'indicativo':
# # 			print('Qual o tipo_pessoa de TEMA DEFAULT INDICATIVO?')
# # 			TEMA_DEFAULT_indicativo = choice.Menu(['declarativo',
# # 			                                       'interrogativo_polar',
# # 			                                       'interrogativo_sujeito_elemental']).ask()
# #
# # 			print('Há TEMA IDENTIFICATIVO?')
# # 			TEMA_IDENTIFICATIVO = choice.Menu(['NA',
# # 			                                   'equativo_codificação',
# # 			                                   'equativo_decodificação']).ask()
# #
# # 			if TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'NA':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_NA'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'NA':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'NA':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_decodificação': \
# #  \
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_decodificação'
# #
# #
# # 			elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_codificação':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'equativo_codificação':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação'
# #
# # 			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_codificação':
# #
# # 				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_codificação'
# #
# #
# # 	elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':
# #
# # 		TEMA_ÂNGULO = choice.Menu(['TID_fonte', 'TID_ponto_de_vista']).ask()
# #
# # 		TEMA_IDEACIONAL = TEMA_ÂNGULO
# #
# #
# #
# # 	elif ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'default':
# #
# # 		TEMA_ELEMENTAL = choice.Menu(['TID_complemento_elemental', 'TID_adjunto_elemental']).ask()
# #
# # 		TEMA_IDEACIONAL = TEMA_ELEMENTAL
# #
# #
# #
# # 	elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':
# # 		print('Qual tipo_pessoa de TEMA PROEMINENTE?')
# #
# # 		TEMA_PROEMINENTE = choice.Menu(['TID_perspectiva_intensificação', \
# # 		                                'TID_perspectiva_outro',
# # 		                                'TID_intensivo_absoluto',
# # 		                                'TID_intensivo_relativo_papel_transitivo_nuclear_participante',
# # 		                                'TID_intensivo_relativo_papel_transitivo_nuclear_processo',
# # 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_elaboração',
# # 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_extensão',
# # 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto',
# # 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_reprisado',
# # 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_recuperável',
# # 		                                'TID_intensivo_relativo_predicação_default_local',
# # 		                                'TID_intensivo_relativo_predicação_proeminente_local'
# #
# # 		                                ]).ask()
# #
# # 		TEMA_IDEACIONAL = TEMA_PROEMINENTE
# #
# # 	return TEMA_IDEACIONAL
# #
# #
# # def conjunção_continuativa():
# # 	'''
# #     '''
# # 	print('Qual o modo de inserção da conjunção?')
# # 	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
# #
# # 	if modo_inserção == 'inserção_manual':
# # 		conjunção_continuativa = input('Escreva o continuativo desejado:')
# #
# # 	elif modo_inserção == 'inserção_menu':
# # 		print('Escolha um continuativo:') \
# # 		conjunção_continuativa = input("""
# #                                  1:e
# #                                  2:é
# #                                  3:ah
# #                                  4:mas
# #                                  5:sim
# #                                  6:bem
# #                                  7:não
# #                                  8:agora
# #                                  9:então
# #                                  10:pois é
# #                                  11:tipo_pessoa
# #                                  12:tipo_pessoa assim
# #                                  13:ó
# #                                  14:daí
# #                                  15:aí
# #                                  16:aí então
# #                                  17:quer
# #                                  18:dizer
# #                                  19:assim
# #                                  20:em
# #                                  21:seguida
# #                                  22:por fim
# #                                  23:porque
# #                                  24:porém
# #                                  25:também
# #                                  26:é que
# #                                  27:olha
# #
# #
# #
# #                                Escolha uma opção:""")
# #
# # 		if conjunção_continuativa == '1':
# # 			conjunção_continuativa = 'e'
# # 		elif conjunção_continuativa == '2':
# # 			conjunção_continuativa = 'é'
# # 		elif conjunção_continuativa == '3':
# # 			conjunção_continuativa = 'ah'
# # 		elif conjunção_continuativa == '4':
# # 			conjunção_continuativa = 'mas'
# # 		elif conjunção_continuativa == '5':
# # 			conjunção_continuativa = 'sim'
# # 		elif conjunção_continuativa == '6':
# # 			conjunção_continuativa = 'bem' \
# # 		elif conjunção_continuativa == '7':
# # 			conjunção_continuativa = 'não'
# # 		elif conjunção_continuativa == '8':
# # 			conjunção_continuativa = 'agora'
# # 		elif conjunção_continuativa == '9':
# # 			conjunção_continuativa = 'então'
# # 		elif conjunção_continuativa == '10':
# # 			conjunção_continuativa = 'pois é'
# # 		elif conjunção_continuativa == '11':
# # 			conjunção_continuativa = 'tipo'
# # 		elif conjunção_continuativa == '12':
# # 			conjunção_continuativa = 'tipo_pessoa assim '
# # 		elif conjunção_continuativa == '13':
# # 			conjunção_continuativa = 'ó'
# # 		elif conjunção_continuativa == '14':
# # 			conjunção_continuativa = 'daí'
# # 		elif conjunção_continuativa == '15':
# # 			conjunção_continuativa = 'aí'
# # 		elif conjunção_continuativa == '16':
# # 			conjunção_continuativa = 'aí então '
# # 		elif conjunção_continuativa == '17':
# # 			conjunção_continuativa = 'quer'
# # 		elif conjunção_continuativa == '18':
# # 			conjunção_continuativa = 'dizer'
# # 		elif conjunção_continuativa == '19':
# # 			conjunção_continuativa = 'assim'
# # 		elif conjunção_continuativa == '20':
# # 			conjunção_continuativa = 'em'
# # 		elif conjunção_continuativa == '21':
# # 			conjunção_continuativa = 'seguida'
# # 		elif conjunção_continuativa == '22':
# # 			conjunção_continuativa = 'por fim'
# # 		elif conjunção_continuativa == '23':
# # 			conjunção_continuativa = 'porque'
# # 		elif conjunção_continuativa == '24':
# # 			conjunção_continuativa = 'porém'
# # 		elif conjunção_continuativa == '25':
# # 			conjunção_continuativa = 'também'
# #
# # 		elif conjunção_continuativa == '26':
# # 			conjunção_continuativa = 'é que'
# # 		elif conjunção_continuativa == '27':
# # 			conjunção_continuativa = 'olha'
# #
# # 	return conjunção_continuativa
# #
# #
# # def elemento_qu():
# # 	'''
# #     '''
# # 	elemento_qu = choice.Menu(['o que', 'quem', 'qual', 'quanto',
# # 	                           'quantos', 'quando', 'como', 'onde',
# # 	                           'de quem', 'por quê', 'pra quê', 'por que']).ask()
# #
# # 	return elemento_qu
# #
# #
# # def partícula_modal():
# # 	'''
# #     '''
# # 	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
# #
# # 	if modo_inserção == 'inserção_manual':
# # 		partícula_modal = input('Escreva partícula modal desejada:')
# #
# # 	elif modo_inserção == 'inserção_menu':
# # 		partícula_modal = choice.Menu(['né', 'ué', 'ó', 'uai', 'é']).ask()  ##HÁ MAIS PARTÍCULAS....
# #
# # 	return partícula_modal
# #
# #
# # ## NO CASO DO SISTEMA DE AVALIAÇÃO_MODAL EU NÃO CONTEMPLEI AINDA  O SISTEMA, POR ENQUANTO VOU ME
# # # ATER APENAS AO SUBSISTEMA DE POLARIDADE.
# #
# # ####FORMAÇÃO DA ORAÇÃO
# #
# #
# # def atribuição_de_relação():
# # 	'''
# #     '''
# # 	atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
# # 	                                     'atribuição_proj_ment_desiderativa',
# # 	                                     'atribuição_proj_verbal',
# # 	                                     'atribuição_expan_elaboração',
# # 	                                     'atribuição_expan_intencificação'
# # 	                                     ]).ask()
# # 	return atribuição_de_relação
# #
# #
# # def PROCESSO_RELACIONAL():
# # 	'''
# #     '''
# # 	tipo_de_relacional = choice.Menu(['PR_relacional_intensivo_atributivo',
# # 	                                  'PR_relacional_intensivo_identificativo',
# # 	                                  'PR_relacional_possessivo_atributivo',
# # 	                                  'PR_relacional_circunstancial_atributivo',
# # 	                                  'PR_relacional_possessivo_identificativo',
# # 	                                  'PR_relacional_circunstancial_identificativo']).ask()
# #
# # 	return tipo_de_relacional
# #
# #
# # def TRANSITIVIDADE(): \
# # 	'''
# #     '''
# # 	print('Qual o tipo_pessoa de Processo?')
# # 	TIPO_DE_PROCESSO = choice.Menu(['Material', 'Relacional', \
# # 	                                'Mental', 'Verbal',
# # 	                                'Existencial']).ask()
# #
# # 	if TIPO_DE_PROCESSO == 'Material':
# # 		print('Selecione as opções do sistema da Oração Material')
# # 		Processo = PROCESSO_MATERIAL()
# # 		Agenciamento = AGENCIAMENTO()
# #
# # 		TRANSITIVIDADE = Processo + '_' + Agenciamento
# #
# # 	elif TIPO_DE_PROCESSO == 'Relacional':
# # 		print('Selecione as opções do sistema da Oração Relacional')
# # 		Processo = PROCESSO_RELACIONAL()
# # 		Agenciamento = AGENCIAMENTO()
# #
# # 		TRANSITIVIDADE = Processo + '_' + Agenciamento
# #
# # 	elif TIPO_DE_PROCESSO == 'Existencial':
# # 		print('Selecione as opções do sistema da Oração Existencial')
# # 		Processo = 'PR_Existencial'
# # 		Agenciamento = AGENCIAMENTO()
# #
# # 		TRANSITIVIDADE = Processo + '_' + Agenciamento
# #
# # 	elif TIPO_DE_PROCESSO == 'Verbal':
# # 		print('Selecione as opções do sistema da Oração Verbal')
# # 		Processo = 'PR_Verbal'
# # 		Agenciamento = AGENCIAMENTO()
# #
# # 		TRANSITIVIDADE = Processo + '_' + Agenciamento
# #
# # 	elif TIPO_DE_PROCESSO == 'Mental':
# # 		print('Selecione as opções do sistema da Oração mental')
# # 		Processo = 'PR_Mental'
# # 		Agenciamento = AGENCIAMENTO() \
# #  \
# # 		TRANSITIVIDADE = Processo + '_' + Agenciamento
# #
# # 	return TRANSITIVIDADE
# #
# #
# # def oraçãoProjetada():
# # 	oração = oração_gerar()
# # 	return oração
# #
# #
# # def oraçãoDownranked():
# # 	oração = oração_gerar()
# # 	return oração
# #
# #
# # def oração_gerar():
# # 	'''(str,str,str)->str
# #     Retorna a formação estrutural na lexicogramática
# #      (oração) de uma figura específica da semântica
# #
# #     >>> oração_gerar()
# #     'eu bebi água'
# #     '''
# # 	Transitividade = TRANSITIVIDADE()
# # 	Modo = MODO()
# # 	Tema_id = TEMA_IDEACIONAL()
# # 	# ORAÇÃO MENTAL
# # 	if Transitividade == 'PR_Mental_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Selecione o tipo_pessoa de processo mental:')
# # 		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
# # 		print('Qual a FENOMENALIZAÇÃO?')
# # 		print('Médio sem alcance: Fenomenalização = não-fenomenalização')
# # 		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
# #
# # 		if FENOMENALIZAÇÃO == 'não-fenomenalização':
# # 			print('Qual tipo_pessoa de não-fenomenalização?')
# # 			print('Médio sem alcance: Não-fenomenalização = comportamento-passivo')
# # 			TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['comportamento-passivo']).ask()
# #
# # 			if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Humanizado)?')
# # 					Experienciador = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade
# # 					+ ' ' + Processo + ' ' + Circunstância + '.'
# # 					# Ex.: Tenho pensado; Eu pensei a noite toda;
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
# # 					print('Selecione verbo lematizado emotivo ou perceptivo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Animalizado)?')
# # 					Experienciador = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Circunstância + '.'
# # 					# 'Eu ouvi perfeitamente' - verificar se esse caso se configura como um sem alcance
# # 					# pois apesar de não esta instanciado, há o potencial de fenômeno
# #
# # 	elif Transitividade == 'PR_Mental_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Selecione o tipo_pessoa de processo mental:')
# # 		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
# # 		print('Qual a FENOMENALIZAÇÃO?')
# # 		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
# # 		if FENOMENALIZAÇÃO == 'não-fenomenalização':
# # 			print('Médio com alcance, Não-fenomenalização = assunto ')
# # 			print('Qual tipo_pessoa de não-fenomenalização?')
# # 			TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['assunto']).ask()
# #
# # 			if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Humanizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Assunto?')
# # 					Assunto = circunstância()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Assunto + ' ' + Circunstância + '.'
# # 					# Ex.: Eu sei de futebol.
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Animalizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Assunto?')
# # 					Assunto = circunstância()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Assunto + ' ' + Circunstância + '.'
# #
# # 		elif FENOMENALIZAÇÃO == 'fenomenalização':
# # 			print('Médio com alcance = mental emanente.')
# # 			print('Qual tipo_pessoa de fenomenalização?')
# # 			TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
# # 			if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Humanizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Fenômeno?')
# # 					Fenômeno = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Fenômeno + ' ' + Circunstância + '.'
# # 			elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Qual tipo_pessoa de hiperfenômeno?')
# # 					print('Projeção = hiperfenômeno: criativo')
# # 					TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()
# #
# # 					if TIPO_HIPERFENÔMENO == 'criativo':
# # 						TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
# # 						if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
# # 							TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
# # 							if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
# # 								print('Selecione o verbo lexical correspondente ao tipo_pessoa de cognitivo:') \
# # 								print('Qual o Processo?')
# # 								Processo = grupo_verbal()
# # 								print('Qual o Experienciador (Ente:Humanizado)?')
# # 								Experienciador = estrutura_GN()
# # 								print('Qual o hiperfenômeno projetado? Selecione orientado-finito')
# # 								Pensamento = oraçãoProjetada()
# # 								Polaridade = POLARIDADE()
# # 								Circunstância = circunstância()
# # 								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador \
# # 								         + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + ' ' + Circunstância + '.'
# # 						elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
# # 							TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
# # 							if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
# # 								print('Selecione o verbo lexical correspondente ao tipo_pessoa de desiderativo:')
# # 								print('Qual o Processo?')
# # 								Processo = grupo_verbal()
# # 								print('Qual o Experienciador (Ente:Humanizado)?')
# # 								Experienciador = estrutura_GN()
# # 								print('Qual o hiperfenômeno projetado?')
# # 								print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
# # 								Desejo = oraçãoProjetada()
# # 								Polaridade = POLARIDADE()
# # 								Circunstância = circunstância()
# # 								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador \
# # 								         + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Desejo \
# # 								         + ' ' + Circunstância + '.'
# #
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Animalizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Fenômeno?')
# # 					Fenômeno = estrutura_GN() \
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Fenômeno + ' ' + Circunstância + '.'
# #
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				print('Qual tipo_pessoa de hiperfenômeno?')
# # 				TIPO_HIPERFENÔMENO = choice.Menu(['reativo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
# # 					print('Qual o tipo_pessoa de reativo?')
# # 					TIPO_reativo = choice.Menu(['metafenômeno']).ask()
# # 					if TIPO_reativo == 'metafenômeno':
# # 						TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
# # 						print('Selecione o verbo lexical correspondente ao tipo_pessoa de emotivo:') \
# # 						print('Qual o Processo?')
# # 						Processo = grupo_verbal()
# # 						print('Qual o Experienciador (Ente:Humanizado)?')
# # 						Experienciador = estrutura_GN()
# # 						print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
# # 						realizacao_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que',
# # 						                                       'GN+oração_qualificadora']).ask()
# # 						if realizacao_metafenômeno == 'oração_mudada_ordem':
# # 							print('Selecione as orientações desejadas:')
# # 							Metafenômeno = oraçãoProjetada()
# #
# # 						elif realizacao_metafenômeno == 'oração_que':
# # 							print('Selecione orientações desejadas') \
# # 							Metafenômeno = 'que' + ' ' + oraçãoProjetada()
# # 						else:
# # 							print('Selecione o GN com oração qualificadora:')
# # 							Metafenômeno = estrutura_GN()
# #
# # 						Polaridade = POLARIDADE()
# # 						Circunstância = circunstância()
# # 						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
# # 						         + ' ' + Processo + ' ' + Metafenômeno + ' ' + Circunstância + '.'
# #
# # 				elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
# # 					print('Qual o tipo_pessoa de reativo?')
# # 					TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
# # 					if TIPO_reativo == 'macrofenômeno':
# # 						print('Qual o Processo?')
# # 						Processo = grupo_verbal()
# # 						print('Qual o Experienciador (Ente:Humanizado)?')
# # 						Experienciador = estrutura_GN()
# # 						print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
# # 						realizacao_macrofenômeno = choice.Menu(
# # 							['não_finito_concretizado', 'não-orientado_gerúndio', 'oração_que',
# # 							 'GN+oração_qualificadora']).ask()
# # 						if realizacao_macrofenômeno == 'não_finito_concretizado':
# # 							print('Selecione grupo verbal não-finito_concretizado')
# # 							Macrofenômeno = oraçãoProjetada()
# #
# # 						elif realizacao_macrofenômeno == 'não-orientado_gerúndio':
# # 							print('Selecione grupo verbal não-orientado_gerúndio')
# # 							Macrofenômeno = oraçãoProjetada()
# # 						elif realizacao_macrofenômeno == 'oração_que':
# # 							print('Selecione orientações desejadas')
# # 							Macrofenômeno = 'que' + ' ' + oraçãoProjetada()
# # 						else:
# # 							print('Selecione o GN com oração qualificadora:')
# # 							Macrofenômeno = estrutura_GN()
# #
# # 						Polaridade = POLARIDADE()
# # 						Circunstância = circunstância()
# # 						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' \
# # 						         + Processo + ' ' + Macrofenômeno + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_Mental_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Efetivo operativo = mental impingente.')
# # 		print('Selecione o tipo_pessoa de processo mental:')
# # 		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
# # 		print('Qual a FENOMENALIZAÇÃO?')
# # 		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
# # 		if FENOMENALIZAÇÃO == 'fenomenalização':
# # 			print('Qual tipo_pessoa de fenomenalização?')
# # 			TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
# # 			if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Humanizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Fenômeno Agente?')
# # 					FenômenoAgente = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
# # 			elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
# # 				print('Qual tipo_pessoa de Processo superior?')
# # 				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask() \
# # 				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
# # 					print('Qual tipo_pessoa de hiperfenômeno?')
# # 					print('Projeção = hiperfenômeno: criativo')
# # 					TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()
# #
# # 					if TIPO_HIPERFENÔMENO == 'criativo':
# # 						TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
# # 						if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
# # 							TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
# # 							if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
# # 								print('Selecione o verbo lexical correspondente ao tipo_pessoa de cognitivo:')
# # 								print('Qual o Processo?')
# # 								Processo = grupo_verbal()
# # 								print('Qual o Experienciador (Ente:Humanizado)?')
# # 								Experienciador = estrutura_GN()
# # 								print('Qual o Pensamento Agente? Selecione orientado-finito')
# # 								PensamentoAgente = oraçãoProjetada()
# # 								Polaridade = POLARIDADE()
# # 								Circunstância = circunstância()
# # 								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + ' ' + 'que' + ' ' + PensamentoAgente
# # 								+ ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.' \
# # 								# Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me
# #
# # 						elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
# # 							TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
# # 							if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
# # 								print('Selecione o verbo lexical correspondente ao tipo_pessoa de desiderativo:')
# # 								print('Qual o Processo?')
# # 								Processo = grupo_verbal()
# # 								print('Qual o Experienciador (Ente:Humanizado)?')
# # 								Experienciador = estrutura_GN()
# # 								print('Qual o Desejo Agente?')
# # 								print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
# # 								DesejoAgente = oraçãoProjetada()
# # 								Polaridade = POLARIDADE()
# # 								Circunstância = circunstância()
# # 								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + ' ' + 'que' + ' ' + DesejoAgente \
# # 								         + ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
# # 								# Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me
# #
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
# # 					print('Selecione verbo lematizado cognitivo ou desiderativo:')
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Animalizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o Fenômeno/Agente?')
# # 					FenômenoAgente = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
# # 					# Ex.: Seus modos entristecem me
# #
# # 			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
# # 				print('Qual tipo_pessoa de Processo inferior?')
# # 				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
# # 				print('Qual tipo_pessoa de hiperfenômeno?')
# # 				TIPO_HIPERFENÔMENO = choice.Menu(['reativo']).ask()
# # 				if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
# # 					print('Qual o tipo_pessoa de reativo?')
# # 					TIPO_reativo = choice.Menu(['metafenômeno']).ask()
# # 					if TIPO_reativo == 'metafenômeno':
# # 						TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
# # 						print('Selecione o verbo lexical correspondente ao tipo_pessoa de emotivo:')
# # 						print('Qual o Processo?')
# # 						Processo = grupo_verbal()
# # 						print('Qual o Experienciador (Ente:Humanizado)?')
# # 						Experienciador = estrutura_GN()
# # 						print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
# # 						realizacao_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que', \
# # 						                                       'GN+oração_qualificadora']).ask() \
# # 						if realizacao_metafenômeno == 'oração_mudada_ordem':
# # 							print('Selecione as orientações desejadas:')
# # 							MetafenômenoAgente = oraçãoProjetada()
# #
# # 						elif realizacao_metafenômeno == 'oração_que':
# # 							print('Selecione orientações desejadas')
# # 							MetafenômenoAgente = 'que' + ' ' + oraçãoProjetada()
# # 						else:
# # 							print('Selecione o GN com oração qualificadora:')
# # 							MetafenômenoAgente = estrutura_GN()
# #
# # 						Polaridade = POLARIDADE()
# # 						Circunstância = circunstância()
# # 						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' \
# # 						         + MetafenômenoAgente + ' ' + Polaridade + ' ' \
# # 						         + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
# #
# # 				elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
# # 					print('Qual o tipo_pessoa de reativo?')
# # 					TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
# # 					if TIPO_reativo == 'macrofenômeno':
# # 						print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual o Experienciador (Ente:Humanizado)?')
# # 					Experienciador = estrutura_GN()
# # 					print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
# # 					realizacao_macrofenômeno = choice.Menu(
# # 						['não_finito_concretizado', 'não-orientado_gerúndio', 'oração_que',
# # 						 'GN+oração_qualificadora']).ask()
# # 					if realizacao_macrofenômeno == 'não_finito_concretizado':
# # 						print('Selecione grupo verbal não-finito_concretizado')
# # 						MacrofenômenoAgente = oraçãoProjetada()
# #
# # 					elif realizacao_macrofenômeno == 'não-orientado_gerúndio':
# # 						print('Selecione grupo verbal não-orientado_gerúndio')
# # 						MacrofenômenoAgente = oraçãoProjetada()
# # 					elif realizacao_macrofenômeno == 'oração_que':
# # 						print('Selecione orientações desejadas')
# # 						MacrofenômenoAgente = 'que' + ' ' + oraçãoProjetada()
# # 					else:
# # 						print('Selecione o GN com oração qualificadora:')
# # 						Macrofenômeno = estrutura_GN() \
# #  \
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância() \
# # 					oração = Tema_interpessoal + ' ' + Tema_textual \
# # 					         + ' ' + MacrofenômenoAgente + ' ' + Polaridade + ' ' \
# # 					         + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
# #
# #
# # 	##ORAÇÃO verbal
# #
# # 	elif Transitividade == 'PR_Verbal_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Qual a Ordem do Dizente?')
# # 		ORDEM_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()
# # 		if ORDEM_DO_DIZENTE == 'atividade':
# # 			TIPO_ATIVIDADE = 'fala'
# #
# # 			if TIPO_ATIVIDADE == 'fala':
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Dizente?')
# # 				Dizente = estrutura_GN()
# # 				print('Há Receptor?')
# # 				print('Selecione a Receptividade') \
# # 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# # 				if RECEPTIVIDADE == '+receptor':
# # 					Receptor = frase_preposicional()
# # 				else:
# # 					Receptor = ''
# # 				Polaridade = POLARIDADE() \
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# # 				         + ' ' + Receptor + ' ' + Circunstância + '.'
# # 				# Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...
# #
# #
# # 		elif ORDEM_DO_DIZENTE == 'semioticidade':
# # 			print('Semioticidade em Médio sem alcance = não_projeção')
# # 			TIPO_SEMIOTICIDADE = choice.Menu(['não_projeção']).ask()
# #
# # 			if TIPO_SEMIOTICIDADE == 'não_projeção':
# # 				print('Não-projeção + médio sem alcance = -verbiagem')
# # 				TIPO_NÃO_PROJEÇÃO = '-verbiagem'
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Dizente?')
# # 				Dizente = estrutura_GN()
# # 				print('Há Receptor?')
# # 				print('Selecione a Receptividade')
# # 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# # 				if RECEPTIVIDADE == '+receptor':
# # 					Receptor = frase_preposicional()
# # 				else:
# # 					Receptor = ''
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Qual a Ordem do Dizente?')
# # 		ORDEM_DO_DIZENTE = choice.Menu(['semioticidade']).ask()
# # 		print('Selecione a Receptividade')
# # 		RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# #
# # 		if ORDEM_DO_DIZENTE == 'semioticidade':
# # 			print('Selecione o tipo_pessoa de Semioticidade')
# #
# # 			TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
# # 			if TIPO_SEMIOTICIDADE == 'projeção':
# # 				print('Selecione o tipo_pessoa de projeção')
# # 				TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()
# # 				if TIPO_PROJEÇÃO == 'citativa':
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Dizente?')
# # 					Dizente = estrutura_GN()
# # 					print('Há Receptor?')
# # 					print('Selecione a Receptividade')
# # 					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# # 					if RECEPTIVIDADE == '+receptor':
# # 						Receptor = frase_preposicional()
# # 					else:
# # 						Receptor = ''
# # 					Polaridade = POLARIDADE()
# # 					print('Qual a oração projetada?')
# # 					Circunstância = circunstância()
# # 					Oração_projetada = oraçãoProjetada()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# # 					         + ' ' + Receptor + '"' + Oração_projetada + '" ' + ' ' + Circunstância + '.'
# # 					# Ex.: Eu disse a ele "Eu comi o bolo".
# #
# # 				elif TIPO_PROJEÇÃO == 'relativa':
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Dizente?')
# # 					Dizente = estrutura_GN()
# # 					print('Há Receptor?')
# # 					print('Selecione a Receptividade')
# # 					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# # 					if RECEPTIVIDADE == '+receptor':
# # 						Receptor = frase_preposicional()
# # 					else:
# # 						Receptor = ''
# # 					Polaridade = POLARIDADE()
# # 					print('Qual a oração projetada?')
# # 					Oração_projetada = oraçãoProjetada()
# # 					Circunstância = circunstância()
# #
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# # 					         + ' ' + Receptor + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + ' ' + Circunstância + '.'
# # 					# Ex.: Eu disse a ele que "Eu comi o bolo".
# #
# # 			elif TIPO_SEMIOTICIDADE == 'não_projeção':
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Dizente?')
# # 				Dizente = estrutura_GN()
# # 				print('Qual é a Verbiagem?')
# # 				Verbiagem = estrutura_GN()
# # 				print('Há Receptor?')
# # 				print('Selecione a Receptividade')
# # 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# # 				if RECEPTIVIDADE == '+receptor':
# # 					Receptor = frase_preposicional()
# # 				else:
# # 					Receptor = ''
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# # 				         + ' ' + Verbiagem + ' ' + Receptor + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_Verbal_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		Polaridade = POLARIDADE()
# # 		print('Qual é o Dizente?')
# # 		Dizente = estrutura_GN()
# # 		Circunstância = circunstância()
# #
# # 		print('O Alvo é realizado por grupo nominal ou frase preposicional?')
# # 		realizacao_alvo = choice.Menu(['GN', 'FP']).ask()
# # 		if realizacao_alvo == 'GN':
# # 			print('Qual é o Alvo?')
# # 			Alvo = estrutura_GN()
# # 			print('Qual a localização do alvo na oração (em relação ao Processo)?')
# # 			localização_alvo = choice.Menu(['ante_processo', 'pós_processo']).ask()
# # 			if localização_alvo == 'ante_processo':
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' \
# # 				         + Alvo + ' ' + Processo + ' ' + Circunstância + '.'
# # 			else:
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Alvo + ' ' + Circunstância + '.' \
# # 		else:
# # 			print('Qual é o Alvo?')
# # 			Alvo = frase_preposicional()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Alvo + ' ' + Circunstância + '.'
# #
# #
# # 	elif Transitividade == 'PR_Verbal_AG_efetivo_receptivo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		Polaridade = POLARIDADE()
# # 		print('Qual é o Dizente?')
# # 		Dizente = frase_preposicional()
# # 		print('Qual é o Alvo?')
# # 		Alvo = estrutura_GN()
# # 		Circunstância = circunstância()
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Alvo + ' ' + Polaridade + ' ' + Processo \
# # 		         + ' ' + Dizente + ' ' + Circunstância + '.'
# #
# # 	###MATERIAL
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		print('Qual é a Meta?')
# # 		Meta = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 		else:
# # 			Iniciador = ''
# #
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask() \
# #  \
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# #
# # 			print('há Resultado_elaboração atributo ou papel?')
# # 			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# # 			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# # 					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# # 				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
# # 				if realizacao_atributo == 'adjetivo':
# # 					Atributo = adjetivo_modificador()
# # 				elif realizacao_atributo == 'frase_preposicional':
# # 					Atributo = frase_preposicional()
# # 			elif RESULTADO_QUALITATIVO == '-resultado':
# # 				Atributo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '.'
# #
# # 		elif TIPO_DE_RESULTADO == 'extensão':
# # 			print('Há Participante Beneficiário na oração?')
# # 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 			if RECEPÇÃO == '+beneficiário':
# # 				Beneficiário = frase_preposicional()
# # 			elif RECEPÇÃO == '-beneficiário':
# # 				Beneficiário = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		print('Qual é a Meta?')
# # 		Meta = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN()
# # 		else:
# # 			Iniciador = ''
# #
# # 		print(
# # 			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# # 		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()
# #
# # 		if CLIENTE == '+cliente':
# # 			Cliente = frase_preposicional()
# # 		else:
# # 			Cliente = ''
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# # 		         + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()
# # 		else:
# # 			Iniciador = ''
# # 		print('Há Participante Beneficiário na oração?')
# # 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 		if RECEPÇÃO == '+beneficiário':
# # 			Beneficiário = frase_preposicional()
# # 		elif RECEPÇÃO == '-beneficiário':
# # 			Beneficiário = ''
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# # 			print('Qual é o Escopo?')
# # 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# # 			if tipo_Escopo == 'escopo(processo)':
# # 				Escopo = estrutura_GN()
# # 			elif tipo_Escopo == 'escopo(entidade)':
# # 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Escopo + ' ' + Beneficiário + ' ' + Circunstância + '.'
# #
# # 		elif TIPO_DE_RESULTADO == 'intensificação':
# # 			print('Qual é o Escopo?')
# # 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# # 			if tipo_Escopo == 'escopo(processo)':
# # 				Escopo = estrutura_GN()
# # 			elif tipo_Escopo == 'escopo(entidade)':
# # 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# # 			print('Há resultado locativo?')
# # 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# # 			if realizacao_locativo == 'sim':
# # 				Resultado_locativo = frase_preposicional()
# # 			else:
# # 				Resultado_locativo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Beneficiário + ' ' + Circunstância + '.'
# #
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA': \
# #  \
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# # 		print('Há Participante Beneficiário na oração?')
# # 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 		if RECEPÇÃO == '+beneficiário':
# # 			Beneficiário = frase_preposicional()
# # 		elif RECEPÇÃO == '-beneficiário':
# # 			Beneficiário = ''
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# # 			print('Orações médio_sem_alcance  selecionam -escopo')
# # 			Escopo = ''
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Beneficiário + '' + Circunstância + '.'
# #
# #
# # 		elif TIPO_DE_RESULTADO == 'intensificação':
# # 			print('Orações médio_sem_alcance selecionam -escopo')
# # 			print('Há Participante Beneficiário na oração?')
# # 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 			if RECEPÇÃO == '+beneficiário':
# # 				Beneficiário = frase_preposicional()
# # 			elif RECEPÇÃO == '-beneficiário':
# # 				Beneficiário = ''
# # 			print('Há resultado locativo?')
# # 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# # 			if realizacao_locativo == 'sim':
# # 				Resultado_locativo = frase_preposicional()
# # 			else:
# # 				Resultado_locativo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Resultado_locativo + ' ' + Circunstância + ' ' + Beneficiário + '.'
# #
# #
# # 	##MATERIAL METEOROLÓGICA
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
# # 			and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		Polaridade = POLARIDADE()
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN()
# # 		else:
# # 			Iniciador = ''
# # 		print('Há Participante Beneficiário na oração?')
# # 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 		if RECEPÇÃO == '+beneficiário':
# # 			Beneficiário = frase_preposicional()
# # 		elif RECEPÇÃO == '-beneficiário':
# # 			Beneficiário = ''
# # 		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
# # 		print('Qual o tipo_pessoa de inTransitividade?')
# # 		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
# # 			print('Há escopo?')
# # 			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
# # 			if escopo_intransitiva == '+escopo':
# # 				print('Qual estrutura realiza o escopo?')
# # 				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
# # 				if realizacao_escopo == 'frase_preposicional':
# # 					Escopo = frase_preposicional()
# # 				elif realizacao_escopo == 'grupo_nominal':
# # 					Escopo = estrutura_GN()
# # 			elif escopo_intransitiva == '-escopo':
# # 				Escopo = ''
# #
# # 		Circunstância = circunstância()
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
# # 		         + ' ' + Escopo + ' ' + Beneficiário + ' ' + Circunstância + '.'
# #
# #
# # 	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		Tema_textual = TEMA_TEXTUAL() \
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()
# # 		else:
# # 			Iniciador = ''
# # 		print('Há Participante Beneficiário na oração?')
# # 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 		if RECEPÇÃO == '+beneficiário':
# # 			Beneficiário = frase_preposicional()
# # 		elif RECEPÇÃO == '-beneficiário':
# # 			Beneficiário = ''
# # 		Circunstância = circunstância()
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 		         + ' ' + Processo + ' ' + Beneficiário + ' ' + Circunstância + '.'
# #
# # 		##########COMEÇO DE AGENCIAMENTO PASSIVA
# # 		# (E CONSEQUENTEMENTE MUDANÇA NO TEMA IDEACIONAL: COMPLEMENTO ELEMENTAL)
# #
# # 	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
# # 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 	#          and Tema_id == 'TID_complemento_elemental':
# # 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# # 	#      Tema_textual=TEMA_TEXTUAL()
# # 	#
# # 	#      print ('Qual o Processo?')
# # 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# # 	#      print('Qual é a Meta?')
# # 	#      Meta = estrutura_GN()
# # 	#      Polaridade = POLARIDADE ()
# # 	#      Circunstância = circunstância()
# # 	#      print('Há Participante Beneficiário na oração?')
# # 	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 	#      if RECEPÇÃO == '+beneficiário':
# # 	#          Beneficiário = frase_preposicional()
# # 	#      elif RECEPÇÃO == '-beneficiário':
# # 	#          Beneficiário = ''
# # 	#      print ('Há Participante Iniciador na oração?')
# # 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# # 	#      if INICIADOR == '+iniciador':
# # 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 	#      else:
# # 	#          Iniciador = ''
# # 	#
# # 	#      print ('O Ator/Agente é realizado na oração?')
# # 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# # 	#      if realizacao_Ator == '+ator/agente':
# # 	#          print('Qual é o Ator/Agente?')
# # 	#          Ator = frase_preposicional()
# # 	#      elif realizacao_Ator == '-ator/agente':
# # 	#          Ator = ''
# # 	#      print ('Há resultado do processo?')
# # 	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
# # 	#
# # 	#      if TIPO_DE_RESULTADO == 'elaboração':
# # 	#
# # 	#          print ('há Resultado_elaboração atributo ou papel?')
# # 	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# # 	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# # 	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# # 	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
# # 	#              if realizacao_atributo == 'adjetivo':
# # 	#                  Atributo = adjetivo_modificador ()
# # 	#              elif realizacao_atributo == 'frase_preposicional':
# # 	#                  Atributo = frase_preposicional()
# # 	#          elif RESULTADO_QUALITATIVO == '-resultado':
# # 	#              Atributo = ''
# # 	#
# # 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
# # 	#                   + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' +Beneficiário+' '+ Circunstância +'.'
# # 	#
# # 	#      elif TIPO_DE_RESULTADO == 'extensão':
# # 	#          print ('Há Participante Beneficiário na oração?')
# # 	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
# # 	#          if RECEPÇÃO == '+beneficiário':
# # 	#              Beneficiário = frase_preposicional()
# # 	#          elif RECEPÇÃO == '-beneficiário':
# # 	#              Beneficiário = ''
# # 	#
# # 	#
# # 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
# # 	#                   + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +' '+Beneficiário+' '+ Circunstância +'.'
# # 	#
# # 	# ##
# # 	#
# # 	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
# # 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 	#          and Tema_id == 'TID_complemento_elemental':
# # 	#
# # 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# # 	#      Tema_textual=TEMA_TEXTUAL()
# # 	#
# # 	#      print ('Qual o Processo?')
# # 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# # 	#      print('Qual é a Meta?')
# # 	#      Meta = estrutura_GN()
# # 	#      Polaridade = POLARIDADE ()
# # 	#      print('Há Participante Beneficiário na oração?')
# # 	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 	#      if RECEPÇÃO == '+beneficiário':
# # 	#          Beneficiário = frase_preposicional()
# # 	#      elif RECEPÇÃO == '-beneficiário':
# # 	#          Beneficiário = ''
# # 	#      Circunstância = circunstância()
# # 	#
# # 	#
# # 	#      print ('Há Participante Iniciador na oração?')
# # 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# # 	#      if INICIADOR == '+iniciador':
# # 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 	#      else:
# # 	#          Iniciador = ''
# # 	#
# # 	#      print ('O Ator/Agente é realizado na oração?')
# # 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# # 	#      if realizacao_Ator == '+ator/agente':
# # 	#          print('Qual é o Ator/Agente?')
# # 	#          Ator = frase_preposicional()
# # 	#      elif realizacao_Ator == '-ator/agente':
# # 	#          Ator = ''
# # 	#
# # 	#
# # 	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# # 	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
# # 	#
# # 	#      if CLIENTE == '+cliente':
# # 	#          Cliente = frase_preposicional()
# # 	#      elif CLIENTE == '-cliente':
# # 	#          Cliente='' \
# # 	#
# # 	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
# # 	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Beneficiário+' '+Circunstância +'.'
# #
# # 	###RELACIONAl
# # 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
# # 		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 		print('Qual o tipo_pessoa de especificação de associação?')
# # 		tipo_especificação_associação = choice.Menu(['entidade', 'qualidade']).ask()
# # 		print('Qual a fase da atribuição?')
# # 		fase_atribuição = choice.Menu(['neutra',
# # 		                               'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
# # 		###não vou especializar os tipos de fase.
# # 		print('Qual o domínio da atribuição')
# # 		domínio_atribuição = choice.Menu(['material', 'semiótico']).ask()
# #
# # 		if (
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN() \
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Atributo + ' ' + Circunstância + '.'
# #
# # 		elif (
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador?') \
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = adjetivo_modificador()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
# # 			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
# # 			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Atributo + ' ' + Circunstância + '.'
# #
# #
# # 	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
# # 	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva
# # 	# (há a possibilidade de Agente de segunda, terceira.....ordem)
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Atribuidor?')
# # 			Atribuidor = estrutura_GN()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Atribuidor?')
# # 			Atribuidor = frase_preposicional()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo
# # 			+ ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstância + '.'
# #
# #
# # 	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação':
# # 		print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito '
# # 		      'deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 		if direcionalidade_voz == 'meio_operativa':
# # 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente'
# # 			      'o elemento em posição temática)')
# # 			# (confluência do Símbolo/Identificado) =
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '.'
# #
# # 		elif direcionalidade_voz == 'meio_receptiva':
# # 			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
# # 			##NESTE CASO, confluência de Valor/Sujeito
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL() \
# #  \
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Símbolo + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação':
# #
# # 		print(
# # 			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 		if direcionalidade_voz == 'meio_operativa':
# # 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
# #
# # 			# (confluência do Símbolo/Identificador/Sujeito) =
# # 			# (Valor/Identificado/complemento)
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Valor + ' ' + Circunstância + '.'
# #
# # 		elif direcionalidade_voz == 'meio_receptiva':
# # 			print('Neste caso, o Valor conflui com o Sujeito')
# # 			##NESTE CASO, confluência de Valor/Identificado/Sujeito
# # 			##(Símbolo/Identificador/Complemento)
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Símbolo + ' ' + Circunstância + '.'
# #
# # 	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
# #
# # 	#    ###TRUE_Efetiva_operativa
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas) \
# # 		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Designador?')
# # 			Designador = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()  ##ou frase preposicional?
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstância + '.'
# # 			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)
# #
# # 	###TRUE_Efetiva_receptiva
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Designador?')
# # 			Designador = frase_preposicional()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()  ##ou frase preposicional?
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# # 			#
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstância + '.'
# # 	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
# # 	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
# #
# # 	# POSSESSIVO ATRIBUTIV0
# #
# # 	if Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()
# #
# # 		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':
# #
# # 			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
# #
# # 			if realizacao_atributo == 'grupo_nominal_possessivo':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Posse?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Possuidor?')
# # 				Atributo_Possuidor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'
# #
# # 			elif realizacao_atributo == 'frase_preposicional':
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Posse?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Possuidor?')
# # 				Atributo_Possuidor = frase_preposicional()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'
# #
# #
# # 		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
# #
# # 			##VERBO TER/POSSUIR/
# #
# # 			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask() \
# #  \
# # 			if tipo_possuidor == 'possuidor_portador':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Possuidor?')
# # 				Portador_Possuidor = estrutura_GN()
# # 				print('Qual é o Atributo/Posse?')
# # 				Atributo_Posse = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstância + '.'
# #
# #
# # 			###VERBOS PERTENCER A/...
# #
# # 			elif tipo_possuidor == 'possuidor_atributo':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Possuidor?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Posse?')
# # 				Atributo_Possuidor = frase_preposicional()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'
# #
# # 		# POSSESSIVO IDENTIFICATIVO
# #
# #
# # 	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()
# #
# # 		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
# #
# # 				print(
# # 					'Escolha o tipo_pessoa de realizacao do Valor:')
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)/Possuído?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)/Possuidor?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O piano é seu
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '.'
# #
# # 				elif realizacao_Valor == 'frase_preposicional':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)?')
# # 					Valor_Possuidor = frase_preposicional()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O piano é do André
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '.'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
# #
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)/Possuído?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)/Possuidor?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O seu é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '.'
# #
# # 				elif realizacao_Valor == 'frase_preposicional':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O do André é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '.'
# #
# # 		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
# # 			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
# # 			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print(
# # 					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)/Possuidor?')
# # 				Símbolo_Possuidor = estrutura_GN()
# # 				print('Qual o Valor(Value)/Possuído?')
# # 				Valor_Possuído = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: O produto contém plástico, Eles merecem a aposentadoria
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstância + '.'
# #
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
# #
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()  ##na passiva
# # 					print('Qual o Valor(Value)/Possuído?')
# # 					Valor_Possuído = estrutura_GN()
# # 					print('Qual é o Símbolo(Token)/Possuidor?')
# # 					Símbolo_Possuidor = frase_preposicional()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O seu é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstância + '.'
# #
# #
# # 	#####RELACIONAL CIRCUNSTANCIAL
# #
# # 	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
# # 		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
# #
# # 		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador')
# # 			Portador = estrutura_GN()
# # 			print('Qual é o Atributo Circunstancial?')
# # 			Atributo_Circunstancial = circunstância()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			# Ex.: O livro é sobre a IIGuerra
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstância + '.'
# #
# # 		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador')
# # 			Portador = estrutura_GN()
# # 			print('Qual é o Atributo Circunstancial?')
# # 			Atributo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			# Ex.: O livro retrata a IIGuerra
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Atributo + ' ' + Circunstância + '.'
# #
# # 	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		print('O significado circunstancial é realixado no participante ou no processo?')
# # 		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
# # 			['participante_circunstancial', 'processo_circunstancial']).ask()
# #
# # 		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: Amanhá é dia 10
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
# # 				         + ' ' + Valor + ' ' + Circunstância + '.'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.:dia 10 é Amanhá
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '.'
# #
# #
# # 		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = circunstância()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: A feira dura o dia
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '.'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()  ## reiterações-verbo na passiva
# # 				print('Qual o Valor(Value)?')
# # 				Valor = circunstância()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# #
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: O dia inteiro é ocupado pela feira
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '.'
# #
# # 	##ORAÇÃO EXISTENCIAL
# #
# # 	elif Transitividade == 'PR_Existencial_AG_NA' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# # 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Existente?')
# # 		Existente = estrutura_GN()
# # 		Circunstância = circunstância()
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Processo + ' ' + Existente + ' ' + Circunstância + '.'
# #
# # 	#
# # 	##
# # 	###
# # 	######
# # 	####### ORAÇÕES INTERROGATIVAS POLARES
# #
# # 	##ORAÇÃO MATERIAL MODO INTERROGATIVO POLAR
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		print('Qual é a Meta?')
# # 		Meta = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 		else:
# # 			Iniciador = ''
# #
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()
# #
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# #
# # 			print('há Resultado_elaboração atributo ou papel?')
# # 			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# # 			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# # 					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# # 				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
# # 				if realizacao_atributo == 'adjetivo':
# # 					Atributo = adjetivo_modificador()
# # 				elif realizacao_atributo == 'frase_preposicional':
# # 					Atributo = frase_preposicional()
# # 			elif RESULTADO_QUALITATIVO == '-resultado':
# # 				Atributo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '?'
# #
# #
# #
# # 		elif TIPO_DE_RESULTADO == 'extensão':
# # 			print('Há Participante Beneficiário na oração?')
# # 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# # 			if RECEPÇÃO == '+beneficiário':
# # 				Beneficiário = frase_preposicional()
# # 			elif RECEPÇÃO == '-beneficiário':
# # 				Beneficiário = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '?'
# #
# #
# # 	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		print('Qual é a Meta?')
# # 		Meta = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN()
# # 		else:
# # 			Iniciador = ''
# #
# # 		print(
# # 			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# # 		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()
# #
# # 		if CLIENTE == '+cliente':
# # 			Cliente = frase_preposicional()
# # 		else:
# # 			Cliente = ''
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 		         + ' ' + Processo + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '?'
# #
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()
# # 		else:
# # 			Iniciador = ''
# #
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# # 			print('Qual é o Escopo?')
# # 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# # 			if tipo_Escopo == 'escopo(processo)':
# # 				Escopo = estrutura_GN()
# # 			elif tipo_Escopo == 'escopo(entidade)':
# # 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Escopo + ' ' + Circunstância + '?'
# #
# # 		elif TIPO_DE_RESULTADO == 'intensificação':
# # 			print('Qual é o Escopo?')
# # 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# # 			if tipo_Escopo == 'escopo(processo)':
# # 				Escopo = estrutura_GN()
# # 			elif tipo_Escopo == 'escopo(entidade)':
# # 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# # 			print('Há resultado locativo?')
# # 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# # 			if realizacao_locativo == 'sim':
# # 				Resultado_locativo = frase_preposicional()
# # 			else:
# # 				Resultado_locativo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'
# #
# #
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# # 		print('Há resultado do processo?')
# # 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# # 		if TIPO_DE_RESULTADO == 'elaboração':
# # 			print('Orações médio_sem_alcance  selecionam -escopo')
# # 			Escopo = ''
# #
# # 		elif TIPO_DE_RESULTADO == 'intensificação':
# # 			print('Orações médio_sem_alcance selecionam -escopo')
# #
# # 			print('Há resultado locativo?')
# # 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# # 			if realizacao_locativo == 'sim':
# # 				Resultado_locativo = frase_preposicional()
# # 			else:
# # 				Resultado_locativo = ''
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'
# #
# #
# # 	##ORAÇÃO METEOROLÓGICA MODO INTERROGATIVO POLAR
# # 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
# # 			and Modo == 'sujeitabilidade_recuperação_NA_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
# # 		print('Qual o tipo_pessoa de inTransitividade?')
# # 		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
# # 			print('Há escopo?')
# # 			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
# # 			if escopo_intransitiva == '+escopo':
# # 				print('Qual estrutura realiza o escopo?')
# # 				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
# # 				if realizacao_escopo == 'frase_preposicional':
# # 					Escopo = frase_preposicional()
# # 				elif realizacao_escopo == 'grupo_nominal':
# # 					Escopo = estrutura_GN()
# # 			elif escopo_intransitiva == '-escopo':
# # 				Escopo = ''
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# #
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN()
# # 		else:
# # 			Iniciador = ''
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
# # 		         + ' ' + Escopo + ' ' + Circunstância + '?'
# #
# #
# # 	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Ator?')
# # 		Ator = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# # 		print('Há Participante Iniciador na oração?')
# # 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# # 		if INICIADOR == '+iniciador':
# # 			Iniciador = estrutura_GN() + grupo_verbal()
# # 		else:
# # 			Iniciador = ''
# #
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# # 		         + ' ' + Processo + ' ' + Circunstância + '?'
# #
# # 		##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)
# #
# # 	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
# # 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
# # 	#          and Tema_id == 'TID_complemento_elemental':
# # 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# # 	#      Tema_textual=TEMA_TEXTUAL()
# # 	#
# # 	#      print ('Qual o Processo?')
# # 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# # 	#      print('Qual é a Meta?')
# # 	#      Meta = estrutura_GN()
# # 	#      Polaridade = POLARIDADE ()
# # 	#      Circunstância = circunstância()
# # 	#      print ('Há Participante Iniciador na oração?')
# # 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# # 	#      if INICIADOR == '+iniciador':
# # 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 	#      else:
# # 	#          Iniciador = ''
# # 	#
# # 	#      print ('O Ator/Agente é realizado na oração?')
# # 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# # 	#      if realizacao_Ator == '+ator/agente':
# # 	#          print('Qual é o Ator/Agente?')
# # 	#          Ator = frase_preposicional()
# # 	#      elif realizacao_Ator == '-ator/agente':
# # 	#          Ator = ''
# # 	#
# # 	#
# # 	#      print ('Há resultado do processo?')
# # 	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
# # 	#
# # 	#      if TIPO_DE_RESULTADO == 'elaboração':
# # 	#
# # 	#          print ('há Resultado_elaboração atributo ou papel?')
# # 	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# # 	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# # 	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# # 	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
# # 	#              if realizacao_atributo == 'adjetivo':
# # 	#                  Atributo = adjetivo_modificador ()
# # 	#              elif realizacao_atributo == 'frase_preposicional':
# # 	#                  Atributo = frase_preposicional()
# # 	#          elif RESULTADO_QUALITATIVO == '-resultado':
# # 	#              Atributo = ''
# # 	#
# # 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta \
# # 	#                   + ' ' + Polaridade + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' + Circunstância +'?'
# # 	#
# # 	#      elif TIPO_DE_RESULTADO == 'extensão':
# # 	#          print ('Há Participante Beneficiário na oração?')
# # 	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
# # 	#          if RECEPÇÃO == '+beneficiário':
# # 	#              Beneficiário = frase_preposicional()
# # 	#          elif RECEPÇÃO == '-beneficiário':
# # 	#              Beneficiário = ''
# # 	#
# # 	#
# # 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
# # 	#                   + Meta + ' ' + Polaridade + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +' ' + Circunstância +'?'
# # 	#
# # 	# ##
# # 	#
# # 	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
# # 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
# # 	#          and Tema_id == 'TID_complemento_elemental':
# # 	#
# # 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# # 	#      Tema_textual=TEMA_TEXTUAL()
# # 	#
# # 	#      print ('Qual o Processo?')
# # 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# # 	#      print('Qual é a Meta?')
# # 	#      Meta = estrutura_GN()
# # 	#      Polaridade = POLARIDADE ()
# # 	#      Circunstância = circunstância()
# # 	#
# # 	#      print ('Há Participante Iniciador na oração?')
# # 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# # 	#      if INICIADOR == '+iniciador':
# # 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# # 	#      else:
# # 	#          Iniciador = ''
# # 	#
# # 	#      print ('O Ator/Agente é realizado na oração?')
# # 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# # 	#      if realizacao_Ator == '+ator/agente':
# # 	#          print('Qual é o Ator/Agente?')
# # 	#          Ator = frase_preposicional()
# # 	#      elif realizacao_Ator == '-ator/agente':
# # 	#          Ator = ''
# # 	#
# # 	#
# # 	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# # 	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
# # 	#
# # 	#      if CLIENTE == '+cliente':
# # 	#          Cliente = frase_preposicional()
# # 	#      elif CLIENTE == '-cliente':
# # 	#          Cliente=''
# # 	#
# # 	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' '\
# # 	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Circunstância +'?'
# # 	#
# #
# # 	###RELACIONAl MODO INTERROGATIVO POLAR
# #
# # 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
# # 		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
# # 		Tema_textual = TEMA_TEXTUAL()
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 		print('Qual o tipo_pessoa de especificação de associação?')
# # 		tipo_especificação_associação = choice.Menu(['entidade', 'qualidade']).ask()
# # 		print('Qual a fase da atribuição?')
# # 		fase_atribuição = choice.Menu(['neutra',
# # 		                               'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
# # 		###não vou especializar os tipos de fase.
# # 		print('Qual o domínio da atribuição')
# # 		domínio_atribuição = choice.Menu(['material', 'semiótico']).ask()
# #
# # 		if (
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstância + '?'
# #
# # 		elif (
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
# # 				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = adjetivo_modificador()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
# # 			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
# # 			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstância + '?'
# #
# #
# # 	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
# # 	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
# # 	####para desenvolver....
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Atribuidor?')
# # 			Atribuidor = estrutura_GN()
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstância + '?'
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Atribuidor?')
# # 			Atribuidor = frase_preposicional()
# #
# # 			print('Qual o Portador?')
# # 			Portador = estrutura_GN()
# # 			print('Qual o Atributo?')
# # 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
# #
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstância + '?'
# #
# #
# # 	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação':
# # 		print('Apesar de Médio(middle), a direcionalidade_voz '
# # 		      'do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina '
# # 		      'se é operativa ou receptiva. Selecione a direcionalidade:')
# # 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 		if direcionalidade_voz == 'meio_operativa':
# # 			print('Neste caso, o Símbolo/Identificado conflui com o '
# # 			      'Sujeito(geralmente o elemento em posição temática')
# #
# # 			# (confluência do Símbolo/Identificado) =
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'
# #
# #
# #
# # 		elif direcionalidade_voz == 'meio_receptiva':
# # 			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
# # 			##NESTE CASO, confluência de Valor/Sujeito
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'
# #
# #
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação':
# #
# # 		print(
# # 			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 		if direcionalidade_voz == 'meio_operativa':
# # 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
# #
# # 			# (confluência do Símbolo/Identificador/Sujeito) =
# # 			# (Valor/Identificado/complemento)
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'
# #
# # 		elif direcionalidade_voz == 'meio_receptiva':
# # 			print('Neste caso, o Valor conflui com o Sujeito')
# # 			##NESTE CASO, confluência de Valor/Identificado/Sujeito
# # 			##(Símbolo/Identificador/Complemento)
# #
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'
# #
# #
# # 	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
# #
# # 	#    ###TRUE_Efetiva_operativa
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Designador?')
# # 			Designador = estrutura_GN()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()  ##ou frase preposicional?
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstância + '?'
# # 			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)
# #
# # 	###TRUE_Efetiva_receptiva
# #
# # 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de atribuição de relação?')
# # 		tipo_atribuição_relação = atribuição_de_relação()
# # 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# # 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# # 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
# #
# # 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# # 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# # 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# # 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# # 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual é o Designador?')
# # 			Designador = frase_preposicional()
# # 			print('Qual é o Símbolo(Token)?')
# # 			Símbolo = estrutura_GN()
# # 			print('Qual o Valor(Value)?')
# # 			Valor = estrutura_GN()  ##ou frase preposicional?
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# # 			#
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstância + '?'
# # 	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
# # 	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
# #
# # 	# POSSESSIVO ATRIBUTIV0
# #
# # 	elif Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()
# #
# # 		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':
# #
# # 			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
# #
# # 			if realizacao_atributo == 'grupo_nominal_possessivo':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Posse?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Possuidor?')
# # 				Atributo_Possuidor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse \
# # 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'
# #
# # 			elif realizacao_atributo == 'frase_preposicional':
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Posse?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Possuidor?')
# # 				Atributo_Possuidor = frase_preposicional()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'
# #
# #
# # 		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
# #
# # 			##VERBO TER/POSSUIR/
# #
# # 			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()
# #
# # 			if tipo_possuidor == 'possuidor_portador':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Possuidor?')
# # 				Portador_Possuidor = estrutura_GN()
# # 				print('Qual é o Atributo/Posse?')
# # 				Atributo_Posse = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor \
# # 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstância + '?'
# # 			###VERBOS PERTENCER A/...
# #
# # 			elif tipo_possuidor == 'possuidor_atributo':
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual o Portador/Possuidor?')
# # 				Portador_Posse = estrutura_GN()
# # 				print('Qual é o Atributo/Posse?')
# # 				Atributo_Possuidor = frase_preposicional()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'
# #
# # 		# POSSESSIVO IDENTIFICATIVO
# #
# #
# # 	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()
# #
# # 		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
# #
# # 				print(
# # 					'Escolha o tipo_pessoa de realizacao do Valor:')
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)/Possuído?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)/Possuidor?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O piano é seu
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '?'
# #
# # 				elif realizacao_Valor == 'frase_preposicional':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)?')
# # 					Valor_Possuidor = frase_preposicional()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O piano é do André
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '?'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
# #
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)/Possuído?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)/Possuidor?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O seu é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '?'
# #
# # 				elif realizacao_Valor == 'frase_preposicional':
# #
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()
# # 					print('Qual é o Símbolo(Token)?')
# # 					Símbolo_Possuído = estrutura_GN()
# # 					print('Qual o Valor(Value)?')
# # 					Valor_Possuidor = estrutura_GN()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O do André é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor \
# # 					         + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '?'
# #
# # 		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
# # 			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
# # 			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print(
# # 					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)/Possuidor?')
# # 				Símbolo_Possuidor = estrutura_GN()
# # 				print('Qual o Valor(Value)/Possuído?')
# # 				Valor_Possuído = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: O produto contém plástico, Eles merecem a aposentadoria
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor \
# # 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstância + '?'
# #
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
# #
# # 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
# #
# # 				if realizacao_Valor == 'grupo_nominal':
# # 					Tema_textual = TEMA_TEXTUAL()
# # 					Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 					print('Qual o Processo?')
# # 					Processo = grupo_verbal()  ##na passiva
# # 					print('Qual o Valor(Value)/Possuído?')
# # 					Valor_Possuído = estrutura_GN()
# # 					print('Qual é o Símbolo(Token)/Possuidor?')
# # 					Símbolo_Possuidor = frase_preposicional()
# # 					Polaridade = POLARIDADE()
# # 					Circunstância = circunstância()
# #
# # 					# Ex.: O seu é o piano
# # 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
# # 					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstância + '?'
# #
# #
# # 	#####RELACIONAL CIRCUNSTANCIAL MODO INTERROGATIVO POLAR
# #
# # 	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# # 		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
# # 		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
# #
# # 		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador')
# # 			Portador = estrutura_GN()
# # 			print('Qual é o Atributo Circunstancial?')
# # 			Atributo_Circunstancial = circunstância()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			# Ex.: O livro é sobre a IIGuerra
# #
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# # 			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstância + '?'
# #
# # 		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# # 			Tema_textual = TEMA_TEXTUAL()
# # 			Tema_interpessoal = TEMA_INTERPESSOAL()
# # 			print('Qual o Processo?')
# # 			Processo = grupo_verbal()
# # 			print('Qual o Portador')
# # 			Portador = estrutura_GN()
# # 			print('Qual é o Atributo Circunstancial?')
# # 			Atributo = estrutura_GN()
# # 			Polaridade = POLARIDADE()
# # 			Circunstância = circunstância()
# #
# # 			# Ex.: O livro retrata a IIGuerra
# # 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# # 			         + ' ' + Atributo + ' ' + Circunstância + '?'
# #
# #
# #
# #
# # 	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		print('O significado circunstancial é realixado no participante ou no processo?')
# # 		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
# # 			['participante_circunstancial', 'processo_circunstancial']).ask()
# #
# # 		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: Amanhá é dia 10
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = estrutura_GN()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.:dia 10 é Amanhá
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'
# #
# #
# # 		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# #
# # 			print(
# # 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# # 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
# #
# # 			if direcionalidade_voz == 'meio_operativa':
# # 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# # 				print('Qual o Valor(Value)?')
# # 				Valor = circunstância()
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# #
# # 				# Ex.: A feira dura o dia inteiro
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'
# #
# #
# # 			elif direcionalidade_voz == 'meio_receptiva':
# # 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
# #
# # 				Tema_textual = TEMA_TEXTUAL()
# # 				Tema_interpessoal = TEMA_INTERPESSOAL()
# #
# # 				print('Qual o Processo?')
# # 				Processo = grupo_verbal()  ## reiterações-verbo na passiva
# # 				print('Qual o Valor(Value)?')
# # 				Valor = circunstância()
# # 				print('Qual é o Símbolo(Token)?')
# # 				Símbolo = circunstância()
# #
# # 				Polaridade = POLARIDADE()
# # 				Circunstância = circunstância()
# # 				# Ex.: O dia todo é ocupado pela feira
# #
# # 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# # 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'
# #
# #
# # 	##ORAÇÃO EXISTENCIAL MODO INTERROGATIVO POLAR
# #
# # 	elif Transitividade == 'PR_Existencial_AG_NA' \
# # 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# # 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# #
# # 		Tema_interpessoal = TEMA_INTERPESSOAL()
# # 		Tema_textual = TEMA_TEXTUAL()
# #
# # 		print('Qual o Processo?')
# # 		Processo = grupo_verbal()
# # 		print('Qual é o Existente?')
# # 		Existente = estrutura_GN()
# # 		Polaridade = POLARIDADE()
# # 		Circunstância = circunstância()
# # 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Polaridade \
# # 		         + ' ' + Processo + ' ' + Existente + ' ' + Circunstância + '?'
# #
# # 	return (re.sub(' +', ' ', oração).strip().capitalize())
