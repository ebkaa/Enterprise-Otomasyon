Login Page Scenarious
=====================


Test-2-1: Valid Login to dashboard
----------------------------------
Tags: Validlogin

* "testinium" ve "Qwe123+" bilgileriyle gecerli login yap


Test-2-2: Invalid Login --> empty username and empty password
-------------------------------------------------------------
Tags: InvalidLoginWithEmptyValues

* "" ve "" bilgileriyle giris yap
* Login başarısız uyarısında "Username or password incorrect!" hata mesajı alınır.

Test-2-3: Invalid Login --> username empty and valid password
------------------------------------------------------------
Tags: InvalidLoginWithEmptyUsername

* "" ve "Qwe123+" bilgileriyle giris yap
* Login başarısız uyarısında "Username or password incorrect!" hata mesajı alınır.


Test-2-4: Invalid Login --> username valid and empty password
------------------------------------------------------------
Tags: InvalidLoginWithEmptyPassword

* "testinium" ve "" bilgileriyle giris yap
* Login başarısız uyarısında "Username or password incorrect!" hata mesajı alınır.

Test-2-5 Invalid Login --> username valid and invalid password
--------------------------------------------------------------
Tags: InvalidLoginWithInvalidPassword

* "testinium" ve "123" bilgileriyle giris yap
* Login başarısız uyarısında "Username or password incorrect!" hata mesajı alınır.

Test-2-6 Invalid Login --> username invalid and valid password
--------------------------------------------------------------
Tags: InvalidLoginWithInvalidUsername

* "rerere" ve "Qwe123+" bilgileriyle giris yap
* Login başarısız uyarısında "Username or password incorrect!" hata mesajı alınır.

Test-2-7 Go to Forgot My Password
------------------------------
Tags: GoToForgotMyPassword

* Forgot my password butonuna tıkla
* Şu anki url "https://dev.testinium.com/forgotPassword.html" ile aynı mı


