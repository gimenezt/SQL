import json

query = system.util.jsonEncode('Analise_risco/get_columns', params)
value = json.loads(query)
	
result =	[]
level =		[]

for i in range(1, 4):
   params = {"workshop_key": i}
   var = system.util.jsonEncode(system.db.runNamedQuery("Queries_Comuns/get_workshop_level", params))
   x = json.loads(var)

   level.append(x["rows"][0])

#	ARMAZENO OS VALORES DE NÍVEL BAIXO E NÍVEL MÉDIO DE CADA FÁBRICA 
#	SENDO : 01 = LMS, 02 = LMB, 03 = LMC

med_level_01 =   level[0][2]
low_level_01 =   level[0][1]

med_level_02 =   level[1][2]
low_level_02 =   level[1][1]

med_level_03 =   level[2][2]
low_level_03 =   level[2][1]

#----------------------------------------------------------------------------

for count in value:
        NPR = 		count['NPR']
        NPRSTA = 	count['NPRSTA']
        NPRLTA = 	count['NPRLTA']

#	REGRA DE NPR
#	NPR BAIXO: 	MENOR OU IGUAL A NPR BAIXO DEFINIDO POR USUÁRIO					>>	VERDE
#	NPR MÉDIO: 	MAIOR QUE NPR BAIXO E MENOR QUE NPR ALTO DEFINIDO POR USUÁRIO	>>	AMARELO
#	NPR ALTO: 	MAIOR OU IGUAL A NPR ALTO DEFINIDO POR USUÁRIO					>>	VERMELHO

