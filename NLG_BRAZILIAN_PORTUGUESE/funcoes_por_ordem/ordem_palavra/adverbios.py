# -*- coding: utf-8 -*-
# """

#
# @author: andre

from builtins import zip
import argparse


def adverbio_modo(indice=None):
    try:
        opcoes = ['bem', 'mal', 'assim', 'adrede',
                  'melhor', 'pior', 'depressa', 'devagar',
                  'acinte', 'debalde', 'cuidadosamente', 'calmamente',
                  'tristemente', 'alegremente', 'bondosamente',
                  'calmamente', 'discretamente', 'elegantemente', 'infelizmente',
                  'evidentemente']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


def adverbio_intensidade(indice=None):
    try:
        opcoes = ['muito', 'demais', 'todo', 'pouco',
                  'tão', 'quão', 'demasiado', 'bastante', 'imenso', 'demais',
                  'mais', 'menos', 'quanto', 'quase', 'tanto',
                  'assaz', 'tudo', 'nada']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


def adverbio_lugar(indice=None):
    try:
        opcoes = ['aí', 'aqui', 'acolá', 'cá',
                  'lá', 'ali', 'adiante', 'abaixo', 'embaixo',
                  'acima', 'adentro', 'dentro']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


def adverbio_tempo(indice=None):
    try:
        opcoes = ['ainda', 'agora',
                  'amanhã', 'à noite', 'anteontem',
                  'antes', 'à tarde', 'às vezes', 'atualmente',
                  'breve', 'cedo', 'depois', 'de manhã', 'de repente',
                  'de vez em quando', 'hoje', 'hoje em dia',
                  'já', 'logo', 'nunca', 'ontem', 'ora',
                  'outrora', 'quando', 'sempre', 'tarde', 'jamais']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


# adverbio_tempo(1)
def adverbio_negacao(indice=None):
    try:

        opcoes = ['não', 'nem', 'tampouco', 'nunca', 'jamais']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


def adverbio_relativo(indice=None):
    try:
        opcoes = ['de onde', 'quando', 'onde',
                  'de quando', 'que', 'por onde']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv

    except KeyError:
        return ''


def adverbio_afirmacao(indice=None):
    try:
        opcoes = ['sim', 'deveras',
                  'indubitavelmente', 'decididamente',
                  'certamente', 'realmente',
                  'decerto', 'certo',
                  'efetivamente']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv
    except KeyError:
        return ''


def adverbio_duvida(indice=None):
    try:
        opcoes = ['possivelmente', 'provavelmente',
                  'acaso', 'porventura',
                  'quiçá', 'será', 'talvez',
                  'casualmente']
        nums = [x for x in range(len(opcoes))]
        adverbios = dict(zip(nums, opcoes))
        adv = adverbios[indice]
        return adv

    except KeyError:
        return ''


def adverbio(tipo_de_adverbio, indice):
    adv = None
    try:
        if tipo_de_adverbio == 'Modo':
            adv = adverbio_modo(indice)

        elif tipo_de_adverbio == 'Intensidade':
            adv = adverbio_intensidade(indice)

        elif tipo_de_adverbio == 'Lugar':
            adv = adverbio_lugar(indice)

        elif tipo_de_adverbio == 'Tempo':
            adv = adverbio_tempo(indice)

        elif tipo_de_adverbio == 'Negação':
            adv = adverbio_negacao(indice)

        elif tipo_de_adverbio == 'Afirmação':
            adv = adverbio_afirmacao(indice)

        elif tipo_de_adverbio == 'Dúvida':
            adv = adverbio_duvida(indice)

        elif tipo_de_adverbio == 'Adv_relativo':
            adv = adverbio_relativo(indice)
        return adv
    except KeyError:
        return ''


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Retorna a realização de um advérbio, "
                                                 "dados o tipo e um índice")

    parser.add_argument('tipo_adv',  choices=['Modo', 'Intensidade', 'Lugar', 'Tempo', 'Negação',
                                                       'Afirmação', 'Dúvida', 'Adv_relativo'],
                        help=""" Opcoes de Tipos: ['Modo','Intensidade','Lugar', 'Tempo','Negação','Afirmação',
                        'Dúvida','Adv_relativo']""")

    parser.add_argument('indice_adv', type=int,
                        help="""SELECIONE UMA DAS OPÇÕES DOS ADVÉRBIOS POR MEIO DO ÍNDICE DO DICIONÁRIO 
                        Opções adv de Modo: {0: 'bem', 1: 'mal', 2: 'assim', 3: 'adrede', 4: 'melhor',
                        5: 'pior',
                        6: 'depressa', 7: 'devagar', 8: 'acinte', 9: 'debalde', 10: 'cuidadosamente', 11: 'calmamente',
                         12: 'tristemente', 13: 'alegremente', 14: 'bondosamente', 15: 'calmamente',
                         16: 'discretamente', 17: 'elegantemente', 18: 'infelizmente', 19: 'evidentemente'}

                         Opções adv de Intensidade: {0: 'muito', 1: 'demais', 2: 'todo', 3: 'pouco', 4: 'tão', 5: 'quão',
                          6: 'demasiado', 7: 'bastante', 8: 'imenso', 9: 'demais', 10: 'mais', 11: 'menos', 12: 'quanto',
                           13: 'quase', 14: 'tanto', 15: 'assaz', 16: 'tudo', 17: 'nada'}

                        Opções adv de Lugar: {0: 'aí', 1: 'aqui', 2: 'acolá', 3: 'cá', 4: 'lá', 5: 'ali', 6: 'adiante',
                          7: 'abaixo', 8: 'embaixo', 9: 'acima', 10: 'adentro', 11: 'dentro'}

                        Opções adv de Tempo: {0: 'ainda', 1: 'agora', 2: 'amanhã', 3: 'à noite', 4: 'anteontem',
                        5: 'antes', 6: 'à tarde', 7: 'às vezes', 8: 'atualmente', 9: 'breve', 10: 'cedo', 11: 'depois',
                        12: 'de manhã', 13: 'de repente', 14: 'de vez em quando', 15: 'hoje', 16: 'hoje em dia',
                        17: 'já', 18: 'logo', 19: 'nunca', 20: 'ontem', 21: 'ora', 22: 'outrora', 23: 'quando',
                        24: 'sempre', 25: 'tarde', 26: 'jamais'}

                        Opções adv de Negação: {0: 'não', 1: 'nem', 2: 'tampouco', 3: 'nunca', 4: 'jamais'}

                        Opções adv de Afirmação: {0: 'sim', 1: 'deveras', 2: 'indubitavelmente', 3: 'decididamente',
                        4: 'certamente', 5: 'realmente', 6: 'decerto', 7: 'certo', 8: 'efetivamente'}

                        Opções adv de Dúvida: {0: 'possivelmente', 1: 'provavelmente', 2: 'acaso', 3: 'porventura',
                        4: 'quiçá', 5: 'será', 6: 'talvez', 7: 'casualmente'}

                        Opções adv Relativo: {0: 'de onde', 1: 'quando', 2: 'onde', 3: 'de quando',
                        4: 'que', 5: 'por onde'}
                         """)

    args = parser.parse_args()

    print(adverbio(args.tipo_adv, args.indice_adv))
