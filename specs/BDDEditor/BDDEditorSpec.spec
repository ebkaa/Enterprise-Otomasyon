Specification Heading
=====================


* "testinium" ve "Qwe123+" bilgileriyle gecerli login yap
* BDD Editor Sayfasına Gidilmesi

Test1-1-BDD Editor Sayfası Kontrolleri
--------------------------------------
Tags: BDDEditorController

* BDD Editor Sayfası Kontrolleri Yapılır

Test 1-2-BDD Editor Sayfasına Rastgele Proje Seçimi
---------------------------------------------------
Tags: BDDEditorRandomProject
* BDD Editor Rastgele Proje Seçimi

Test 1-3-BDD Editor Sayfasına Yanlış Proje Seçimi
-------------------------------------------------
Tags: BDDEditorSelectWrongProject
* Yanlış Proje Seçimi ve Hata Mesajı alma

Test 1-4-BDD Editor Sayfası Searchable Ozelligi Kontrolu
--------------------------------------------------------
Tags: BDDEditorControllSearchable
* Searchable olduğu kontrol edilir

Test 1-5-Boş İsimli Concept File oluşturulması
----------------------------------------------
Tags: BDDEditorEmptyFileNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "" adıyla Concept oluştur
* New Concept Save
* Karakter hata mesajı olmaması kontrol edilir
* Boş hata mesajı kontrolu

Test 1-6- Bir karakterli İsimli Concept File oluşturulması
----------------------------------------------------------
Tags: BDDEditorOneCharacterFileNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Concept oluştur
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu

Test 1-7- İki karakterli İsimli Concept File oluşturulması
----------------------------------------------------------
Tags: BDDEditorTwoCharacterFileNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "ab" adıyla Concept oluştur
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu

Test 1-8- Bir karakter ve boş senaryo name hatası
-------------------------------------------------
Tags: BDDEditorOneCharacterFileNameAnaEmptyScenarioNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Concept oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu

Test 1-9- İki karakter ve boş senaryo name hatası
-------------------------------------------------
Tags: BDDEditorTwoCharacterFileNameAndEmptyScenarioNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "ab" adıyla Concept oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu

Test 1-10- Hatasız karakter ve boş senaryo name hatası
----------------
Tags: BDDEditorCorrectCharacterFileNameAndEmptyScenarioNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "abc" adıyla Concept oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı olmaması kontrol edilir
* SenaryoName hata mesajı kontrolu

Test 1-11- Hatasız karakter ve dogru senaryo name eksik Step hatası
----------------
Tags: BDDEditorCorrectCharacterFileNameAndCorrectScenarioNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "abc" adıyla Concept oluştur
* "senaryo" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı olmaması kontrol edilir
* SenaryoName Hata mesajı olmaması kontrol edilir
* TestStep hata mesajı kontrolu

Test 1-12- Boş Conceptname and boş ScenarioName
--------------------
Tags: BDDEditorEmptyConceptNameAndEmptyScenarioNameForConcept
* BDD Editor Sayfası Kontrolleri Yapılır
* "" adıyla Concept oluştur
* "" adlı senaryo eklenmesi
* Boş Senaryo ve Boş File Name ile Concept Kontrolu


Test 1-13-Boş FileName ile Spec File oluşturulması
----------------
Tags: EmptyFileNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "" adıyla Spec oluştur
* New Concept Save
* Karakter hata mesajı olmaması kontrol edilir
* Boş hata mesajı kontrolu

Test 1-14- Bir karakterli FileName ile Spec File oluşturulması
----------------
Tags: OneCharacterFileNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Spec oluştur
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu

Test 1-15- İki karakterli File Name ile Spec File oluşturulması
----------------
Tags: TwoCharacterFileNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Spec oluştur
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu

Test 1-16- Doğru FileName ile Spec File oluşturulması
----------------
Tags: CorrectCharacterFileNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Spec oluştur
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu


Test 1-17- Boş FileName Boş SenaryoName Boş TagName ile Spec File Oluşturulması
----------------
Tags: EmptyCharacterFileNameAndEmptyScenarioNameAndEmptyTagNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "" adıyla Spec oluştur
* "" adlı senaryo eklenmesi
* "" adlı Tag eklenmesi
* New Concept Save
* Boş hata mesajı kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu


Test 1-18- Bir Karakterli FileName Boş SenaryoName Boş TagName ile Spec File Oluşturulması
----------------
Tags: OneCharacterFileNameAndEmptyScenarioNameAndEmptyTagNameForSpec
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Spec oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu

Test 1-20- Doğru karakterli İsimli Boş Snearyolu Boş Tag ile Spec File oluşturulması
----------------
Tags: OpenBDDEditorPage
* BDD Editor Sayfası Kontrolleri Yapılır
* "a" adıyla Spec oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu

Test 1-21- İki karakterli İsimli Boş Snearyolu Spec File oluşturulması
----------------
Tags: OpenBDDEditorPage
* BDD Editor Sayfası Kontrolleri Yapılır
* "ab" adıyla Spec oluştur
* "" adlı senaryo eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı kontrolu
* SenaryoName hata mesajı kontrolu

Test 1-22- Üç karakterli İsimli Boş Snearyolu Spec File oluşturulması
----------------
Tags: OpenBDDEditorPage
* BDD Editor Sayfası Kontrolleri Yapılır
* "abc" adıyla Spec oluştur
* "" adlı senaryo eklenmesi
* "deneme" adlı Tag eklenmesi
* New Concept Save
* Boş hata mesajı olmaması kontrolu
* Karakter hata mesajı olmaması kontrol edilir
* SenaryoName hata mesajı kontrolu