#	CONDIÇÃO QUE PERSONALIZA COR DE NPR DE ACORDO COM REGRA DE NPR DE CADA FÁBRICA

        if count['Fabrica'] == 'LMS':
                wkey = 1

        elif count['Fabrica'] == 'LMB':
                wkey = 2

        else:
                wkey = 3


        baixo = eval('low_level_0{}'.format(wkey))
        medio = eval('med_level_0{}'.format(wkey))

        if NPR == None:
                corNPR = '#00000000'
        elif NPR < baixo:
                corNPR = '#1DAB8B90'
        elif NPR > medio:
                corNPR = '#FF234090'
        else:
                corNPR = '#F1C21B90'


        if NPRSTA == None:
                corSTA = '#00000000'
        elif NPRSTA < baixo:
                corSTA = '#1DAB8B90'
        elif NPRSTA > medio:
                corSTA = '#FF234090'
        else:
                corSTA = '#F1C21B90'


        if NPRLTA == None:
                corLTA = '#00000000'
        elif NPRLTA < baixo:
                corLTA = '#1DAB8B90'
        elif NPRLTA > medio:
                corLTA = '#FF234090'
        else:
                corLTA = '#F1C21B90'


        id = 		{ "value": count['ID'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                                   "borderLeftStyle": "none",
                                   "borderRightColor": "#CDD1DB",
                                   "borderRightStyle": "solid",
                                   "borderRightWidth": 2,
                                   "borderTopStyle": "none"
                                }
                                }

        date = 		{ "value": count['Date'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                                   "borderLeftColor": "#CDD1DB",
                                   "borderLeftStyle": "none",
                                   "borderRightColor": "#CDD1DB",
                                   "borderRightStyle": "solid",
                                   "borderRightWidth": 2,
                                   "borderTopStyle": "none"}
                                }

        workshop =	{ "value": count['Fabrica'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                                   "borderLeftColor": "#CDD1DB",
                                   "borderLeftStyle": "none",
                                   "borderRightColor": "#CDD1DB",
                                   "borderRightStyle": "solid",
                                   "borderRightWidth": 2,
                                   "borderTopStyle": "none"}
                                }

        area = 		{ "value": count['Area'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                                  "borderLeftColor": "#CDD1DB",
                                  "borderLeftStyle": "none",
                                  "borderRightColor": "#CDD1DB",
                                  "borderRightStyle": "solid",
                                  "borderRightWidth": 2,
                                  "borderTopStyle": "none"}
                                }

        function =	{ "value": count['Funcao'],
                                 "style":{"backgroundColor" : "{}".format('#00000000'),
                                 "borderBottomStyle": "none",
			     	 "borderLeftColor": "#CDD1DB",
			     	 "borderLeftStyle": "none",
			    	 "borderRightColor": "#CDD1DB",
			    	 "borderRightStyle": "solid",
			   	 "borderRightWidth": 2,
			    	 "borderTopStyle": "none"}
                                }

        stretch =	{ "value": count['Trecho'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                             	  "borderLeftColor": "#CDD1DB",
                            	  "borderLeftStyle": "none",
                           	  "borderRightColor": "#CDD1DB",
                            	  "borderRightStyle": "solid",
                            	  "borderRightWidth": 2,
                            	  "borderTopStyle": "none"}
                                }

        doctype =	{ "value": count['TipoDocumento'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                             	  "borderLeftColor": "#CDD1DB",
                           	  "borderLeftStyle": "none",
                          	  "borderRightColor": "#CDD1DB",
                           	  "borderRightStyle": "solid",
                           	  "borderRightWidth": 2,
                           	  "borderTopStyle": "none"}
                                }

        docnum =	{ "value": count['NumDocumento'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        priority =	{ "value": count['Priorizacao'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                           	  "borderLeftColor": "#CDD1DB",
                            	  "borderLeftStyle": "none",
                           	  "borderRightColor": "#CDD1DB",
                           	  "borderRightStyle": "solid",
                            	  "borderRightWidth": 2,
                            	  "borderTopStyle": "none"}
                                  }

        item = 		{ "value": count['Item'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                         	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        comp = 		{ "value": count['Componente'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        detail = 	{ "value": count['Detalhe'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                                  "borderBottomStyle": "none",
                                  "borderLeftColor": "#CDD1DB",
                                  "borderLeftStyle": "none",
                                  "borderRightColor": "#CDD1DB",
                                  "borderRightStyle": "solid",
                                  "borderRightWidth": 2,
                                  "borderTopStyle": "none"}
                                }

        local = 	{ "value": count['Local'],
                                  "style":{ "backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                       		  "borderTopStyle": "none"}
                                }

        requir = 	{ "value": count['Requisito'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                         	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                       		  "borderRightColor": "#CDD1DB",
                       		  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        defect =	{ "value": count['ModoFalha'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                       		  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        effect = 	{ "value": count['Efeito'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        cause = 	{ "value": count['Causa'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                        	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                        	  "borderTopStyle": "none"}
                                }

        cod_aud =	{ "value": count['CODAUD'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "none",
                        	  "borderRightColor": "#CDD1DB",
                       	 	  "borderRightStyle": "solid",
                        	  "borderRightWidth": 2,
                       		  "borderTopStyle": "none"}
                                }

        control = 	{ "value": count['Controle'],
                                  "style":{"backgroundColor" : "{}".format('#00000000'),
                       		  "borderBottomStyle": "none",
                        	  "borderLeftStyle": "none",
                        	  "borderRightStyle": "none",
                        	  "borderTopStyle": "none"}
                                }

        npr = 		{ "value": count['NPR'],
                                  "style":{"backgroundColor" : "{}".format(corNPR),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "solid",
                        	  "borderLeftWidth": 1.5,
                        	  "borderRightStyle": "none",
                        	  "borderTopStyle": "none"}
                                }

        nprsta = 	{ "value": count['NPRSTA'],
                                  "style":{"backgroundColor" : "{}".format(corSTA),
                        	  "borderBottomStyle": "none",
                        	  "borderLeftColor": "#CDD1DB",
                        	  "borderLeftStyle": "solid",
                        	  "borderLeftWidth": 1.5,
                        	  "borderRightStyle": "none",
                       	 	  "borderTopStyle": "none"}
                                }

        nprlta = 	{ "value": count['NPRLTA'],
                                  "style":{"backgroundColor" : "{}".format(corLTA),
                       		  "borderBottomStyle": "none",
                       		  "borderLeftColor": "#CDD1DB",
                       		  "borderLeftStyle": "solid",
                        	  "borderLeftWidth": 1.5,
                        	  "borderRightStyle": "none",
                        	  "borderTopStyle": "none"}
                                }

        aprovlid =  { "value": count['aprovLid'],
                                  "style":{"backgroundColor" : "{}".format('#00000000')}}

        cong = 		{"value": count['cong'],
                                  "style":{"backgroundColor" : "{}".format('#00000000')}}

        statuslta =	{"value": count['StatusLTA'],
                                  "style":{"backgroundColor" : "{}".format('#00000000')}}

        result.append({'ID':id, 'Date':date, 'Fabrica': workshop, 'Area': area, 'Funcao':function, 'Trecho':stretch, 'TipoDocumento':doctype,
                                'NumDocumento':docnum, 'Priorizacao':priority, 'Item': item, 'Componente': comp, 'Detalhe':detail,
                                'Local':local, 'Requisito':requir,  'ModoFalha':defect, 'Efeito':effect, 'Causa':cause, 'CODAUD':cod_aud,
                                'Controle':control, 'NPR':npr, 'NPRSTA':nprsta, 'NPRLTA': nprlta, 'aprovLid':aprovlid, 'cong':cong, 'StatusLTA':statuslta})

return result
