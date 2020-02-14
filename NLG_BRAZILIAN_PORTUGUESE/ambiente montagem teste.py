print('Selecione a finitude:')
FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
print('Há a seleção de  tempo secundário')
TEMPO_SECUNDÁRIO = choice.Menu(['-', '1_reiteração', '2_reiterações', '3_reiterações', '4_reiterações']).ask()
print('Qual o aspecto verbal?')
ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
print('Qual a dêixis temporal?')
DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
print('Qual a dêixis modal?')
DÊIXIS_MODAL = choice.Menu(['modalizado_modulação', 'modalizado_modalização', 'não-modalizado']).ask()


def grupo_verbal_teste():
    '''()->str

    Retorna a estrutura que realiza o grupo verbal
    >>>grupo_verbal()
    'ando'
    >>>grupo_verbal()
    'estou andando'
    >>>grupo_verbal()
    'andava'
    '''
    print ('Qual o tipo de evento desejado?')
    TIPO_DE_EVENTO = choice.Menu(['Ser','Fazer','Sentir']).ask()

    if TIPO_DE_EVENTO == 'Ser' or TIPO_DE_EVENTO == 'Fazer' or TIPO_DE_EVENTO == 'Sentir':
        print ('Selecione um lema que realize o tipo de evento desejado:')
        print('Qual a agência do GV?')
        AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado']).ask()
        print('Há a seleção de  tempo secundário')
        TEMPO_SECUNDÁRIO = choice.Menu(['-', '1_reiteração', '2_reiterações', '3_reiterações', '4_reiterações']).ask()

        if (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '-' or
                AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '-'):
            print ('Dêixis modal = não_modalizada')
            print('Selecione a finitude')
            FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()

            if FINITUDE == 'finito':
                print('Qual a dêixis temporal?')
                DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()

                if ASPECTO == 'perfectivo' and DÊIXIS_TEMPORAL == 'presente':
                    print('Selecione morfologia de presente e aspecto perfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                elif ASPECTO == 'perfectivo' and DÊIXIS_TEMPORAL == 'passado':
                    print('Selecione morfologia de pretérito e aspecto perfectivo:')##este
                    # casso curioso, não sei se possível
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                elif ASPECTO == 'perfectivo' and DÊIXIS_TEMPORAL == 'futuro':
                    print('Selecione morfologia de pretérito e aspecto perfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                elif ASPECTO == 'imperfectivo' and DÊIXIS_TEMPORAL == 'presente':
                    print('Selecione morfologia de presente e aspecto imperfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                elif ASPECTO == 'perfectivo' and DÊIXIS_TEMPORAL == 'passado':
                    print('Selecione morfologia de pretérito e aspecto imperfectivo:')##este
                    # casso curioso, não sei se possível
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                elif ASPECTO == 'perfectivo' and DÊIXIS_TEMPORAL == 'futuro':
                    print('Selecione morfologia de pretérito e aspecto imperfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()

###
######
#########PAREI A INSPEÇÃO AQUI ,,REVISAR OS ABAIXO

            elif FINITUDE == 'não-finito':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_não_finito()
                else:
                    print('Selecione morfologia de imperfectivo:')
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_não_finito()

            elif FINITUDE == 'não-orientado':
                grupo_verbal = formação_verbo_não_orientado()

        elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '1_reiteração'
              or AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '1_reiteração'):
            print('Selecione a finitude')
            FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
            print('Qual a dêixis modal?')
            DÊIXIS_MODAL = choice.Menu(['modalizado_modulação', 'modalizado_modalização', 'não-modalizado']).ask()

            if FINITUDE == 'finito' and DÊIXIS_MODAL == 'não-modalizado':
                print('Qual a dêixis temporal?')
                DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()

                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia do perfectivo:')
                    grupo_verbal = verbo_geral2() + ' ' + verbo_geral2()
                else:
                    print('Selecione morfologia do imperfectivo:')
                    grupo_verbal = verbo_geral2() + ' ' + verbo_geral2()

            elif FINITUDE == 'não-finito' and DÊIXIS_MODAL == 'não-modalizado':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    grupo_verbal = grupo_verbal = verbo_geral2() + ' ' + verbo_geral2()
                else:
                    print('Selecione morfologia de imperfectivo:')
                    grupo_verbal = verbo_geral2() + ' ' + verbo_geral2()
    return grupo_verbal
        ####

        elif AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '1_reiteração':
            print('Selecione a finitude')
            FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
            print('Qual o verbo auxiliar de agência passiva desejado?')
            auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()

            if auxiliar_da_passiva == 'ser' and FINITUDE == 'finito':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_ser_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
                else:
                    print('Selecione morfologia de imperfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_ser_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical


            elif auxiliar_da_passiva == 'estar' and FINITUDE == 'finito':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_estar_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
                else:
                    print('Selecione morfologia de imperfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_estar_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical

            elif auxiliar_da_passiva == 'ser' and FINITUDE == 'não-finito':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_ser_não_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
                else:
                    print('Selecione morfologia de imperfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_ser_não_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical


            elif auxiliar_da_passiva == 'estar' and FINITUDE == 'finito':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_estar_não_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
                else:
                    print('Selecione morfologia de imperfectivo:')
                    verbo_auxiliar_da_passiva = formação_verbo_estar_não_finito()
                    verbo_lexical = formação_verbo_particípio()
                    grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
            ###########################################################################



    elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '2_reiterações' or
      AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '2_reiteração'):\
    print('Selecione a finitude')
    FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
    print('Qual a dêixis modal?')
    DÊIXIS_MODAL = choice.Menu(['modalizado_modulação', 'modalizado_modalização', 'não-modalizado']).ask()
    if FINITUDE == 'finito' and DÊIXIS_MODAL == 'não-modalizado':
        print('Qual a dêixis temporal?')
        DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()

        print('Qual o aspecto verbal?')
        ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()

        if ASPECTO == 'perfectivo':
            print('Selecione morfologia do perfectivo:')
            grupo_verbal = formação_da_estrutura_do_verbo_auxiliar () + ' ' + formação_da_estrutura_do_verbo_auxiliar () + ' ' + formação_da_estrutura_do_verbo_lexical ()

        else:
            print('Selecione morfologia do imperfectivo:')
            grupo_verbal = formação_da_estrutura_do_verbo_auxiliar () + ' ' + formação_da_estrutura_do_verbo_auxiliar () + ' ' + formação_da_estrutura_do_verbo_lexical ()

    elif FINITUDE == 'finito' and DÊIXIS_MODAL == 'modalizado':
        print('Qual a dêixis temporal?')
        DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
        print('Qual o aspecto verbal?')
        ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()

        if ASPECTO == 'perfectivo':
            print('Selecione morfologia do perfectivo:')
            grupo_verbal = formação_da_estrutura_do_verbo_auxiliar() + ' ' + formação_da_estrutura_do_verbo_auxiliar() + ' ' + formação_da_estrutura_do_verbo_lexical()

        else:
            print('Selecione morfologia do imperfectivo:')
            grupo_verbal = formação_da_estrutura_do_verbo_auxiliar() + ' ' + formação_da_estrutura_do_verbo_auxiliar() + ' ' + formação_da_estrutura_do_verbo_lexical()











        elif (AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '2_reiterações':

            verbo1 = verbo_geral2()
            verbos_passiva = realização_de_AGÊNCIA_passiva()

            grupo_verbal = verbo1 + ' ' + verbos_passiva


        elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '3_reiterações' or
              AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '3_reiteração'):
            grupo_verbal = verbo_geral2() + ' ' + verbo_geral2() + ' ' + verbo_geral2()

        elif AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '3_reiterações':

            verbo1 = verbo_geral2()
            verbo2 = verbo_geral2()
            verbos_passiva = realização_de_AGÊNCIA_passiva()

            grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbos_passiva

        elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '4_reiterações' or
              AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '4_reiteração'):
            grupo_verbal = verbo_geral2() + ' ' + verbo_geral2() + ' ' + verbo_geral2()

        elif AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '4_reiterações':

            verbo1 = verbo_geral2()
            verbo2 = verbo_geral2()
            verbo3 = verbo_geral2()
            verbos_passiva = realização_de_AGÊNCIA_passiva()

            grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva

    ######

    return grupo_verbal


###A FAZER : CONTINUAR A ORAÇÃO mental
## REVER OS PARÂMETROS PASSADAS A CADA UMA DAS FUNÇÕES PARA PODER USAR O JSON
## VER SE VAI PRECISAR SEPARAR AS ORAÇÕES POR TIPO PARA PODER ESTABELECER OS PARÂMETROS PRA CADA
	#UMA DELAS




def ler_json2(json_test):
    
    a = json.load (open('json_test_func.json'))
    return grupo_verbal(a['AGENCIA'], a['TEMPO_SECUNDARIO'], a['FINITUDE'], a['verbo_lematizado'])
	
#





def oraçãoMental():
	'''
	'''
	Transitividade = TRANSITIVIDADE()
	Modo = MODO()
	Tema_id = TEMA_IDEACIONAL()
	Tema_interpessoal = TEMA_INTERPESSOAL()
	Tema_textual=TEMA_TEXTUAL()
	
	if Transitividade == 'PR_Mental_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		print ('Selecione o tipo de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
	    
		if TIPO_DE_PROCESSO == 'superior':
			TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
			print ('Qual o Experienciador (Ente:Humanizado)?')
			Experienciador = estrutura_GN()
		else:
			TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
			print ('Qual o Experienciador (Ente:Animalizado☺)?')
			Experienciador = estrutura_GN()
			 
		print ('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE ()
	    
		print ('Em orações mentais médio sem alcance, a Fenomenalização seleciona especificamente a Não-fenomenalização:comportamento_passivo')
		
		oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Experienciador  + ' ' + Polaridade + ' ' + Processo + '.'
    
	
		
		
			
	
	    
	
	
	
	
	
	
	
	elif Transitividade == 'PR_Mental_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		
		
		print ('Selecione o tipo de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
	    
		if TIPO_DE_PROCESSO == 'superior':
			TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
			print ('Qual o Experienciador (Ente:Humanizado)?')
			Experienciador = estrutura_GN()
		else:
			TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
			print ('Qual o Experienciador (Ente:Animalizado☺)?')
			Experienciador = estrutura_GN()
			 
		print ('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE ()
        
		print ('Qual o tipo de Fenomenalizalção?')
		FENOMENALIZAÇÃO = choice.Menu(['fenomenalização', 'não-fenomenalização']).ask()
		if FENOMENALIZAÇÃO == 'fenomenalização':
			TIPO_fenomenalização = choice.Menu(['hiperfenômeno','fenômeno_simples']).ask()
			if TIPO_fenomenalização == 'hiperfenômeno':
				TIPO_hiperfenômeno = choice.Menu(['criativo','reativo']).ask()
                if TIPO_hiperfenômeno == 'criativo':
                    TIPO_criativo = choice.Menu(['pensamento','desejo']).ask()
                elif TIPO_hiperfenômeno == 'reativo':
                    TIPO_reativo = choice.Menu(['metafenômeno','macrofenômeno']).ask()
            elif TIPO_fenomenalização == 'fenômeno_simples':
                #ver qual a realização
		elif FENOMENALIZAÇÃO == 'não-fenomenalização':
			print ('Em caso de orações mentais médio com alcance e Não-fenomenalização seleciona-se a opção: assunto']).ask()
	        Assunto = frase_preposicional()
			
			oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Experienciador  + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'
	return oração
		
		
		if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
			TIPO_DE_COGNITIVO = choice.Menu (['pensar','saber','sonhar']).ask()
		
	    elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
			TIPO_DE_DESIDERATIVO = choice.Menu(['querer','esperar']).ask()
			
		elif TIPO_INFERIOR == 'emotivo' and TIPO_reativo == 'metafenômeno':
			TIPO_DE_EMOTIVO = choice.Menu(['gostar','agradar']).ask()
		
		
        
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
#		op
        TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
        if TIPO_DE_PROCESSO == 'superior':
            TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
        else:
            TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
            
        FENOMENALIZAÇÃO = choice.Menu(['fenomenalização', 'não-fenomenalização']).ask()
        if FENOMENALIZAÇÃO == 'fenomenalização':
            TIPO_fenomenalização = choice.Menu(['hiperfenômeno','fenômeno_simples']).ask()
            if TIPO_fenomenalização == 'hiperfenômeno':
                TIPO_hiperfenômeno = choice.Menu(['criativo','reativo']).ask()
                if TIPO_hiperfenômeno == 'criativo':
                    TIPO_criativo = choice.Menu(['pensamento','desejo']).ask()
                elif TIPO_hiperfenômeno == 'reativo':
                    TIPO_reativo = choice.Menu(['metafenômeno','macrofenômeno']).ask()
            elif TIPO_fenomenalização == 'fenômeno_simples':
                #ver qual a realização
		elif FENOMENALIZAÇÃO == 'não-fenomenalização':
			NÃO_FENOMENALIZAÇÃO = choice.Menu (['comportamento_passivo', 'assunto']).ask()
        
		
		
		if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
			TIPO_DE_COGNITIVO = choice.Menu (['pensar','saber','sonhar']).ask()
		
	    elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
			TIPO_DE_DESIDERATIVO = choice.Menu(['querer','esperar']).ask()
			
		elif TIPO_INFERIOR == 'emotivo' and TIPO_reativo == 'metafenômeno':
			TIPO_DE_EMOTIVO = choice.Menu(['gostar','agradar']).ask()


def oraçãoProjetada():
    oração = oraçãoGerada ()
    return oração

#
#
#
#
#
# substantivo_lematizado= 'professor'

substantivo_lematizado[-2:] == 'or'



def formação_da_estrutura_do_substantivo_comumteste ():
    '''(str, str)-str

    Retorna a realização de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.

    >>>formação_da_estrutura_do_substantivo_comum ()

    '''
    
  
    substantivo_lematizado = input ('Qual é o substantivo lematizado?')
    
    if substantivo_lematizado[-2:] == 'or':
        print ('Qual o gênero')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino']).ask()
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
        
            substantivo_comum = substantivo_lematizado

        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo   
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
    
    
    
    elif substantivo_lematizado[-2:] == 'al':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado

        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'ais'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
    elif substantivo_lematizado[-2:] == 'el':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'éis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

    elif substantivo_lematizado[-2:] == 'il':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'is'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
       
    
    elif substantivo_lematizado[-2:] == 'ol':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'óis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


    elif substantivo_lematizado[-2:] == 'ul':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'úis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

    else:
    
        print ('Qual o gênero')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino', 'não_binário']).ask()
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'o'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo   
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'os'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
        
    return substantivo_comum





def oraçãoGerada_teste():
    '''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática (oração) de uma figura específica
    da semãntica

    >>> oraçãoGerada()
    'eu bebi água'
    '''

    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()

    ##ORAÇÃO verbal

    if Transitividade == 'PR_Verbal_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('erro1')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Selecione a Receptividade')
        RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
        print('Qual a Ordem do Dizente?')
        ORDEM_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()

        if ORDEM_DO_DIZENTE == 'atividade':
            TIPO_ATIVIDADE = 'fala'

            if TIPO_ATIVIDADE == 'fala' and RECEPTIVIDADE == '-receptor':

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + '.'
                # Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...

            elif TIPO_ATIVIDADE == 'fala' and RECEPTIVIDADE == '+receptor':

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                print('Qual é o Receptor?')
                Receptor = frase_preposicional()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + '.'

                # Ex.: Eu conversei com você até anoitecer; Eu falei com você muito ontem; Nós discutimos com ela...



        elif ORDEM_DO_DIZENTE == 'semioticidade' and RECEPTIVIDADE == '+receptor':
            print('Selecione o tipo de Semioticidade')

            TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
            if TIPO_SEMIOTICIDADE == 'projeção':
                print('Selecione o tipo de projeção')
                TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()

                if TIPO_PROJEÇÃO == 'citativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()
                    print('Qual é o Receptor?')
                    Receptor = frase_preposicional()
                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oraçãoProjetada()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse a ele "Eu comi o bolo".

                elif TIPO_PROJEÇÃO == 'relativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()
                    print('Qual é o Receptor?')
                    Receptor = frase_preposicional()
                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oraçãoProjetada()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse a ele que "Eu comi o bolo".

        elif ORDEM_DO_DIZENTE == 'semioticidade' and RECEPTIVIDADE == '-receptor':
            print('Selecione o tipo de Semioticidade')

            TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
            if TIPO_SEMIOTICIDADE == 'projeção':
                print('Selecione o tipo de projeção')
                TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()

                if TIPO_PROJEÇÃO == 'citativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()

                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oraçãoProjetada()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse  "Eu comi o bolo".

                elif TIPO_PROJEÇÃO == 'relativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()

                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oração()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse que "Eu comi o bolo".



            elif TIPO_SEMIOTICIDADE == 'não_projeção':

                TIPO_NÃO_PROJEÇÃO = '-verbiagem'
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + '.'


    elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro2')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()
        TIPO_SEMIOTICIDADE = 'não_projeção'
        print('Selecione a Receptividade')
        RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()

        if RECEPTIVIDADE == '+receptor':
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Dizente?')
            Dizente = estrutura_GN()
            print('Qual é a Verbiagem?')
            Verbiagem = estrutura_GN()
            print('Qual é o Receptor?')
            Receptor = frase_preposicional()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Verbiagem + ' ' + Receptor + '.'



        else:
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Dizente?')
            Dizente = estrutura_GN()
            print('Qual é a Verbiagem?')
            Verbiagem = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Verbiagem + '.'



    elif  Transitividade == 'PR_Verbal_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro3iii')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        Polaridade = POLARIDADE()
        print('Qual é o Dizente?')
        Dizente = estrutura_GN()

        print('O Alvo é realizado por grupo nominal ou frase preposicional?')
        realização_alvo = choice.Menu(['GN', 'FP']).ask()
        if realização_alvo == 'GN':
            print('Qual é o Alvo?')
            Alvo = estrutura_GN()
            print('Qual a localização do alvo na oração (em relação ao Processo)?')
            localização_alvo = choice.Menu(['ante_processo', 'pós_processo']).ask()
            if localização_alvo == 'ante_processo':
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Alvo + ' ' + Processo + '.'
            else:
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Alvo + '.'


        else:
            print('Qual é o Alvo?')
            Alvo = frase_preposicional()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Alvo + '.'

    elif Transitividade == 'PR_Verbal_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro4')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        Polaridade = POLARIDADE()
        print('Qual é o Dizente?')
        Dizente = frase_preposicional()
        print('Qual é o Alvo?')
        Alvo = estrutura_GN()

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Alvo + ' ' + Polaridade + ' ' + Processo + ' ' + Dizente + '.'


    ###MATERIAL

    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro5')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()

        if TIPO_DE_RESULTADO == 'elaboração':

            print('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
                    RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta + ' ' + Atributo + '.'



        elif TIPO_DE_RESULTADO == 'extensão':
            print('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + '.'



    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        print('erro6')
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''

        print(
            'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        else:
            Cliente = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta + ' ' + Cliente + '.'


    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro7')
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Escopo + '.'

        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Escopo + ' ' + Resultado_locativo + '.'


    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro8')
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
            print('Orações médio_sem_alcance  selecionam -escopo')
            Escopo = ''

        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Orações médio_sem_alcance selecionam -escopo')

            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Resultado_locativo + '.'


    ##ORAÇÃO METEOROLÓGICA
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro9')
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
        print('Qual o tipo de inTransitividade?')
        if tipo_intransitiva == 'impessoal(fenômeno_natural)':
            print('Há escopo?')
            escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
            if escopo_intransitiva == '+escopo':
                print('Qual estrutura realiza o escopo?')
                realização_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
                if realização_escopo == 'frase_preposicional':
                    Escopo = frase_preposicional()
                elif realização_escopo == 'grupo_nominal':
                    Escopo = estrutura_GN()
            elif escopo_intransitiva == '-escopo':
                Escopo = ''

        print('Qual o Processo?')
        Processo = grupo_verbal()

        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo + ' ' + Escopo + '.'


    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + '.'

        ##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)

    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        print('erro10')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu(['+ator/agente', '-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()

        if TIPO_DE_RESULTADO == 'elaboração':

            print('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
                    RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + ' ' + Ator + '.'

        elif TIPO_DE_RESULTADO == 'extensão':
            print('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo + '  ' + Beneficiário + ' ' + Ator + '.'

    ##

    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        print('erro11')
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu(['+ator/agente', '-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''

        print(
            'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        elif CLIENTE == '-cliente':
            Cliente = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Cliente + ' ' + Ator + '.'


    ###RELACIONAl

    ###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        ####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
        ## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
        print('erro12')
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o tipo de especificação de associação?')
        tipo_especificação_associação = choice.Menu(['entidade', 'qualidade']).ask()
        print('Qual a fase da atribuição?')
        fase_atribuição = choice.Menu(['neutra',
                                       'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
        ###não vou especializar os tipos de fase.
        print('Qual o domínio da atribuição')
        domínio_atribuição = choice.Menu(['material', 'semiótico']).ask()

        if (
                tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
                tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
                tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
                tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Portador?')
            Portador = estrutura_GN()
            print('Qual o Atributo?')
            Atributo = estrutura_GN()

            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + '.'

        elif (
                tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
                tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
                tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
                tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Portador?')
            Portador = estrutura_GN()
            print('Qual o Atributo?')
            Atributo = adjetivo_modificador()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
            # o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
            ##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + '.'


    ###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
    ##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
    ####para desenvolver....
    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro13')
        print('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        # elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação == 'atribuição_proj_verbal',
            tipo_atribuição_relação == 'atribuição_expan_elaboração',
            tipo_atribuição_relação == 'atribuição_expan_intencificação'):
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Atribuidor?')
            Atribuidor = estrutura_GN()
            print('Qual o Portador?')
            Portador = estrutura_GN()
            print('Qual o Atributo?')
            Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Portador + ' ' + Atributo + '.'

    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro14')
        print('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        # elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO

        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação == 'atribuição_proj_verbal',
            tipo_atribuição_relação == 'atribuição_expan_elaboração',
            tipo_atribuição_relação == 'atribuição_expan_intencificação'):
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Atribuidor?')
            Atribuidor = frase_preposicional()

            print('Qual o Portador?')
            Portador = estrutura_GN()
            print('Qual o Atributo?')
            Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + ' ' + Atribuidor + '.'


    ####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)

    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação':

        print('erro15')
        print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito '
              'deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

        if direcionalidade_voz == 'meio_operativa':
            print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')

            # (confluência do Símbolo/Identificado) =

            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + '.'



        elif direcionalidade_voz == 'meio_receptiva':
            print('Neste caso, o Valor/Identificador conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Sujeito

            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo + '.'



    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação':
        print('erro16')
        print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

        if direcionalidade_voz == 'meio_operativa':
            print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')

            # (confluência do Símbolo/Identificador/Sujeito) =
            # (Valor/Identificado/complemento)

            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + '.'



        elif direcionalidade_voz == 'meio_receptiva':
            print('Neste caso, o Valor conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Identificado/Sujeito
            ##(Símbolo/Identificador/Complemento)

            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo + '.'

    ####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)

    #    ###TRUE_Efetiva_operativa
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro17')
        print('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        # elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        # POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação == 'atribuição_proj_verbal',
            tipo_atribuição_relação == 'atribuição_expan_elaboração',
            tipo_atribuição_relação == 'atribuição_expan_intencificação'):
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Designador?')
            Designador = estrutura_GN()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()  ##ou frase preposicional?
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + '.'
            ###rever possíveis estruturas para este tipo de oração(pode haver 2 processos?)

    ###TRUE_Efetiva_receptiva

    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro18')
        print('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        # elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação == 'atribuição_proj_verbal',
            tipo_atribuição_relação == 'atribuição_expan_elaboração',
            tipo_atribuição_relação == 'atribuição_expan_intencificação'):
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Designador?')
            Designador = frase_preposicional()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()  ##ou frase preposicional?
            Polaridade = POLARIDADE()
            #
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + ' ' + Designador + '.'
    ####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realização de cada participante;
    #        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)

    # POSSESSIVO ATRIBUTIV0

    elif Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro19')
        TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()

        if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':

            realização_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()

            if realização_atributo == 'grupo_nominal_possessivo':

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = estrutura_GN()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + '.'

            elif realização_atributo == 'frase_preposicional':
                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + '.'


        elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':

            ##VERBO TER/POSSUIR/

            tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()

            if tipo_possuidor == 'possuidor_portador':

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual o Portador/Possuidor?')
                Portador_Possuidor = estrutura_GN()
                print('Qual é o Atributo/Posse?')
                Atributo_Posse = estrutura_GN()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse + '.'


            ###VERBOS PERTENCER A/...

            elif tipo_possuidor == 'possuidor_atributo':

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual o Portador/Possuidor?')
                Portador_Posse = estrutura_GN()
                print('Qual é o Atributo/Posse?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + '.'

        # POSSESSIVO IDENTIFICATIVO


    elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro20')
        TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()

        if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':

            print(
                'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

            if direcionalidade_voz == 'meio_operativa':
                print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')

                print(
                    'Escolha o tipo de realização do Valor:')
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

                if realização_Valor == 'grupo_nominal':

                    Tema_textual = TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL()

                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE()

                    # Ex.: O piano é seu
                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor + '.'

                elif realização_Valor == 'frase_preposicional':

                    Tema_textual = TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL()

                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print('Qual o Valor(Value)?')
                    Valor_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE()

                    # Ex.: O piano é do André
                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor + '.'


            elif direcionalidade_voz == 'meio_receptiva':
                print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')

                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

                if realização_Valor == 'grupo_nominal':

                    Tema_textual = TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL()

                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE()

                    # Ex.: O seu é o piano
                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído + '.'

                elif realização_Valor == 'frase_preposicional':

                    Tema_textual = TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL()

                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print('Qual o Valor(Value)?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE()

                    # Ex.: O do André é o piano
                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído + '.'

        elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
            ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
            ##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS

            print(
                'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

            if direcionalidade_voz == 'meio_operativa':
                print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()

                print(
                    'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
                Processo = grupo_verbal()
                print('Qual é o Símbolo(Token)/Possuidor?')
                Símbolo_Possuidor = estrutura_GN()
                print('Qual o Valor(Value)/Possuído?')
                Valor_Possuído = estrutura_GN()
                Polaridade = POLARIDADE()

                # Ex.: O produto contém plástico, Eles merecem a aposentadoria

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído + '.'



            elif direcionalidade_voz == 'meio_receptiva':
                print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')

                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

                if realização_Valor == 'grupo_nominal':
                    Tema_textual = TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL()

                    print('Qual o Processo?')
                    Processo = grupo_verbal()  ##na passiva
                    print('Qual o Valor(Value)/Possuído?')
                    Valor_Possuído = estrutura_GN()
                    print('Qual é o Símbolo(Token)/Possuidor?')
                    Símbolo_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE()

                    # Ex.: O seu é o piano
                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuidor + '.'


    #####RELACIONAL CIRCUNSTANCIAL

    elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro21')
        print('Qual o tipo de realização da Relacional Circunstancial?')
        TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()

        if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Portador')
            Portador = estrutura_GN()
            print('Qual é o Atributo Circunstancial?')
            Atributo_Circunstancial = circunstância()
            Polaridade = POLARIDADE()

            # Ex.: O livro é sobre a IIGuerra

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Circunstancial + '.'

        elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual o Portador')
            Portador = estrutura_GN()
            print('Qual é o Atributo Circunstancial?')
            Atributo = estrutura_GN()
            Polaridade = POLARIDADE()

            # Ex.: O livro retrata a IIGuerra
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + '.'




    elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('erro22')
        print('O significado circunstancial é realixado no participante ou no processo?')
        TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
            ['participante_circunstancial', 'processo_circunstancial']).ask()

        if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':

            print(
                'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

            if direcionalidade_voz == 'meio_operativa':
                print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE()

                # Ex.: Amanhá é dia 10

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + '.'


            elif direcionalidade_voz == 'meio_receptiva':
                print('Neste caso, há confluência Valor/Sujeito/Identificado')

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE()

                # Ex.:dia 10 é Amanhá

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo + '.'


        elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':

            print(
                'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

            if direcionalidade_voz == 'meio_operativa':
                print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print('Qual o Valor(Value)?')
                Valor = circunstância()
                Polaridade = POLARIDADE()

                # Ex.: A feira dura o dia todo

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + '.'


            elif direcionalidade_voz == 'meio_receptiva':
                print('Neste caso, há confluência Valor/Sujeito/Identificado')

                Tema_textual = TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL()

                print('Qual o Processo?')
                Processo = grupo_verbal()  ## reiterações-verbo na passiva
                print('Qual o Valor(Value)?')
                Valor = circunstância()
                print('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()

                Polaridade = POLARIDADE()

                # Ex.: O dia todo é ocupado pela feira

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo + '.'
    return oração










































































































    