SET LANGUAGE Portuguese

DECLARE @ID AS int
SET @ID = id

--------------------------------------- NPR

DECLARE @NPR_key AS int
SET @NPR_key = (SELECT NPR_key FROM [dbo].[fact_lake] WHERE id = @ID)

UPDATE dim_NPR
SET    NPR_severity = NPR_severity 
      ,NPR_occurrence = NPR_occurrence 
      ,NPR_detection = NPR_detection 
      ,NPR = NPR 
WHERE id = @NPR_key

--------------------------------------- MANAGEMENT

DECLARE @management_key AS int
SET @management_key = (SELECT management_key FROM [dbo].[fact_lake] WHERE id = @ID)

UPDATE dim_management
SET      last_edit_date = GETDATE()
	,last_edit_user = user 
WHERE id = @management_key

------------------------------------------ MAP

UPDATE fact_lake SET map_key =  station_description 
WHERE id =  @ID

------------------------------------------ RISK

DECLARE @risk_key AS int
SET @risk_key = (SELECT risk_key FROM [dbo].[fact_lake] WHERE id = @ID)

DECLARE @component_code AS int
SET @component_code = (SELECT component_code FROM [dbo].[standard_component] WHERE id = :component_key)

UPDATE dim_risk
SET    document_type_key =  document_type_key 
      ,document_number =  document_number 
      ,component_key = component_key
      ,component_code = @component_code
      ,detail_key =  detail_key 
      ,local_key =  local_key 
      ,element_name =  element_name 
      ,requeriment_key =  requeriment_key 
      ,defect_key =  defect_key 
      ,effect_key =  effect_key 
      ,cause =  cause 
      ,control_key =  control_key 
      ,code =  code 
      ,aud_cod_key =  aud_cod_key 
WHERE id = @risk_key
