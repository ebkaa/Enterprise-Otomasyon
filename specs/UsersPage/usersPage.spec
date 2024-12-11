UsersPage Scenarios
====================


* Bilgiler girilerek geçerli giriş yapılır
* Users Tabına tıkla ve Users sayfasında olduğunu kontrol et
     
Test-1-Users Sayfasının element kontrollerini yap
-------------------------------------------------
Tags: UsersSayfasiElementKontrolleri
* Users Sayfasının element kontrollerini yap

Test-2-Enes Turan Company'si seçilir ve Companyde hiçbir üye olmadığı doğrulanır
--------------------------------------------------------------------------------
Tags: UyesiOlmayanCompanySecimiVeUyeOlmadigiDogrulanmasi

* Company Name "Enes Turan" seçilir
* There is not exist any user mesajı alınır

Test-3-Furkan Kartal Company'si seçilir ve Üyelerin doğru listelendiği doğrulanır
---------------------------------------------------------------------------------
Tags: UyesiOlanCompanySecimiVeDogruUyeListelendigiKontrolu

* Company Name "Furkan Kartal" seçilir
* "harun.aktas" Üyesinin Üye listesinde listelendiği doğrulanır

Test-4-Users sayfası içindeki Manage Roles sayfasının element kontrolleri yapılır
---------------------------------------------------------------------------------
Tags: UsersSayfasindakiManageRolesSayfasininElementKontrolleri

* Manage Roles tabına tıkla
* Manage Roles sayfasının element kontrolleri yapılır

Test-5-Users sayfasında Manage Roles sayfası içindeki Create new role sayfasının element kontrolü
-------------------------------------------------------------------------------------------------
Tags: CreateNewRoleSayfasiElementKontrolu

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* Create new role sayfasının element kontrolü yapılır

Test-6- Create new role sayfasında bir rol oluştur ve sil oluşturulup silindiğini kontrol edilir
------------------------------------------------------------------------------------------------
Tags: RolOlusturVeSilOlusturulupSilindiginiKontrolEt

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* Bilgileri doldurarak "roleForTest" rolünü oluştur ve oluşturulduğunu kontrol et
* Oluşturulan rolü sil ve silindiğini kontrol et

Test-7 Create new role sayfasında Aynı isimde yeni rol oluşturulur ve already exists! uyarısı alınır
---------------------------------------------------------------------------------------------------
Tags: AyniIsimdeRolOlusturVeUyariAl

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* Bilgileri doldurarak "Test" rolünü oluştur
* "already exists!" Uyarı mesajı alınır

Test-8 Create new role sayfasında Rol ismi boş bırakılarak rol oluşturulduğunda Role Name field is required. uyarısı alınır
---------------------------------------------------------------------------------------------------------------------------
Tags: RolismiBosBirakilarakRolOlusturuldugundaRoleNameIsRequiredHatasiAlinir

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* Rol oluşturma sayfasındaki save butonuna bas
* "Role Name field is required." Uyarı mesajı alınır

Test-9 Create new role sayfasında Cancel tuşuna basılır Rol listesine geri dönüldüğü kontrol edilir
---------------------------------------------------------------------------------------------------
Tags: CreateNewRoleSayfasindaCancelTusuIslevKontrolu

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* Create new role sayfasında Cancel tuşuna bas geri dönüldüğünü kontrol et

Test-10 Create new role sayfasında All Permissionsdaki herhangi bir izni Role permissionsa taşı kontrollerini yap
-----------------------------------------------------------------------------------------------------------------
Tags: IzinleriAllPermissionsdanRolePermissionsaTasimaKontrolu

* Manage Roles tabına tıkla
* Create new role tabına tıkla
* "PERM_DASHBOARD_MENU_ITEM" adlı izni seç ve role permissions kısmına taşı ve kontrollerini yap

Test-11 Create new user sayfasının element kontrollerini yap
------------------------------------------------------------
Tags: CreateNewUserSayfasiElementKontrolu

* Create new user tabına tıkla
* Create new user sayfasının element kontrollerini yap


