SET LANGUAGE Portuguese

--------------------------------- DIM TIME

INSERT INTO dim_time VALUES (GETDATE()
                            ,DATENAME(day,GETDATE())
                            ,DATENAME(WEEKDAY,GETDATE())
                            ,DATEPART(MONTH, getdate())
                            ,DATENAME(MONTH, GETDATE())
                            ,DATENAME(YEAR, GETDATE())
                            ,DATENAME(quarter, GETDATE())
                            ,CASE WHEN DATEPART(quarter,GETDATE()) >= 3 THEN 2 ELSE 1 END);

DECLARE @id_dim_time int;
SET @id_dim_time = (SCOPE_IDENTITY());

------------------------------------ DIM NPR

INSERT INTO dim_NPR VALUES (NPR_severity,
                            NPR_occurrence,
                            NPR_detection,
                            NPR);

DECLARE @id_dim_NPR int;
SET @id_dim_NPR = (SCOPE_IDENTITY()) 

------------------------------------ DIM MANAGEMENT

INSERT INTO dim_management (status_leadership,
                            status_quality,
                            status_freeze,
                            user_origin)
                            VALUES (0,0,0,user);

DECLARE @id_dim_management int;
SET @id_dim_management = (SCOPE_IDENTITY())

------------------------------------ DIM MAP

DECLARE @id_dim_map int;
SET @id_dim_map = station_description

------------------------------------ DIM RISK

DECLARE @component_code int;
SET @component_code = (select component_code FROM standard_component WHERE id = component_key)

INSERT INTO [dim_risk] VALUES (null
                              ,document_type_key 
                              ,document_number 
                              ,component_key 
                              ,@component_code 
                              ,detail_key 
                              ,local_key 
                              ,element_name 
                              ,requirement_key 
                              ,defect_key 
                              ,effect_key 
                              ,cause  
                              ,control_key 
                              ,code 
                              ,aud_cod_key);

DECLARE @id_dim_risk int;
SET @id_dim_risk = (SCOPE_IDENTITY())

------------------------------------ DIM TERM ACTION

INSERT INTO [dim_term_action] (STA_status, 
                               STA_status)
                               VALUES (1,1);

DECLARE @id_dim_term_action int;
SET @id_dim_term_action = (SCOPE_IDENTITY())

------------------------------------ FACT LAKE

INSERT INTO [fact_lake] VALUES ('risk'
                                ,@id_dim_map
                                ,@id_dim_time
                                ,@id_dim_risk
                                ,@id_dim_NPR
                                ,@id_dim_term_action
                                ,@id_dim_management)





