@echo off
setlocal enabledelayedexpansion

start "CRUD API" cmd /c "python api.py"
timeout /t 2 >nul


curl  http://127.0.0.1:5000/

:main
cls
echo ======================================
echo             CRUD SELECTION
echo ======================================
echo 1. [C] Insert
echo 2. [R] Select
echo 3. [U] Update
echo 4. [D] Delete 
echo 5. [A] Additional Search Functionality

set /p choice=Enter your choice: 

if "%choice%"=="1" (
	cls
	goto insert
) else if "%choice%"=="2" (
	cls
	goto select
) else if "%choice%"=="3" (
	cls
	goto update
) else if "%choice%"=="4" (
	cls
	goto delete
) else if "%choice%"=="5" (
	cls
	goto additional
) else (
	cls
	goto end
)

goto end


:insert 
cls
echo =========================================================================
echo In this code, you will be inserting the amount into the payments table. 
echo =========================================================================
set /p amount=Enter the payment amount: 
curl -X POST -H "Content-Type: application/json" -d "{\"amount\": \"%amount%\"}" http://127.0.0.1:5000/payments/amount
set /p run=Do you want to run again? (Yes/No): 
if "%run%" == "yes" (
    goto main
) else if "%run%" == "no" (
    goto end
)

:select 
cls
echo ====================================
echo           SELECT OPERATION
echo ====================================
echo 1. Select ALL Customers      
echo 2. Join Statement

set /p select=Enter your selection: 
if %select% == 1 (
    goto select_all
) else if %select% == 2 ( 
   goto modify
) else (
    echo Invalid choice.
    goto join
)

:select_all
echo ===============================================================
echo In this code, it will select all the column in customers table
echo ===============================================================
echo Choose response format:
echo 1. JSON
echo 2. XML
set /p format_choice=Enter choice: 

if %format_choice% == 1 (
    cls
    curl  -X GET http://127.0.0.1:5000/customers/modify
) else if %format_choice% == 2 (
    cls
	curl "http://127.0.0.1:5000/customers/modify?format=xml"
) else (
    echo Invalid choice.
    goto main
)

set /p run=Do you want to run again? (Yes/No): 
if "%run%" == "yes" (
    goto main
) else if "%run%" == "no" (
    goto end
)


:join
cls
echo ================================================================================
echo In this code, it will show you the self join statement.
echo In the customers table, all the customers with the same country will be joined.
echo ================================================================================

curl http://127.0.0.1:5000/customers/join

set /p run=Do you want to run again? (Yes/No): 
if /i "%run%" == "yes" (
    goto start
) else if /i "%run%" == "no" (
    goto end
)


:update 
cls
echo ====================================
echo           SELECT OPERATION
echo ====================================
echo 1. Update Payment       
echo 2. Update Payment with modification

set /p select=Enter your selection:
if %select% == 1 (
    goto update_payment
) else if %select% == 2 ( 
   goto modify
) else (
    echo Invalid choice.
    goto update
)
 

:update_payment
cls
echo ==========================================================================
echo In this code, you will be updating the amount in the payments table. 
echo You need to input the checkNumber for which you want to update the amount.
echo ==========================================================================
set /p checkNumber=Enter the check number: 
set /p amount=Enter the new payment amount:

curl -X PUT -H "Content-Type: application/json" -d "{\"amount\": %amount%}" http://127.0.0.1:5000/payments/%checkNumber%
set /p run=Do you want to run again? (Yes/No): 
if "%run%" == "yes" (
    goto main
) else if "%run%" == "no" (
    goto end
)


:modify
cls
echo ===========================================================================
echo In this code, it will update the city of a customer in the customers table.
echo ===========================================================================
echo Choose response format:
echo 1. JSON
echo 2. XML
set /p format_choice=Enter choice:  

if %format_choice% == 1 (
    set format_param=json
) else if %format_choice% == 2 (
    set format_param=xml
) else (
    echo Invalid choice.
    goto main
)

cls
curl -H "Accept: application/xml" "http://127.0.0.1:5000/update/modify?format=%format_param%"

set /p run=Do you want to run again? (Yes/No): 
if "%run%" == "yes" (
    goto main
) else if "%run%" == "no" (
    goto end
)


:delete
cls
echo ===================================================================
echo In this code, you can delete rows in the payments table by inputting 
echo the check number of the rows you want to delete.
echo ===================================================================
set /p checkNumber=Enter check number: 
curl -X DELETE http://127.0.0.1:5000/payments/%checkNumber%
set /p run=Do you want to run again? (Yes/No): 
if "%run%" == "yes" (
    goto main
) else if "%run%" == "no" (
    goto end
)

:additional
cls
echo ==================================================
echo In this code, it will help you to search the data 
echo using the provided keyword that you will give.
echo ==================================================
set /p keyword=Enter keyword to search: 

if "%keyword%" == "" (
    echo Keyword cannot be empty.
    goto start
)

curl -X POST -H "Content-Type: application/json" -d "{\"keyword\": \"%keyword%\"}" http://127.0.0.1:5000/customers/search

set /p run=Do you want to run again? (Yes/No): 
if /i "%run%" == "yes" (
    goto main
) else if /i "%run%" == "no" (
    goto end
)



:end
echo Thank you for using this program!
pause


