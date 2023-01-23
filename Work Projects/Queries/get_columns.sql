DECLARE @SELECT_QUERY INT
SET @SELECT_QUERY =  x


DECLARE @query VARCHAR(MAX)
SET @query = 'SELECT 
	FTL.id AS ID,
	FORMAT(TIME_RISK.date_full,''dd/MM/yyyy'') AS Date,
	MAP.workshop_name AS [Fabrica],
	MAP.departament AS [Area],
	MAP.sub_departament AS [Funcao],
	MAP.stretch AS Trecho,
	DOC.document_type AS [TipoDocumento], 
	RISK.document_number AS [NumDocumento],
	RISK.priority AS [Priorizacao],
	ITEM.description AS [Item],
	COMP.description AS [Componente],
	DETAIL.description AS [Detalhe],
	PLACE.description AS [Local],
	REQUI.description AS [Requisito],
	DEFECT.description AS [ModoFalha],
	EFFECT.description AS [Efeito],
	RISK.cause AS [Causa],
	AUD.description AS [CODAUD],
	CONTROLE.description AS [Controle],
	NPR.NPR AS NPR,
	NPR.NPR_STA AS [NPRSTA],
	NPR.NPR_LTA AS [NPRLTA],
	management.status_leadership AS aprovLid,
	management.status_freeze  AS cong,
	term_action. LTA_status  as StatusLTA

FROM fact_lake AS FTL

----------------dim_npr
LEFT JOIN [dbo].[dim_NPR] AS NPR
ON FTL.NPR_key = NPR.id

----------------dim_map
LEFT JOIN [dbo].[dim_map] AS MAP
ON FTL.map_key = MAP.id

----------------dim_risk
LEFT JOIN [dbo].[dim_risk] AS RISK
ON FTL.risk_key = RISK.id

----------------standard_detail
LEFT JOIN [dbo].[standard_detail] AS DETAIL
ON  RISK.detail_key = DETAIL.id

----------------standard_local
LEFT JOIN [dbo].[standard_local] AS PLACE
ON RISK.local_key = PLACE.id

----------------standard_requirement
LEFT JOIN [dbo].[standard_requirement] AS  REQUI
ON RISK.requeriment_key = REQUI.id

----------------standard_defect
LEFT JOIN [dbo].[standard_defect] AS DEFECT
ON RISK.defect_key = DEFECT.id

----------------standard_effect
LEFT JOIN [dbo].[standard_effect] AS EFFECT
ON RISK.effect_key = EFFECT.id

----------------standard_control
LEFT JOIN [dbo].[standard_control] AS CONTROLE
ON RISK.control_key = CONTROLE.id

----------------standard_cod_aud
LEFT JOIN [dbo].[standard_cod_aud] AS AUD
ON RISK.aud_cod_key = AUD.id

----------------standard_document_type
LEFT JOIN  standard_document_type  AS DOC
ON RISK.document_type_key = DOC.id 

----------------standard_component
LEFT JOIN [dbo].[standard_component] AS COMP
ON RISK.component_key = COMP.id

----------------standard_item
LEFT JOIN  [dbo].[standard_item] AS ITEM
ON COMP.item_key = ITEM.id

----------------dim_time
LEFT JOIN  [dbo].[dim_time] AS TIME_RISK
ON FTL.time_key = TIME_RISK.id

----------------dim_management
LEFT JOIN  [dbo].[dim_management] AS management
ON FTL.management_key = management.id

----------------dim_term_action
LEFT JOIN  [dbo].[dim_term_action] AS term_action
ON FTL.term_action_key  = term_action.id'


DECLARE @PESQUISA01 varchar(MAX)
SET @PESQUISA01 = CONCAT(@query, ' where ', :name01 ,' LIKE ',CHAR(39), '%', :val01 ,'%',CHAR(39),' ORDER BY FTL.id ')


DECLARE @PESQUISA02 varchar(MAX)
SET @PESQUISA02 = CONCAT(@query, ' where ', :name01 ,' LIKE ',CHAR(39), '%', :val01 ,'%',CHAR(39),' AND ',
:name02 ,' LIKE ',CHAR(39), '%', :val02 ,'%',CHAR(39),'ORDER BY FTL.id ')

DECLARE @PESQUISA03 varchar(MAX)
SET @PESQUISA03 = CONCAT(@query, ' where ', :name01 ,' LIKE ',CHAR(39), '%', :val01 ,'%',CHAR(39),' AND ',
:name02 ,' LIKE ',CHAR(39), '%', :val02 ,'%',CHAR(39), ' AND ',
:name03 ,' LIKE ',CHAR(39), '%', :val03 ,'%',CHAR(39),'ORDER BY FTL.id ')

DECLARE @PESQUISA04 varchar(MAX)
SET @PESQUISA04 = CONCAT(@query, ' where ', :name01 ,' LIKE ',CHAR(39), '%', :val01 ,'%',CHAR(39),' AND ',
:name02 ,' LIKE ',CHAR(39), '%', :val02 ,'%',CHAR(39), ' AND ',
:name03 ,' LIKE ',CHAR(39), '%', :val03 ,'%',CHAR(39), ' AND ',
:name04 ,' LIKE ',CHAR(39), '%', :val04 ,'%',CHAR(39),'ORDER BY FTL.id ')


DECLARE @PESQUISA05 varchar(MAX)
SET @PESQUISA05 = CONCAT(@query, ' where ', :name01 ,' LIKE ',CHAR(39), '%', :val01 ,'%',CHAR(39),' AND ',
:name02 ,' LIKE ',CHAR(39), '%', :val02 ,'%',CHAR(39), ' AND ',
:name03 ,' LIKE ',CHAR(39), '%', :val03 ,'%',CHAR(39), ' AND ',
:name04 ,' LIKE ',CHAR(39), '%', :val04 ,'%',CHAR(39), ' AND ',
:name05 ,' LIKE ',CHAR(39), '%', :val05 ,'%',CHAR(39),'ORDER BY FTL.id ')


DECLARE @RESULTADO varchar(MAX)
SET @RESULTADO = 
	(CASE
		WHEN @SELECT_QUERY = 0 THEN @query
		WHEN @SELECT_QUERY = 1 THEN @PESQUISA01
		WHEN @SELECT_QUERY = 2 THEN @PESQUISA02
		WHEN @SELECT_QUERY = 3 THEN @PESQUISA03
		WHEN @SELECT_QUERY = 4 THEN @PESQUISA04
		WHEN @SELECT_QUERY = 5 THEN @PESQUISA05
	END)

EXEC(@RESULTADO) 
