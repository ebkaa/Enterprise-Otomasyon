Forgot Password Scenarious
=====================

     
* "https://dev.testinium.com/forgotPassword.html" adresine git
* Şu anki url "https://dev.testinium.com/forgotPassword.html" ile aynı mı


Test-2-1: Forgot Password to Login Page
---------------------------------------
Tags: ForgotPasswordToLoginPage

* Forgot Password sayfasında olduğunu kontrol et
* Forgot Password sayfasından Back To Login butonuna tıklayıp login sayfasına git
* Şu anki url "https://dev.testinium.com/login.html" ile aynı mı

Test-2-2: Forgot Password - Input Controls - Valid email
--------------------------------------------------------
Tags: ForgotPasswordValidEmail

* Forgot Password sayfasında olduğunu kontrol et
* Forgot Password sayfasında Email alanına geçerli "sena.eroglu@testinium.com" girişi yapılır

Test-2-3 Forgot Password - Input Controls - Invalid Email - Without @
---------------------------------------------------------------------
Tags: ForgotPasswordInvalidEmailWithoutAt

* Forgot Password Email alanına "senaeroglutestinium.com" texti girilir "Geçerli bir eposta adresi giriniz." hatası alınır

Test-2-4 Forgot Password - Input Controls - Invalid Email - Invalid Char
------------------------------------------------------------------------
Tags: ForgotPasswordInvalidEmailInvalidChar

* Forgot Password Email alanına "<sena>.eroglu@testinium.com" texti girilir "Geçerli bir eposta adresi giriniz." hatası alınır

Test-2-5 Forgot Password - Input Controls - Invalid Email - Quote char
----------------------------------------------------------------------
Tags: ForgotPasswordInvalidEmailWithQuotedChar

* Forgot Password Email alanına "sena\".eroglu@testinium.com" texti girilir "Geçerli bir eposta adresi giriniz." hatası alınır

Test-2-6 Forgot Password - Input Controls - Empty Email
-------------------------------------------------------
Tags: ForgotPasswordEmptyEmail

* Forgot Password Email alanına "" texti girilir "Email alanına bir değer girilmesi gereklidir" hatası alınır


