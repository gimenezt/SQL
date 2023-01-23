DECLARE @SELECT_QUERY int
SET @SELECT_QUERY =  :SELECT_QUERY 



-- Quando o usuário estiver cadastrando um novo um STA/LTA, deve ser salvo na dim_management o usuário de criação
DECLARE @CadManagement varchar(MAX)
SET @CadManagement = CONCAT(' DECLARE @management_key as int
					SET @management_key = (SELECT management_key FROM fact_lake WHERE id =', :id, ') ',
					' UPDATE dim_management
					SET user_input_STALTA =',				CHAR(39), :user, CHAR(39),
					' WHERE id = @management_key')

-- Quando o usuário estiver editando um STA/LTA existente, deve ser salvo na dim_management o usuário de quem edita, assim como a adata da edição
DECLARE @EditManagement varchar(MAX)
SET @EditManagement = CONCAT(' DECLARE @management_key as int
					SET @management_key = (SELECT management_key FROM fact_lake WHERE id =', :id, ') ',
					' UPDATE dim_management
					SET last_edit_date = ',					CHAR(39), GETDATE(), CHAR(39), 
					', last_edit_user = ',					CHAR(39), :user, CHAR(39),
					' WHERE id = @management_key')



--- STA
DECLARE @UpdateSTA varchar(MAX)
SET @UpdateSTA = CONCAT('DECLARE @NPR_key as int
					SET @NPR_key = (SELECT NPR_key FROM fact_lake WHERE id =', :id, ')',
					' UPDATE dim_NPR SET STA_severity =', 	:severity,
					', STA_occurrence =', 					:occurrence,
					', STA_detection =', 					:detection,
					', NPR_STA =', 							:NPR,
					' WHERE id = @NPR_key',
					' DECLARE @term_action_key as int
					SET @term_action_key = (SELECT term_action_key FROM fact_lake WHERE id =', :id, ') ',
					' UPDATE dim_term_action
					SET STA_description = ', 				CHAR(39), :description, CHAR(39),
					', STA_responsable = ', 				CHAR(39), :responsable, CHAR(39),
					', STA_deadline = ', 					CHAR(39), :deadline, CHAR(39),
					', STA_status = ', 						:status,
					' WHERE id = @term_action_key')


--- LTA
DECLARE @UpdateLTA varchar(MAX)
SET @UpdateLTA = CONCAT('DECLARE @NPR_key as int
					SET @NPR_key = (SELECT NPR_key FROM fact_lake WHERE id =', :id, ')',
					' UPDATE dim_NPR SET LTA_severity =',	:severity,
					', LTA_occurrence =', 					:occurrence,
					', LTA_detection =', 					:detection,
					', NPR_LTA =', 							:NPR,
					' WHERE id = @NPR_key',
					
					' DECLARE @term_action_key as int
					SET @term_action_key = (SELECT term_action_key FROM fact_lake WHERE id =', :id, ') ',
					' UPDATE dim_term_action
					SET LTA_description = ', 				CHAR(39), :description, CHAR(39),
					', LTA_responsable = ', 				CHAR(39), :responsable, CHAR(39),
					', LTA_deadline = ', 					CHAR(39), :deadline, CHAR(39),
					', LTA_status = ',						:status,
					' WHERE id = @term_action_key')


/* 	
	SELECT_QUERY = 0 >> Query de inserção de novo STA
	SELECT_QUERY = 1 >> Query de inserção de novo lTA
	SELECT_QUERY = 2 >> Query de edição de STA existente
	SELECT_QUERY = 3 >> Query de edição de LTA existente
*/



DECLARE @Result varchar(MAX)
SET @Result = 
	(CASE
		WHEN @SELECT_QUERY  = 0 THEN CONCAT(@UpdateSTA, @CadManagement)
		WHEN @SELECT_QUERY  = 1 THEN CONCAT(@UpdateLTA, @CadManagement)
		WHEN @SELECT_QUERY  = 2 THEN CONCAT(@UpdateSTA, @EditManagement)
		WHEN @SELECT_QUERY  = 3 THEN CONCAT(@UpdateLTA, @EditManagement)
	END)

EXEC(@Result) 	
