import json

query = system.util.jsonEncode('Analise_risco/get_columns', params)
value = json.loads(query)

result = []
nprSTA = ''
nprLTA = ''

dateNow = system.date.now()

qua_access =	(self.session.custom.quaTeam or self.session.custom.quaLeader) or self.session.custom.ADM
lead_access =	self.session.custom.proLeader or self.session.custom.ADM

for count in value:

  if count['AprovLeadership'] and qua_access:
    qua_bool = True
  else:
    qua_bool = False

  if count['NPRSTA'] != None and lead_access:
    lead_bool = True
  else:
    lead_bool = False

#		Cálculo de prazo de preenchimento de STA e LTA

  startDate =			system.date.parse(count['Data'], 'dd/MM/yyyy')
  endDateSTA =		system.date.addHours(startDate, 24)
  endDateLTA =		system.date.addDays(startDate, 10)

  atrasoSTA =			system.date.isAfter(dateNow, endDateSTA)
  atrasoLTA =			system.date.isAfter(dateNow, endDateLTA)


#		Definição de cor para atrasados, pendentes e vazios

#		NPR STA
  if count['NPRSTA'] == None:
    if atrasoSTA: 
      nprSTA = '#FF234090'
    else:
      nprSTA = '#F1C21B90'
  else:
    nprSTA = '#00000000'

#		NPR LTA
  if count['NPRLTA'] == None:
    if atrasoLTA: 
      nprLTA = '#FF234090'
    else:
      nprLTA = '#F1C21B90'
  else:
    nprLTA = '#00000000'

  id = 		{ "value": count['id'],
          "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  date = 		{ "value": count['Data'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  workshop = 		{ "value": count['Workshop'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  area = 		{ "value": count['Area'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  function = 	{ "value": count['Funcao'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  component = { "value": count['Componente'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  defect = 		{ "value": count['Defeito'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  user = 		{ "value": count['User'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  npr = 		{ "value": count['NPR'],
             "style":{"borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  npr_sta = 	{ "value": count['NPRSTA'],
             "style":{"backgroundColor" : "{}".format(nprSTA),
             "borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  npr_lta = 	{ "value": count['NPRLTA'],
             "style":{"backgroundColor" : "{}".format(nprLTA),
             "borderBottomStyle": "none",
             "borderLeftStyle": "none",
             "borderRightColor": "#CDD1DB",
             "borderRightStyle": "solid",
             "borderRightWidth": 2,
             "borderTopStyle": "none"
        }
        }
  aprov_lead = { "value": count['AprovLeadership'],
            "editable":lead_bool,
            "style":{"borderBottomStyle": "none",
            "borderLeftStyle": "none",
            "borderRightColor": "#CDD1DB",
            "borderRightStyle": "solid",
            "borderRightWidth": 2,
            "borderTopStyle": "none"
        }
        }
  aprov_qua = { "value": count['AprovQuality'],
            "editable": qua_bool,
            "style":{"borderBottomStyle": "none",
            "borderLeftStyle": "none",
            "borderRightColor": "#CDD1DB",
            "borderRightStyle": "solid",
            "borderRightWidth": 2,
            "borderTopStyle": "none"
        }
        }

  result.append({'id':id, 'Data':date, 'Workshop':workshop, 'Area':area, 'Funcao':function, 'Componente':component, 'Defeito':defect, 'User':user,
  'NPR':npr, 'NPRSTA':npr_sta, 'NPRLTA':npr_lta, 'AprovLeadership':aprov_lead, 'AprovQuality':aprov_qua})

return result
