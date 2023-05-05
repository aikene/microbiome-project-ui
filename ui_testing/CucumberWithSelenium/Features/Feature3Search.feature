Feature: Conducting Search


	Scenario: TestCase-301: Successful search - criteria: library layout
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22librarylayout%22:%20[%22PAIRED%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20false}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-302: Successful search - criteria: sra study
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22sra_study%22:%20[%22SRP002462%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-303: Successful search - criteria: center name
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22center_name%22:%20[%22HARVARD%20MEDICAL%20SCHOOL%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-304: Successful search - criteria: experiment ID
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22experiment%22:%20[%22ERX084377%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-305: Successful search - criteria: sample ACC
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22sample_acc%22:%20[%22SRS1466819%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-306: Successful search - criteria: biosample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22biosample%22:%20[%22SAMEA3543292%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-307: Successful search - criteria: organism
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22organism%22:%20[%22gut%20metagenome%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-308: Successful search - criteria: bioproject
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22bioproject%22:%20[%22PRJEB10006%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-309: Successful search - criteria: country
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22geo_loc_name_country_calc%22:%20[%22Japan%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-310: Successful search - criteria: continent
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22geo_loc_name_country_continent_calc%22:%20[%22Africa%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-311: Successful search - criteria: breed sample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22breed_sam%22:%20[%22Human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-312: Successful search - criteria: cultivar sample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22cultivar_sam%22:%20[%2240BL24hr%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-313: Successful search - criteria: ecotype sample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22ecotype_sam%22:%20[%22Asian%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-314: Successful search - criteria: isolate sample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22isolate_sam%22:%20[%22human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-315: Successful search - criteria: library selection
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22libraryselection%22:%20[%22PCR%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser
		
	Scenario: TestCase-316: Successful search - criteria: strain sample
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria={%22strain_sam%22:%20[%220821200151%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}"			
		Then Verify html element with class exists "table-generic-td"
		Then Close Browser