Test-12 Create new user sayfasında kullanıcı adı ve mail boş bırakılarak giriş yapılır alınan uyarı kontrol edilir
------------------------------------------------------------------------------------------------------------------
Tags: KullaniciVeMailBosBirakilarakUserOlusturmaKontrolu

* Create new user tabına tıkla
* Users Page sayfasında User Name field is required ve Email field is required hatalarının alındığı görülür

Test-13 Create new user sayfasında kullanıcı adı boş bırakılırak giriş yapılır ve User name field is required hatasının alındığı görülür
----------------------------------------------------------------------------------------------------------------------------------------
Tags: KullaniciAdiBosBirakilarakUserOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page mail alanına "enes.turan@testinium.com" mailini yaz
*  UsersPage sayfasında "User Name field is required." hatasının alındığı görülür


Test-14 Create new user sayfasında mail boş bırakılarak giriş yapılır ve Email field is required hatasının alındığı görülür
---------------------------------------------------------------------------------------------------------------------------
Tags: MailBosBirakilarakUserOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "enes.turan" kullanıcı adını yaz
*  UsersPage sayfasında "Email field is required." hatasının alındığı görülür

Test-15 Create new user sayfasında var olan kullanıcı adıyla bir kullanıcı oluştur ve This username is already taken hatasını kontrol et
----------------------------------------------------------------------------------------------------------------------------------------
Tags: VarOlanKullaniciAdiylaKullaniciOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "testinium" kullanıcı adını yaz
* Users Page mail alanına "enes.turan@testinium.com" mailini yaz
* UsersPage sayfasında "This username is already taken." hatasının alındığı görülür

Test-16 Create new user sayfasında var olan mail ile kullanıcı oluştur ve This email address is already in use hatasını kontrol et
----------------------------------------------------------------------------------------------------------------------------------
Tags: VarOlanMailIleKullaniciOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "enes.turan" kullanıcı adını yaz
* Users Page mail alanına "user@testinium.com" mailini yaz
* UsersPage sayfasında "This email address is already in use" hatasının alındığı görülür

Test-17 Create new user sayfasında 4 karakterden az bir kullanıcı adı oluştur ve hatayı kontrol et
--------------------------------------------------------------------------------------------------
Tags: DortKarakterdenAzKullaniciAdiylaKullaniciOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "ens" kullanıcı adını yaz
* Users Page mail alanına "enes.turan@testinium.com" mailini yaz
* UsersPage sayfasında "Please be sure that username length is between 4 and 30. Valid characters are A-Z a-z 0-9 . _ and -" hatasının alındığı görülür

Test-18 Create new user sayfasında 30 karakterden fazla kullanıcı adı oluştur ve hatayı kontrol et
--------------------------------------------------------------------------------------------------
Tags: OtuzKarakterdenFazlaKullaniciAdiylaKullaniciOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "qwerty1234567890zxcvbnmlkjhgfds" kullanıcı adını yaz
* Users Page mail alanına "enes.turan@testinium.com" mailini yaz
* UsersPage sayfasında "Please be sure that username length is between 4 and 30. Valid characters are A-Z a-z 0-9 . _ and -" hatasının alındığı görülür

Test-19 Create new user sayfasında geçersiz maill ile kullanıcı oluştur ve hatayı kontrol et
--------------------------------------------------------------------------------------------
Tags: GecersizMailleKullaniciOlusturmaVeHataKontrolu

* Create new user tabına tıkla
* Users Page kullanıcı adı alanına "enes.turan" kullanıcı adını yaz
* Users Page mail alanına "enes.turan@" mailini yaz
* UsersPage sayfasında "Please enter a valid email address." hatasının alındığı görülür

Test-20 Basarili bir sekilde kullanici olusturulmasi ve silinmesi kontrolu
--------------------------------------------------------------------------
Tags: BasariliBirsekildeKullaniciOlusturVeSil

* Create new user tabına tıkla
* Başarılı bir şekilde kullanıcı oluştur ve sil

